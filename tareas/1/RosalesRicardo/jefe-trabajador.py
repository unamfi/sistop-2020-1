#Realizando el programa de tarea de Sistemas Operativos 

import threading
import time 
from random import randint

m = threading.Semaphore(1)

#Servidor que crea los trabajadores que se encargan de completar la peticion de busqueda
class Jefe:

    def __init__ (self):
        self.trabajadores = []

        for k in range(100):
            self.trabajadores.append(Trabajor(k))

    def nuevaBusqueda(self , direccion):
        m.acquire()
        n = randint(0, len(self.trabajadores)-1)
        if(self.trabajadores[n].disponible):
            print("Trabajador %d , Yo me encargo" %(n) )
            self.trabajadores[n].asignarTarea(direccion)
        m.release()

#Objeto que maneja los eventos de búsqueda para que seven acabo 
class Trabajor:

    def __init__(self, value):
        self.pagina = value
        self.direccion = None
        self.tiempo = None 
        self.disponible = True

    def asignarTarea(self , value):
        self.disponible = False 
        self.tiempo = randint(0,10)
        self.direccion = value
        time.sleep(self.tiempo)
        self.terminar() 


    def terminar(self):
        self.disponible = True 
        print("-------------")
        print("Pagina buscada %s , Tarde %d" %(self.direccion, self.tiempo))
        print("Conexion satisfactoria")
        print("-------------")
        return 


paginas = ["youtube.com" , "facebook.com" , "messenger.com", "google.com", "debian.org" , "www.ingenieria.unam.mx"]

def __main__():
    j = Jefe()


    while True:
        
        pagina = paginas[ randint(0, len(paginas)-1) ]
        print("Solicitando pagina %s" %pagina)
        threading.Thread(target = j.nuevaBusqueda , args = [pagina] ).start()
        time.sleep(1)

__main__()