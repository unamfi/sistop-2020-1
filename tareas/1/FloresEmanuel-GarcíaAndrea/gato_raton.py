import threading
import sys

mutex = threading.Semaphore(1)
mutexg = threading.Semaphore(1)
n_platos = threading.Semaphore(int(sys.argv[3]))
ratones = 0
gatos = 0
puede_comer = threading.Semaphore(1)

class Gato():
    def __init__(self, num_gato):
        self.num_gato = num_gato
        print("Soy el gato %d y tengo hambre" % (self.num_gato))
        #print('En este momento hay %d hilos en ejecuci贸n.' % len(threading.enumerate()))
        self.comerPlato()

    def comerPlato(self):
        global gatos
        puede_comer.acquire()
        puede_comer.release()
        n_platos.acquire()
        print("Soy el gato  %d y estoy comiendo" % (self.num_gato))
        mutexg.acquire()
        gatos = gatos +1
        mutexg.release()
        print('El gato %d ha terminado de comer' % (self.num_gato))
        mutexg.acquire()
        gatos = gatos -1
        mutexg.release()
        n_platos.release()

class Raton:
    def __init__(self, num_raton):
        self.raton = num_raton
        self.vivo = True
        print("Soy el raton %d y tengo hambre" % (num_raton))
        self.comerPlato()

    def comerPlato(self):
        global ratones, gatos
        n_platos.acquire()
        mutex.acquire()
        ratones += 1
        if ratones == 1:
            puede_comer.acquire()
        mutex.release()
        print("Soy el ratón %d y estoy comiendo" % (self.raton))
        mutexg.acquire()
        if(gatos > 0):
            self.vivo = False
        mutexg.release()
        if(self.vivo == True):
            print("Soy el ratón %d y terminé de comer" % (self.raton))                
        else:
            print("Se han comido al ratón %d" % (self.raton))        
        mutex.acquire()
        ratones-=1
        if ratones == 0:
            puede_comer.release()
        mutex.release()
        n_platos.release()


if __name__ == '__main__':

   # Recupera el valor de los argumentos
    num_gatos = int(sys.argv[1])
    num_ratones = int(sys.argv[2])

   #------------------------------------
   #Inicia los hilos
   #Genera la cantidad de gatos y ratones que se le indique   
    for i in range(num_gatos):
        threading.Thread(target=Gato, args=[i]).start()

    for i in range(num_ratones):
        threading.Thread(target=Raton, args=[i]).start()
   #------------------------------------
