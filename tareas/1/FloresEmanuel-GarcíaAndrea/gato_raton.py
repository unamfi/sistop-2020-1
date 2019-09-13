import threading
import sys

mutex = threading.Semaphore(1)
n_platos = threading.Semaphore(int(sys.argv[3]))
ratones = 0
puede_comer = threading.Semaphore(1)

class Gato():
    def __init__(self, num_gato):
        self.num_gato = num_gato
        print("Soy el gato %d y tengo hambre" % (self.num_gato))
        #print('En este momento hay %d hilos en ejecución.' % len(threading.enumerate()))
        self.comerPlato()

    def comerPlato(self):
        global ratones
        puede_comer.acquire()
        puede_comer.release()
        n_platos.acquire()
        print("Soy un gato  %d y estoy comiendo" % (self.num_gato))
        mutex.acquire()
        if ratones != 0:
               print("El gato %d se comió al ratón %d" % (self.num_gato,ratones))
               ratones -= 1
               n_platos.release()
        print('El gato %d ha terminado de comer' % (self.num_gato))
        mutex.release()
        n_platos.release()

class Raton:
    def __init__(self, num_raton):
        self.raton = num_raton
        print("Soy el raton %d y tengo hambre" % (num_raton))
        #print('En este momento hay %d hilos en ejecución.' % len(threading.enumerate()))
        self.comerPlato()

    def comerPlato(self):
        global ratones
        n_platos.acquire()
        mutex.acquire()
        ratones += 1
        if ratones == 1:
            puede_comer.acquire()
        mutex.release()
        print("Soy un ratón %d y estoy comiendo" % (self.raton))
        #n_platos.release()
        print("Soy el ratón %d y terminé de comer" % (self.raton))
        mutex.acquire()
        ratones-=1
        #n_platos.release()
        #print("Soy el ratón %d y terminé de comer" % (self.raton))
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
   #Mientras no se lo indiquemos sigue creando gatos   
    for i in range(num_gatos):
        threading.Thread(target=Gato, args=[i]).start()

    for i in range(num_ratones):
        threading.Thread(target=Raton, args=[i]).start()
   #------------------------------------
