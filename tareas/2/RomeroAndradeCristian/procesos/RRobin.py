#!/usr/bin/python3
# -*-coding: utf-8 -*-x

from math import ceil
from procesos.Planificar import Planificar


class RRobin(Planificar):

    def __init__(self, quantum, proceso):
        Planificar.__init__(self, quantum, proceso)

    def start(self):
        # print(self.mostrar_procesos())
        texto = str()
        total = 0
        procesos_listos = []
        for proceso in self.proceso:
            proceso = {"nombre": proceso.nombre,
                       "t": ceil(proceso.t/self.quantum),
                       "quantum": ceil(proceso.t/self.quantum),
                       "llegada": proceso.llegada,
                       "inicio": -1,
                       "fin": 0}
            procesos_listos.append(proceso)
        procesos_terminados = []
        texto = ""
        while(len(procesos_listos) > 0):
            procesos_temp = []
            avant = False
            for proceso in procesos_listos:
                if(proceso["quantum"] > 0):
                    if(proceso["llegada"] > total and total == 0):
                        proceso["inicio"] = proceso["llegada"]
                        total = proceso["inicio"]
                        texto = texto + proceso["nombre"]
                        proceso["quantum"] = (proceso["quantum"] - 1)
                        total = total + 1
                        avant = True
                    elif(proceso["llegada"] == total and proceso["inicio"] == -1):
                        proceso["inicio"] = total
                        texto = texto + proceso["nombre"]
                        proceso["quantum"] = proceso["quantum"] - 1
                        total = total + 1
                        avant = True
                    elif(proceso["llegada"] < total):
                        if(proceso["inicio"] < 0):
                            proceso["inicio"] = total
                        texto = texto + proceso["nombre"]
                        proceso["quantum"] = proceso["quantum"] - 1
                        total = total + 1
                        avant = True
                    procesos_temp.append(proceso)
                else:
                    proceso["fin"] = total
                    procesos_terminados.append(proceso)
            if(avant == False):
                texto = texto + "[  ]"
                total = total + 1
            procesos_listos = procesos_temp
        for proceso in procesos_terminados:
            T = proceso["fin"] - proceso["llegada"]
            self.T_list.append(T)
            P = T/proceso["t"]
            self.P_list.append(P)
            R = proceso["t"]/T
            self.R_list.append(R)
            E = T - proceso["t"]
            self.E_list.append(E)

        promedios = self.promedios()
        print("Round Robin: T =", promedios['T'],
              ", E =", promedios['E'],
              ", P =", promedios['P'])
        print(texto + '\n')
