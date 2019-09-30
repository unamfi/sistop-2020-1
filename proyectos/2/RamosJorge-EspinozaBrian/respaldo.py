import threading
from time import sleep

numeroSemaforos = 1
semaforo = threading.Semaphore(numeroSemaforos) 

hilos= list()



def imprime():
    for i in range(10):
        #semaforo.acquire()
        print ('soy el hilo',threading.currentThread().getName())
        #semaforo.release()

 
for i in range (3):
    hilos.append (threading.Thread(target=imprime, name=i+1))

for i in range(3):
    hilos[i].start()
    







import threading
from threading import Semaphore
from time import sleep

numeroSemaforos = 1
semaforo = threading.Semaphore(numeroSemaforos) 

hilos= list()
semaforos=list()
baños=list()
mutex = Semaphore(1)

numeroSemaforos=4

for i in range (numeroSemaforos):
    semaforos.append(Semaphore())
    baños.append(Semaphore())

def imprime():
    mutex.acquire()
    semaforos[0].acquire()
    semaforos[1].acquire()
    semaforos[2].acquire()
    print ('soy la persona',threading.currentThread().getName(),'')        
    j=int((threading.currentThread().getName()))%2
    baños[j].acquire()
    print('la persona',threading.currentThread().getName(),' esta en el baño',j)
    baños[j].release()
    semaforos[0].release()
    semaforos[1].release()
    semaforos[2].release()
    mutex.release()

numeroHilos=10




for i in range (numeroHilos):
    hilos.append (threading.Thread(target=imprime, name=i+1))

for i in range(numeroHilos):
    hilos[i].start()
    

