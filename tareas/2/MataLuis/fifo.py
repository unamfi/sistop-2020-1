import threading
import time
import random

resultados = []
tiempos = []
tiempoEspera = 0
mutexActivo = threading.Semaphore(1)
torniquete = threading.Semaphore()

def ejecucion(idProceso):
    global tiempoEspera
    if(tiempoEspera == 0):
        resultados[2][idProceso] = tiempoEspera
        resultados[1][idProceso] = tiempos[2][idProceso]
        tiempoEspera = tiempos[2][idProceso] + tiempos[1][idProceso]
    else:
        aux = tiempoEspera - tiempos[1][idProceso]
        resultados[2][idProceso] = round(aux,2)
        resultados[1][idProceso] = round(resultados[2][idProceso] + tiempos[2][idProceso],2)
        tiempoEspera += tiempos[2][idProceso]
    resultados[3][idProceso] = round(float(tiempos[2][idProceso] / resultados[1][idProceso]),2)
    resultados[4][idProceso] = round(float(resultados[1][idProceso] / tiempos[2][idProceso]),2)


def proceso(idProceso):
    global tiempos
    torniquete.release()
    torniquete.acquire()
    time.sleep(tiempos[1][idProceso])
    torniquete.release()
    mutexActivo.acquire()
    ejecucion(idProceso)
    mutexActivo.release()


def lanza_hilos():
    for i in range(5):
        threading.Thread(target=proceso, args=[i]).start()


def ff(ti, res):
    global tiempos
    global resultados
    resultados = res
    tiempos = ti
    lanza_hilos()
    time.sleep(15)
    print("FCFS")
    for i in range(len(resultados)):
        print("Proceso: %s -> T:%d E:%d P:%d R:%d" %(resultados[0][i],resultados[1][i],resultados[2][i],resultados[3][i],resultados[4][i]))








