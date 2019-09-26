import numpy as np

class Proceso(object):
    def __init__(self, nombre : str, t_llegada : int, t_requerido : int):
        self.nombre = nombre
        self.t_llegada = t_llegada
        self.t_requerido = t_requerido
        self.t_restante = t_requerido
        self.t_finalizacion = t_llegada + t_requerido

    @property
    def t_respuesta(self): 
        return self.t_finalizacion - self.t_llegada

    @property
    def t_espera(self): 
        return self.t_respuesta - self.t_requerido

    @property
    def p_penalizacion(self): 
        return self.t_respuesta / self.t_requerido

    @property
    def p_respuesta(self): 
        return self.t_requerido / self.t_respuesta
    
    def reset(self):
        self.t_restante = self.t_requerido
        self.t_finalizacion = self.t_llegada + self.t_requerido

def fcfs(lista_procesos=[]):
    """First come, first serve.
    Ingresa una lista de procesos ordenados por tiempo de llegada y devuelve la cola de ejecución.
    También devuelve la lista de procesos de entrada con los tiempos de ejecución.

    """
    cola_ejec = []
    procesos_ejecutados = []
    lp = lista_procesos
    t_total = lp[0].t_llegada

    while lp:
        if lp[0].t_llegada <= t_total:
            p_ejec = lp[0] # p_ejec : proceso en ejecucion
            lp = lp[1:]

            while p_ejec.t_restante:
                cola_ejec.append(p_ejec.nombre)     
                p_ejec.t_restante -= 1
                t_total+=1

            p_ejec.t_finalizacion = t_total
            procesos_ejecutados.append(p_ejec)
        else:
            cola_ejec.append('-')     
            t_total += 1

    return [cola_ejec, procesos_ejecutados]

def roundrobin(lista_procesos=[], quantum=1):
    """De las implementaciones más feas que he hecho, pero funciona :D"""
    cola_ejec = []
    procesos_ejecutados = []
    ronda_procesos = []
    lp = lista_procesos 
    t_total = lp[0].t_llegada # Hacemos que inicie desde el proceso que llegó primero
    ronda_procesos.append(lp[0]) # Agregamos el primer proceso a la ronda
    lp = lp[1:] # Removemos el primer valor de la lista
    while lp or ronda_procesos: # Seguimos ejecutando mientras haya procesos, ya sea en ronda o aún sin iniciar
        cont = 0
        while not ronda_procesos: # si no hay procesos en cola para ronda...
            while True: # Validamos si algún proceso llegó
                if lp[0].t_llegada == t_total:
                    ronda_procesos.append(lp[0]) # De ser así, lo ponemos en cola de espera
                    lp = lp[1:]
                    break
                else:
                    cola_ejec.append('-') # indicamos que en ese tiempo no se ejecutó nada
                    t_total += 1 # Aumentamos un tick
                    break
            
        # p_ejec : proceso en ejecución
        p_ejec = ronda_procesos[0] # Ejecutamos el siguiente proceso en cola para ronda
        trq = quantum # Reiniciamos el contador para el quantum
        while True:
            while lp: # Validamos si algún proceso llegó mientras estabamos en el quantum
                if lp[0].t_llegada <= t_total:
                    ronda_procesos.append(lp[0]) # De ser así, lo ponemos en cola de espera
                    lp = lp[1:]
                else:
                    break
            cola_ejec.append(p_ejec.nombre)
            p_ejec.t_restante -= 1
            trq -= 1
            t_total += 1
            if not p_ejec.t_restante: # Si ya ecabamos de ejecutarlo
                p_ejec.t_finalizacion = t_total
                procesos_ejecutados.append(p_ejec) # Lo mandamos a la lista de procesos ejecutados
                break 
            if not trq: # Si se acaba el tiempo en el quantum
                ronda_procesos.append(p_ejec) # Mandamos el proceso de nuevo a la ronda
                break
        ronda_procesos = ronda_procesos[1:] # Removemos de la lista el proceso que acabamos de ejecutar
    return [cola_ejec, procesos_ejecutados]

def spn(lista_procesos=[]):
    #t_total = 0
    cola_ejec = []
    procesos_ejecutados = []
    lp_esp = [] # lista de procesos en espera
    lp = lista_procesos 
    t_total = lp[0].t_llegada # Hacemos que inicie desde el proceso que llegó primero
    while lp: # Recorremos la lista para ver si encontramos otro proceso que haya llegado al mismo tiempo
        if lp[0].t_llegada == t_total:
            lp_esp.append(lp[0]) # De ser así, lo ponemos en cola de espera
            lp = lp[1:]
        else:
            break
    if len(lp_esp)>1: # Si la lista tiene más de un proceso...
                lp_esp.sort(key=lambda x: x.t_requerido) # La ordenamos de acuerdo al tiempo de ejecucion
    while lp or lp_esp:
        while not lp_esp: # Si no hay procesos en cola para ronda...
            cola_ejec.append('-') # indicamos que en ese tiempo no se ejecutó nada
            t_total += 1 # Aumentamos un tick
            while lp: # Validamos si algún proceso llegó mientras estabamos ejecutando otro
                if lp[0].t_llegada <= t_total:
                    lp_esp.append(lp[0]) # De ser así, lo ponemos en cola de espera
                    lp = lp[1:]
                else:
                    break
        if len(lp_esp)>1:
            lp_esp.sort(key=lambda x: x.t_requerido) # Ordenamos la lista de acuerdo al tiempo de ejecucion
        p_ejec = lp_esp[0]
        lp_esp = lp_esp[1:]
        while True:
            cola_ejec.append(p_ejec.nombre)
            p_ejec.t_restante -= 1
            t_total +=1
            while lp: # Recorremos la lista para ver si encontramos otro proceso que haya llegado al mismo tiempo
                if lp[0].t_llegada == t_total:
                    lp_esp.append(lp[0]) # De ser así, lo ponemos en cola de espera
                    lp = lp[1:]
                else:
                    break
            if not p_ejec.t_restante: # Si terminamos de ejecutar...
                p_ejec.t_finalizacion = t_total 
                procesos_ejecutados.append(p_ejec)
                break
    return [cola_ejec, procesos_ejecutados]

def fb(lista_procesos=[],n_colas_prioridad=2, ejec_p_degrad=1, quantum=1):
    colas_prioridad = [[] for i in range(n_colas_prioridad)]
    t_total = 0
    cola_ejec = []
    procesos_ejecutados = []
    while lista_procesos:
        if lista_procesos[0].t_llegada <= t_total:
            pass
        else:
            t_total+=1
    return [cola_ejec, procesos_ejecutados]