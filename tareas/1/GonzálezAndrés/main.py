#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Thread, Semaphore
from random import randint
from time import sleep
from cubiculo import Alumno, Profesor, Cubiculo

if __name__ == "__main__":
    preg_max = 6
    sillas_cubiculo = 5

    a = Alumno('Andrés', ['preg'+str(i) for i in range(randint(1,preg_max))])
    print(a.preguntas)
    a.run()