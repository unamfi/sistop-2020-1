 
# Sistemas operativos
*Ramos Barraza Jorge Luis
Espinoza Ceron Brian Arian*
### Problema 2 cruce de caminos sin señalamiento vial

#### Requerimientos
* python V3  
* linea de comandos
#### instrucciones
colocarse en el directorio `tareas/1/RamosJorge-EspinozaBrian` y ejecutar el siguiente comando

```
python3 problema2.py
```
listo deberia verse la ejecucion del programa

> nota: Este problema se implemento en una version 3.5.3 de python en un ordenador con sistema operativo debian 9

#### estrategia

Para este problema se utilizaron semaforos como estrategia para poder resolver este problema con las condiciones que se pedian.

Decidimos definir 4 secciones  de la siguiente forma:

|2|3|
|1|0|

se tomaron en cuenta las refinaciones 

#####refinamiento 2

para poder dar giros a la izquierda o a la derecha se encontro que con la siguiente formula `(numberSection - 1) % 4` se puede llegar a el comportamiento deseado variando el numero de iteraciones a dicha formula

>1 iteracion giro a la derecha
 2 iteraciones continua derecho
 3 iteraciones giro a la izquierda


#### entendiendo el codigo 

existen 2 funciones principales en el codigo

la primera es la funcion car la cual  recibe como parametros el numero de la seccion donde se inicia, la posible direccion que va a tomar y un identificador de hilo (id) dentro de la cual se adquieren o se sueltan los semaforos, se controla la direccion que los carros tomaran y se hace una impresion para saber cual es el comportamiento que tiene que realizar el carro 
```
def car(numberSection,direction,id):
	listSemaphore[numberSection%4].acquire()
	listSemaphore[numberSection%4].release()
	#seccion de codigo protegida
	mutex.acquire()
	print('   Carro',id)
	#para saber a donde gira
	for i in range(direction):
		j=(numberSection-i)%4
		listSections[j].acquire()
		print("      El carro esta pasando por la seccion ",j)
		listSections[j].release()
		#ponerlo porque si no se imprimen cosas feas
	mutex.release()
    
```

la segunda es la funcion masterChief la cual no recibe parametros pero va a ser la encargada de controlar el flujo de los semaforos dandoles un tiempo de espera de 0.001 segundos para asi evitar la inanicion cuando se cambie el estado de un semaforo no se queden atorados los carros en el cruce y asi no exista un bloqueo
```
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
    
```

hilo independiente
```
#un tread que controla el estado de los semaforos 
masterChief = Thread(target=masterChief).start()
```

>se considero pertinente la creacion de un hilo independiente como hilo maestro para que pueda contolar los semaforos

por ultimo mediante un ciclo for se hace la inicializacion de los hilos mediante un ciclo for

```
for i in range(666):
		# caso donde todos los carros salen de la seccion 0 y toman cualquiera de las 3 posibles direcciones
		Thread(target=car,args=(0,1,"inicio en seccion 0 giro -> "+ str(i) )).start()
		Thread(target=car,args=(0,2,"inicio en seccion 0 sigo ^ "+ str(i) )).start()
		Thread(target=car,args=(0,3,"inicio en seccion 0 giro <- "+ str(i) )).start()
```
>aqui se planeaba inicialmente mediante la generacin de numeros aleatorio dentro del rango asignar la seccion de donde sale el carro y la direccion que tomara pero teniamos que considerar cada caso e incluirlo dentro de un if para que imprima en pantalla cual es el punto de partida y la direccion a tomar por lo que se iban a gastar las mismas lineas de codigo (¿existe una mejor opcion para este problema?) que inicializando los carros de forma individual, para fines practicos solo se considera el punto de partida en la seccion 0 y las 3 posibles direcciones a tomar, si se quiere probar con todos los casos posibles solamente agrega el siguiente codigo
```

#caso donde todos los carros salen de la seccion 0 y toman cualquiera de las 3 posibles direcciones
Thread(target=car,args=(0,1,"inicio en seccion 0 giro -> "+ str(i) )).start()
Thread(target=car,args=(0,2,"inicio en seccion sigo ^ "+ str(i) )).start()
Thread(target=car,args=(0,3,"inicio en seccion giro <- "+ str(i) )).start()
#caso donde todos los carros salen de la seccion y toman cualquiera de las 3 posibles direcciones
Thread(target=car,args=(2,1,'inicio en seccion giro -> '+str(i) )).start()
Thread(target=car,args=(2,2,'inicio en seccion sigo ^ '+str(i) )).start()
Thread(target=car,args=(2,3,'inicio en seccion giro <- '+str(i) )).start()
#caso donde todos los carros salen de la seccion y toman cualquiera de las 3 posibles direcciones
Thread(target=car,args=(1,1,'inicio en seccion giro -> '+str(i) )).start()
Thread(target=car,args=(1,2,'inicio en seccion sigo ^ '+str(i) )).start()
Thread(target=car,args=(1,3,'inicio en seccion giro <- '+str(i) )).start()
#caso donde todos los carros salen de la seccion y toman cualquiera de las 3 posibles direcciones
Thread(target=car,args=(3,2,'inicio en seccion sigo ^ '+str(i) )).start()
Thread(target=car,args=(3,1,'inicio en seccion giro -> '+str(i) )).start()		
Thread(target=car,args=(3,3,'inicio en seccion giro <- '+str(i) )).start()	
```

