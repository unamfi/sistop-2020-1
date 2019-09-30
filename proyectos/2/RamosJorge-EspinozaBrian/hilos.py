
import threading
import time

def worker():
    print (threading.currentThread().getName(), 'Lanzado  worker')
    #time.sleep(2)
    print (threading.currentThread().getName(), 'Deteniendo worker')

def servicio():
    print (threading.currentThread().getName(), 'Lanzado servicio')
    print (threading.currentThread().getName(), 'Deteniendo servicio')

t = threading.Thread(target=servicio, name='Servicio t' )
w = threading.Thread(target=worker, name='Worker w')
z = threading.Thread(target=worker, name='Worker z') 

w.start()
z.start()
t.start()

# import threading
# from time import sleep

# numeroSemaforos = 1
# semaforo = threading.Semaphore(numeroSemaforos)
# class Hilo(threading.Thread):
#     def __init__(self, id):
#         threading.Thread.__init__(self)
#         self.id = id
#     def run(self):
#         semaforo.acquire()
#         print ('entra hilo',(self.id))
#         #sleep(3)
#         semaforo.release()
        
# hilos = [Hilo(1), Hilo(2), Hilo(3), Hilo(4)]



# for h in hilos:
#     h.start()