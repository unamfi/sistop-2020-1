# -*- coding: utf-8 -*-
import threading as th

menu = []

class Cocinero(object):
    def recibirOrden(self, parameter_list):
        pass
    def anotarOrden(self, parameter_list):
        pass
    def obtenerPlatillo(self):
        pass
    def entregarPlatillo(self, parameter_list):
        pass

class Cliente(object):
    def ordenarPlatillo(self, parameter_list):
        pass
    def comerPlatillo(self, parameter_list):
        pass


class Mesero(object):
    def prepararPlatillo(self, parameter_list):
        pass

class Platillo(object):
    def __init__(self, cliente, descripcion):
        pass
