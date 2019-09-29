from math import floor

class Proceso(object):
    def __init__(self, nombre : str, t_llegada : int, t_requerido : int):
        self.nombre = nombre
        self.t_llegada = t_llegada
        self.t_requerido = t_requerido
        self.t_restante = t_requerido
        self.t_finalizacion = t_llegada + t_requerido
        self.veces_ejecutado = 0
        self.prioridad = 0

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
        self.veces_ejecutado = 0
        self.prioridad = 0

def procesos_entrantes(lista_procesos : list, t : int):
    """Aquí sacamos de la lista los procesos que llegaron en determinado tiempo"""
    lpe = [] # lpe : lista de procesos entrantes
    while lista_procesos:
        if lista_procesos[0].t_llegada == t:
            lpe.append(lista_procesos[0]) # p_ejec : proceso en ejecucion
            lista_procesos = lista_procesos[1:] # Quitamos el primer elemento de la lista
        else:
            break
    return [lpe, lista_procesos]

def fcfs(lista_procesos=[]):
    """First come, first serve.
    Ingresa una lista de procesos ordenados por tiempo de llegada y devuelve la cola de ejecución.
    También devuelve la lista de procesos de entrada con los tiempos de ejecución.

    """
    cola_ejec = []
    procesos_ejecutados = []
    lp = lista_procesos
    t = lp[0].t_llegada

    while lp:
        if lp[0].t_llegada <= t:
            p_ejec = lp[0] # p_ejec : proceso en ejecucion
            lp = lp[1:]

            while p_ejec.t_restante:
                cola_ejec.append(p_ejec.nombre)     
                p_ejec.t_restante -= 1
                t +=1

            p_ejec.t_finalizacion = t
            procesos_ejecutados.append(p_ejec)
        else:
            cola_ejec.append('-')     
            t += 1

    return [cola_ejec, procesos_ejecutados]

def roundrobin(lista_procesos=[], quantum=1):
    """De las implementaciones más feas que he hecho, pero funciona :D"""
    cola_ejec = []
    procesos_ejecutados = []
    ronda_procesos = []
    lp = lista_procesos 
    t = lp[0].t_llegada # Hacemos que inicie desde el proceso que llegó primero
    ronda_procesos.append(lp[0]) # Agregamos el primer proceso a la ronda
    lp = lp[1:] # Removemos el primer valor de la lista
    while lp or ronda_procesos: # Seguimos ejecutando mientras haya procesos, ya sea en ronda o aún sin iniciar
        while not ronda_procesos: # si no hay procesos en cola para ronda...
            [lpn, lp] = procesos_entrantes(lp, t) # verificamos si hay nuevos procesos entrantes en ese tick
            if lpn:
                ronda_procesos += lpn  # de ser así, los agregamos a ronda
            else: # de no serlo...
                cola_ejec.append('-') # indicamos que en ese tiempo no se ejecutó nada
                t += 1 # Aumentamos un tick            
        # p_ejec : proceso en ejecución
        p_ejec = ronda_procesos[0] # Ejecutamos el siguiente proceso en cola para ronda
        trq = quantum # Reiniciamos el contador para el quantum
        while True:
            [lpn, lp] = procesos_entrantes(lp, t) # verificamos si hay nuevos procesos entrantes en ese tick
            if lpn:
                ronda_procesos += lpn  # de ser así, los agregamos a ronda
            cola_ejec.append(p_ejec.nombre)
            p_ejec.t_restante -= 1
            trq -= 1
            t += 1
            if not p_ejec.t_restante: # Si ya ecabamos de ejecutarlo
                p_ejec.t_finalizacion = t
                procesos_ejecutados.append(p_ejec) # Lo mandamos a la lista de procesos ejecutados
                break 
            if not trq: # Si se acaba el tiempo en el quantum
                ronda_procesos.append(p_ejec) # Mandamos el proceso de nuevo a la ronda
                break
        ronda_procesos = ronda_procesos[1:] # Removemos de la lista el proceso que acabamos de ejecutar
    return [cola_ejec, procesos_ejecutados]

