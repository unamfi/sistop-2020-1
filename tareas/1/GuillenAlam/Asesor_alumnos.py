#Guillen Alam
#Los alumnos y el asesor

import threading
import time
import random

alumnos = 0 #Contador de alumnos en el cubiculo
sillas = 5 #Defino numero de sillas = 5
preguntasMaximas = 3 #Defino numero de preguntas que puede hacer cada alumno = 3
alumnosMaximos = 10 #Defino numero de alumnos del día = 10

semaphoreAsesor = threading.Semaphore(0)
multiplex = threading.Semaphore(sillas)
mutexContador = threading.Semaphore(1)
mutexAsesoria = threading.Semaphore(1)
torniquete = threading.Semaphore(1)

def Asesor(): #Definimos al asesor
    global alumnos
    print ("El asesor duerme") #Menasje que indica que el asesor duerme
    while(alumnos < alumnosMaximos):
        semaphoreAsesor.acquire() #El asesor despierta
        if(alumnos != 0):
            print ("El asesor despierta") #Menasje que indica que el asesor  esta despierto

def Alumno(num): #Definimo alumno
    multiplex.acquire() #Usamos mutex
    global alumnos
    time.sleep(random.random()) #Esperamos
    print ("Alumno %d esperando" %num)  #Alumno esperando
    alumnos += 1 #Contamos al alumno
    semaphoreAsesor.release()
    for i in range(1,preguntasMaximas): #Numero de preguntas del alumno
        torniquete.acquire() #Entra al cubiculo
        torniquete.release()
        Asesoria(num,i) #Usa la asesoria
    multiplex.release() #Soltamos mutex

def Asesoria(num,i): #Definimos asesoria
    mutexAsesoria.acquire() #Usamos mutez
    print ("Alumno %d preguntando..." %num) #Mensaje de pregunta
    time.sleep(random.random()) #Espera
    print ("El profesor esta respondiendo la pregunta " + str(i) + " del alumno " + str(num)) #Mensaje de resolviendo
    time.sleep(random.random()) #Espera
    mutexAsesoria.release() #Soltamos mutex

threading.Thread(target=Asesor, args=[]).start() #Iniciamos hilos
for i in range(alumnosMaximos):
    threading.Thread(target=Alumno, args=[i]).start()