# !/usr/bin/python
# -*- coding: UTF-8 -*-

class Cubiculo:
    """Clase que define un cubiculo y sus interacciones"""

    def __init__(self, sillas: int, profesor, capacidad_alumnos=3):
        """Contructor

        :param silla: El números de sillas
        :param profesor: El profesor del cubiculo
        :param alumnos: Los alumnos que entran y salen
        :param capacidad_alumnos: La capacidad de alumnos del cubiculo
        :type sillas: int
        :type alumnos: list
        :type capacidad_alumnos: int
        """

        self.sillas = sillas
        self.profesor = profesor
        self.capacidad_alumnos = capacidad_alumnos
        self.alumno_silla = dict()
        for i in range(capacidad_alumnos):
            self.alumno_silla[i] = ''

    def ver_sillas_disponibles(self):
        """Ve si hay lugares disponibles

        :return: Retorna la silla que esta disponible, un False si no
        """

        lista_sillas = list(self.alumno_silla.values())

        for index, value in enumerate(lista_sillas):
            if value == '':
                return index

        return False

    def sentarse(self, alumno, silla: int):
        """Se sienta un alumno"""

        self.alumno_silla[silla] = alumno

    def entra_alumno(self, alumno):
        """Entra un alumno

        :param alumno: Entra un alumno a checar si esta libre un ligar
        """

        preguntar_lugar = self.ver_sillas_disponibles()
        if preguntar_lugar:
            self.sentarse(alumno, preguntar_lugar)

    def sale_alumno(self, lugar):
        """Sale un alumno - Libera una silla

        :param lugar: El lugar que el alumno va a liberar
        """

        self.alumno_silla[lugar] = ''

    def tamanio_ocupado(self):
        """Devuelve el tamaño ocupado"""

        lista_sillas = list(self.alumno_silla.values())
        cont = 0
        for _, value in enumerate(lista_sillas):
            if value != '':
                cont += 1
        return cont

    def lista_sillas(self):
        """Lista las sillas disponibles"""

        lista_sillas = list(self.alumno_silla.values())
        lista = list()

        for index, value in enumerate(lista_sillas):
            if value == '':
                lista.append(index)
        return lista

    def cubiculo_vacio(self):
        """Determina si el cubiculo esta vacio

        :rtype: bool
        """

        lista_sillas = list(self.alumno_silla.values())

        for _, value in enumerate(lista_sillas):
            if value != '':
                return False
        return True
