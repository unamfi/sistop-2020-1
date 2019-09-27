# -*- coding: utf-8 -*-
#%%
import sys, getopt
import numpy as np
import string
import algoritmos_planeacion as ap

def crear_procesos(num_procesos = 5, llegada_max = 10, requerido_max = 10, seed = None):
    np.random.seed(seed)    
    nombre_procesos = np.array(list(string.ascii_uppercase))
    if llegada_max==0:
        tiempos_llegadas = np.zeros(num_procesos)
    else:
        tiempos_llegadas = np.sort(np.random.randint(low='0', high=llegada_max, size=num_procesos))
    tiempos_requeridos = np.random.randint(low='1', high=requerido_max, size=num_procesos)
    lista_procesos = []
    for i in range(num_procesos):
        nombre = nombre_procesos[i]
        tiempo_llegada = tiempos_llegadas[i]
        tiempo_requerido = tiempos_requeridos[i]
        lista_procesos.append(ap.Proceso(nombre, tiempo_llegada, tiempo_requerido))
        print("%s: t_llegada=%d, t_requerido=%d." % (nombre, tiempo_llegada, tiempo_requerido))
    return lista_procesos

def test_fcfs(lista_procesos):
    [cola_ejecucion, procesos_ejecutados] = ap.fcfs(lista_procesos)

    T = [proceso.t_respuesta for proceso in procesos_ejecutados]
    T = np.mean(T)
    E = [proceso.t_espera for proceso in procesos_ejecutados]
    E = np.mean(E)
    P = [proceso.p_penalizacion for proceso in procesos_ejecutados]
    P = np.mean(P)

    print('\nFCFS: T=%.2f, E=%.2f, P=%.2f' % (T, E, P))
    print(''.join(cola_ejecucion))

def test_roundrobin(lista_procesos, quantum):
    for p in lista_procesos:
        p.reset() # Reiniciamos los procesos a sus valores iniciales
    [cola_ejecucion, procesos_ejecutados] = ap.roundrobin(lista_procesos, quantum)

    T = [proceso.t_respuesta for proceso in procesos_ejecutados]
    T = np.mean(T)
    E = [proceso.t_espera for proceso in procesos_ejecutados]
    E = np.mean(E)
    P = [proceso.p_penalizacion for proceso in procesos_ejecutados]
    P = np.mean(P)

    print('\nRR%d: T=%.2f, E=%.2f, P=%.2f' % (quantum, T, E, P))
    print(''.join(cola_ejecucion))

def test_spn(lista_procesos):
    for p in lista_procesos:
        p.reset() # Reiniciamos los procesos a sus valores iniciales
    [cola_ejecucion, procesos_ejecutados] = ap.spn(lista_procesos)

    T = [proceso.t_respuesta for proceso in procesos_ejecutados]
    #print(T)
    T = np.mean(T)
    E = [proceso.t_espera for proceso in procesos_ejecutados]
    #print(E)
    E = np.mean(E)
    P = [proceso.p_penalizacion for proceso in procesos_ejecutados]
    #print(P)
    P = np.mean(P)

    print('\nSPN: T=%.2f, E=%.2f, P=%.2f' % (T, E, P))
    print(''.join(cola_ejecucion))

def test_fb(lista_procesos, n_cp, ej_d, quantum):
    for p in lista_procesos:
        p.reset() # Reiniciamos los procesos a sus valores iniciales
    [cola_ejecucion, procesos_ejecutados] = ap.fb(lista_procesos, n_cp, ej_d, quantum)

    T = [proceso.t_respuesta for proceso in procesos_ejecutados]
    T = np.mean(T)
    E = [proceso.t_espera for proceso in procesos_ejecutados]
    E = np.mean(E)
    P = [proceso.p_penalizacion for proceso in procesos_ejecutados]
    P = np.mean(P)

    print(('\nFB: T=%.2f, E=%.2f, P=%.2f, '+
            '(n_colas_prioridad = %d, ejec_para_degradado = %d, quantum = %d)')
                % (T, E, P, n_cp, ej_d, quantum))
    print(''.join(cola_ejecucion))

def main(argv):

    num_procesos = 5
    llegada_max = 10
    requerido_max = 10
    seed = None

    try:
        opts, args = getopt.getopt(argv,"hp:l:t:s:",["procesos=","llegada_max=","requerido_max=","semilla="])
    except getopt.GetoptError:
        print("uso: tarea2.py -p <num de procesos> -l <t de llegada máx.> -t <t requerido máx.> -s <semilla>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("uso: tarea2.py -p <num de procesos> -l <t de llegada máx.> -t <t requerido máx.> -s <semilla>")
            print("El número de procesos debe estar entre 1 y 26")
            print("El tiempo máximo de llegada debe ser un número positivo")
            print("El tiempo requerido máximo debe ser un número mayor a 0")
            sys.exit()
        elif opt in ("-p", "--procesos"):
            num_procesos = int(arg)
            if num_procesos<=0 or num_procesos>26:
                print("El número de procesos debe ser entre 1 y 26")
                sys.exit(2)
        elif opt in ("-l", "--tiempo_llegada"):
            llegada_max = int(arg)
            if llegada_max<0:
                print("El tiempo máximo de llegada debe ser un número positivo")
                sys.exit(2)
        elif opt in ("-t", "--tiempo_requerido"):
            requerido_max = int(arg)
            if requerido_max<1:
                print("El tiempo máximo requerido debe ser un número mayor a 0")
                sys.exit(2)
        elif opt in ("-s", "--seed"):
            seed = int(arg)

    lista_procesos = crear_procesos(num_procesos, llegada_max, requerido_max, seed)

    test_fcfs(lista_procesos) # FIFO
    
    test_roundrobin(lista_procesos, 1) # Round Robin 1
    
    test_roundrobin(lista_procesos, 2) # Round Robin 2
    
    test_roundrobin(lista_procesos, 4) # Round Robin 4

    test_spn(lista_procesos) # SPN

    test_fb(lista_procesos, 4, 1, 1) # Multilevel Feedback n=4, e=1, q=1

    test_fb(lista_procesos, 4, 2, 2) # Multilevel Feedback n=4, e=2, q=2

    test_fb(lista_procesos, 4, 4, 1) # Multilevel Feedback n=4, e=3, q=1

    test_fb(lista_procesos, 4, 1, 4) # Multilevel Feedback n=4, e=3, q=1

if __name__ == "__main__":
    # for i in range(5):
    #     print('\n\n---- Ronda %i ----\n' % (i+1))
    #     main([])
    main(sys.argv[1:])
