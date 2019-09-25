#!/usr/bin/python3
# -*-coding: utf-8 -*-x

from procesos.Planificar import Planificar
from procesos.Proceso import Proceso
from procesos.Spn import Spn
from procesos.RRobin import RRobin
from procesos.Fcfs import Fcfs


if __name__ == "__main__":
    procesos = list()
    procesos.append(Proceso([70, 600], [0, 15]))
    procesos.append(Proceso([70, 600], [0, 15]))
    procesos.append(Proceso([70, 600], [0, 15]))
    procesos.append(Proceso([70, 600], [0, 15]))
    procesos.append(Proceso([70, 600], [0, 15]))

    fcfs = Fcfs(70, procesos)
    spn = Spn(70, procesos)
    roundr = RRobin(70, procesos)
    fcfs.start()
    spn.start()
    roundr.start()
