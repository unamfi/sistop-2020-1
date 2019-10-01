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
