#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Semaphore, Condition
from time import sleep
from random import randint
from cubiculo import Alumno, Profesor, Cubiculo
from faker import Faker

def main():
    fake = Faker()

    num_alumnos = 5
    num_sillas = 2

    sem_entrada = Semaphore(num_sillas)
    
    prof = Profesor(fake.name(), sem_entrada) 
    Cubiculo(sillas=num_sillas, nombre_profesor=fake.name(), num_alumnos=num_alumnos).start()

if __name__ == "__main__":
    main()