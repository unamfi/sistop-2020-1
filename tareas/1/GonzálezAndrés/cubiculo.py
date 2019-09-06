from threading import Thread, Semaphore
from random import randint
from time import sleep
from faker import Faker
class Alumno(Thread):
    def __init__(self, nombre, preguntas=[], cubiculo=None):
        self.nombre = nombre
        self.preguntas = preguntas
        self.cubiculo = cubiculo
        self.ya_acabe = Semaphore(0)

    def preguntar(self):
        if not self.preguntas:
            print("No hay mas preguntas por hacer")
            return False
        else:
            #self.cubiculo.profesor.mut_pregunta.acquire()
            pregunta = self.preguntas.pop()
            sleep(0.5)
            print(self.nombre + "pregunta : " + pregunta)
            return pregunta

    def preguntar_todo(self):
        self.cubiculo.sem_puerta.acquire()
        print("--> Entró al salon: " + self.nombre + " con " + str(len(self.preguntas)) + " preguntas")

        num_preg = len(self.preguntas)
        for _ in range(num_preg):
            #Thread(target=self.preguntar).start()
            self.preguntar()
        print("<-- Salió del salon: " + self.nombre)
        self.cubiculo.sem_puerta.release()

    def run(self):        
        Thread(target=self.preguntar_todo).start()
        

class Profesor(Thread):
    def __init__(self, nombre):
        self.nombre = nombre
        self.mut_pregunta = Semaphore(1)

    def responder_duda(self):
        respuesta = 1
        print("Respondo a ")
        return respuesta

    def responer_dudas(self):
        pass

    def run(self):
        Thread(target=self.responder_dudas).start()

class Cubiculo(Thread):
    def __init__(self, sillas, profesor, alumnos=[]):
        self.sillas = sillas
        self.profesor = profesor
        self.lugares_disp = sillas
        self.alumnos = alumnos
        self.sem_puerta = Semaphore(sillas)

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)
        return True

    def sacar_alumno(self, alumno):
        self.alumnos.remove(alumno)
        return True

    def iniciar_operaciones(self):
        print("Iniciando operación del salón")

        fake = Faker()
        preg_max = 6
        for _ in range(10):
            preguntas = ['preg'+str(i) for i in range(randint(1,preg_max))]       
            a = Alumno(fake.name(), preguntas, self)
            a.run()
            
    def run(self):
        t = Thread(target=self.iniciar_operaciones)
        t.run()

class Monitor(Thread):
    pass