def spn(lista_procesos=[]):
    #t = 0
    cola_ejec = []
    procesos_ejecutados = []
    lp_esp = [] # lista de procesos en espera
    lp = lista_procesos 
    t = lp[0].t_llegada # Hacemos que inicie desde el proceso que llegó primero
    [lpn, lp] = procesos_entrantes(lp, t) # Vemos si encontramos otro proceso que haya llegado al mismo tiempo
    if lpn:
        lp_esp += lpn  # de ser así, los agregamos a ronda

    if len(lp_esp)>1: # Si la lista tiene más de un proceso...
        lp_esp.sort(key=lambda x: x.t_requerido) # La ordenamos de acuerdo al tiempo de ejecucion

    while lp or lp_esp:
        while not lp_esp: # Si no hay procesos en cola para ronda...
            cola_ejec.append('-') # indicamos que en ese tiempo no se ejecutó nada
            t += 1 # Aumentamos un tick
            [lpn, lp] = procesos_entrantes(lp, t) # Verificamos si algún proceso llegó mientras ejecutábamos este
            if lpn:
                lp_esp += lpn  # de ser así, lo(s) agregamos a lista
        if len(lp_esp)>1:
            lp_esp.sort(key=lambda x: x.t_requerido) # Ordenamos la lista de acuerdo al tiempo de ejecucion
        p_ejec = lp_esp[0]
        lp_esp = lp_esp[1:]
        while True:
            cola_ejec.append(p_ejec.nombre)
            p_ejec.t_restante -= 1
            t +=1
            [lpn, lp] = procesos_entrantes(lp, t) # Verificamos si algún proceso llegó mientras ejecutábamos este
            if lpn:
                lp_esp += lpn  # de ser así, lo(s) agregamos a lista
            if not p_ejec.t_restante: # Si terminamos de ejecutar...
                p_ejec.t_finalizacion = t 
                procesos_ejecutados.append(p_ejec)
                break
    return [cola_ejec, procesos_ejecutados]

def colas_vacias(lista_colas = []):
    if not lista_colas:
        return True
    for cola in lista_colas:
        if cola:
            return False
    return True

def fb(lista_procesos=[],n_colas_prioridad=4, ejec_p_degrad=1, quantum=1):
    colas_prioridad = [[] for i in range(n_colas_prioridad)] # la cola 0 es la de mayor prioridad
    cola_ejec = []
    procesos_ejecutados = []
    lp = lista_procesos 
    t = lp[0].t_llegada # Hacemos que inicie desde el proceso que llegó primero
    [lpn, lp] = procesos_entrantes(lp, t) # Vemos qué procesos llegaron...
    if lpn:
        colas_prioridad[0] += lpn  # y los agregamos a la cola de prioridad 0
    while lp or not colas_vacias(colas_prioridad): # Seguimos ejecutando mientras haya procesos, ya sea en elguna cola o aún sin llegar
        while colas_vacias(colas_prioridad): # si no hay procesos en ninguna cola...
            [lpn, lp] = procesos_entrantes(lp, t) # verificamos si hay nuevos procesos entrantes en ese tick
            if lpn:
                colas_prioridad[0] += lpn  # de ser así, los agregamos cola de prioridad 0
            else: # de no serlo...
                cola_ejec.append('-') # indicamos que en ese tiempo no se ejecutó nada
                t += 1 # Aumentamos un tick            
        for prioridad_actual, cola_p in enumerate(colas_prioridad):
            if cola_p:
                # p_ejec : proceso en ejecución
                p_ejec = cola_p[0] # Ejecutamos el siguiente proceso en cola de mayor prioridad
                pr_ac = prioridad_actual # Guardar variable para saber de qué lista debemos sacar procesos
                break        
        trq = quantum # Reiniciamos el contador para el quantum

        while True:
            [lpn, lp] = procesos_entrantes(lp, t) # verificamos si hay nuevos procesos entrantes en ese tick
            if lpn:
                colas_prioridad[0] += lpn  # de ser así, los agregamos cola de prioridad 0
            cola_ejec.append(p_ejec.nombre)
            p_ejec.t_restante -= 1
            trq -= 1
            t += 1
            if not p_ejec.t_restante: # Si ya ecabamos de ejecutarlo
                p_ejec.t_finalizacion = t
                p_ejec.veces_ejecutado += 1
                procesos_ejecutados.append(p_ejec) # Lo mandamos a la lista de procesos ejecutados
                break 
            if not trq: # Si se acaba el tiempo en el quantum
                p_ejec.veces_ejecutado += 1
                if p_ejec.prioridad != n_colas_prioridad-1:
                    p_ejec.prioridad = floor(p_ejec.veces_ejecutado / ejec_p_degrad)
                colas_prioridad[p_ejec.prioridad].append(p_ejec) # Mandamos a la cola de prioridad que le corresponda
                break
        colas_prioridad[pr_ac] = colas_prioridad[pr_ac][1:] # Removemos de la lista el proceso que acabamos de ejecutar
    return [cola_ejec, procesos_ejecutados]