from Proceso import Proceso, crea_procesos, medias_procesos, llega_proceso
"""
Algoritmo de Planificacion SPN

"""

def genera_lista_procesos():
  lista = []
  p1 = Proceso(0,3,"A")
  p2 = Proceso(1,5,"B")
  p3 = Proceso(3,2,"C")
  p4 = Proceso(9,5,"D")
  p5 = Proceso(12,5,"E")
  lista.append(p1)
  lista.append(p2)
  lista.append(p3)
  lista.append(p4)
  lista.append(p5)
  return lista

def SPN(lista_procesos):
	print("SPN")
	t_sistema = 0
	# El numero de procesos que deben ser atendidos
	num_procesos = len(lista_procesos)
	#El proceso actual en ejecucion
	proceso_actual = None
	cola_procesos = []
	
	def proximo_mas_corto(cola_procesos):
		min = cola_procesos[0].duracion_trabajo
		indice = 0
		for i in range(0,len(cola_procesos) ):
			if(cola_procesos[i].duracion_trabajo <= min):
				min = cola_procesos[i].duracion_trabajo
				indice = i
		return indice

	while(num_procesos != 0):
		cola_llegada = llega_proceso(lista_procesos, t_sistema)
		if(len(cola_llegada) != 0):
			if(len(cola_procesos) == 0):
				p = cola_llegada.pop(0)
				cola_procesos.append(p)
				proceso_actual = cola_procesos[0]
				proceso_actual.ejecucion = True
				for p in cola_llegada:
					cola_procesos.append(p)
			else:
				for p in cola_llegada:
					cola_procesos.append(p)

		if(len(cola_procesos) != 0 ):
			#Se porcede a buscar el de menor duracion y a mover el que seugia 
			#Despues se le da la ejecucion al proximo mas corto
			if(proceso_actual == None):
				indice = proximo_mas_corto(cola_procesos)
				proceso_actual = cola_procesos[indice]
				cola_procesos.pop(indice)
				cola_procesos.insert(0,proceso_actual)
				proceso_actual.ejecucion = True

			# Se ponen a trabajar a todos los procesos, en caso de no tener la ejecucion, estos descansan
			for proceso in cola_procesos:
				proceso.trabaja()

			# Si el proceso en ejecucion ya acabo se le cede la ejecucion al siguente proceso en la cola
			if(proceso_actual.terminado == True):
				cola_procesos.pop(0)
				num_procesos -= 1
				proceso_actual = None
		# Sigue pasando el tiempo en el sistema
		t_sistema += 1
	medias = medias_procesos(lista_procesos)
	print("")
	print(medias)

