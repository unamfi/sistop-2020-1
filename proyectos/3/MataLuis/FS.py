from sys import exit

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
def info():
    print("Nombre del Sistema: " + nombre)
    print("Version: " + version)
    print("Etiqueta del Volumen: " + etiqueta)
    print("Tamano del cluster en bytes: " + cluster)
    print("Numero de clusters que mide el directorio: " + numero)
    print("Numero de cluster que mide la unidad completa: " + numeroCompleto)

def listar():
    ##print('Hola')
    file = open("fiunamfs.img","r")
    file.seek(2048)
    for i in range(64):
        name = file.read(15)
        if name != 'Xx.xXx.xXx.xXx.':
            print(name)
        file.seek(file.tell()+49)

if (nombre == "FiUnamFS" and version == "0.6"):
    correcto = True
    while(correcto):
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
else:
    print("No se puede abrir el sistema de archivos debido a que no es el archivo correcto o la version correcta. Revise nuevamente que tenga la imagen correcta.")
    exit()

    


