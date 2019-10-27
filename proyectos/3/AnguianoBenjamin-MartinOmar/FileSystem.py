import os

ficheros = []
tamanio = []
ubicacion = []
informacion = []

def getFileSystem():
	buscarArchivos()
	imprimirDatosArchivos()
	
def buscarArchivos():
	for i in range(len(ficheros)):
		ficheros.pop(0)
		tamanio.pop(0)
		ubicacion.pop(0)
	fileSystem = open('fiunamfs.img','r')
	posicion = 2048
	while posicion < 10240:
		fileSystem.seek(posicion)
		consulta = fileSystem.read(15)
		if(consulta != 'Xx.xXx.xXx.xXx.'):
			ficheros.append(consulta.replace(" "," "))
			fileSystem.seek(posicion+16)
			tamanio.append(fileSystem.read(8))
			fileSystem.seek(posicion+25)
			ubicacion.append(fileSystem.read(5))
		posicion+=64
	fileSystem.close()

def imprimirDatosArchivos():
	rango = len(ficheros)
	for i in range(rango):
		print("nombre: "+ ficheros[i]+" tamanio: "+tamanio[i]+" ubicacion: "+ubicacion[i])

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

def anadirInfo(posicion,fileSystem, peso):
	fileSystem.seek(posicion)
	informacion.append(fileSystem.read(peso))

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
	
def copiarAPC(nombre):
	fileSystem = open('fiunamfs.img', 'r')
	posicion = buscarArchivo(nombre)
	print(posicion)
	if(posicion !=-1):
		copia = open(nombre, 'w')
	#print("ubicacion "+ ubicacion[posicion])
		fileSystem.seek(int(ubicacion[posicion]))
	#print(fileSystem.read(int(tamanio[posicion])))
		copia.write(fileSystem.read(int(tamanio[posicion])))
		print("El archivo "+ nombre + " ha sido copiado con exito")
		copia.close()
	else:
		print('No se encontro el archivo '+ nombre)
	fileSystem.close()	

def buscarArchivo(nombre):
	buscarArchivos()
	posicion = -1
	for i in range(len(ficheros)):
		if ficheros[i].strip() == nombre:
			posicion = i
	return posicion	

def copiarAMiFileSystem(nombre):
	archivo = open(str(nombre), 'r')
	fileSystem = open('fiunamfs.img', 'r+')
	posicion = 2048
	while posicion < 10240:
		fileSystem.seek(posicion)
		consulta = fileSystem.read(15)
		if consulta == 'Xx.xXx.xXx.xXx.':
			fileSystem.seek(posicion)
			fileSystem.write(' '*(15-len(nombre)) + nombre)
			fileSystem.seek(posicion+16)
			fileSystem.write("0"*(8 -(len(str(os.stat(nombre).st_size)))) + str(os.stat(nombre).st_size).encode())
			fileSystem.seek(posicion+25)
			fileSystem.write("0"*(5-len(str(posicion+25/2048).encode())) + str(posicion+25/2048).encode())
			fileSystem.close()
			archivo.close()
			print("Archivo " + nombre + " copiado al file system")
			break
		posicion += 64
	archivo.close()
	fileSystem.close()

def desfragmentar():
	getFileSystem()
	fileSystem = open('fiunamfs.img', 'r+')
	posicion = 2048
	eliminarTodos()
	for i in range(len(ficheros)):
		fileSystem.seek(posicion)
		fileSystem.write(ficheros[i])
		fileSystem.seek(posicion+16)
		fileSystem.write("0"*(8 -(len(str(tamanio[i])))) + str(tamanio[i]).encode())
		fileSystem.seek(posicion+25)
		fileSystem.write("0"*(5-len(str((posicion)))) + str((posicion)))
		posicion = posicion+64
	fileSystem.close()
	print('Se ha desfragmentado correctamente')

def eliminarTodos():
	fileSystem = open('fiunamfs.img', 'r+')
	posicion = 2048
	while(posicion< 10240):
		fileSystem.seek(posicion)
		fileSystem.write('Xx.xXx.xXx.xXx.')
		posicion= posicion + 64
	fileSystem.close()

def menu():
	while(True):
		print('1 Listar archivos \n2 Copiar un archivo de fiunamfs a mi PC\n3 Copiar un archivo de mi PC a fiunamfs\n4 Eliminar un archivo de fiunamfs\n5 desfragmentar\n6 Salir')
		opcion = input("Escoja una opcion >> ")
		if(opcion == 1):
			getFileSystem()
		elif(opcion == 2):
			archivoACopiar = raw_input("Escriba el nombre del archivo, incluidad la extension ")
			copiarAPC(archivoACopiar)
		elif(opcion == 3):
				archivoACopiar = raw_input('Escriba el nombre del archivo, incluida la extension ')
				copiarAMiFileSystem(archivoACopiar)
		elif(opcion == 4):
			archivoABorrar = raw_input('Escriba el nombre del archivo a borrar, incluida la extension ')
			eliminarArchivo(archivoABorrar)
		elif(opcion == 5):
			desfragmentar()
		elif(opcion == 6):
			print('Hasta la vista')
			break
def main():
	infoFileSystem()
	menu()
main()

