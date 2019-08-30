#!/usr/bin/python3
import threading
import time

mostrar = 1
candado = threading.Lock()

def par(num):
    global mostrar
    while True:
        candado.acquire()
        print('%d-%d' % (mostrar,num))
        mostrar = 0
        candado.release()
        time.sleep(0.1)

def impar(num):
    global mostrar
    while True:
        candado.acquire()
        print('%d-%d' % (mostrar,num))
        mostrar = 1
        candado.release()
        time.sleep(0.1)

threading.Thread(target=par, args=[0]).start()
threading.Thread(target=impar, args=[1]).start()
