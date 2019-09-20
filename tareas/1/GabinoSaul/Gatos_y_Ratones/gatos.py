"""
Problema: Gatos y ratones

Realizado en python
"""
import threading
import time
import random
mutex = threading.Semaphore(1) 
mutex2 = threading.Semaphore(1) 
hay_platos = threading.Semaphore(0)
Platos = []
animales = []
comiendo = 0
MaxEat = 1
EComiendo = threading.Semaphore(0)
acabado = 0

class plato:
    def __init__(self):
        self.plato = random.random()
        print ("Sirviendo comida al plato  %1.3f" % self.plato)
        time.sleep(self.plato*1/3)
    def comido(self):
        numero=self.plato
        time.sleep(self.plato*2/3)
        return(numero)
class cats:
    def __init__(self):
        self.cats = random.random()
        print ("llego el gato numero %1.3f" % self.cats)
        time.sleep(self.cats)
    def numero(self):
        numero=self.cats
        return(numero)
class ratones:
    def __init__(self):
        self.ratones = random.random()
        print ("salio el raton numero %1.3f" % self.ratones)
        time.sleep(self.ratones)
    def numero(self):
        numero=self.ratones
        return(numero)
    

def pongo_plato():
    global comiendo
    global MaxEat
    global acabado
    while True:
        numero = plato().comido()
        evento = plato()
        mutex2.acquire()
        if comiendo < 0:
            comiendo=0
        if comiendo == MaxEat:
            mutex2.release()
            if(acabado != 0):
                print ("Alguien comio el plato (%1.3f)" % acabado)
            EComiendo.acquire()
        else:
            mutex2.release()
            print ("Puede alguien comerse el plato (%1.3f)" % numero)
            comiendo += 1

        mutex.acquire()
        Platos.append(evento)
        if (len(animales) != 0):
            anim=animales.pop()
        mutex.release()
        hay_platos.release()

def gato():
    global comiendo
    global MaxEat
    global acabado
    while True:
        numero = plato().comido()
        evento=cats()
        animal_n = cats().numero()
        hay_platos.acquire() 
        mutex2.acquire()
        if comiendo == MaxEat:
            print ("\tEl gato(%1.3f) tiene mucha hambre, y comera del plato (%1.3f)"%(animal_n,  numero))
            acabado = numero
            EComiendo.release()
        mutex2.release()
        mutex.acquire()
        comiendo -= 1
        animales.append(evento)
        plat = Platos.pop()
        mutex.release()
def raton():
    global comiendo
    global MaxEat
    global acabado
    while True:
        numero = plato().comido()
        evento= ratones()
        animal_n=ratones().numero()
        hay_platos.acquire()
        mutex2.acquire()
        if comiendo == MaxEat:
            print ("\t\tEl raton (%1.3f) voy a comer (%1.3f)" % (animal_n, numero))
            acabado = numero
            EComiendo.release()
        mutex2.release()
        mutex.acquire()
        comiendo -= 1
        animales.append(evento)
        plat = Platos.pop()
        mutex.release()
#inicio de hilos
threading.Thread(target=pongo_plato, args=[]).start()
threading.Thread(target=gato, args=[]).start()
threading.Thread(target=raton, args=[]).start()