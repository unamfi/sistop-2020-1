#!/usr/bin/python3
import threading
import time

mostrar = 1

def par(num):
    global mostrar
    while True:
        while (mostrar == 0):
            pass
        print('%d-%d' % (mostrar,num))
        time.sleep(0.1)
        mostrar = 0

def impar(num):
    global mostrar
    while True:
        while (mostrar == 1):
            pass
        print('%d-%d' % (mostrar,num))
        time.sleep(0.1)
        mostrar = 1

for i in range(3):
    threading.Thread(target=par, args=[i]).start()
    threading.Thread(target=impar, args=[i]).start()
