"""
"""
memoria = []
"""
La función llena memoria se usa para agregar procesos nuevos
a la memoria, se verifica que haya espacio libre y en caso de no tener 
espacio para agregar más elementos se llama a la función compactacion.
Al agregar nuevos procesos se muestra el mapa de memoria
"""
def llena_memoria(proceso, tamano):
	global memoria
	elementos = len(memoria)
	limite_mem = elementos + tamano
	if limite_mem > 30:
		compactacion(proceso, tamano)
	else:
		conta=0
		while conta < tamano:
			memoria.append(proceso)
			conta+=1
		print("\n!!!!!!!!!!!!!!!!!!!mapa de memoria!!!!!!!!!!!!!!!!!\n")
		for x in memoria[0:10]:
			print('|'+x+'|', end=" ")
		print("\n")
		for x in memoria[10:20]:
			print('|'+x+'|', end=" ")
		print("\n")
		for x in memoria[20:30]:
			print('|'+x+'|', end=" ")
		print("\n")

"""
La función vacia memoria la utilizaremos eliminar elementos de la memoria,
se verifica que exista el proceso indicado y de ser asi se elimina. Una 
vez eliminado el elemento se muestra el mapa de memoria.
"""
def vacia_memoria(proceso, tamano):
	global  memoria
	conta = tamano
	while conta > 0:
		index = memoria.index(proceso)
		memoria.remove(proceso)
		memoria.insert(index ,'*')
		conta-=1
	print("\n!!!!!!!!!!!!!!!!!!!mapa de memoria!!!!!!!!!!!!!!!!!\n")
	for x in memoria[0:10]:
		print('|'+x+'|', end=" ")
	print("\n")
	for x in memoria[10:20]:
		print('|'+x+'|', end=" ")
	print("\n")
	for x in memoria[20:30]:
		print('|'+x+'|', end=" ")
	print("\n")
"""
La función compactacion sirve para agregar procesos a la memoria, 
sólo si existen suficientes * en donde se puedan remplazar por el 
proceso que se quiere ingresar. De ser posible agregar nuevos
elementos esta función muestra el mapa de memoria.
"""
def compactacion(proceso, tamano):
	global memoria
	existe_espacio = '*' in memoria
	if existe_espacio:
		print("se requiere compactar memoria")
		espacio = memoria.count('*')
		if espacio >= tamano:
			conta = tamano
			while conta > 0:
				index = memoria.index('*')
				memoria.remove('*')
				memoria.insert(index ,proceso)
				conta-=1
			print("\n!!!!!!!!!!!!!!!!!!!mapa de memoria!!!!!!!!!!!!!!!!!\n")
			for x in memoria[0:10]:
				print('|'+x+'|', end=" ")
			print("\n")
			for x in memoria[10:20]:
				print('|'+x+'|', end=" ")
			print("\n")
			for x in memoria[20:30]:
				print('|'+x+'|', end=" ")
			print("\n")
		else:
			print("memoria insuficiente...!")
	else:
		print("No hay memoria disponible")

"""
La función opcion sirve para mostrar las opciones que el usuario
puede escoger, además de verificar si los procesos que se quieren 
agregar ya existen.
"""
def opcion(numero):
	global memoria
	if numero == '1':
		proceso = input("ingresa el nombre del proceso: ")
		existe= proceso in memoria
		if existe:
			print("El proceso ya existe en memoria..!")
		else:
			tamano = int(input("ingresa el tamaño de tu proceso: "))
			if tamano < 2 or tamano > 15:
				print("tamaño de proceso: invalido...!")
			else:
				llena_memoria(proceso,tamano)
	elif numero == '2':
		proceso = input("ingresa el nombre del proceso: ")
		existe = proceso in memoria
		if existe:
			tamano= memoria.count(proceso)
			vacia_memoria(proceso, tamano)
		else:
			print("proceso inexistente...!")
	else:
		print("opcion invalida..!")
"""
La función control sirve para mostrar las opciones que 
puede elegir el usuario y pedir la opcion deseada.
"""
def control():
	while True:
		print("1 => Agregar proceso")
		print("2 => Quitar proceso")
		print("0 => salir")
		numero = input("$$ ")
		if numero == '0':
			break
		opcion(numero)

control()