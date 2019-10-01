# -*- coding: utf-8 -*-
import threading as th
from faker import Faker
import random
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
]
clientes = []
ordenesListas = []
ordenesSinAtender = []
ordenesSinCocinar = []

# Candados, semáforos, apagadores, necesarios para sincronización
lClientes = th.Lock()
lMenu = th.Lock()
lOrdenesListas = th.Lock()
lOrdenesSinAtender = th.Lock()
lOrdenesSinCocinar = th.Lock()
apagadorClientes = th.Semaphore(0) # Apagador para que el mesero duerma si no hay clientes
semOrdenesSinAtender = th.Semaphore(0) # Semáforo que los clientes levantarán para indicar que hay una orden que atender


class Mesero(th.Thread):
    def __init__(self, name : str):
        th.Thread.__init__(self)
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
        apagadorClientes.acquire()

class Cliente(th.Thread):
    def __init__(self, name : str, orden):
        th.Thread.__init__(self)
        self.name = name
        self.orden = orden
        #self.lOrden = th.Lock()

    def ordenarPlatillos(self):
        while self.orden:
            platillo = self.orden.pop(0)
            print('%s: Quiero ordenar %s' % (self.name, platillo))

    def comerPlatillo(self):
        pass

    def run(self):
        print('Hola, soy %s y voy a entrar al restaurante.' % self.name, end=' ')
        print('Voy a ordenar %i platillo(s).' % len(self.orden))
        with lClientes:
            clientes.append(self)
            print('%s: Estoy dentro, somos %i en el restaurante.' % (self.name, len(clientes)))
        
        apagadorClientes.release() # Aviso que hay un cliente por ser atendido

        with lOrdenesSinAtender:
            ordenesSinAtender.append(self.orden)
        semOrdenesSinAtender.release() # Aviso a los meseros que hay órdenes por atender
        self.orden.mesero.lock.acquire() # Aviso a los meseros que hay órdenes por atender
        self.ordenarPlatillos()

        self.comerPlatillo()

        with lClientes:
            clientes.remove(self)
            print('%s: Terminé de comer, quedan %i en el restaurante.' % (self.name, len(clientes)))

class Cocinero(th.Thread):
    def __init__(self, name : str):
        th.Thread.__init__(self)
        self.name = name

    def prepararPlatillo(self):
        pass

    def run(self):
        pass

class Orden(object):
    def __init__(self, id, platillos, cliente, mesero):
        self.id = id
        self.platillos = platillos
        self.cliente = cliente
        self.mesero = mesero
        self.atendida = False

class Platillo(object):
    def __init__(self, nombre, orden):
        self.nombre = nombre
        self.orden = orden
        self.preparado = False
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
