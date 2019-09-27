from random import randint
"""
Clase Proceso:
	Representa un  proceso
	Como atributos tiene los estados que puede tener un proceso
	y el tiempo en el que llega al sistema y el tiempo en el cual debe trabajar
"""
class Proceso():
	"""
		----------------------Inicializador----------------------
		duracion_trabajo:	Cuanto tiempo va  a estar trabajando
		tiempo_llegada: 	En que tiempo de sistema va a llegar a querer ser ejecutado
		tiempo_reposo:		Cuanto tiempo lleva sin trabajar
		terminado:			Bandera que indica si el proceso ya termino
		ejecucion:			Bandera que indica si el proceso puede estar en ejecucion
		longitud_trabajo 	Cuanto tiempo va a estar trabajando
		nombre				nombre del procesos
	"""
	def __init__(self, tiempo_llegada, duracion_trabajo, nombre):
			self.longitud_trabajo = duracion_trabajo
			self.duracion_trabajo = duracion_trabajo
			self.tiempo_llegada = tiempo_llegada
			self.tiempo_trabajo = 0
			self.tiempo_reposo = 0
			self.terminado = False
			self.ejecucion = False
			self.nombre = nombre
	"""
		----------------------reset----------------------
		Descripcion: 		Este metodo "re-inizializa a un proceso ya terminado" se emplea 
							debido al tipo de implementacion manejada en los algoritmos
	"""

	def reset(self):
		self.longitud_trabajo = self.duracion_trabajo
		self.duracion_trabajo = self.duracion_trabajo
		self.tiempo_llegada = self.tiempo_llegada
		self.tiempo_trabajo = 0
		self.tiempo_reposo = 0
		self.terminado = False
		self.ejecucion = False
		self.nombre = self.nombre

	"""
		----------------------Trabaja----------------------
		Descripcion: 		Representa lo  que hace un proceso despues de llegar 
							Si no ha terminado y tiene la ejecucion entonces se pone a trabajr
							Si no entonces reposa
	"""
	def trabaja(self):
		if(not self.terminado and self.ejecucion):
			self.tiempo_trabajo += 1
			self.longitud_trabajo -= 1
			print(self.nombre,end="")
			if(self.longitud_trabajo == 0):
				self.terminado = True
		else:
			self.tiempo_reposo += 1
	"""
		----------------------calc_t_respuesta----------------------
		Descripcion: 		Calcula el tiempo de respuesta del proceso
							definido como el tiempo que trabajo as el tiempo de
	"""

	def calc_t_respuesta(self):
		self.t_respuesta = self.tiempo_trabajo + self.tiempo_reposo

	"""
		----------------------calc_proporcion_respuesta----------------------
		Descripcion: 		Calcula la proporcion de respuesta del proceso
							definida como la razon del tiempo que trabajo entre el timepo de respuesta
	"""
	def calc_proporcion_respuesta(self):
		self.respuesta = self.tiempo_trabajo/self.t_respuesta
	"""
		----------------------calc_proporcion_penalizacion----------------------
		Descripcion: 		Calcula la proporcion de penalizacion del proceso
							definida como el tiempo de respuesta entre el tiempo de trabajo
	"""	

	def calc_proporcion_penalizacion(self):
		self.penalizacion = self.t_respuesta/self.tiempo_trabajo
	"""
		----------------------calc_metricas----------------------
		Descripcion: 		Calcula las metricas del proceso
	"""
	def calc_metricas(self):
		self.calc_t_respuesta()
		self.calc_proporcion_penalizacion()
		self.calc_proporcion_respuesta()
	"""
		----------------------imprime_proceso----------------------
		Descripcion: 		Imprime un proceso
	"""

	def imprime_proceso(self):
		print(f"{self.nombre}:{self.tiempo_llegada}, t:{self.duracion_trabajo}",end=" ")

	"""
		----------------------crea_procesos----------------------
		Descripcion: 		Esta funcion crea n procesos, que llegan al sistema entre el tiempo 0 y el 15
							La duracion de su trabajo esta entre 1 y 10 para no imprimir cadenas demasiado 
							grandes a la hora de imprimir lo visual

		n:					Numero de procesos a ser creados
	"""
def crea_procesos(n):
	lista = []
	nombre = 65
	tiempo_llegada = 0
	duracion_trabajo = 0
	max_tiempo_llegada = 15
	max_duracion_trabajo = 10
	for i in range (0,n):
	  tiempo_llegada = randint(0,max_tiempo_llegada)
	  duracion_trabajo = randint(1,max_duracion_trabajo)
	  p = Proceso(tiempo_llegada,duracion_trabajo,chr(nombre))
	  nombre += 1
	  lista.append(p)
	return lista
	"""
		----------------------medias_procesoss----------------------
		Descripcion: 		Esta funcion calcula la media de varias metricas de una lista de procesos
		lista_procesos:		La lista de procesos ya ejecutados cuyas metricas seran calculadas
	"""
def medias_procesos(lista_procesos):
	t_respuesta = 0
	proporcion_penalizacion = 0 
	t_espera = 0
	for proceso in lista_procesos:
	  proceso.calc_metricas()
	  t_respuesta += proceso.t_respuesta
	  t_espera += proceso.tiempo_reposo
	  proporcion_penalizacion += proceso.penalizacion
	t_respuesta /= len(lista_procesos)
	proporcion_penalizacion /= len(lista_procesos)
	t_espera /= len(lista_procesos)
	return f"T:{t_respuesta:.3f} E:{t_espera:.3f} P:{proporcion_penalizacion:.3f}"

	"""
		----------------------llega_procesos----------------------
		Descripcion: 		Esta funcion va guardando los procesos que llegan en un tiempo "t" en una cola 
		lista_procesos:		La lista de procesos que van a llegar al planificador
		t_sistema:			Tiempo del sistema
		return:				Devuelve la cola de procesos
	"""

def llega_proceso(lista_procesos, t_sistema):
	cola_llegada = []
	for proceso in lista_procesos:
		if( proceso.tiempo_llegada == t_sistema):
			cola_llegada.append(proceso)
	return cola_llegada
 
def main():
	P1 = Proceso(0,5,"A")

	P1.ejecucion = True

	t_sistema = 0

	while(not P1.terminado):
		
		if( (t_sistema %2) == 0):
			P1.ejecucion = False
		else:
			P1.ejecucion = True
		
		P1.trabaja()
		t_sistema += 1
	P1.calc_metricas()
	print(f"R:{P1.respuesta} P:{P1.penalizacion}")


if __name__ == '__main__':
	main()


