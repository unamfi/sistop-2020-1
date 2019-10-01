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
