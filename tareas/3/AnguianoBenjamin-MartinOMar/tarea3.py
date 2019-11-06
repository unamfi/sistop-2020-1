unidades = []
tamanios = []
inicios = []

def limpiarUnidad(tamanio):
	global unidades
	for i in range(len(unidades)):
		unidades.remove(0)
	for i in range(0, int(tamanio)):
		unidades.append('-')
	#return unidades

def mostrarUnidades():
	global unidades
	palabra = ''
	for i in range(len(unidades)):
		palabra = palabra+unidades[i]
	print palabra

def obtenerEspaciosVacios():
	global unidades
	global tamanios
	global inicios
	inicio = 0
	tamanioDisponible = 0
	for i in range(len(unidades)):
		if(unidades[i] == '-' and inicio == 0):
			inicio = i
			tamanioDisponible = tamanioDisponible+1
		elif(unidades[i] =='-' and inicio != 0):
			tamanioDisponible = tamanioDisponible+1
			if(i<len(unidades)-1 and unidades[i+1] != '-'):
				inicios.append(inicio)
				tamanios.append(tamanioDisponible)
				inicio == 0
				tamanioDisponible == 0
			elif(i == len(unidades)-1):
				inicios.append(inicio)
				tamanios.append(tamanioDisponible)
				inicio == 0
				tamanioDisponible == 0
		
	


def asignarProceso(nombre, tamanio):
	global inicios
	global tamanios
	global unidades
	indice_del_mejor_espacio = mejorDisponible(tamanio)
	print(indice_del_mejor_espacio)
	for i in range(len(unidades)):
		if(inicios[indice_del_mejor_espacio] == i):
			for j in range(tamanio):
				if(i == 1):
					unidades[i+j-1] = nombre
					unidades[i+j] = nombre
				else:
					unidades[i+j] = nombre
					unidades[i+j+1] = nombre

def mejorDisponible(tamanio):
	global inicios
	global tamanios
	if(tamanio< min(tamanios)):
		return tamanios.index(min(tamanios))
	elif(tamanio<max(tamanios)):
		return tamanios.index(max(tamanios))

def eliminarProceso(nombre):
	global unidades
	for i in range(len(unidades)):
		if(unidades[i]== nombre):
			unidades[i] == '-'
	



def main():
	global unidades
	cantidadUnidades = raw_input('Introduce el numero de unidades >>')
	limpiarUnidad(cantidadUnidades)
	print(unidades)
	for i in range(len(unidades)):
		print(i)
	while (True):
		mostrarUnidades()
		obtenerEspaciosVacios()
		nombre = raw_input('Asigne letra del proceso>> ')
		tamanio_proceso = raw_input('Tamanio del proceso>> ')
		asignarProceso(nombre, int(tamanio_proceso)-1)
		
main()

