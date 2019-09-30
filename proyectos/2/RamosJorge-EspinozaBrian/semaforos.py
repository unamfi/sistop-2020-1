import threading
from time import sleep

listSemaphore=list()

numeroSemaforos = 1
semaforo = threading.Semaphore(numeroSemaforos)
class Hilo(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
    def run(self):
        #semaforo.acquire()
        print ('entra hilo',(self.id))
        #sleep(3)
        # semaforo.release()
        
# hilos = [Hilo(1), Hilo(2), Hilo(3), Hilo(4)]

hilos=list()
for i in range (50):
    hilos.append(Hilo(i))

for h in hilos:
    h.start()

