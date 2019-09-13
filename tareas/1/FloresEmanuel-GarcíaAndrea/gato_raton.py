import threading
import sys

#Protege la variable ratones
mutex = threading.Semaphore(1)
#Protege la variable gatos
mutexg = threading.Semaphore(1)
#Se usa el patrón multiplex para verificar, que únicamente un animal coma a la vez de un plato, por lo que los animales comiendo a la vez en todos los platos no deben sobrepasar el número de platos que se le pasa como parámetro
n_platos = threading.Semaphore(int(sys.argv[3]))
ratones = 0
gatos = 0
#Se utiliza para checar la condición de que ningún gato puede acercarse cuando hay ratones comiendo, utiliza el patrón apagador
puede_comer = threading.Semaphore(1)

class Gato():
    def __init__(self, num_gato):
        self.num_gato = num_gato
        print("Soy el gato %d y tengo hambre" % (self.num_gato))
        self.comerPlato()

    def comerPlato(self):
        global gatos
        #Una vez que se valida que no hay ratones, procedemos a comer 
        puede_comer.acquire()
        #Permite que los ratones se acerquen a comer aunque haya gatos comiendo
        puede_comer.release()
        #Pide un plato
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
        #Pide un plato
        n_platos.acquire()
        mutex.acquire()
        ratones += 1
        #Si es el primer ratón que llega y enciende el apagador indicando que los ratones están comiendo
        if ratones == 1:
            puede_comer.acquire()
        mutex.release()
        print("Soy el ratón %d y estoy comiendo" % (self.raton))
        #Revisa que no haya gatos comiendo        
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
        #Una vez que todos los ratones se hayan ido, apaga e indica que ahora los gatos pueden comer
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
