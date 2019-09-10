#!/usr/bin/python3
import threading
import time
from random import randint

class ListaEspera:
    def __init__(self):
        self.lista = []

    def cantidad(self):
        return len(self.lista)

    def hay_alguien(self):
        if self.cantidad() > 0:
            return True
        else:
            return False

    def forma(self, persona):
        self.lista.append(persona)
        print("    Formando a %s (estamos %d esperando)" % (persona.nombre, self.cantidad() ))
        persona.duerme()
    def saca(self):
        p = self.lista.pop(0)
        return p

class Elevador:
    def __init__(self, lugares, pisos_max):
        self.lugares = lugares
        self.pisos_max = pisos_max
        self.piso = 0
        self.pasajeros = []
        self.lista = [ ListaEspera() for i in range(self.pisos_max) ]

    def sube(self):
        time.sleep(0.333)
        if self.piso < (self.pisos_max - 1):
            self.piso += 1
            print("                Elevador subiendo al piso %d" % self.piso )

            if self.lista[self.piso].hay_alguien() and self.lugares > 0:
                persona = self.lista[self.piso].saca()
                self.aborda(persona)

            for pers in self.pasajeros:
                if self.piso == pers.destino:
                    self.bajate(pers)

            return 1
        else:
            print( "                Elevador no puede subir: Estoy en %d" % self.piso)
            return 0

    def baja(self):
        time.sleep(0.3)
        if self.piso > 0:
            self.piso -= 1
            print("                Elevador bajando al piso %d" % self.piso)
            if self.lista[self.piso].hay_alguien() and self.lugares > 0:
                persona = self.lista[self.piso].saca()
                self.aborda(persona)

            for pers in self.pasajeros:
                if self.piso == pers.destino:
                    self.bajate(pers)

            return 1
        else:
            print( "                Elevador no puede bajar: Estoy en %d" % self.piso)
            return 0

    def aborda(self, persona):
        print("                Tomando a %s de la lista, habemos %d" % (persona.nombre, len(self.pasajeros)))
        self.pasajeros.append(persona)
        self.lugares -= 1

    def bajate(self, persona):
        self.pasajeros.remove(persona)
        self.lugares += 1
        persona.despierta(self.piso)
        print("                Sacando a %s de la lista, habemos %d" % (persona.nombre, len(self.pasajeros)))

    def llamada(self, piso, persona):
        # Falta: Subir cuando esté en ese piso
        self.lista[piso].forma(persona)

    def atiende(self):
        print('                El elevador inicia su atención.')
        direccion = 1
        while True:
            while direccion == 1:
                if not self.sube():
                    direccion = 0 - direccion
            while direccion == -1:
                if not self.baja():
                    direccion = 0 - direccion

class Persona:
    def __init__(self, nombre, origen, destino, elev):
        print('Me llamo %s, estoy en %d y voy a %d' % (nombre, origen, destino))
        print('En este momento hay %d hilos en ejecución.' % len(threading.enumerate()))
        self.nombre = nombre
        self.actual = origen
        self.destino = destino
        self.e = elev
        self.dormidor = threading.Semaphore(0)

        if (self.actual != destino):
            self.e.llamada(self.actual, self)

        print('Soy %s.Ya llegué a mi destino: %d = %d' % (nombre, self.actual, destino))
        print('Terminé mi ejecución. Quedan %d hilos en ejecución.' % (len(threading.enumerate())-1))

    def duerme(self):
        self.dormidor.acquire()
    def despierta(self, piso):
        self.actual = piso
        self.dormidor.release()

nombres = ['Juan', 'Pedro', 'Paco', 'Juana', 'Petra', 'Francisca']
apellidos = ['Ap1', 'Ap2', 'Ap3', 'Ap4']

if __name__ == '__main__':
    e = Elevador(5, 5)

    threading.Thread(target=e.atiende, args=[]).start()

    while True:
        nombre = '%s %s' % (nombres[ randint(0, len(nombres)-1) ], apellidos[ randint(0, len(apellidos)-1) ])
        origen = randint(0,4)
        destino = randint(0,4)
        threading.Thread(target=Persona, args=[nombre, origen, destino, e]).start()
        time.sleep(1)
