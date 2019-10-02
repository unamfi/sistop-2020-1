# -*- coding: utf-8 -*-
import threading as th
from faker import Faker
import random
from itertools import count
from time import sleep
from colorama import init, Fore, Back, Style
init()

menu = [
    'Pozole', 
    'Tacos al Pastor', 
    'Enchiladas Verdes', 
    'Enchiladas Rojas',
    'Enchiladas de Mole',
    'Caldo de pollo',
    'Caldo de res',
    'Mole de Olla',
    'Chiles en Nogada',
    'Tacos dorados de pollo',
    'Tacos dorados de res',
    'Tacos dorados de papa',
    'Tacos dorados combinados',
    'Especial de la casa',
    'Cochinita',
    'Tinga de res',
    'Tinga de pollo'
]

clientes = []
meseros = []
ordenesSinAtender = [] # Órdenes que aún no tienen mesero asignado
ordenesAtendiendose = [] # Órdenes que están siendo escuchadas por un mesero
ordenesSinCocinar = [] # Órdenes en lista de espera para ser cocinadas
ordenesEscuchadas = []
ordenesCocinadas = []
ordenesPorEntregar = []
platillos = []

# Candados, semáforos y variables de condición necesarios para sincronización
lClientes = th.Lock()
lMeseros = th.Lock()
lMenu = th.Lock()
lOrdenesCocinadas = th.Lock()
lOrdenesSinAtender = th.Lock()
lOrdenesAtendiendose = th.Lock()
lOrdenesEscuchadas = th.Lock()
lOrdenesSinCocinar = th.Lock()
lOrdenesPorEntregar = th.Lock()

semMeseros = th.Semaphore(0)

cvClientes = th.Condition() #Variable de condición para que los meseros esperen si no hay clientes
cvOrdenesSinAtender = th.Condition() #Variable de condición para que los meseros no hagan su hilo de recibir ordenes si no hay órdenes en espera
cvOrdenesAtendiendose = th.Condition() #Variable de condición para que los clientes puedan revisar si ya pueden empezar a pedirle su órden al mesero
cvOrdenesSinCocinar = th.Condition() #Variable de condición para avisar a los cocineros que tienen que iniciar a cocinar las órdenes
cvOrdenesSinEntregar = th.Condition() #Variable de condición para avisar a los cocineros que tienen que iniciar a cocinar las órdenes
cvOrdenesCocinadas = th.Condition() #Variable de condición para avisar a los meseros que tienen ordenes listas para ser entregadas
cvOrdenesEscuchadas = th.Condition() #Variable de condición para avisar a los meseros que ya deben entregar la orden a la cocina
cvOrdenesPorEntregar = th.Condition() #Variable de condición para avisar a los clientes que tienen ordenes listas para ser comidas

def hayClientes():
    global clientes
    with lClientes:
        losHay = True if clientes else False
    return losHay

def hayOrdenesSinAtender():
    global ordenesSinAtender
    with lOrdenesSinAtender:
        lasHay = True if ordenesSinAtender else False
    return lasHay

def hayOrdenesAtendiendose():
    global ordenesAtendiendose
    with lOrdenesAtendiendose:
        lasHay = True if ordenesAtendiendose else False
    return lasHay

def hayOrdenesPorEntregar():
    global ordenesPorEntregar
    with lOrdenesPorEntregar:
        lasHay = True if ordenesPorEntregar else False
    return lasHay

def hayOrdenesEscuchadas():
    global ordenesEscuchadas
    with lOrdenesEscuchadas:
        lasHay = True if ordenesEscuchadas else False
    return lasHay

class Mesero(th.Thread):
    _ids = count(0)
    def __init__(self, name : str):
        th.Thread.__init__(self)
        self.id = next(self._ids)
        self.name = name
        self.lock = th.Lock()

    def recibirOrdenes(self):
        global ordenesSinAtender, clientes
        while True:
            with cvOrdenesSinAtender:
                while not hayOrdenesSinAtender():
                    #print("No hay ordenes por atender.")
                    cvOrdenesSinAtender.wait()
                ordenPorAtender = ordenesSinAtender.pop(0)
            #self.lock.acquire()
            ordenPorAtender['mesero'] = {
                'id' : self.id,
                'name' : self.name
            }
            with cvOrdenesAtendiendose:
                ordenesAtendiendose.append(ordenPorAtender)
                print(("\t"+Fore.GREEN+"%s: Atenderé la órden de %s."+ Style.RESET_ALL) % (self.name, ordenPorAtender['cliente']['name']))
                cvOrdenesAtendiendose.notifyAll() # Le aviso a los clientes que el mesero tomó una de sus órdenes
            # self.escucharOrden(ordenPorAtender)
            # self.anotarOrdenesSinCocinar(ordenPorAtender)

    def escucharOrden(self, orden):
        global ordenesEscuchadas
        print('ordenesEscuchadas: ', ordenesEscuchadas)
        print('Orden por atender: ', orden)
        with cvOrdenesEscuchadas:
            miOrden = list(filter(lambda x : x['mesero']['id'] == self.id, ordenesEscuchadas)) # veo si es mia la orden
            while not miOrden:
                cvOrdenesEscuchadas.wait()
                miOrden = list(filter(lambda x : x['mesero']['id'] == self.id, ordenesEscuchadas)) # veo si es mia la orden
            ordenesEscuchadas.remove(miOrden)
    def anotarOrdenesSinCocinar(self, orden):
        global ordenesSinCocinar
        with cvOrdenesSinCocinar:
                ordenesSinCocinar.append(orden)
                cvOrdenesSinCocinar.notifyAll() # Notificamos a los cocineros para que hagan su trabajo

    def obtenerOrdenesCocinadas(self):
        pass

    def entregarOrdenes(self):
        pass

    def run(self):
        global clientes, meseros
        print('Hola, soy %s y voy a atender clientes.' % self.name)
        with lMeseros:
            meseros.append(self)
            print('%s: Somos %i meseros en el restaurante.' % (self.name, len(meseros)))
        semMeseros.release()
        with cvClientes:
            while not hayClientes():
                print("No hay clientes, me wa dormir. Zzzz")
                cvClientes.wait()
        #     with lClientes:
        #         clientePorAtender = clientes.pop(0)
        # print('%s: atendiendo a cliente: %s' % (self.name, clientePorAtender.name))
        print(("\t"+Fore.RED+Back.LIGHTWHITE_EX+"%s: Llegaron clientes y me despertaron :c"+Style.RESET_ALL) % self.name)
        th.Thread(target=self.recibirOrdenes).start()
        th.Thread(target=self.entregarOrdenes).start()
        

