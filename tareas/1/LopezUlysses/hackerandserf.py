#Importamos los modulos de threadin y de time que vamos a requerir
import threading
from time import sleep 
#Declaración de variables globales y de semáforos a utilizar
numberhackers = 0  
numberserfs = 0    
passengers = 0   
hackers = threading.Semaphore(0) 
serfs = threading.Semaphore(0)   
mutex = threading.Semaphore(1)        
mutexboat = threading.Semaphore(1) 
#Definición de un hacker
def hacker():
	global numberhackers 
	global numberserfs     
	mutex.acquire()	
	numberhackers = numberhackers + 1 
	if (numberhackers == 4): 
		hackers.release()
		hackers.release()
		hackers.release()
		numberhackers = 0
		mutex.release()
		up("Hacker de Linux")
	elif(numberhackers == 2 and numberserfs == 2):
		hackers.release()
		serfs.release()
		serfs.release()
		numberhackers = 0
		numberserf = 0
		mutex.release()
		up("Hacker de Linux")
	else: 
		mutex.release()                   
		hackers.acquire()            
		up("Hacker de Linux")   

#Definicion de un Serf
def serf():
	global numberhackers
	global numberserfs     
	mutex.acquire()
	numberserfs = numberserfs + 1    
	if (numberserfs == 4):			
		serfs.release()
		serfs.release()
		serfs.release()
		numberserfs = 0
		mutex.release()
		up("Serf de Microsoft")
	elif (numberhackers == 2 and numberserfs == 2):
		serfs.release()	
		hackers.release()
		hackers.release()
		numberhackers = 0
		numberserf = 0
		mutex.release()
		up("Serf de Microsoft")
	else:
		mutex.release()
		serfs.acquire()
		up("Serf de Microsoft")

#Definición de la funcion para subir "up"
def up(person):
	global passengers  
	mutexboat.acquire()
	passengers = passengers + 1
	print ("\nSe está subiendo un ", person, "a la balsa\n")
	if(passengers == 4):
		print("\nYa somos 4 personas en la balsa\n")
		go()
		passengers = 0
	mutexboat.release()

#Definición de la función para zarpar "go"
def go():
	print("\n**********************************Vamos a zarpar y no habrán problemas...creo...************************************\n")
	sleep(1)

#
iteraciones = int(input("¿Cuántas iteraciones requiere?\n"))

#implementación de los hilos
for i in range(iteraciones):
	threading.Thread(target = hacker, args = []).start()
	threading.Thread(target = hacker, args = []).start()
	threading.Thread(target = serf, args = []).start()	
	threading.Thread(target = serf, args = []).start()
