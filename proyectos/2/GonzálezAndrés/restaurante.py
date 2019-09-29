# -*- coding: utf-8 -*-
import threading as th

menu = []
clientes = 0
ordenesListas = []
ordenesPendientes = []

# Candados necesarios para variabes globales
lClientes = th.Lock()
lMenu = th.Lock()
lOrdenesListas = th.Lock()
lOrdenesPendiente = th.Lock()

class Mesero(object):
    def __init__(self, nombre : str):
        pass

    def recibirOrden(self, parameter_list):
        pass

    def anotarOrden(self, parameter_list):
        pass

    def obtenerPlatillo(self):
        pass

    def entregarPlatillo(self, parameter_list):
        pass

    def start(self, parameter_list):
        pass

class Cliente(object):
    def __init__(self, nombre : str, orden=[]):
        pass

    def ordenarPlatillo(self, parameter_list):
        pass

    def comerPlatillo(self, parameter_list):
        pass
    
    def start(self, parameter_list):
        pass


class Cocinero(object):
    def __init__(self, nombre : str):
        pass

    def prepararPlatillo(self, parameter_list):
        pass

    def start(self, parameter_list):
        pass

class Platillo(object):
    def __init__(self, cliente, descripcion):
        pass