class Cliente(th.Thread):
    _ids = count(0)
    def __init__(self, name, orden):
        th.Thread.__init__(self)
        self.id = next(self._ids)
        self.name = name
        self.orden = orden
        self.ordeno = False
        self.comio = False
        #self.lOrden = th.Lock()

    def entraralRestaurante(self):
        with cvClientes:
            clientes.append(self)
            print('%s: Estoy dentro, somos %i en el restaurante.' % (self.name, len(clientes)))
            #print('\t%s: Agito la mano para llamar la atención de un un mesero.' % self.name)
            cvClientes.notify() # Aviso a los meseros que hay clientes

    def ponerOrdenEnEspera(self):
        with cvOrdenesSinAtender:
            ordenesSinAtender.append({
                'orden' : self.orden,
                'cliente' : {
                        'id' : self.id,
                        'name' : self.name,
                    },
            })
            print('\t%s: Agito la mano para llamar la atención de un un mesero.' % self.name)
            cvOrdenesSinAtender.notify() # Aviso a los meseros que hay órdenes por atender
    
    def ordenarPlatillos(self):
        global ordenesAtendiendose, ordenesEscuchadas
        with cvOrdenesAtendiendose:
            miOrden = list(filter(lambda x : x['cliente']['id'] == self.id, ordenesAtendiendose)) # veo si es mia la orden
            while not miOrden:
                cvOrdenesAtendiendose.wait()
                miOrden = list(filter(lambda x : x['cliente']['id']== self.id, ordenesAtendiendose))
            ordenesAtendiendose.remove(miOrden[0])
        semMeseros.acquire()
        with cvOrdenesEscuchadas:
            for platillo in self.orden:
                print('\t\t%s: Quiero ordenar %s' % (self.name, platillo))
                sleep(1)
            ordenesEscuchadas.append(miOrden)
            print('ordenesEscuchadas cliente: ', ordenesEscuchadas)
            cvOrdenesEscuchadas.notifyAll() # Le avisamos al mesero que ya terminó de decir su orden
        semMeseros.release()

    def comerPlatillo(self):
        global ordenesPorEntregar
        with cvOrdenesPorEntregar:
            miOrden = list(filter(lambda x : x['cliente']['id'] == self.id, ordenesPorEntregar))
            while not miOrden:
                cvOrdenesPorEntregar.wait()
                miOrden = list(filter(lambda x : x['cliente']['id'] == self.id, ordenesPorEntregar))
        print('%s: comiendo mi orden :9' % self.name)
        sleep(2)


            
    def run(self):
        global clientes, cvClientes
        print('Hola, soy %s y voy a entrar al restaurante.' % self.name, end=' ')
        print('Voy a ordenar %i platillo(s).' % len(self.orden))
        
        self.entraralRestaurante()

        self.ponerOrdenEnEspera()
        
        self.ordenarPlatillos()

        # self.comerPlatillo()

        # with lClientes:
        #     clientes.remove(self)
        #     print('%s: Terminé de comer, quedan %i en el restaurante.' % (self.name, len(clientes)))

class Cocinero(th.Thread):
    _ids = count(0)
    def __init__(self, name : str):
        th.Thread.__init__(self)
        self.id = next(self._ids)
        self.name = name

    def prepararPlatillo(self):
        pass

    def run(self):
        pass

# class Orden(object):
#     _ids = count(0)
#     def __init__(self, mesero=None):
#         self.id = next(self._ids)
#         self.cliente = cliente
#         self.mesero = mesero
#         self.atendida = False
#         self.cocinada = False
#         self.servida = False

# class Platillo(object):
#     _ids = count(0)
#     def __init__(self, nombre, orden):
#         self.id = next(self._ids)
#         self.nombre = nombre
#         self.cocinado = False
#     def __str__(self):
#         return self.nombre

def iniciar(n_clientes, n_meseros, n_cocineros):
    fake = Faker(locale='es_mx')

    for i in range(n_meseros):
        Mesero(fake.name()).start()
        #sleep(1)

    for i in range(n_cocineros):
        Cocinero(fake.name()).start()
        #sleep(1)

    for i in range(n_clientes):
        l_platillos = random.sample(menu, random.randint(1,3))
        #orden = Orden(i, l_platillos)
        #c = Cliente(fake.name(), orden)
        c = Cliente(fake.name(), l_platillos)
        c.orden.cliente = c
        c.start()
        sleep(0.1)

# [
#     {
#         'orden': ['Tacos dorados de res'], 
#         'cliente': {'id': 1, 'name': 'Natividad Ramiro Palomino'}, 
#         'mesero': {'id': 1, 'name': 'Teodoro Soledad Pichardo Reséndez'}
#     }
# ]