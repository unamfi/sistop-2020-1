from sys import exit
from os import stat

file = open("fiunamfs.img","r")
nombre = file.read(8)
file.seek(10)
version = file.read(3)
file.seek(20)
etiqueta = file.read(15)
file.seek(40)
cluster = file.read(5)
file.seek(47)
numero = file.read(2)
file.seek(52)
numeroCompleto = file.read(8)
file.close()

archivos = []
tams = []
clusters = []

def clusterVacio():
    arreAux = []
    busca = 1
    bandera = True
    for i in range(len(clusters)):
        clu=clusters[i]
        arreAux.append(int(clu[0]))
    print(arreAux)
    while bandera:
        if busca in arreAux:
            busca = busca + 1
        else:
            bandera = False
    return busca   

def tablaArchivos():
    global archivos
    global tams
    global clusters
    archivos = []
    tams = []
    clusters = []
    file = open("fiunamfs.img","r+")
    file.seek(2048)
    for i in range(64):
        archivos.append(file.read(15))
        tams.append(file.read(8))
        clusters.append(file.read(5))
        file.seek(file.tell()+36)
    file.close()

def info():
    print("Nombre del Sistema: " + nombre)
    print("Version: " + version)
    print("Etiqueta del Volumen: " + etiqueta)
    print("Tamano del cluster en bytes: " + cluster)
    print("Numero de clusters que mide el directorio: " + numero)
    print("Numero de cluster que mide la unidad completa: " + numeroCompleto)

def listar():
    file = open("fiunamfs.img","r")
    file.seek(2048)
    for i in range(64):
        name = file.read(15)
        if name != 'Xx.xXx.xXx.xXx.':
            print(name)
        file.seek(file.tell()+49)
    file.close()

def borrar(archivo):
    borrado = False
    file = open("fiunamfs.img","r+")
    file.seek(2048)
    for i in range(64):
        name = file.read(15)
        aux = name.strip()
        if aux == archivo:
            file.seek(file.tell()-15)
            file.write('Xx.xXx.xXx.xXx.')
            borrado = True
        file.seek(file.tell()+49)
    file.close()
    return borrado

def tamaArchivo(path):
    si = stat(path).st_size
    return si

def dePcASistema(path, nombre):
    posicion =0
    actual =0
    try:
        new = open(path,"r+")
        file = open("fiunamfs.img","r+")
        file.seek(2048)
        bandera  =  False
        tam = stat(path).st_size
        while(bandera == False):
            name = file.read(15)
            if (name == 'Xx.xXx.xXx.xXx.'):
                file.seek(file.tell()-15)
                file.write(nombre)
                actual = file.tell()
                print("El archivo fue copiado")
                bandera = True
            file.seek(file.tell()+49)
        file.close()
        file = open("fiunamfs.img","r+")
        pa = clusterVacio()
        inde = 2048*pa
        tamano = tamaArchivo(path)
        file.seek(inde)
        file.write(new.read(tamano))
        file.close()
        file = open("fiunamfs.img","r+")
        file.seek(actual)
        file.write(str(pa))
        file.close()
    except:
        print("Este archivo no existe")
    
def deSistemaAPc(archivo,nombre):
    tam = 0 
    clu = 0
    file = open("fiunamfs.img","r") #Se abre el archivo en modo solo lectura
    file.seek(2048) #Se salta el superbloque 
    new = open(archivo,"r+")
    for i in range(64):
        name = file.read(15)
        aux = name.strip()
        if (aux == nombre):
            tam = file.read(8)
            clu = file.read(5)
            file.close()
    aux2 = 2048*clu
    file = open("fiunamfs.img","r")
    file.seek(aux2)
    new.write(file.read(tam))
   
    
def nombreArchivo(path):
    tam = len(path)
    slash = 0
    name = ''
    name2 = ''
    for i in range(tam):
        if (path[i] == '/'):
            slash = i
    for i in range(slash+1,tam):
        name = name + path[i]
    ##Agregar funcion de limiar nombres de los archivos a 15 caracteres
    espaces = 15 - len(name)
    for i in range (espaces):
        name2 = name2 + " "
    return name2 + name
            

  

if (nombre == "FiUnamFS" and version == "0.7"):
    correcto = True
    while(correcto):
        tablaArchivos()
        print("Sistema de Archivos FI Unam FS")
        print("1: Listar")
        print("2: Copiar archivo")
        print("3: Copiar archivo a la computadora")
        print("4: Eliminar archivo")
        print("5: Desgramentar")
        print("6: Mostar informacion del sistema de archivos")
        print("7: Salir")
        opcion = input("Opcion: ")
        if opcion == 6:
            info()
        elif opcion == 1:
            listar()
        elif opcion == 4:
            archivo = raw_input("Nombre del archivo a borrar: ")
            if(borrar(archivo)):
                print('El archivo fue borrado')
            else:
                print('No se encontro el archivo')
        elif opcion == 3:
            archivo = raw_input("Nombre del archivo a copiar: ")
            nombre = nombreArchivo(archivo)
            deSistemaAPc(archivo, nombre)
        elif opcion == 2:
            archivo = raw_input("Nombre del archivo a copiar: ")
            nombre = nombreArchivo(archivo)
            dePcASistema(archivo, nombre)
        elif opcion == 9:
            print(archivos)
            print(clusters)
            print(tams)
        elif opcion == 8:
            va = clusterVacio()
            print (va)
        elif opcion == 7:
            print("Sistema desmontado")
            correcto = False
        elif opcion == 5:
            print("No se implemento")
else:
    print("No se puede abrir el sistema de archivos debido a que no es el archivo correcto o la version correcta. Revise nuevamente que tenga la imagen correcta.")
    exit()

    


