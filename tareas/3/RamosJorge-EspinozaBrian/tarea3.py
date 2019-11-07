#librerias a usar
import os 
import time

# arreglo donde se almacenara la memoria
memory = []

# funcion que va a llenar el arreglo memory con procesos 
def initMemory(proceso, size):
	global memory
	elementos = len(memory)
	limite_mem = elementos + size
	if limite_mem > 30:
		compactacion(proceso, size)
	else:
		counter=0
		while counter < size:
			memory.append(proceso)
			counter+=1
		print("\nmapa de memoria: \n")
		for i in memory[0:10]:
			print(i, end="")
		print("\n")
		for i in memory[10:20]:
			print(i, end="")
		print("\n")
		for i in memory[20:30]:
			print(i, end="")
		print("\n")

# funcion que elimina procesos de la memoria
def deleteMemory(proceso, size):
	global  memory
	counter = size
	while counter > 0:
		index = memory.index(proceso)
		memory.remove(proceso)
		memory.insert(index ,'-')
		counter-=1
	print("\nmapa de memoria: \n")
	for i in memory[0:10]:
		print(i, end="")
	print("\n")
	for i in memory[10:20]:
		print(i, end="")
	print("\n")
	for i in memory[20:30]:
		print(i, end="")
	print("\n")

# realizacion de la compactacion de la memoria
def compactacion(proceso, size):
	global memory
	exist_espacio = '-' in memory
	if exist_espacio:
		print("se requiere compactar la memoria")
		espacio = memory.count('-')
		if espacio >= size:
			counter = size
			while counter > 0:
				index = memory.index('-')
				memory.remove('-')
				memory.insert(index ,proceso)
				counter-=1
			print("\nmapa de memoria: \n")
			for i in memory[0:10]:
				print(i, end="")
			print("\n")
			for i in memory[10:20]:
				print(i, end="")
			print("\n")
			for i in memory[20:30]:
				print(i, end="")
			print("\n")
		else:
			print("memoria insuficiente")
	else:
		print("No hay memoria disponible")


	
# funcion para animar la salida
def salida(textTo):
    textOut = textTo.split()
    for palabra in textOut:
        print(palabra)
        time.sleep(.4)

#funcion principal
def main():
	while True:
		print("Bienvenido a el programa asignacion de memoria")
		print("¿Que deseas hacer?")		
		print("1. Agregar proceso")
		print("2. Quitar proceso")
		print("3. Salir")
		option = input(">>")

		global memory
		if option == '1':
			os.system('clear')
			proceso = input("ingresa el nombre del proceso: ")
			exist= proceso in memory
			if exist:
				print("El proceso ya existe en memoria")
			else:
				size = int(input("ingresa el tamaño de tu proceso: "))
				if size < 2 or size > 15:
					print("tamaño de proceso: invalido")
				else:
					initMemory(proceso,size)
		elif option == '2':
			os.system('clear')
			proceso = input("ingresa el nombre del proceso: ")
			exist = proceso in memory
			if exist:
				size= memory.count(proceso)
				deleteMemory(proceso, size)
			else:
				print("El proceso no existe")
		elif(option=='3'):
				os.system('clear')
				salida (" saliendo . . . 3 2 1 gracias!! bye")
				os.system('clear')
				break
		else:
			print("opcion no valida")


main()