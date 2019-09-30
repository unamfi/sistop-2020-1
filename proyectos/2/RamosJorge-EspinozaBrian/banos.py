import threading
from threading import Semaphore
from time import sleep

numeroSemaforos = 1
semaforo = threading.Semaphore(numeroSemaforos) 

hilos= list()
semaforos=list()
baños=list()
mutex = Semaphore()

numeroBaños=2

for i in range (numeroBaños):
    semaforos.append(Semaphore())
    baños.append(Semaphore())

def imprime():
    mutex.acquire()
    print ('soy la persona',threading.currentThread().getName(),'')        
    baños[0].acquire()
    baños[1].acquire()
    print('la persona',threading.currentThread().getName(),' esta en el baño')
    baños[0].release()
    baños[1].release()
    mutex.release()
    sleep(2)

numeroHilos=100

for i in range (numeroHilos):
    hilos.append (threading.Thread(target=imprime, name=i+1))

for i in range(numeroHilos):
    hilos[i].start()
    

