import numpy as np

class Proceso(object):
    def __init__(self, nombre, t_llegada, t_requerido, t_respuesta=0):
        self.nombre = nombre
        self.t_llegada = t_llegada
        self.t_requerido = t_requerido
        self.t_respuesta = t_respuesta
        self.t_restante = self.t_requerido

    @property
    def t_espera(self): 
        return self.t_respuesta - self.t_requerido

    @property
    def p_penalizacion(self): 
        return self.t_respuesta / self.t_requerido

    @property
    def p_respuesta(self): 
        return self.t_requerido / self.t_respuesta

def fcfs(lista_procesos=[]):
    """First come, first serve.
    Ingresa una lista de procesos ordenados por tiempo de llegada y devuelve la cola de ejecución.
    También devuelve tiempo de respuesta (T), tiempo de espera (E), proporción de penalización (P) y proporción de respuesta (R). 
    """

    t_total = 0
    cola_ejec = []
    procesos_ejecutados = []

    while lista_procesos:
        if lista_procesos[0].t_llegada <= t_total:
            proceso_en_ejec = lista_procesos[0]
            lista_procesos = lista_procesos[1:]
            
            while proceso_en_ejec.t_restante:
                cola_ejec.append(proceso_en_ejec.nombre)     
                proceso_en_ejec.t_restante -= 1
                proceso_en_ejec.t_respuesta += 1
                for i in range(len(lista_procesos)):
                    if lista_procesos[i].t_llegada < t_total:
                        lista_procesos[i].t_requerido += 1
                    else:
                        break
                t_total+=1        

            procesos_ejecutados.append(proceso_en_ejec)
        else:
            t_total += 1

    return [cola_ejec, procesos_ejecutados]