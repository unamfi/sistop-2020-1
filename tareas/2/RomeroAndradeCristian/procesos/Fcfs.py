#!/usr/bin/python3
# -*-coding: utf-8 -*-x


from math import ceil
from procesos.Planificar import Planificar

class Fcfs(Planificar):

    def __init__(self, quantum, proceso):
        Planificar.__init__(self, quantum, proceso)

    def start(self):
        print(self.mostrar_procesos())
        print('\n' + '-'*100 + '\n')
        texto = str()
        total = 0
        inicio = 0
        for proceso in self.proceso:
            while(proceso.llegada > total):
                total = total + 1
                texto = texto + "[  ]"
            inicio = total
            fin = inicio + ceil(proceso.t/self.quantum)
            T = (fin - proceso.llegada)
            quantum_tick = proceso.t/self.quantum
            self.T_list.append(T)
            P = T/quantum_tick
            self.P_list.append(P)
            R = quantum_tick/T
            self.R_list.append(R)
            E = T - quantum_tick
            self.E_list.append(E)
            for _ in range(ceil(quantum_tick)):
                texto = texto + proceso.nombre
            total = total + ceil(proceso.t/self.quantum)
        promedios = self.promedios()
        print("FCFS: T =", promedios['T'], ", E =", promedios['E'],
              ", P =", promedios['P'])
        print(texto+ '\n')
