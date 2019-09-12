from threading import Thread, Semaphore, enumerate
#from threading import enumerate as t_enumerate
from random import randint, random
from time import sleep
from faker import Faker
#from colorama import init, Fore, Back, Style

class Alumno(Thread):
    #def __init__(self, name, cond_entrada, cond_pregunta, cond_resp, preguntas=[]):
    def __init__(self, name, alumnos_dentro, num_max_preguntas=5, 
                    sem_entrada = None, mutex_pregunta = None, preg_lista=None, resp_lista=None):
        Thread.__init__(self)
        self.name = name
        self.num_max_preguntas = num_max_preguntas
        self.sem_entrada = sem_entrada
        self.mutex_pregunta = mutex_pregunta
        self.preg_lista = preg_lista
        self.resp_lista = resp_lista
        self.alumnos_dentro = alumnos_dentro

        self.preguntas_alumno = ['preg'+str(i) for i in range(randint(1,num_max_preguntas))]

    def preguntar(self):
        sleep(random()*2.0)
        pregunta = self.preguntas_alumno.pop()
        with self.mutex_pregunta:
            sleep(0.5)
            print("\t\t%s hace una pregunta: %s" % (self.name, pregunta))
            self.preg_lista.release()
            print("\t\t%s: estoy esperando respuesta del profesor..." % (self.name))
            self.resp_lista.acquire()

    def preguntar_todo(self):
        num_preguntas = len(self.preguntas_alumno)
        print("Hola, soy %s y quiero entrar al cubículo." % (self.name))
        with self.sem_entrada:
            self.alumnos_dentro.append(self.name)
            print(("---> %s entró al cubículo y tiene %i preguntas.\n"+
                   "  ** Somos %i personas en el cubiculo **") % (self.name, num_preguntas ,len(self.alumnos_dentro)))
            t_list = []
            for _ in range(num_preguntas):
                t = Thread(target=self.preguntar)
                t_list.append(t)
                t.start()
            for t in t_list:
                t.join()
            self.alumnos_dentro.remove(self.name)
            print(("<--- %s ya no tiene más preguntas y salió del cubículo.\n"+
                   "  ** Quedan %i personas en el cubiculo **") % (self.name, len(self.alumnos_dentro)))
            #print("*--- Quedan %d hilos corriendo. --*" % (len(t_enumerate())-1))


    def run(self):    
        Thread(target=self.preguntar_todo).start()
        

class Profesor(Thread):
    def __init__(self, name='Dr. Fulano', sem_entrada = None, 
                    mutex_pregunta = None, preg_lista=None, resp_lista=None):
        Thread.__init__(self)
        self.name = name
        self.sem_entrada = sem_entrada
        self.mutex_pregunta = mutex_pregunta
        self.preg_lista = preg_lista
        self.resp_lista = resp_lista

    def responder_duda(self):
        print("\tEl profesor está esperando una pregunta...")
        self.preg_lista.acquire()
        #print("\t\tEl profesor está respondiendo una pregunta...")
        #sleep(0.1)
        self.resp_lista.release()
        print("\t\tEl profesor ha respondido a tu pregunta!")


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
        self.alumnos_dentro = []

        self.sem_entrada = Semaphore(sillas)
        self.mutex_pregunta = Semaphore(1)
        self.preg_lista = Semaphore(0)
        self.resp_lista = Semaphore(0)

        fake = Faker()
        #Crear N numero de alumnos
        self.alumnos = [Alumno(name=fake.name(), 
                                alumnos_dentro = self.alumnos_dentro,
                                num_max_preguntas=6, 
                                sem_entrada = self.sem_entrada, 
                                mutex_pregunta = self.mutex_pregunta, 
                                preg_lista=self.preg_lista, 
                                resp_lista=self.resp_lista)
                        for i in range(num_alumnos)]   
        self.profesor = Profesor(name=fake.name(), 
                                sem_entrada = self.sem_entrada, 
                                mutex_pregunta = self.mutex_pregunta, 
                                preg_lista=self.preg_lista, 
                                resp_lista=self.resp_lista)

    def iniciar_operaciones(self):
        print("Iniciando al profesor...")
        self.profesor.start()
        print("Iniciando %i alumnos..." % self.num_alumnos)
        for alumno in self.alumnos:
            sleep(1)
            alumno.start()
            
    def run(self):
        print("Iniciando cubículo con %i sillas..." % self.sillas)
        t = Thread(target=self.iniciar_operaciones)
        t.run()
        #exit(0)