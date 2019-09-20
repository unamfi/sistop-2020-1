import threading	
from time import sleep
from random import randint



l_platos = 5 

platos = [threading.Semaphore(1) for i in range(l_platos)]
max_animales = threading.Semaphore(l_platos)
puerta = threading.Semaphore(1)
mutex_gatos_en_cuarto = threading.Semaphore(1) 
gatos_en_cuarto = 0
ratones_en_cuarto = 0
mutex_ratones_en_cuarto = threading.Semaphore(1)
torniquete = threading.Semaphore(1)

def gato_entra_a_cuarto(id):
	global platos,max_animales,puerta,mutex_gatos_en_cuarto,gatos_en_cuarto
	global ratones_en_cuarto,mutex_ratones_en_cuarto,torniquete
	torniquete.acquire()
	torniquete.release()
	puerta.acquire()
	mutex_gatos_en_cuarto.acquire()
	gatos_en_cuarto += 1
	mutex_gatos_en_cuarto.release()
	gato_obtine_plato(id)
	gato_come(id)
	gato_deja_plato(id)
	mutex_gatos_en_cuarto.acquire()
	gatos_en_cuarto -= 1
	mutex_gatos_en_cuarto.release()
	puerta.release()
	print("Soy el gato " + str(id) + " y ya me fui")
	
def gato_obtine_plato(id):
	global platos,max_animales,puerta,mutex_gatos_en_cuarto,gatos_en_cuarto
	global ratones_en_cuarto,mutex_ratones_en_cuarto,torniquete
	max_animales.acquire()
	platos[(id)%l_platos].acquire()
	print("Soy el gato " + str(id) + "  y tengo el plato: " + str((id)%l_platos))

def gato_come(id):
	global platos,max_animales,puerta,mutex_gatos_en_cuarto,gatos_en_cuarto
	global ratones_en_cuarto,mutex_ratones_en_cuarto,torniquete	
	print("Soy el gato " + str(id) + "  y estoy comiendo en  el plato: " + str((id)%l_platos))	

def gato_deja_plato(id):
	global platos,max_animales,puerta,mutex_gatos_en_cuarto,gatos_en_cuarto
	global ratones_en_cuarto,mutex_ratones_en_cuarto,torniquete
	platos[(id)%l_platos].release()
	max_animales.release()

	
def raton_entra_a_cuarto(id):
	global platos,max_animales,puerta,mutex_gatos_en_cuarto,gatos_en_cuarto
	global ratones_en_cuarto,mutex_ratones_en_cuarto,torniquete
	torniquete.acquire()
	torniquete.release()
	mutex_gatos_en_cuarto.acquire()
	if(gatos_en_cuarto > 0):
		print("Soy el raton " + str(id),end=" ")
		print("Ya me comio un gato x.x")
		mutex_gatos_en_cuarto.release()
	else:
		mutex_gatos_en_cuarto.release()
		mutex_ratones_en_cuarto.acquire()
		ratones_en_cuarto += 1
		if(ratones_en_cuarto == 1):
			puerta.acquire()
		mutex_ratones_en_cuarto.release()
		raton_obtine_plato(id)
		raton_come(id)
		raton_deja_plato(id)
		mutex_ratones_en_cuarto.acquire()
		ratones_en_cuarto -= 1
		if(ratones_en_cuarto == 0):
			puerta.release()
		print("Soy el raton " + str(id) + " y ya me fui")
	
		mutex_ratones_en_cuarto.release()

def raton_obtine_plato(id):
	global platos,max_animales,puerta,mutex_gatos_en_cuarto,gatos_en_cuarto
	global ratones_en_cuarto,mutex_ratones_en_cuarto,torniquete
	max_animales.acquire()
	platos[(id)%l_platos].acquire()

def raton_come(id):
	global platos,max_animales,puerta,mutex_gatos_en_cuarto,gatos_en_cuarto
	global ratones_en_cuarto,mutex_ratones_en_cuarto,torniquete
	print("Soy el raton " + str(id) + "  y estoy comiendo en  el plato: " + str((id)%l_platos))

def raton_deja_plato(id):
	global platos,max_animales,puerta,mutex_gatos_en_cuarto,gatos_en_cuarto
	global ratones_en_cuarto,mutex_ratones_en_cuarto,torniquete
	platos[(id)%l_platos].release()
	max_animales.release()


m = 0
k = 0
for i in range(20):
	numero = randint(0,1)
	if(numero==0):
		m += 1
		rat = threading.Thread(target=raton_entra_a_cuarto, args=[m]).start()
	else:
		k += 1
		gat = threading.Thread(target=gato_entra_a_cuarto, args=[k]).start()
	
	
	
		
