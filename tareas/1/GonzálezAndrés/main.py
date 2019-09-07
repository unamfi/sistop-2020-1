#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Semaphore
from time import sleep
from random import randint
from cubiculo import Alumno, Profesor, Cubiculo
from faker import Faker

if __name__ == "__main__":
    fake = Faker()

    num_alumnos = 5
    num_sillas = 2
    num_preguntas_max = 6

    sem_entrada = Semaphore(num_sillas)

    preguntas = ['preg'+str(i) for i in range(randint(1,num_preguntas_max))]
    
    prof = Profesor(fake.name(), sem_entrada)
    alumnos = [Alumno(fake.name(), preguntas, sem_entrada) for i in range(num_alumnos)]    
    Cubiculo(sem_entrada, prof, alumnos).start()