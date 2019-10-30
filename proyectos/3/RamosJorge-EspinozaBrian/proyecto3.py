# -*- encoding: utf-8	

# importamos las librerias nescesarias
import os
import math
import time
import datetime

# declaracion de arreglos a utilizar
files = []
size = []
localitation = []
info=[]

#Abro y recorro el archivo obteniendo listas de los nombres, sizes y cluster inicial de cada archivo
def getFiles():
	fileSystem = open('fiunamfs.img','r')
	currentPosition = 2048
	while currentPosition < 10240:
		fileSystem.seek(currentPosition)
		# nombre del archivo
		byte = fileSystem.read(15)
		if byte != 'Xx.xXx.xXx.xXx.':
			files.append(byte.replace(" ",""))
			fileSystem.seek(currentPosition+16)
			# tamano del archivo
			size.append(int(fileSystem.read(8)))
			fileSystem.seek(currentPosition+25)
			# ubicacion del archivo
			localitation.append(int(fileSystem.read(5)))
		currentPosition += 64
	currentPosition = 10240
	fileSystem.close()


#Aqui se obtine y guarda la informacion del sistema para luego ser mostrada
def getInfo():
	fileSystem = open('fiunamfs.img','r')
	currentPosition = 0
	fileSystem.seek(currentPosition)
	# nombre del sistema de archivos
	byte = fileSystem.read(8)
	info.append(byte)
	# Version de la implementacion.
	currentPosition = 10
	fileSystem.seek(currentPosition)
	byte = fileSystem.read(3)
	info.append(byte)
	# Etiqueta del volumen
	currentPosition = 20
	fileSystem.seek(currentPosition)
	byte = fileSystem.read(15)
	info.append(byte)
	# Tamaño del cluster en bytes
	currentPosition = 40
	fileSystem.seek(currentPosition)
	byte = fileSystem.read(5)
	info.append(byte)
	# Numero de clusters que mide el directorio
	currentPosition = 47
	fileSystem.seek(currentPosition)
	byte = fileSystem.read(2)
	info.append(byte)
	# Numero de clusters que mide el directorio
	currentPosition = 52
	fileSystem.seek(currentPosition)
	byte = fileSystem.read(8)
	info.append(byte)
	# se cierra el archivopara evitar problemas
	fileSystem.close()


# copiar a
def copyTo(archivo):
	# abro mi imagen
	fileSystem = open('fiunamfs.img', 'r+b')
	# obtengo la posicion donde se encuentra en la lista files
	posicion_arch = files.index(archivo)
	# obtengo el tamano 
	size_archivo_a_copiar = size[posicion_arch] 
	ubicacion = localitation[posicion_arch]*2048
	fileSystem.seek(ubicacion) 
	copia = open(archivo,'wb') 
	copia.write(fileSystem.read(size_archivo_a_copiar)) 
	copia.close()
	fileSystem.close()
	print("\n archivo copiado con exito ...\n")

# borrar archivos
def deleteFile(archivo_a_eliminar):
	with open('fiunamfs.img','r+') as fileSystem:
		currentPosition = 2048
		fileSystem.seek(currentPosition)
		# mientras la posicion este dentro del directorio puedo buscar el archivo
		while currentPosition < 10240:
			# vamos a leer el nombre de los files en el directorio
			nombre_arch = fileSystem.read(15)
			nombre_arch_stp = nombre_arch.strip()
			# compruebo que el nombre del archivo a eliminar exista en directorio en la posicion actual en fiunamfs.img
			if (nombre_arch_stp == archivo_a_eliminar):
				# si se encuentra, se eliminan metadatos del archivo
				fileSystem.seek(currentPosition)
				fileSystem.write("               ")
				fileSystem.write('0'*49)
				print(" archivo eliminado ...\n")
				x = len(files)
				# actualizacion de las listas de informacion de los files
				for i in range(x):
					files.pop(0)
					size.pop(0)
					localitation.pop(0)
				getFiles()
				break
			else:
				# no se encuentra el archivo: se recorre nuestro puntero para encontrarlo
				currentPosition += 64
				fileSystem.seek(currentPosition)
				# si acabamos de recorrer el directorio y no se encuentra el archivo, no existe
				if(currentPosition==10240):
					print(" error: el archivo no existe")

