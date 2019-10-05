import threading
import random
import time

numberCashier= 8 # Variable para el número de cajeros
numberGuards = 8 # Variable para el número de guardias
numberClients = 15 #	Variable para el número de clientes
Clients=0 #Variable del número de clientes en el banco
smart= 0.01 # Probabilidad que alguien quiera hacerse el listo y retirar más de lo debido
Guards=0 # Variable para el número de guardias en el banco

cashiers = [threading.Semaphore(1)]*numberCashier #Se define un arreglo de semaforos que representa a los cajeros
guardin = threading.Semaphore(1) # Semáforo de el guardia en el banco
clientin = threading.Semaphore(1)#Semáforo de los clientes en el banco

def client(who): #La funcion client recibe el numero de clientes que entran al banco
	global Clients
	global smart
	global Guards
	times = random.randint(1,3) 
	print(chr(27)+"[1;31m"+'Soy el cliente ', who, ' y voy a pasar ', times, 'veces al cajero') #El cliente indica que se ha iniciado y se identifica con su numero
	for x in range(0,times):
		if random.random() > smart: 
			time.sleep(random.random()*2) #Con esto buscamos la concurrencia
			guardin.acquire() #Se adquiere el mutex 
			if Clients == 0:
				clientin.acquire() #Si es el primer cliente en entrar al banco utiliza el semaforo para indicar que hay un cliente en el banco
			Clients += 1#Se actualiza el contador de clientes
			guardin.release() #Se libera el mutex
			drawoutordeposit('Cliente  '+str(who)) #El cliente retira dinero
			guardin.acquire()
			if Clients == 1:
				clientin.release()
				print(chr(27)+"[1;31m"+'\nSe fueron todos los clientes\n') 
			Clients -= 1
			guardin.release()
		else:
			guardin.acquire()
			if Guards > 0: #Aqui es donde un listillo quiera entrar con los guardias
				time.sleep(random.random()%0.2)
				print(chr(27)+"[1;33m"+'\n--------------------------------------------El cliente ', who, ' se pasó de listillo----------------------------------------------------\n')
				clientin.release()
				return 0
			clientin.release()

def guard(who):#La funcion guard recibe el numero de guardias que hay en el banco
	global Guards
	times = random.randint(1,3) #El guardia pasará a depositar n veces al cajero
	print(chr(27)+"[1;36m"+'Soy el guardia', who, 'y depositaré ', times, ' veces') 
	for x in range(0,times):
		time.sleep(random.random()*3) #Con esto buscamos la concurrencia
		clientin.acquire() #Se adquiere el mutex para utilizar la variable Guards
		if Guards == 0:
			guardin.acquire() #Si es el primer guardia en entrar al banco utiliza el semaforo para indicar que hay un guardia en el banco
		Guards += 1 #Se actualiza el contador de guardias
		clientin.release() #Se libera el mutex
		drawoutordeposit('Guardia  '+ str(who)) #El guardia deposita
		clientin.acquire()
		if Guards == 1:
			guardin.release()
			print(chr(27)+"[1;36m"+'\nLos guardias ya depositaron\n') #Se indica que ya no hay guardias
		Guards -= 1
		clientin.release()

def drawoutordeposit(who):
	global numberCashier
	cash = random.randint(0, numberCashier-1) 
	cashiers[cash].acquire() 
	print(chr(27)+"[1;34m"+who, 'esta utilizando el cajero', cash)
	time.sleep(random.random()*2) 
	print(chr(27)+"[1;35m"+'El Cajero ', cash, ' se desocupo')
	cashiers[cash].release() #Se desocupa el cajero

for i in range(0,numberGuards): #Se crea a los gatos
	threading.Thread(target=guard, args=[i]).start()

for i in range(0,numberClients): #Se crea a los ratones
	threading.Thread(target=client, args=[i]).start()
