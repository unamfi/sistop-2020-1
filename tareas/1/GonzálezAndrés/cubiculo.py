from threading import Thread, Semaphore
from random import randint
from time import sleep
from faker import Faker
#from colorama import init, Fore, Back, Style

class Alumno(Thread):
    #def __init__(self, name, cond_entrada, cond_pregunta, cond_resp, preguntas=[]):
    def __init__(self, name, preguntas_alumno=[], preguntas_profesor=[], 
                    sem_entrada = None, mutex_pregunta = None, preg_lista=None, resp_lista=None):
        Thread.__init__(self)
        self.name = name
        self.preguntas_alumno = preguntas_alumno
        self.preguntas_profesor = preguntas_profesor
        self.sem_entrada = sem_entrada
        self.mutex_pregunta = mutex_pregunta
        self.preg_lista = preg_lista
        self.resp_lista = resp_lista

    def preguntar(self):
        pregunta = self.preguntas_alumno.pop()
        with self.mutex_pregunta:
            print("\t%s hace una pregunta: %s" % (self.name, pregunta))
            sleep(0.5)
            self.preg_lista.release()
            print("\t%s está esperando respuesta..." % (self.name))
            self.resp_lista.acquire()

    def preguntar_todo(self):
        num_preguntas = len(self.preguntas_alumno)
        print("Hola, soy %s y tengo %i pregunta(s)" % (self.name, num_preguntas))
        with self.sem_entrada:
            print("<-- %s entró al cubículo" % self.name)
            t_list = []
            for _ in range(num_preguntas):
                t = Thread(target=self.preguntar)
                t_list.append(t)
                t.start()
            for t in t_list:
                t.join()
            print("--> %s salió del cubículo" % self.name)

    def run(self):    
        Thread(target=self.preguntar_todo).start()
        

class Profesor(Thread):
    def __init__(self, name='Fulano', preguntas_profesor=[], sem_entrada = None, 
                    mutex_pregunta = None, preg_lista=None, resp_lista=None):
        Thread.__init__(self)
        self.name = name
        self.preguntas_profesor = preguntas_profesor
        self.sem_entrada = sem_entrada
        self.mutex_pregunta = mutex_pregunta
        self.preg_lista = preg_lista
        self.resp_lista = resp_lista

    def responder_duda(self):
        print("\tEl profesor está esperando una pregunta...")
        self.preg_lista.acquire()
        print("\tEl profesor está respondiendo una pregunta...")
        sleep(0.5)
        self.resp_lista.release()


    def responder_dudas(self):
        print("Hola, soy %s e iniciaré a responder dudas..." % self.name)
        while True:
            self.responder_duda()

    def run(self):
        Thread(target=self.responder_dudas).start()

class Cubiculo(Thread):
    def __init__(self, nombre_profesor='Fulano', sillas=2, num_alumnos=0):
        Thread.__init__(self)
        
        self.sillas = sillas
        self.num_alumnos = num_alumnos
        self.nombre_profesor = nombre_profesor

        self.sem_entrada = Semaphore(sillas)
        self.mutex_pregunta = Semaphore(1)
        self.preg_lista = Semaphore(0)
        self.resp_lista = Semaphore(0)

        fake = Faker()
        #preguntas_alumno = ['preg'+str(i) for i in range(randint(1,6))]
        self.alumnos = [Alumno(name=fake.name(), 
                            preguntas_alumno=['preg'+str(i) for j in range(randint(1,6))], 
                            preguntas_profesor=[], 
                            sem_entrada = self.sem_entrada, 
                            mutex_pregunta = self.mutex_pregunta, 
                            preg_lista=self.preg_lista, 
                            resp_lista=self.resp_lista)
                        for i in range(num_alumnos)]   
        self.profesor = Profesor(name=fake.name(), 
                                preguntas_profesor=[], 
                                sem_entrada = self.sem_entrada, 
                                mutex_pregunta = self.mutex_pregunta, 
                                preg_lista=self.preg_lista, 
                                resp_lista=self.resp_lista)

    def iniciar_operaciones(self):
        print("Iniciando al profesor...")
        self.profesor.start()
        print("Iniciando %i alumnos..." % self.num_alumnos)
        for alumno in self.alumnos:
            alumno.start()
            
    def run(self):
        print("Iniciando cubículo con %i sillas..." % self.sillas)
        t = Thread(target=self.iniciar_operaciones)
        t.run()