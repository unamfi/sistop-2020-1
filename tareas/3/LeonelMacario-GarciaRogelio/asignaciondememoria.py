'Leonel Macario Falcon'
'Rogelio García Hernández'

'Asignacion de memoria'

memoria = []

def llenar_memoria(proceso, tamano):
	global memoria
	elementos = len(memoria)
	limite_mem = elementos + tamano
	if limite_mem > 30:
		compactacion(proceso, tamano)
	else:
		contador1=0
		while contador1 < tamano:
			memoria.append(proceso)
			contador1+=1
		print("\n Mapa de memoria \n")
		for x in memoria[0:10]:
			print('|'+x+'|', end=" ")
		print("\n")
		for x in memoria[10:20]:
			print('|'+x+'|', end=" ")
		print("\n")
		for x in memoria[20:30]:
			print('|'+x+'|', end=" ")
		print("\n")


def vacia_memoria(proceso, tamano):
	global  memoria
	contador = tamano
	while contador1 > 0:
		index = memoria.index(proceso)
		memoria.remove(proceso)
		memoria.insert(index ,'*')
		contador1-=1
	print("\n================= MAPA DE MEMORIA =================\n")
	for x in memoria[0:10]:
		print('|'+x+'|', end=" ")
	print("\n")
	for x in memoria[10:20]:
		print('|'+x+'|', end=" ")
	print("\n")
	for x in memoria[20:30]:
		print('|'+x+'|', end=" ")
	print("\n")

def compactacion(proceso, tamano):
	global memoria
	existe_espacio = '*' in memoria
	if existe_espacio:
		print("se requiere compactar la memoria")
		espacio = memoria.count('*')
		if espacio >= tamano:
			contador1 = tamano
			while contador1 > 0:
				index = memoria.index('*')
				memoria.remove('*')
				memoria.insert(index ,proceso)
				contador1-=1
			print("\nMapa de memoria \n")
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
			print("Memoria insuficiente")
	else:
		print("No hay memoria disponible")


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
				print("tamaño de proceso: invalido")
			else:
				llenar_memoria(proceso,tamano)
	elif numero == '2':
		proceso = input("ingresa el nombre del proceso: ")
		existe = proceso in memoria
		if existe:
			tamano= memoria.count(proceso)
			vacia_memoria(proceso, tamano)
		else:
			print("El proceso no existe")
	else:
		print("opcion no valida")

def control():
	while True:
		print("1 => Agregar proceso")
		print("2 => Quitar proceso")
		print("0 => Salir")
		numero = input("$$ ")
		if numero == '0':
			break
		opcion(numero)

control()
