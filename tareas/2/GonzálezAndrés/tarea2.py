# -*- coding: utf-8 -*-
#%%
import sys, getopt
import numpy as np
import string
import algoritmos_planeacion as ap

def main(argv):

    num_procesos = 5
    seed = None

    try:
        opts, args = getopt.getopt(argv,"hp:s:",["procesos=","seed="])
    except getopt.GetoptError:
        print("uso: tarea2.py -p <num de procesos> -s <seed>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("uso: tarea2.py -p <num de procesos> -s <seed>")
            print("El número de procesos debe ser entre 1 y 26")
            sys.exit()
        elif opt in ("-p", "--procesos"):
            num_procesos = int(arg)
            if num_procesos<=0 or num_procesos>26:
                print("El número de procesos debe ser entre 1 y 26")
                sys.exit(2)
        elif opt in ("-s", "--seed"):
            seed = int(arg)

    np.random.seed(seed)

    nombre_procesos = np.array(list(string.ascii_uppercase))
    tiempos_llegadas = np.sort(np.random.randint(low='0', high='35', size=26))
    tiempos_requeridos = np.random.randint(low='1', high='10', size=26)

    lista_procesos = []

    for i in range(num_procesos):
        nombre = nombre_procesos[i]
        tiempo_llegada = tiempos_llegadas[i]
        tiempo_requerido = tiempos_requeridos[i]
        lista_procesos.append(ap.Proceso(nombre, tiempo_llegada, tiempo_requerido))
        print("%s: t_llegada=%d, t_requerido=%d." % (nombre, tiempo_llegada, tiempo_requerido))

    # FIFO
    [cola_ejecucion, procesos_ejecutados] = ap.fcfs(lista_procesos)

    T = [proceso.t_respuesta for proceso in procesos_ejecutados]
    T = np.mean(T)
    E = [proceso.t_espera for proceso in procesos_ejecutados]
    E = np.mean(E)
    P = [proceso.p_penalizacion for proceso in procesos_ejecutados]
    P = np.mean(P)

    print('\nFCFS: T=%.2f, E=%.2f, P=%.2f' % (T, E, P))
    print(''.join(cola_ejecucion))
    
    # Round Robin 1
    for p in lista_procesos:
        p.reset() # Reiniciamos los procesos a sus valores iniciales
    [cola_ejecucion, procesos_ejecutados] = ap.roundrobin(lista_procesos, 1)

    T = [proceso.t_respuesta for proceso in procesos_ejecutados]
    T = np.mean(T)
    E = [proceso.t_espera for proceso in procesos_ejecutados]
    E = np.mean(E)
    P = [proceso.p_penalizacion for proceso in procesos_ejecutados]
    P = np.mean(P)

    print('\nRR1: T=%.2f, E=%.2f, P=%.2f' % (T, E, P))
    print(''.join(cola_ejecucion))

    # Round Robin 4
    for p in lista_procesos:
        p.reset() # Reiniciamos los procesos a sus valores iniciales
    [cola_ejecucion, procesos_ejecutados] = ap.roundrobin(lista_procesos, 4)

    T = [proceso.t_respuesta for proceso in procesos_ejecutados]
    T = np.mean(T)
    E = [proceso.t_espera for proceso in procesos_ejecutados]
    E = np.mean(E)
    P = [proceso.p_penalizacion for proceso in procesos_ejecutados]
    P = np.mean(P)

    print('\nRR4: T=%.2f, E=%.2f, P=%.2f' % (T, E, P))
    print(''.join(cola_ejecucion))

    # SPN
    for p in lista_procesos:
        p.reset() # Reiniciamos los procesos a sus valores iniciales
    [cola_ejecucion, procesos_ejecutados] = ap.spn(lista_procesos)

    T = [proceso.t_respuesta for proceso in procesos_ejecutados]
    T = np.mean(T)
    E = [proceso.t_espera for proceso in procesos_ejecutados]
    E = np.mean(E)
    P = [proceso.p_penalizacion for proceso in procesos_ejecutados]
    P = np.mean(P)

    print('\nSPN: T=%.2f, E=%.2f, P=%.2f' % (T, E, P))
    print(''.join(cola_ejecucion))

if __name__ == "__main__":
    main(sys.argv[1:])
