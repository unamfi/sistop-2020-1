from threading import Thread, Semaphore
from random import randint
from time import sleep

class Alumno(Thread):
    def __init__(self, nombre, preguntas=[]):
        self.nombre = nombre
        self.preguntas = preguntas

    def preguntar(self):
        if not self.preguntas:
            print("No hay mas preguntas por hacer")
            return False
        else:
            pregunta = self.preguntas.pop()

            #mutex.aquire()
            print("Soy " + self.nombre + " y mi pregunta es: " + pregunta)
            #mutex.release()
            
            return pregunta

    def run(self):
        while self.preguntas:
            Thread(target=self.preguntar).start()

class Profesor(Thread):
    def __init__(self, nombre):
        self.nombre = nombre
        self.mut_pregunta = Semaphore(1)

    def responder_duda(self, alumno, pregunta):
        respuesta = 1
        print("Respondo a ")
        return respuesta

    def run(self):
        pass

class Cubiculo(Thread):
    def __init__(self, lugares_max):
        self.lugares_max = lugares_max
        self.lugares_disp = lugares_max
        self.alumnos = []
        self.sem_puerta = Semaphore(3)

    def iniciar_operaciones(self):
        print("Iniciando operación del salón")
        while True:
            sleep(0.5)
            a = Alumno()
            
    def run(self):
        t = Thread(target=self.iniciar_operaciones)
        t.run()