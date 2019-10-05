import threading
import time
import random

resultados = []
procesos = []
ronda = []
mutexActivo = threading.Semaphore(1)
mutexActivo2 = threading.Semaphore(1)

def ejecucion(idProceso,quantum):
    tiempo = 0
    while(len(ronda)>0):
        tiempo += 1
        mutexActivo.acquire()
        aux = ronda[0]
        ronda.pop(0)
        mutexActivo.release()
        if(aux>0):
            aux-=quantum
            if(aux>0):
                mutexActivo2.acquire()
                ronda.append(aux)
                mutexActivo2.release()
        if(aux>0):
            if(len(ronda) == 1):
                tiempo += 0
            elif(len(ronda) == 2):
                tiempo += 1
            elif(len(ronda) == 3):
                tiempo += 2
            elif(len(ronda) == 4):
                tiempo += 3
            elif(len(ronda) == 5):
                tiempo += 4 
        time.sleep(quantum)
    resultados[2][idProceso] = float(tiempo)
    resultados[1][idProceso] = round(float(resultados[2][idProceso] + procesos[2][idProceso]),2)
    resultados[3][idProceso] = round(float(procesos[2][idProceso]) / float(resultados[1][idProceso]),2)
    resultados[4][idProceso] = round(float(resultados[1][idProceso]) / float(procesos[2][idProceso]),2)


def proceso(idProceso,quantum):
    time.sleep(procesos[1][idProceso])
    ronda.append(int(procesos[2][idProceso]))
    ejecucion(idProceso,quantum)

def lanza_hilos(quantum):
    for i in range(5):
        threading.Thread(target=proceso, args=[i,quantum]).start()

def rr(pro, res, quantum):
    global procesos
    global resultados
    resultados = res
    procesos = pro
    lanza_hilos(quantum)
    time.sleep(15)
    if (quantum == 1):
        print("R1")
    if (quantum == 4):
        print("R4")
    for i in range(len(resultados)):
        print("Proceso: %s -> T:%d E:%d P:%d R:%d" %(resultados[0][i],resultados[1][i],resultados[2][i],resultados[3][i],resultados[4][i]))


