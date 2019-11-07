unidades = []
tamanios = []
inicios = []
memoriaDisponible = 0

#Crea la unidad con el tamanio que se requiera
def limpiarUnidad(tamanio):
	global memoriaDisponible
	global unidades
	for i in range(len(unidades)):
		unidades.remove(0)
		memoriaDisponible.pop(0)
	for i in range(0, int(tamanio)):
		unidades.append('-')
	memoriaDisponible = tamanio

#Muestra lo que hay en la memoria
def mostrarUnidades():
	global unidades
	palabra = ''
	for i in range(len(unidades)):
		palabra = palabra+unidades[i]
	print palabra

#Obtiene los espacios vacios, donde inician y la cantidad de unidades que ocupan
def obtenerEspaciosVacios():
	global unidades
	global tamanios
	global inicios
	for j in range(len(tamanios)):
		tamanios.pop(0)
		inicios.pop(0)
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
	
#Asigna un nuevo proceso
def asignarProceso(nombre, tamanio):
	tamanio+=1
	global inicios
	global tamanios
	global unidades
	global memoriaDisponible
	indice_del_mejor_espacio = mejorDisponible(tamanio)
	if(indice_del_mejor_espacio!= 0):
		print('No cabe el proceso, es necesario borrar un proceso o comprimir')
		menu()
	else:
		print(indice_del_mejor_espacio)
		for i in range(len(unidades)):
			if(inicios[indice_del_mejor_espacio] == i):
				for j in range(tamanio):
					if(i == 1):
						unidades[j] = nombre
						#unidades[j+1] = nombre
					elif(i<len(unidades)-1):
						unidades[i] = nombre
						unidades[i+j] = nombre
					else:
						unidades[i+j] = nombre
					
				inicios.append(i)
				tamanios.append(tamanio+1)
		tamanios.pop(indice_del_mejor_espacio)
		inicios.pop(indice_del_mejor_espacio)
		if(memoriaDisponible == len(unidades)-1):
			memoriaDisponible.append(int(memoriaDisponible)-(int(tamanio)))
		else:
			memoriaDisponible = int(memoriaDisponible) - int(tamanio)

#Revisa donde cabe el proceso y devuelve 0 si el proceso tiene espacio disponible para ser asignado 
def mejorDisponible(tamanio):
	global inicios
	global tamanios
	global memoriaDisponible
	print(str(tamanio) + 'tamanio, memdisp '+ str(memoriaDisponible))
	if(tamanio <= memoriaDisponible):
		return 0

	else:
		return 1

#Compacta la memoria,desplaza los espacios vacios hacia el final
def compactar():
	global unidades
	bandera = 0
	i = 0
	vaciosJuntos = 0
	while bandera == 0:
		if(i>0 and unidades[i]=='-'):
			if(unidades[i-1]=='-'):
				vaciosJuntos +=1
		if(i>0 and unidades[i]!= '-'):
			if(unidades[i-1]=='-'):
				unidades[i-1]= unidades[i]
				unidades[i] = '-'
			if(vaciosJuntos != 0):
				compactar()
		if(i==len(unidades)-1):
			if(unidades[i]=='-' and unidades[i-1] =='-'):
				bandera = 1
			i=0
		i+=1
	#mostrarUnidades()

#Elimina un proceso, asignando espacios libres en su lugar
def eliminarProceso(nombre):
	global unidades
	global memoriaDisponible
	tamanio = 0
	for i in range(len(unidades)):
		if(unidades[i]== nombre):
			unidades[i] = '-'
			tamanio +=1
	memoriaDisponible += tamanio
	print('Se elimino correctamente. Se compactara la unidad')
	compactar()

#Muestra un sencillo menu para controlar las acciones del programa
def menu():
	while (True):
		opcion = raw_input('Escoja una opcion: \n1 Agregar proceso \n2 Eliminar Proceso y compactar unidad \n >>')
		obtenerEspaciosVacios()
		mostrarUnidades()
		if(opcion == '1'):
			nombre = raw_input('Asigne letra del proceso>> ')
			tamanio_proceso = raw_input('Tamanio del proceso>> ')
			if(int(tamanio_proceso)>1 and int(tamanio_proceso)<16):
				asignarProceso(nombre, int(tamanio_proceso)-1)
				mostrarUnidades()
				print('\n\n\n\n')
			else:
				print('Los procesos deben tener un tamanio entre 2 y 15, intente de nuevo')
				print('\n\n\n\n')
				menu()
		elif(opcion == '2'):
			nombre = raw_input('Asigne letra del proceso>> ')
			eliminarProceso(nombre)
			mostrarUnidades()
			print('\n\n\n\n')
		else:
			print('No es una opcion correcta, pruebe de nuevo')
			print('\n\n\n\n')

#funcion main
def main():
	global unidades
	global tamanios
	global inicios
	cantidadUnidades = raw_input('Introduce el numero de unidades >>')
	if(int(cantidadUnidades)<15):
		print('No puede tener un tamanio menor a 15, puesto que pueden haber procesos de tamanio 15')
		main()
	else:
		limpiarUnidad(cantidadUnidades)
		menu()

main()


