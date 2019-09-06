#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from threading import Thread, Semaphore
from time import sleep
from random import randint
from cubiculo import Alumno, Profesor, Cubiculo
from faker import Faker

if __name__ == "__main__":
    """     fake = Faker()
    preg_max = 6
    sillas_cubiculo = 2
    prof = Profesor(fake.name())
    c = Cubiculo(sillas_cubiculo, prof)

    for _ in range(10):
        #sleep(1)
        preguntas = ['preg'+str(i) for i in range(randint(1,preg_max))]       
        a = Alumno(fake.name(), preguntas, c)
        #c.sem_puerta.acquire()
        a.run()
        #c.sem_puerta.release() """
    fake = Faker()
    sillas_cubiculo = 2
    prof = Profesor(fake.name())
    c = Cubiculo(sillas_cubiculo, prof)
    c.run()