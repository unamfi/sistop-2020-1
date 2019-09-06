# !/usr/bin/python
# -*- coding: UTF-8 -*-
from random import randint

class Alumnos:
    """Clase que define al alumno"""

    __preguntas = ('¿El hombre es realmente libre?',
                   '¿Nuestro universo es real?',
                   '¿Dios existe?',
                   '¿El número 42 es perfecto?',
                   'Para ir al espacio necesito una toalla',
                   '¿Qué es todo?')

    def __init__(self, nombre: str):
        """Nace un alumno

        :param self: El apuntador
        :param nombre: El nombre del alumno
        :type nombre: str
        """

        self.nombre = nombre

    def __seleccionar_pregunta(self):
        """Selecciona una pregunta al azar
        :rtype: string
        """

        return self.get_pregunta(randint(0, 5))

    def get_pregunta(self, num: int):
        """Se obtiene una pregunta
        :param num: Un número del 0 al 5
        :type num: int
        :rtype: string
        """

        return self.__preguntas[num]

    def hacer_pregunta(self):
        """Hace la pregunta
        :rtype: string
        """

        return self.__seleccionar_pregunta()


if __name__ == '__main__':
    ALU = Alumnos('Miguelon')
    print(ALU.hacer_pregunta())
