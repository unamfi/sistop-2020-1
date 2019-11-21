'Macario Falcon Leonel'
'Garcia Hernandez Rogelio'

'Ejercicios de Sincronizacion'
'Problema: Los alumnos y el asesor'
'Puede haber hasta 5 alumnos en una misma asesoria'
'Sopora hasta 2 preguntas por alumno'
import threading
import time
import random

alumnos = 0
auxiliarPreguntas = 0
turno = 0
dicAlu = {}
hilos_alum = 1#no hay 0 alumnos

mutex = threading.Semaphore(1)
mano = threading.Semaphore(1)
cubiculo_vacio = threading.Semaphore(1)
torniquete = threading.Semaphore(1)

#Asesoria al alumno
def asesoria(num):
    print "Asesorando al alumno %d\n" % num
    time.sleep(1.2)

#Alumno pregunta
def duda(num,preguntasMax):
    print "El  %d alumno pregunta por %da vez" % (num,preguntasMax)
    print "El  %d alumno ya termino de preguntar" % num
    time.sleep(1.3)
    asesoria(num)

#Reinicia contador de hilos
def Profesor():
    global hilos_alum 
    cubiculo_vacio.acquire()
    print "--->Sala vacia, Sieta del profesor en proceso<---\n"
    hilos_alum = 1
    time.sleep(1.0)
    cubiculo_vacio.release()


def alumno(num):
    global alumnos
    
    print "El  %d alumno tocar la puerta y entra" % num
    mutex.acquire()
    dicAlu[str(unichr(num+48))] = 0
    mutex.release()

    torniquete.acquire()
    torniquete.release()

    turno = 0
    while ((dicAlu[str(unichr(num+48))] != 2) and (turno < 2)):

      mano.acquire()
      mutex.acquire() 
      alumnos = alumnos + 1
      if alumnos == 1:
	  cubiculo_vacio.acquire()
      auxiliarPreguntas = dicAlu[str(unichr(num+48))]
      auxiliarPreguntas += 1
      dicAlu[str(unichr(num+48))] = auxiliarPreguntas
      duda(num, auxiliarPreguntas)
      mutex.release()
      mano.release()
      time.sleep(0.3)

      mutex.acquire()
      turno += 1
      if dicAlu[str(unichr(num+48))] == 2:
	alumnos -=2
	if alumnos == 0:
	  cubiculo_vacio.release()
	  Profesor()
      mutex.release()
      time.sleep(0.2)

while True:

#contado de hilos 
  while (hilos_alum < 6):
    time.sleep(0.05)
    if random.random() < 0.05:
      threading.Thread(target=alumno, args=[hilos_alum]).start()
      hilos_alum += 1

