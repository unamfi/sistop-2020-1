#!/usr/bin/python3
# -*-coding: utf-8 -*-x

from queue import Queue

class Fcfs:
    """[nombre, llegada, duracion]"""

    __cola_procesos = Queue()
    __proceso_actual = list()
    __lista_atendida = list()

    tiempo_transcurrido = 0

    def __init__(self):
        pass

    def app(self):
        if self.__proceso_actual == []:
            if self.__cola_procesos.empty():
                return
            self.__proceso_actual = self.sacar_proceso()
            while self.__proceso_actual[2] != self.__proceso_actual[1] + self.tiempo_transcurrido:
                self.mover_reloj()
            
            print("Proceso %s")
       
       
    def mover_reloj(self):
        self.tiempo_transcurrido += 1

    def asignar_tiempo_espera_E(self):
        """T-t"""
        pass

    def asignar_penalizacion(self):
        """P=T/t"""
        pass

    def asignar_respuesta(self):
        """t/T"""
        pass

    def encolar_proceso(self, proceso):
        """"""
        self.__cola_procesos.put(proceso)

    def sacar_proceso(self):
        self.__proceso_actual.self.__cola_procesos.get()

if __name__ == '__main__':
    pass
