# !/usr/bin/python
# -*- coding: UTF-8 -*-

from . import Profesor, Alumnos
from time import sleep
from random import randint
from threading import Semaphore


class Cubiculo:
    """Clase que define un cubiculo y sus interacciones"""

    def __init__(self, profe: Profesor, capacidad_alumnos=3):
        """Contructor

        :param capacidad_alumnos: La capacidad de alumnos del cubiculo
        :type capacidad_alumnos: int
        """

        self.profe = profe
        self.capacidad_alumnos = capacidad_alumnos
        self.en_clase_alumno = list()
        self.cola = list()

    def agrega_alumno_cola(self, alumno: Alumnos):
        """Agrega uno más a la cola"""

        self.cola.append(alumno)

    def cola_vacia(self):
        """Checa si NO hay gente afuera"""

        return len(self.cola) == 0

    def entra_salon(self, alumno: Alumnos):
        """Entra al salón"""

        sleep(0.333)
        if self.checar_lleno():
            self.cola.append(alumno)
        else:
            self.en_clase_alumno.append(alumno)
        
    def obtener_capacidad_actual(self):
        """Devuelve la capacidad actual"""

        return len(self.en_clase_alumno)

    def checar_lleno(self):
        """Checa si está lleno"""

        return self.obtener_capacidad_actual() == self.capacidad_alumnos

    def checar_alguien(self):
        """Checa si está vació el salón"""

        return len(self.en_clase_alumno) == 0

    def sacar_alu(self, apu: int):
        """Saca a un alumno del cubiculo
        :param apu: en apuntador de la lista de asistencia
        """

        alumno = self.en_clase_alumno.pop(apu)

        print(' '*10, 'Sale:', alumno)
        alumno.reiniciar_contador()

        if len(self.cola) > 0:
            self.hacer_entra_alumno()

    def sillas_disponibles(self):
        """Devuelve el numero de sillas disponibles"""

        return self.capacidad_alumnos - len(self.en_clase_alumno)

    def hacer_entra_alumno(self):
        """Hace entrar a un numero de alumnos de la cola"""

        self.en_clase_alumno.append(self.cola.pop(0))

    def responder(self):
        """Responde pregunta si aún puede el alumno

        :return: Devuelve False si el alumno ya no puede hacer preguntas,
        una cadena si aun puede
        """

        print('En espera:', [i.nombre for i in self.cola])
        print('En el Cubiculo:', [i.nombre for i in self.en_clase_alumno])
        if not self.checar_alguien():
            apu_alu = randint(0, self.obtener_capacidad_actual()-1)
            print('*'*7, 'apuntando a:', apu_alu, ':', self.en_clase_alumno[apu_alu])
            response = self.en_clase_alumno[apu_alu].hacer_pregunta()
            if response:
                if randint(0, 15) == 3:
                    self.sacar_alu(apu_alu)
                return self.profe.responder(response)
            self.sacar_alu(apu_alu)
            return '...¿¿Más preguntas??'

        if self.checar_alguien() and self.cola_vacia():
            return self.profe.dormir(True)
        return 'Adelante!!!'
