##Alumno: Mata Mota Luis Valentin 

import threading    
import time 
import random 

preguntas = []
alumnos = []
colaPreguntas = threading.Semaphore(1)
tomarPalabra = threading.Semaphore(1)
agregar = threading.Semaphore(1)
contador = 1


def profesor():
    global contador
    time.sleep(random.randrange(20))   ##Permitimos que algunos alumnos lleguen antes que el profesor
    print("Llego el profesor")
    while(1):
        if(len(alumnos) == 0):    ##Se revisa si hay alumnos formado para asesoria
            print("Me voy a dormir")   ##Si no hay se puede dormir
            if(len(preguntas) == 0):  ##Revisamos si hay preguntas por responder 
                print("Se acabo mi turno")
                return 0
            else:
                print("Me voy a dormir")
        else:
            responderPregunta()    
            contador -= 1   ##Incrementa cada que responde una pregunta 

def alumno(numAlumno):
    global contador
    time.sleep(random.randrange(10))    ##Nos da un poco de aleatoriedad en la llegada de los alumnos 
    print("Ah llegado el alumno %d" %numAlumno)
    masdudas = 1
    while(masdudas != 0):    ##Con este ciclo el mismo alumno podra tener mas de una pregunta 
        contador += 1
        time.sleep(random.randrange(5))
        agregarPregunta(numAlumno)  ##Manda una nueva pregunta a la lista
        masdudas = random.randrange(2)    ##No regresa aleatoriamente un 1 o un 0, si es uno, hara otra pregunta y si es 0 termio 

    
def agregarPregunta(numAlumno):
    global preguntas
    colaPreguntas.acquire()     ##Nos aseguramos que nadie quiera acceder a ambas listas al mismo tiempo 
    alumnos.append(numAlumno)     ##Manejamos dos lista, una de alumno, que se agregan cada que llega alguno o quiere repetir su turno
    preguntas.append(numAlumno)     ##Y en esta agregamos una pregunta en caso de que el alumno tenga una duda
    colaPreguntas.release()

def responderPregunta():
    global alumnos, preguntas
    if (len(alumnos)>0):
        numAlumno = alumnos[0]
        tomarPalabra.acquire()  ##Nos permite que solo un alumno pregunte al mismo tiempo, tome la palabra. 
        print (".........................Falta atender a estos alumnos:")
        print '.........................', alumnos
        print("Alumno %d: Mi  duda es:...." %numAlumno)
        print("Profesor: Mira, eso es muy sencillo....")
        time.sleep(random.randrange(5))   ##Le agega aleatoriedad al tiempo que tarda el profesor en contestar la pregunta planteada
        print("Alumno %d: Entiendo... Gracias!!" %numAlumno)
        alumnos.pop(0)  ##Retira un elemento del arreglo alumno, lo que quiere decir que se contesto su pregunta 
        preguntas.pop(0) ##Retira un elemento del arreglo preguntas, lo que quiere decir que la pregunta fue resuelta
        if numAlumno in alumnos:
            pass
        else:
            print(".........................El alumno %d se fue" %numAlumno)
        tomarPalabra.release()
    else:
        return 1

threading.Thread(target=profesor).start()    ##Lanza hilo profesor  
alumnosDelDia = random.randrange(20)    ##Cada ejecucion sera un dia diferente, por lo que la cantidad de alumnos que llegan es diferente, elegida al azar. 
for i in range(alumnosDelDia):
    threading.Thread(target=alumno, args=[i+1]).start()    ##Lanza hilos alumnos 
    


    
