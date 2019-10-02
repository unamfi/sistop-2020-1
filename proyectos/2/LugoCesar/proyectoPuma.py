#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading
import random
import time

#Se hace esta declaración porque son las que más se van a reutilizar en el código (de esta forma creo que es más optimo)
global persons
global timeMin

timeMin = 0 #Es el tiempo que que ha transcurrido en minutos
persons = 0 #Numero de personas en la fila (contador)


mutex = threading.Semaphore(1)
pumaBus = threading.Semaphore(0)

#Comemienza el planteamiento de las funciones a utilizar las que se consideran es la funciones del tiempo, las personas y la del puma
#La del tiempo es la que va calculando cunto tiempo ha pasado en minutos si la espera es muy grande se libera el puma
#La de las personas es el caso de la fila enorme, a ojo de buen cubero propuse que las personas dentro de la fila enorme eran 30 aprox
#pero esperar a que lleguen 30 personas me causo demasiada flojera al esperar x.x asi que mejor lo baje a 20 ñwñ
#Finalmente la que creo es la principal la del puma que es la que conjunta los problemas y da la solucion

#definimos una funcion para la impresion de la simulacion del recorrido del PumaBus
def start():

    print(">> Comienza el viaje ¬¬ << ")
    time.sleep(4)
    print ("7w7")
    print ("7w7")
    print ("7w7")
    print ("7w7")
    print(">> Termina el vieje ñuñ <<")


#aquí comienza la definicion de los elementos de la solucion del problema
def person():

    global persons
    mutex.acquire()

    if random.random() <= 0.5: #Añadimos la llegada aleatorea de la cual solo la mitad de las personas se formaran
        persons += 1

    if persons == 20: #Si se llena la fila con 20 personas comienza el viaje del puma
        pumaBus.release()
    mutex.release()

def pumaBus():

    global timeMin
    global persons
    while True:

        pumaBus.acquire()
        mutex.acquire()

        if timeMin == 25:
            start()
            timeMin -= 25 #Vaciamos el contador de minutos
            persons -= persons
        elif persons >= 20:
            start()
            personas -= 20 #Vaciamos la fila
        mutex.release()


def timeInMin():

    global timeMin

    mutex.acquire()

    timeMin += 1

    if timeMin == 25:

        pumaBus.release()

    mutex.release()

#Ahora ponemos el tiempo que va a durar cada uno de nuestros hilos
threading.Thread(target = pumaBus, args = []).start()
while True:
	threading.Thread(target = person, args = []).start()
	time.sleep(0.8)
	threading.Thread(target = timeInMin, args = []).start()
	time.sleep(0.8)
