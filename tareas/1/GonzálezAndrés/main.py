#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, getopt
from faker import Faker
from cubiculo import Alumno, Profesor, Cubiculo

def main(argv):
    fake = Faker()
    num_alumnos = 5
    num_sillas = 2

    try:
        opts, args = getopt.getopt(argv,"hs:a:",["n_sillas=","n_alumnos="])
    except getopt.GetoptError:
        print("uso: main.py -s <num_sillas> -a <num_alumnos>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("uso: main.py -s <num_sillas> -a <num_alumnos>")
            sys.exit()
        elif opt in ("-s", "--n_sillas"):
            num_sillas = int(arg)
        elif opt in ("-a", "--n_alumnos"):
            num_alumnos = int(arg)

    Cubiculo(sillas=num_sillas, num_alumnos=num_alumnos, nombre_profesor=fake.name()).start()

if __name__ == "__main__":
    main(sys.argv[1:])