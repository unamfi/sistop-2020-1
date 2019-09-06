#!/usr/bin/python3
import threading
import time
from random import randint

class ListaEspera:
    def __init__(self):
        self.lista = []
    def forma(self, persona):
        self.lista.append(persona)
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
        time.sleep(1)
        if self.piso < self.pisos_max:
            self.piso += 1
            print("Elevador subiendo al piso %d" % self.piso )
            return 1
        else:
            print( "Elevador no puede subir: Estoy en %d" % self.piso)
            return 0

    def baja(self):
        time.sleep(0.9)
        if self.piso > 0:
            self.piso -= 1
            print("Elevador bajando al piso %d" % self.piso)
            return 1
        else:
            print( "Elevador no puede bajar: Estoy en %d" % self.piso)
            return 0

    def aborda(self, persona):
        pass

    def bajate(self, persona):
        pass

    def llamada(self, piso, persona):
        # Falta: Subir cuando esté en ese piso
        self.lista[piso].forma(persona)

    def atiende(self):
        print('El elevador inicia su atención.')
        direccion = 1
        while True:
            while direccion == 1:
                if not self.sube():
                    direccion = 0 - direccion
            while direccion == -1:
                if not self.baja():
                    direccion = 0 - direccion

class Persona:
    global e
    def __init__(self, nombre, origen, destino):
        print('Me llamo %s, estoy en %d y voy a %d' % (nombre, origen, destino))
        self.nombre = nombre
        self.actual = origen
        self.destino = destino
        self.dormidor = threading.Semaphore(0)

        while (actual != destino):
            e.llamada(self.actual, self)

        print('Soy %s.Ya llegué a mi destino: %d = %d' % (nombre, actual, destino))

    def duerme(self):
        self.dormidor.aquire()
    def despierta(self):
        self.dormidor.release()

nombres = ['Juan', 'Pedro', 'Paco', 'Juana', 'Petra', 'Francisca']
apellidos = ['Ap1', 'Ap2', 'Ap3', 'Ap4']

if __name__ == '__main__':
    e = Elevador(5, 5)

    threading.Thread(target=e.atiende, args=[])
    #e.atiende()

    while True:
        nombre = '%s %s' % (nombres[ randint(0, len(nombres)-1) ], apellidos[ randint(0, len(apellidos)-1) ])
        origen = randint(0,5)
        destino = randint(0,5)
        #threading.Thread(target=Persona, args=[nombre, origen, destino])
        time.sleep(0.1)
