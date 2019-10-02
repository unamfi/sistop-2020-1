# -*- coding: utf-8 -*-
import threading as th
from faker import Faker
import random
from itertools import count
from time import sleep

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
ordenesListas = []
ordenesSinAtender = []
ordenesSinCocinar = []
platillos = []

# Candados, semáforos y variables de condición necesarios para sincronización
lClientes = th.Lock()
lMeseros = th.Lock()
lMenu = th.Lock()
lOrdenesListas = th.Lock()
lOrdenesSinAtender = th.Lock()
lOrdenesSinCocinar = th.Lock()

cvClientes = th.Condition() #Variable de condición para que los meseros esperen si no hay clientes
cvOrdenesSinAtender = th.Condition() #Variable de condición para que los meseros no hagan su hilo de recibir ordenes si no hay órdenes en espera
cvOrdenesSinCocinar = th.Condition() #Variable de condición para avisar a los cocineros que tienen que iniciar a cocinar las órdenes

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

class Mesero(th.Thread):
    _ids = count(0)
    def __init__(self, name : str):
        th.Thread.__init__(self)
        self.id = next(self._ids)
        self.name = name
        self.lock = th.Lock()

    def recibirOrdenes(self):
        global ordenesSinAtender
        with cvOrdenesSinAtender:
            while not hayOrdenesSinAtender():
                print("No hay ordenes por atender.")
                cvOrdenesSinAtender.wait()
            ordenPorAtender = ordenesSinAtender.pop(0)
        ordenPorAtender['idMesero'] = self.id
        with cvOrdenesSinCocinar:
            ordenesSinCocinar.append(ordenPorAtender)
            cvOrdenesSinCocinar.notifyAll() # Notificamos a los cocineros para que hagan su trabajo

    def anotarOrdenesSinCocinar(self):
        pass

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
        with cvClientes:
            while not hayClientes():
                print("No hay clientes, me wa dormir. Zzzz")
                cvClientes.wait()
        #     with lClientes:
        #         clientePorAtender = clientes.pop(0)
        # print('%s: atendiendo a cliente: %s' % (self.name, clientePorAtender.name))
        print("%s: Llegaron clientes y me despertaron :c" % self.name)
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
            cvClientes.notify() # Aviso a los meseros que hay clientes

    def ponerOrdenEnEspera(self):
        with cvOrdenesSinAtender:
            ordenesSinAtender.append({
                'idCliente' : self.id,
                'orden' : self.orden
            })
            print('%s: Mando señal de que necesito un mesero.' % self.name)
            cvOrdenesSinAtender.notify() # Aviso a los meseros que hay órdenes por atender
    
    def ordenarPlatillos(self):
        while self.orden:
            platillo = self.orden.pop(0)
            print('%s: Quiero ordenar %s' % (self.name, platillo))

    def comerPlatillo(self):
        pass
            
    def run(self):
        global clientes, cvClientes
        print('Hola, soy %s y voy a entrar al restaurante.' % self.name, end=' ')
        print('Voy a ordenar %i platillo(s).' % len(self.orden))
        
        self.entraralRestaurante()

        self.ponerOrdenEnEspera()
        
        self.ordenarPlatillos()

        self.comerPlatillo()
        sleep(2)
        with lClientes:
            clientes.remove(self)
            print('%s: Terminé de comer, quedan %i en el restaurante.' % (self.name, len(clientes)))

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

class Orden(object):
    _ids = count(0)
    def __init__(self, mesero=None):
        self.id = next(self._ids)
        self.cliente = cliente
        self.mesero = mesero
        self.atendida = False
        self.cocinada = False
        self.servida = False

class Platillo(object):
    _ids = count(0)
    def __init__(self, nombre, orden):
        self.id = next(self._ids)
        self.nombre = nombre
        self.cocinado = False
    def __str__(self):
        return self.nombre

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
        orden = Orden(i, l_platillos)
        c = Cliente(fake.name(), orden)
        c.orden.cliente = c
        c.start()
        sleep(0.1)
