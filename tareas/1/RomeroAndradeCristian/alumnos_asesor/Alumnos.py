# !/usr/bin/python
# -*- coding: UTF-8 -*-
from random import randint

class Alumnos:
    """Clase que define al alumno
    Limite de preguntas es 7
    """

    __preguntas = ('¿El hombre es realmente libre?',
                   '¿Nuestro universo es real?',
                   '¿Dios existe?',
                   '¿El número 42 es perfecto?',
                   'Para ir al espacio necesito una toalla',
                   '¿Qué es todo?')

    __cont = 0

    def __init__(self, nombre: str, limite_preguntas=7):
        """Nace un alumno

        :param self: El apuntador
        :param nombre: El nombre del alumno
        :type nombre: str
        """

        self.nombre = nombre
        self.limite_preguntas = limite_preguntas

    def reiniciar_contador(self):
        """Cuando se sale se vuelve otro con el mismo nombre
        y pude hacer preguntas"""

        self.__cont = 0
        
    def __incremetar_contador(self):
        """Incrementa el contador de peguntas"""

        self.__cont += 1

    def cont(self):
        """obtiene el contador de sus preguntas"""

        return self.__cont

    def __seleccionar_pregunta(self):
        """Selecciona una pregunta al azar
        :rtype: string
        """

        return self.get_pregunta(randint(0, 5))

    def validar_permiso_pregunta(self):

        return self.cont() != self.limite_preguntas()
    
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

        if self.cont() != self.limite_preguntas:
            prg = self.__seleccionar_pregunta()
            self.__incremetar_contador()
            print(self.nombre, 'Pregunta:', prg ,'{}/{}'.
                  format(self.cont(), self.limite_preguntas))
            return prg
        return False

    def __str__(self):
        return self.nombre


if __name__ == '__main__':
    ALU = Alumnos('Miguelon')
    print(ALU.hacer_pregunta())
