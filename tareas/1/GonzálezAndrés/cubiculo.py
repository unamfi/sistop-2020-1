from threading import Thread, Semaphore
from random import randint
from time import sleep
from faker import Faker
#from colorama import init, Fore, Back, Style

class Alumno(Thread):
    #def __init__(self, name, cond_entrada, cond_pregunta, cond_resp, preguntas=[]):
    def __init__(self, name, preguntas=[], sem_entrada = None):
        Thread.__init__(self)
        self.name = name
        self.preguntas = preguntas
        self.sem_entrada = sem_entrada
        #self.cond_entrada = cond_entrada
        #self.cond_pregunta = cond_pregunta
        #self.cond_resp = cond_resp

    def preguntar(self):
        print("\t%s hace una pregunta" % self.name)

    def preguntar_todo(self):
        print("Hola, soy %s y tengo %i pregunta(s)" % (self.name, len(self.preguntas)))
        self.sem_entrada.acquire()
        print("<-- %s entró al cubículo" % self.name)
        for pregunta in self.preguntas:
            Thread(target=self.preguntar).start()
        print("--> %s salió del cubículo" % self.name)
        self.sem_entrada.release()

    def run(self):    
        Thread(target=self.preguntar_todo).start()
        

class Profesor(Thread):
    def __init__(self, name='Fulano', sem_entrada=None):
        Thread.__init__(self)
        self.name = name
        self.sem_entrada = sem_entrada
        self.mut_pregunta = Semaphore(1)

    def responder_duda(self):
        pass

    def responder_dudas(self):
        print("Hola, soy %s e iniciaré a responder dudas..." % self.name)

    def run(self):
        Thread(target=self.responder_dudas).start()

class Cubiculo(Thread):
    def __init__(self, sem_entrada=None, profesor=Profesor('Fulano'), alumnos=[]):
        Thread.__init__(self)
        self.profesor = profesor
        self.sem_entrada = sem_entrada
        self.alumnos = alumnos

    def iniciar_operaciones(self):
        print("Iniciando cubiculo...")
        print("Iniciando al profesor...")
        self.profesor.start()
        print("Iniciando alumnos...")
        for alumno in self.alumnos:
            alumno.start()
            
    def run(self):
        t = Thread(target=self.iniciar_operaciones)
        t.run()