# !/usr/bin/python
# -*- coding: UTF-8 -*-

import alumnos_asesor.Alumnos as al
import alumnos_asesor.Profesor as pr
import alumnos_asesor.Cubiculo as cu
from random import randint
from threading import Thread, Semaphore

sillas_vacias = Semaphore(1)
mutex = Semaphore(1)
torniquete = Semaphore(1)
pregunta = Semaphore(1)

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

P = pr.Profesor('Prof. Crono')

CUB = cu.Cubiculo(MAX_SILLAS, P, MAX_SILLAS)

def preguntones():
    torniquete.acquire()
    CUB.
    
