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
semOrdenes = th.Semaphore(0) # Semáforo que los clientes levantarán para indicar que hay una orden que atender


class Mesero(th.Thread):
    def __init__(self, name : str):
        pass

    def recibirOrden(self):
        pass

    def anotarOrden(self):
        pass

    def obtenerPlatillo(self):
        pass

    def entregarPlatillo(self):
        pass

    def run(self):
        pass

class Cliente(th.Thread):
    def __init__(self, name : str, orden=[]):
        th.Thread.__init__(self)
        self.name = name
        self.orden = orden
        self.lOrden = th.Lock()

    def ordenarPlatillos(self):
        while self.orden:
            platillo = self.orden.pop(0)
            semOrdenes.release() # Aviso a los meseros que hay órdenes por atender
            print('%s: Quiero ordenar %s' % (self.name, platillo))

    def comerPlatillo(self):
        pass

    def run(self):
        print('Hola, soy %s y voy a entrar al restaurante.' % self.name)
        print('Voy a ordenar %i platillos.' % len(self.orden))
        with lClientes:
            clientes.append(self)
            print('%s: Estoy dentro, somos %i en el restaurante.' % (self.name, len(clientes)))
        
        apagadorClientes.release() # Aviso que hay un cliente por ser atendido

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

class Platillo(th.Thread):
    def __init__(self, nombre : str, cliente : Cliente):
        self.cliente = cliente
        self.nombre = nombre
    def __str__(self, parameter_list):
        return self.nombre


def iniciar(n_clientes, n_meseros, n_cocineros):
    fake = Faker(locale='es_mx')

    for i in range(n_meseros):
        orden = random.sample(menu, random.randint(1,3))
        Mesero(fake.name(), orden).start()
        sleep(1)

    for i in range(n_cocineros):
        orden = random.sample(menu, random.randint(1,3))
        Cliente(fake.name(), orden).start()
        sleep(1)

    for i in range(n_clientes):
        orden = random.sample(menu, random.randint(1,3))
        Cliente(fake.name(), orden).start()
        sleep(0.1)
