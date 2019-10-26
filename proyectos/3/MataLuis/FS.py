from sys import exit

file = open("fiunamfs.img","r")
nombre = file.read(8)
print(nombre)
file.seek(10)
version = file.read(3)
print(version)
if (nombre == "FiUnamFS" and version == "0.6"):
    correcto = True
    while(correcto):
        print("Sistema de Archivos FI Unam FS")
        print("1: Listar")
        print("2: Copiar archivo")
        print("3: Copiar archivo a la computadora")
        print("4: Eliminar archivo")
        print("5: Desgramentar")
        print("6: Salir")
        opcion = input("Opcion: ")
else:
    print("No se puede abrir el sistema de archivos debido a que no es el archivo correcto o la version correcta. Revise nuevamente que tenga la imagen correcta.")
    exit()
