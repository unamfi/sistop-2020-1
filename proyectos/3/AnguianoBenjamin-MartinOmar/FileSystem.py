import os
import datetime
import time
import math

ficheros = []
tamanio = []
ubicacion = []
informacion = []
fechaCreacion = []
fechaModificacion = []
nombres=[]
bitacora = []
bitacoraArchivo = []


	#Obtengo e imprimo los metadatos de los archivos que hay en el sistema
def getFileSystem():
	buscarArchivos()
	imprimirDatosArchivos()
	
	#Busca los metadatos de los archivos
def buscarArchivos():
	#Quito los datos temporales de los arreglos, para que no aparezcan duplicados
	for i in range(len(ficheros)):
		ficheros.pop(0)
		tamanio.pop(0)
		ubicacion.pop(0)
		fechaCreacion.pop(0)
		fechaModificacion.pop(0)
	fileSystem = open('fiunamfs.img','r')
	posicion = 2048
		#Recorro los clusters de metadatos y guardo la info en arreglos
	while posicion < 10240:
		fileSystem.seek(posicion)
		consulta = fileSystem.read(15)
		if(consulta != 'Xx.xXx.xXx.xXx.'):
			ficheros.append(consulta.replace(" "," "))
			fileSystem.seek(posicion+16)
			tamanio.append(fileSystem.read(8))
			fileSystem.seek(posicion+25)
			ubicacion.append(fileSystem.read(5))
			fileSystem.seek(posicion+31)
			fechaCreacion.append(fileSystem.read(14))
			fileSystem.seek(posicion+46)
			fechaModificacion.append(fileSystem.read(14))
		posicion+=64
	fileSystem.close()
	#Imprime los metadatos de los archivos
def imprimirDatosArchivos():
	rango = len(ficheros)
	for i in range(rango):
		print("nombre: "+ ficheros[i]+" tamanio: "+tamanio[i]+" CusterInicial: "+ubicacion[i]+" Fecha Creacion "+str(fechaCreacion[i])+ " ultima modificacion "+ str(fechaModificacion[i]))
#Obtengo la informacion del sistema de archivos
def infoFileSystem():
	fileSystem = open('fiunamfs.img', 'r')
	anadirInfo(0,fileSystem,8)
	anadirInfo(10,fileSystem,3)
	anadirInfo(20,fileSystem,15)
	anadirInfo(40,fileSystem,5)
	anadirInfo(47,fileSystem,2)
	anadirInfo(52,fileSystem,8)
	print('NOMBRE <'+informacion[0]+'> VERSION <'+informacion[1]+'> ETIQUETA <'+informacion[2].strip()+'> TAMANIO CLUSTER <'+informacion[3]+'> CLUSTERS EN DIR <'+informacion[4]+'> CLUSTERS UNIDAD COMPLETA <'+ informacion[5]+'>')
	fileSystem.close()
#Metodo de apoyo a infoFileSystem, para reducir codigo
def anadirInfo(posicion,fileSystem, bytes):
	fileSystem.seek(posicion)
	informacion.append(fileSystem.read(bytes))
#Elimina el archivo con nombre especificado
def eliminarArchivo(nombre):
	fileSystem = open('fiunamfs.img', 'r+')
	fileSystem.seek(2048)
	posicion = 2048
	while posicion < 2048*5:		
		archivo = fileSystem.read(15)
		if(archivo.strip() == nombre):
			fileSystem.seek(posicion)
			fileSystem.write('Xx.xXx.xXx.xXx.')
			print(nombre + ' ha sido eliminado')
			break
		else:
			posicion+=64
			fileSystem.seek(posicion)
			if posicion == 2048*5:
				print('No existe el archivo ' + nombre + ' en el directorio')
	fileSystem.close()
#copia un archivo a la carpeta donde estoy trabajando en PC
def copiarAPC(nombre):
	fileSystem = open('fiunamfs.img', 'r')
	posicion = buscarArchivo(nombre)
	if(posicion !=-1):
		copia = open(nombre, 'w')
		fileSystem.seek(int(ubicacion[posicion])*2048)
		print(int(ubicacion[posicion])*2048)
		copia.write(fileSystem.read(int(tamanio[posicion])))
		print("El archivo "+ nombre + " ha sido copiado con exito")
		nombres.append(nombre)
		copia.close()
	else:
		print('No se encontro el archivo '+ nombre)
	fileSystem.close()	
#Metodo que busca si un archivo existe, devuelve la posicion temporal en el arreglo ficheros
def buscarArchivo(nombre):
	buscarArchivos()
	posicion = -1
	for i in range(len(ficheros)):
		if ficheros[i].strip() == nombre:
			posicion = i
	return posicion	
