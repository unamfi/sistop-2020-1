

ficheros = []
tamanio = []
ubicacion = []
informacion = []

def getFileSystem():
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
	print(informacion)

	fileSystem.close()

def anadirInfo(posicion,fileSystem, duracion):
	fileSystem.seek(posicion)
	informacion.append(fileSystem.read(duracion))

def eliminarArchivo(nombre):
	fileSystem = open('fiunamfs.img', 'r+')
	fileSystem.seek(2048)
	posicion = 2048
	while posicion < 2048*5:		
		archivo = fileSystem.read(15).strip()
		if(archivo == nombre):
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
	
		

		


def main():
	getFileSystem()
	infoFileSystem()
	archivoAEliminar = raw_input()
	eliminarArchivo(archivoAEliminar)
main()
