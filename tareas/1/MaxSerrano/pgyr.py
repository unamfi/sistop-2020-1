#Hecho por Max Serrano
#Sistop-2020-1
#Ejercicio: gatos y ratones
#Lenguaje: Python version 3.7

import threading
import time
import random

mutex1 = threading.Semaphore(1)  # protege linea_de_platos
mutex2 = threading.Semaphore(1) # protege a "comer"
platos = threading.Semaphore(0)# protege el plato
l_platos = []#platos de comida generados y guardados
gyr = []#guarda los gatos y ratones comiendo
comer = 0#saber si alguien come
c_comen = 1#no pueden comer 1 a la vez
comiendo = threading.Semaphore(0)#quien come
p_vacio = 0 #platos que ya estan vacios


class plato:
    def __init__(self):
        self.plato = random.random()
        print ("plato con comida # %1.3f" % self.plato)
        time.sleep(self.plato*1/3)
    def vacio(self):
        numero=self.plato
        time.sleep(self.plato*2/3)
        return(numero) 

class mushus:
    def __init__(self):
        self.mushus = random.random()
        print ("Generando al gato # %1.3f" % self.mushus)
        time.sleep(self.mushus)
    def numero(self):
        numero=self.mushus
        return(numero)

class ratones:
    def __init__(self):
        self.ratones = random.random()
        print ("Generando al raton # %1.3f" % self.ratones)
        time.sleep(self.ratones)
    def numero(self):
        numero=self.ratones
        return(numero)

def hay_plato():
    global comer
    global c_comen
    global p_vacio
    while True:
        numero = plato().vacio()
        evento = plato()#plato con comida
        mutex2.acquire()
        if comer < 0:#variable comer - 
            comer=0
        if comer == c_comen:
            mutex2.release()
            if(p_vacio != 0):# platos vacios se indica
                print ("¡Alguien se comio el plato (%1.3f)" % p_vacio)
            comiendo.acquire()
        else:
            mutex2.release()
            print ("Alguien quiere comer (%1.3f)" % numero)
            comer += 1

        mutex1.acquire()
        l_platos.append(evento)
        if (len(gyr) != 0):
            animales=gyr.pop()#se saca al animal que ya comio
        mutex1.release()
        platos.release()#se libera el semaforo porque ya hay un plato disponible

def gato():
    global comer
    global c_comen
    global p_vacio
    while True:
        numero = plato().vacio()
        evento=mushus()#se generan gatos 
        animal = mushus().numero()
        platos.acquire() #se trae el semaforo para comer
        mutex2.acquire()
        if comer == c_comen:#si pueden comer 
            print ("\tSoy un gato (%1.3f)y voy  a comer este(%1.3f)"%(animal,  numero))
            p_vacio = numero#para saber que plato esta vacio
            comiendo.release()
        mutex2.release()
        mutex1.acquire()
        comer -= 1
        gyr.append(evento)#se agrega al gato generado
        plat = l_platos.pop()#se saca el plato vacio
        mutex1.release()

def raton():
    global comer
    global c_comen
    global p_vacio
    while True:
        numero = plato().vacio()
        evento= ratones()#se generan ratones 
        animal=ratones().numero()
        platos.acquire()#se trae el semaforo para comer 
        mutex2.acquire()
        if comer == c_comen:#si pueden comer 
            print ("\t\tSoy el RATON (%1.3f) y voy a comer  este(%1.3f)" % (animal, numero))
            p_vacio = numero#para saber que plato fue comido
            comiendo.release()
        mutex2.release()
        mutex1.acquire()
        comer -= 1
        gyr.append(evento)#se agrega al raton 
        plat = l_platos.pop()#se saca el plato vacio
        mutex1.release()

#iniciando hilos
threading.Thread(target=hay_plato, args=[]).start()
threading.Thread(target=gato, args=[]).start()
threading.Thread(target=raton, args=[]).start()