#Metodo que copia un archivo de la carpeta actual del PC a mi file system
def copiarAMiFileSystem(nombre):
	fileSystem = open('fiunamfs.img', 'r+') 
	peso = os.path.getsize(nombre) #obtengo el tamanio del archivo a copiar
	clusters =  math.ceil(int(peso)/ 2048.00) #calculo cuantos cluster se van a utilizar
	f = datetime.datetime.strptime(time.ctime(os.path.getctime(nombre)),"%a %b %d %H:%M:%S %Y")
	#Obtengo la fecha de creacion en el formato requerido 
	fechaCreacion = str(f.year)+str(f.month).zfill(2) + str(f.day).zfill(2) + str(f.hour).zfill(2)+ str(f.minute).zfill(2) + str(f.second).zfill(2) 
	fm = datetime.datetime.now()
	#Obtengo la fecha de modificacion en el formato requerido
	fechaModificacion = str(fm.year)+str(fm.month).zfill(2) + str(fm.day).zfill(2) + str(fm.hour).zfill(2)+ str(fm.minute).zfill(2) + str(fm.second).zfill(2) 
	try:
		#Indice del arreglo de ubicacion del cluster mas alto en el que hay un archivo
		ubicacionMasAlta =ubicacion.index(max(ubicacion))
		#Ultimo cluster en el que hay un archivo
		ultimoCluster = ubicacion[ubicacionMasAlta]
		tamanioClusters = int(round(int(tamanio[ubicacionMasAlta])/2048.00)) 
	except:
		ultimoCluster = 5
		tamanioClusters = 0
	#calculo donde terminara el archivo
	total = (float(ultimoCluster) + tamanioClusters)*2048 
	archivo = open(nombre,'r')  
	fileSystem.seek(total) 
	#escribo los datos
	fileSystem.write(archivo.read(peso)) #
	name = nombre.rjust(15) 
	posicion = 2048
	while posicion < 10240:
		fileSystem.seek(posicion)
		consulta = fileSystem.read(15)
		if consulta == 'Xx.xXx.xXx.xXx.':
			#Agrego la informacion del archivo
			fileSystem.seek(posicion)
			fileSystem.write(name.encode())
			fileSystem.seek(posicion+16)
			fileSystem.write('0'*(8-len(str(peso)))+str(peso).encode())
			fileSystem.seek(posicion+25)
			fileSystem.write('0'*(5-len(str(int(round(total/2048))).encode()))+str(int(round(total/2048))).encode())
			fileSystem.seek(posicion+31)
			fileSystem.write(fechaModificacion.encode())
			fileSystem.seek(posicion+46)
			fileSystem.write(fechaCreacion.encode())
			fileSystem.close()
			archivo.close()
			print("Archivo "+ nombre +" Copiado a FiUnamFS")
			return
		posicion += 64

#Metodo que copia archivos a pc, elimina metadatos en fileSystem y 
#copia los archivos de forma contigua al fileSystem
def desfragmentar():
	fileSystem = open('fiunamfs.img', 'r+')
	for i in range(len(ficheros)):
		copiarAPC(str(ficheros[i]).strip())
	eliminarTodos()
	buscarArchivos()
	for i in range(len(nombres)):
		copiarAMiFileSystem(str(nombres[i]))
		buscarArchivos()
	fileSystem.close()
	print('Se ha desfragmentado correctamente')
#Metodo que marca como disponible los bytes del nombre de archivo
def eliminarTodos():
	fileSystem = open('fiunamfs.img', 'r+')
	posicion = 2048
	while(posicion< 10240):
		fileSystem.seek(posicion)
		fileSystem.write('Xx.xXx.xXx.xXx.')
		posicion= posicion + 64
	fileSystem.close()

def menu(banderaBitacora):
	while(True):
		print('1 Listar archivos \n2 Copiar un archivo de fiunamfs a mi PC\n3 Copiar un archivo de mi PC a fiunamfs\n4 Eliminar un archivo de fiunamfs\n5 desfragmentar\n6 Salir')
		buscarArchivos()
		opcion = input("Escoja una opcion >> ")
		if(opcion == 1):
			print(banderaBitacora)
			if(banderaBitacora == 'Y'):
				agregarABitacora('getFileSystem()','')
			else:
				getFileSystem()
		elif(opcion == 2):
			archivoACopiar = raw_input("Escriba el nombre del archivo, incluidad la extension ")
			if(banderaBitacora == 'Y'):
				agregarABitacora('copiarAPC()', archivoACopiar)
			else:
				copiarAPC(archivoACopiar)
		elif(opcion == 3):
			archivoACopiar = raw_input('Escriba el nombre del archivo, incluida la extension ')
			if(banderaBitacora == 'Y'):
				agregarABitacora('copiarAMiFileSystem()', archivoACopiar)
			else:
				copiarAPC(archivoACopiar)
		elif(opcion == 4):
			archivoABorrar = raw_input('Escriba el nombre del archivo, incluida la extension ')
			if(banderaBitacora == 'Y'):
				agregarABitacora('eliminarArchivo()', archivoABorrar)
			else:
				eliminarArchivo(archivoABorrar)
		elif(opcion == 5):
			if(banderaBitacora == 'Y'):
				agregarABitacora('desfragmentar()','')
			else:
				desfragmentar()
		elif(opcion == 6):
			if(banderaBitacora == 'Y'):
				print('Eventos a realizar desde la bitacora')
				for i in range(len(bitacora)):
					print(bitacora[i])
				for i in range(len(bitacora)):
					lanzarProceso(bitacora[i], bitacoraArchivo[i])
			print('Hasta la vista')
			break
def agregarABitacora(proceso, archivo):
	bitacora.append(proceso)
	bitacoraArchivo.append(archivo)
def lanzarProceso(proceso, archivo):
	if(proceso == 'getFileSystem()'):
		getFileSystem()
	elif(proceso == 'copiarAPC'):
		copiarAPC(archivo)
	elif(proceso == 'copiarAMiFileSystem'):
		copiarAMiFileSystem(archivo)
	elif(proceso == 'eliminarArchivo'):
		eliminarArchivo(archivo)
	else:
		desfragmentar()

def main():
	#Revisa dos lineas de abajo y banderaBitacora (Esta hasta arriba), no lo reconoce en el metodo menu.
	print('Desea usar bitacora: Y o N >>')
	banderaBitacora = raw_input()
	infoFileSystem()
	menu(banderaBitacora)
	
main()