# copiar desde la ruta de mi programa.py 
def copyFrom(path):
	fileSystem = open('fiunamfs.img', 'r+b')
	peso = os.path.getsize(path) 
	t = datetime.datetime.strptime(time.ctime(os.path.getctime(path)),"%a %b %d %H:%M:%S %Y")
	fecha_creacion = str(t.year)+str(t.month).zfill(2) + str(t.hour).zfill(2)+ str(t.minute).zfill(2) + str(t.second).zfill(2) #obtengo fecha de creacion
	fm = datetime.datetime.now()
	fecha_modificacion = str(fm.year)+str(fm.month).zfill(2) + str(fm.hour).zfill(2)+ str(fm.minute).zfill(2) + str(fm.second).zfill(2) #obtengo fecha de modificacion
	x =localitation.index(max(localitation))
	# obtengo el cluster origen
	clusterOrigin = localitation[x] 
	# obtener el tamano que ocupa en cluster el archivo
	clusterSize = math.ceil(size[x]/2048.00)
	# calculo la direccion del cluster
	total = (clusterOrigin + clusterSize)*2048 
	filePath = open(path,'rb') 
	datos = filePath.read(peso) 
	fileSystem.seek(total) 
	fileSystem.write(datos) 
	fileSystem.close()
	# obtengo el nombre del archivo 
	name = path.rjust(15) 
	fileSystem = open('fiunamfs.img','r+b')
	currentPosition = 2048

	while currentPosition < 10240:
		fileSystem.seek(currentPosition)
		byte = fileSystem.read(15)
		if byte == 'Xx.xXx.xXx.xXx.':
			# guardo la informacion 
			fileSystem.seek(currentPosition+0)
			# nombre del archivo
			fileSystem.write(name.encode('ascii'))
			fileSystem.seek(currentPosition+16)
			# Tamaño del archivo
			fileSystem.write(str(peso).encode('ascii'))
			fileSystem.seek(currentPosition+25)
			# Cluster inicial
			fileSystem.write(str(total).encode('ascii'))
			fileSystem.seek(currentPosition+31)
			# Hora y fecha de ultima modificacion 
			fileSystem.write(fecha_modificacion.encode('ascii'))
			fileSystem.seek(currentPosition+46)
			# Hora y fecha de creación
			fileSystem.write(fecha_creacion.encode('ascii'))
			fileSystem.close()
			filePath.close()
			print("archivo copiado ...")
			return
		currentPosition += 64
	currentPosition = 10240

# funcion para animar la salida
def salida(textTo):
    textOut = textTo.split()
    for palabra in textOut:
        print(palabra +" ")
        time.sleep(.4)

# funcion principal 
def main():
	#Abrimos el archivo y leemos donde se encuentra el nombre del sistema
	validation=[]
	fileSystem = open('fiunamfs.img','r')
	currentPosition = 0
	fileSystem.seek(currentPosition)
	byte = fileSystem.read(8)
	validation.append(byte)
	print("Bienvenido acaba de montar "+validation[0])
	#Aqui se verifica que el sistema tenga el nombre de FiUnamFS
	if (validation[0] == 'FiUnamFS'): 
		fileSystem = open('fiunamfs.img', 'r+')
		fileSystem.close()
		getFiles()
		
		while(True):
			print("\nOpciones:\n1. Listar files\n2. Copiar un archivo a mi PC\n3. Copiar un archivo desde mi PC\n4. Eliminar un archivo\n5. salir\n")
			option = input("¿Que deseas hacer? ")
			tipoDato = type(option)
			#Se obtine la informacion del sistema
			if(option==1):
				os.system('clear')
				print("\n\nopcion: Listar archivos\n")
				x = len(files)
				for i in range(x):
					files.pop(0)
					size.pop(0)
					localitation.pop(0)
				getFiles()
				for i in range(len(files)):
					print(files[i])
				x = len(files)
				for i in range(x):
					files.pop(0)
					size.pop(0)
					localitation.pop(0)
				getFiles()
			elif(option==2):
				os.system('clear')
				print("\n\nopcion: Copiar archivo a mi ordenador\n")
				nombreArchivo = raw_input("Ingresa el nombre del archivo: ")
				copyTo((nombreArchivo))
			elif(option==3):
				os.system('clear')
				print("\n\nopcion: Copiar archivo desde mi ordenador\n")
				nombreArchivo = raw_input("Ingresa el nombre del archivo: ")
				copyFrom((nombreArchivo))
			elif(option==4):
				os.system('clear')
				print("\n\nopcion: Eliminar un archivo\n")
				archivo_a_eliminar = raw_input("\nArchivo a eliminar: ")
				deleteFile(archivo_a_eliminar)
			elif(option==5):
				os.system('clear')
				salida (" saliendo . . . 3 2 1 bye")
				os.system('clear')
				break
			elif (tipoDato==str):
				print('no se puede esa opcion intentalo de nuevo')
				main()
				
	else:
		print("error: no se pudo montar correctamente")
		return

#funcion para obtener la informacion del sistema de archivos
getInfo()
print("Informacion:")
print("Nombre: "+info[0] + "\nVersion: "+info[1] +"\nEtiqueta Volumen:"+info[2]+"\nTamano Cluster: "+info[3]+"\nNumero de Clusters: "+info[4]+ "\nNumero Total de Clusters: "+info[5]+"\n\n")

#funcion principal
main()
