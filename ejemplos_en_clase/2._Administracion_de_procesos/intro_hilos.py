#!/usr/bin/python3
from threading import Thread, enumerate
from time import sleep
from random import randint

ultimo = 0

def un_hilo(yo):
    global ultimo
    while True:
        print('   ' * yo, '%d%d' % (ultimo, yo) )
        ultimo = yo
        sleep(randint(0,5))

hilos = []
for i in range(10):
    hilo = Thread(target=un_hilo, args=[i], name="Hilo-%s"%i)
    hilo.start()
    hilos.append(hilo)

while True:
    print(enumerate())
    sleep(5)
