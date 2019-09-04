import threading
import time
import random
mutex = threading.Semaphore(1)
elementos = threading.Semaphore(0)
buffer = []
maximo = 5
cuantos_hay = 0
mutex_cuantos = threading.Semaphore(1)
espera_banda = threading.Semaphore(0)

class Evento:
    global cuantos_hay
    def __init__(self):
        self.ident = random.random()
        print "Generando evento %1.3f, hay %d en cola" % (self.ident, cuantos_hay)
        time.sleep(self.ident)
    def process(self):
        print "Procesando evento %1.3f, hay %d en cola" % (self.ident, cuantos_hay)
        time.sleep(self.ident)


def productor():
    global cuantos_hay
    while True:
        event = Evento()

        if cuantos_hay >= maximo:
            print "Esperando por la banda (hay %d)" % cuantos_hay
            espera_banda.acquire()
        mutex_cuantos.acquire()
        cuantos_hay += 1
        mutex_cuantos.release()

        mutex.acquire()
        buffer.append(event)
        mutex.release()
        elementos.release()

def consumidor():
    global cuantos_hay
    while True:
        elementos.acquire()
        mutex.acquire()
        event = buffer.pop()
        mutex.release()

        if cuantos_hay == maximo:
            print "Liberando la banda (hay %d)" % cuantos_hay
            espera_banda.release()
        mutex_cuantos.acquire()
        cuantos_hay -= 1
        mutex_cuantos.release()

        event.process()

threading.Thread(target=productor, args=[]).start()
threading.Thread(target=productor, args=[]).start()
threading.Thread(target=productor, args=[]).start()
threading.Thread(target=consumidor, args=[]).start()
