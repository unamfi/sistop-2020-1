#!/usr/bin/python3
# -*-coding: utf-8 -*-x

from procesos.Planificar import Planificar
from procesos.Spn import Spn
from procesos.Proceso import Proceso


if __name__ == "__main__":
    procesos = list()
    procesos.append(Proceso([70, 600], [0, 15]))
    procesos.append(Proceso([70, 600], [0, 15]))
    procesos.append(Proceso([70, 600], [0, 15]))
    procesos.append(Proceso([70, 600], [0, 15]))
    procesos.append(Proceso([70, 600], [0, 15]))
    spn = Spn("registro.txt", 70, procesos)
    spn.start()
