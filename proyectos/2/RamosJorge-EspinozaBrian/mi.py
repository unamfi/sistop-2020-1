# se importan las librerias nescesarias para implementar hilos y semaforos
from threading import Semaphore,Thread
from time import sleep 
import random
#se crean las listas para crear y manejar las 4 secciones y los semaforos
baños=list()
listSemaphore=list()
mutex = Semaphore(1)

#Creacion de 4 semaforos uno para cada seccion 
for i in range(4):
	#abrimos las secciones 
	baños.append(Semaphore(1))
	#inicializas en 0 para que inicien rojo 
	listSemaphore.append(Semaphore(0))
# funcion que recibe como parametros el numero de la seccion donde se inicia, la posible direccion que va a tomar y un identificador de hilo
def car(numberSection,sexo,id):
	listSemaphore[numberSection%4].acquire()
	listSemaphore[numberSection%4].release()
	#seccion de codigo protegida
	mutex.acquire()
	print('persona',id)
	#para saber a donde gira
	for i in range(sexo):
		# iteracion para tomar la direccion correcta
		j=(numberSection-i)%4
		baños[j].acquire()
		print("      la persona esta en el baño ",j)
		baños[j].release()
		#ponerlo porque si no se imprimen cosas feas
	mutex.release()
# funcion masterChief que controla los semaforos
def masterChief():
	#para que se esperen cierto tiempo
	wait=0.001
	while (True):
		sleep(wait)
		print("Estado del baño 0 libre baño 2 libre")
		listSemaphore[0].release()
		listSemaphore[2].release()
		#solo va a estar en verde este tiempo
		sleep(wait)
		print("Estado del baño 0 ocupado  baño 2 ocupado")
		listSemaphore[0].acquire()
		listSemaphore[2].acquire()
		#sleep para dar tiempo a que se salgan para evitar bloqueo mutuo
		sleep(wait)
		print("Estado del baño 1 libre baño 3 libre")
		listSemaphore[1].release()
		listSemaphore[3].release()
		sleep(wait)
		print("Estado del baño 0 ocupado baño 2 ocupado")
		listSemaphore[1].acquire()
		listSemaphore[3].acquire()
		sleep(wait)	
	return

#un tread que controla el estado de los semaforos 
masterChief = Thread(target=masterChief).start()

#inicializamos los carros mediante la funcion cars
for i in range(10):
	Thread(target=car,args=(0,1,"baño 0 sexo hombre"+ str(i) )).start()












