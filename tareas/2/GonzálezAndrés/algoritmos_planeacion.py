import numpy as np

class Proceso(object):
    def __init__(self, nombre, t_llegada, t_requerido, t_respuesta=0, t_espera=0, p_penalizacion=0, p_respuesta=0):
        self.nombre = nombre
        self.t_llegada = t_llegada
        self.t_requerido = t_requerido
        self.t_respuesta = t_respuesta
        self.t_espera = t_espera
        self.p_penalizacion = p_penalizacion
        self.p_respuesta = p_respuesta


def fcfs(procesos=[]):
    """First come, first serve.
    Ingresa una lista de procesos ordenados por tiempo de llegada y devuelve la cola de ejecución.
    También devuelve tiempo de respuesta (T), tiempo de espera (E), proporción de penalización (P) y proporción de respuesta (R). 
    """
    T=0
    E=0
    P= 0
    R=0

    t_total = 0
    cola_ejec = []

    while procesos:
        np.append(cola_ejec, procesos[0])
        procesos = procesos[1:]
        for i, proceso in enumerate(procesos):            
            proceso
        t_total += 1

    return [procesos, T, E, P, R]