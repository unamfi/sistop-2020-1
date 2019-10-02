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

# Candados, semáforos, apagadores, necesarios para sincronización
lClientes = th.Lock()
lMeseros = th.Lock()
lMenu = th.Lock()
lOrdenesListas = th.Lock()
lOrdenesSinAtender = th.Lock()
lOrdenesSinCocinar = th.Lock()
cvClientes = th.Condition() #Variable de condición para que los meseros esperen si no hay clientes
semOrdenesSinAtender = th.Semaphore(0) # Semáforo que los clientes levantarán para indicar que hay una orden que atender

def hayClientes():
    with lClientes:
        losHay = True if clientes else False
    return losHay

class Mesero(th.Thread):
    _ids = count(0)
    def __init__(self, name : str):
        th.Thread.__init__(self)
        self.id = next(self._ids)
        self.name = name
        self.lock = th.Lock()

    def recibirOrden(self):
        pass

    def anotarOrden(self):
        pass

    def obtenerPlatillo(self):
        pass

    def entregarPlatillo(self):
        pass

    def run(self):
        global clientes, meseros
        print('Hola, soy %s y voy a atender clientes.' % self.name)
        with lMeseros:
            meseros.append(self)
        print('%s: Somos %i meseros en el restaurante.' % (self.name, self._ids))
        cvClientes.acquire()
        while not clientes:
            print("No hay clientes, me wa dormir. Zzzz")
            cvClientes.wait()
        with lClientes:
            clientePorAtender = clientes.pop(0)
        cvClientes.release()
        print('%s: atendiendo a cliente: %s' % (self.name, clientePorAtender.name))
        self.recibirOrden()
        

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

    def ordenarPlatillos(self):
        while self.orden:
            platillo = self.orden.pop(0)
            print('%s: Quiero ordenar %s' % (self.name, platillo))

    def comerPlatillo(self):
        pass

    def entraralRestaurante(self):
        with cvClientes:
            clientes.append(self)
            print('%s: Estoy dentro, somos %i en el restaurante.' % (self.name, len(clientes)))
            cvClientes.notify() # Aviso a los meseros que hay clientes
            
    def run(self):
        global clientes, cvClientes
        print('Hola, soy %s y voy a entrar al restaurante.' % self.name, end=' ')
        print('Voy a ordenar %i platillo(s).' % len(self.orden))
        
        self.entraralRestaurante()

        with lOrdenesSinAtender:
            ordenesSinAtender.append(self.orden)
            # Aviso a los meseros que hay órdenes por atender
        
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
