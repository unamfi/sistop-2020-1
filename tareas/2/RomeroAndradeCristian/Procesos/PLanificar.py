#!/usr/bin/python3
# -*- codig: utf-8 -*-

class Planificar:
    def __init__(self, registro, quantum: int, proceso):
        self.registro = registro
        self.quantum = quantum
        self.proceso = proceso
        self.proceso.sort(key=lambda x: x.llegada, reverse=False)
        self.total = 0
        self.T_list = list()
        self.P_list = list()
        self.R_list = list()
        self.E_list = list()

    def mostrar_procesos(self):
        texto = "\t"
        suma = 0
        for proc in self.proceso:
            suma += proceso.t
            texto += proceso.nombre + ": " + str(proceso.llegada) +\
                ", t=" + str(proceso.t/self.quantum) + "[quantum];\n\t"
        self.total = suma
        return texto + "\t(total: " + str(self.total/1000) + "[s])"

    def promedios(self):
        prom = {"P": 0.0,
                "T": 0.0,
                "R": 0.0,
                "E":0.0}
        cantidad_pro = len(self.proceso)
        for P in self.P_list:
            prom["P"] += P
        for T in self.T_list:
            prom["T"] += T
        for R in self.R_list:
            prom["R"] += R
        for E in self.E_list:
            prom["E"] += E
        prom["P"] /=   cantidad_pro
        prom["R"] /=   cantidad_pro
        prom["T"] /=   cantidad_pro
        prom["E"] /=   cantidad_pro
        return prom
