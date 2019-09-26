#!/usr/bin/python3
# -*-coding: utf-8 -*-x

from procesos.Proceso import Proceso
from procesos.Spn import Spn
from procesos.RRobin import RRobin
from procesos.Fcfs import Fcfs

def main():
    procesos = list()

    for _ in range(5):
        procesos.append(Proceso([70, 600], [0, 15]))

    fcfs = Fcfs(70, procesos)
    spn = Spn(70, procesos)
    roundr = RRobin(70, procesos)
    rr4 = RRobin(70*4, procesos)
    fcfs.start()
    spn.start()
    roundr.start()
    rr4.start()

if __name__ == '__main__':
    main()
