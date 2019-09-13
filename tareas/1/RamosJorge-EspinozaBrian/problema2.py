# se importan las librerias nescesarias para implementar hilos y semaforos
from threading import Semaphore,Thread
from time import sleep 
import random
#se crean las listas para crear y manejar las 4 secciones y los semaforos
listSections=list()
listSemaphore=list()
mutex = Semaphore(1)
#Creacion de 4 semaforos uno para cada seccion 
for i in range(4):
	#abrimos las secciones 
	listSections.append(Semaphore(1))
	#inicializas en 0 para que inicien rojo 
	listSemaphore.append(Semaphore(0))
# funcion que recibe como parametros el numero de la seccion donde se inicia, la posible direccion que va a tomar y un identificador de hilo
def car(numberSection,direction,id):
	listSemaphore[numberSection%4].acquire()
	listSemaphore[numberSection%4].release()
	#seccion de codigo protegida
	mutex.acquire()
	print('   Carro',id)
	#para saber a donde gira
	for i in range(direction):
		# iteracion para tomar la direccion correcta
		j=(numberSection-i)%4
		listSections[j].acquire()
		print("      El carro esta pasando por la seccion ",j)
		listSections[j].release()
		#ponerlo porque si no se imprimen cosas feas
	mutex.release()
# funcion masterChief que controla los semaforos
def masterChief():
	#para que se esperen cierto tiempo
	wait=0.001
	while (True):
		sleep(wait)
		print("Estado de la interseccion 0 verde  2 verde")
		listSemaphore[0].release()
		listSemaphore[2].release()
		#solo va a estar en verde este tiempo
		sleep(wait)
		print("Estado de la interseccion 0 rojo  2 rojo")
		listSemaphore[0].acquire()
		listSemaphore[2].acquire()
		#sleep para dar tiempo a que se salgan para evitar bloqueo mutuo
		sleep(wait)
		print("Estado de la interseccion 1 verde  3 verde")
		listSemaphore[1].release()
		listSemaphore[3].release()
		sleep(wait)
		print("Estado de la interseccion 0 rojo  2 rojo")
		listSemaphore[1].acquire()
		listSemaphore[3].acquire()
		sleep(wait)	
	return

#un tread que controla el estado de los semaforos 
masterChief = Thread(target=masterChief).start()

#inicializamos los carros mediante la funcion cars
for i in range(666):
		# caso donde todos los carros salen de la seccion 0 y toman cualquiera de las 3 posibles direcciones
		Thread(target=car,args=(0,1,"inicio en seccion 0 giro -> "+ str(i) )).start()
		Thread(target=car,args=(0,2,"inicio en seccion 0 sigo ^ "+ str(i) )).start()
		Thread(target=car,args=(0,3,"inicio en seccion 0 giro <- "+ str(i) )).start()

		# caso donde todos los carros salen de la seccion 2 y toman cualquiera de las 3 posibles direcciones
		# Thread(target=car,args=(2,1,'inicio en seccion 2 giro -> '+str(i) )).start()
		# Thread(target=car,args=(2,2,'inicio en seccion 2 sigo ^ '+str(i) )).start()
		# Thread(target=car,args=(2,3,'inicio en seccion 2 giro <- '+str(i) )).start()
		# caso donde todos los carros salen de la seccion 1 y toman cualquiera de las 3 posibles direcciones
		# Thread(target=car,args=(1,1,'inicio en seccion 1 giro -> '+str(i) )).start()
		# Thread(target=car,args=(1,2,'inicio en seccion 1 sigo ^ '+str(i) )).start()
		# Thread(target=car,args=(1,3,'inicio en seccion 1 giro <- '+str(i) )).start()
		# caso donde todos los carros salen de la seccion 3 y toman cualquiera de las 3 posibles direcciones
		# Thread(target=car,args=(3,2,'inicio en seccion 3 sigo ^ '+str(i) )).start()
		# Thread(target=car,args=(3,1,'inicio en seccion 3 giro -> '+str(i) )).start()		
		# Thread(target=car,args=(3,3,'inicio en seccion 3 giro <- '+str(i) )).start()	













