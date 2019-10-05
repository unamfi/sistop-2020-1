from Proceso import Proceso, crea_procesos, medias_procesos, llega_proceso
"""
Algoritmo de Planificacion FCFS(First Come, First Serve)

"""


def FCFS(lista_procesos):
	print("FCFS: ")
	t_sistema = 0
	# El numero de procesos que deben ser atendidos
	num_procesos = len(lista_procesos)
	#El proceso actual en ejecucion
	proceso_actual = None
	cola_procesos = []
	while(num_procesos != 0):
		cola_llegada = llega_proceso(lista_procesos, t_sistema)
		#Si la cola de llegadas no esta vacia
		if(len(cola_llegada) != 0):
			#El primer proceso que llega sera agregado a la cola de ejecucion y ejecutado inmediatamente
			if(len(cola_procesos) == 0):
				p = cola_llegada.pop(0)
				cola_procesos.append(p)
				proceso_actual = cola_procesos[0]
				proceso_actual.ejecucion = True
				for p in cola_llegada:
					cola_procesos.append(p)
			#Si no es el primero
			else:
				for p in cola_llegada:
					cola_procesos.append(p)
		if(len(cola_procesos) != 0 ):
			# Se ponen a trabajar a todos los procesos, en caso de no tener la ejecucion, estos descansan
			for proceso in cola_procesos:
				proceso.trabaja()

			# Si el proceso en ejecucion ya acabo se le cede la ejecucion al siguente proceso en la cola
			if(proceso_actual.terminado == True):
				cola_procesos.pop(0)
				num_procesos -= 1
				if(len(cola_procesos) != 0):
					proceso_actual = cola_procesos[0]
					proceso_actual.ejecucion = True
		# Sigue pasando el tiempo en el sistema
		t_sistema += 1
	medias = medias_procesos(lista_procesos)
	print("")
	print(medias)


