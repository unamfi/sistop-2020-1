# !/usr/bin/python
# -*- coding: UTF-8 -*-

from time import sleep
from random import randint
from threading import Thread, Semaphore
import alumnos_asesor.Alumnos as al
import alumnos_asesor.Profesor as pr
import alumnos_asesor.Cubiculo as cu


TORNIQUETE = Semaphore(1)
PREGUNTA = Semaphore(1)

MAX_SILLAS = 4

A1 = al.Alumnos('Juanito')
A2 = al.Alumnos('Pedro')
A3 = al.Alumnos('Sandra')
A4 = al.Alumnos('Georgina')
A5 = al.Alumnos('Cristian')
A6 = al.Alumnos('Hugo')
A7 = al.Alumnos('Sagiri')
A8 = al.Alumnos('Muramasa')
A9 = al.Alumnos('Jesus')
A10 = al.Alumnos('Jose')
A11 = al.Alumnos('Zeus')
A12 = al.Alumnos('Ninfa')
A13 = al.Alumnos('Gea')

ALUMNOS = [
    A1,
    A2,
    A3,
    A4,
    A5,
    A6,
    A7,
    A8,
    A9,
    A10,
    A11,
    A12,
    A12
]

P = pr.Profesor('Prof. Crono')

CUB = cu.Cubiculo(P, MAX_SILLAS)


def entran_a_salon():
    """Entran o esperan a entrar al salón

    Cumpliendo con:
      Los alumnos pueden tocar a su puerta en cualquier momento"""

    while True:
        sleep(0.15)
        if randint(0, 1) == 1:
            with TORNIQUETE:
                CUB.entra_salon(ALUMNOS[randint(0, len(ALUMNOS)-1)])

def inicia_clase():
    """Inicia la clase

    Cumpliendo con:
      Los alumnos pueden tocar a su puerta en cualquier momento
      Los demás alumnos sentados deben esperar pacientemente su turno
      Pueden hace de 1 a 7 PREGUNTAs"""

    while True:
        with PREGUNTA:
            print(CUB.responder())
            sleep(0.1)

if __name__ == "__main__":

    Thread(target=entran_a_salon).start()
    Thread(target=inicia_clase).start()
