import sys
import core.menu as v
from os import listdir
from os.path import isfile, isdir, exists
from core.Fiunamfs import Fiunamfs



def lista():
    for i in listdir('.'):
        if isfile(i):
            print(i)


def main():
    arch = input("Escriba el nombre del archivo a montar"+v.point)
    if not exists(arch):
        fs = Fiunamfs(arch)
    else Fiunamfs.crear_fs:
        vol = input("Nombre del volumen"+v.point)
        fs = Fiunamfs.crear_fs(arch, vol)
    while True:
        print(v.menu)
        opt = input(v.point)
        if opt == "1":
            fs.listar_contenido()
        elif opt == "2":
            arch_fs = input("Archivo de FS a copiar"+v.point)
            nombre_dest = input("Nombre a otorgar"+v.point)
            if not self.copiar_FILESYS_a_eXFILESYS(arch_fs, nombre_dest):
                print("Error")
        elif opt == "3":
            op = input("\t¿Desea ver el contenido del directorio actual?[s/N]"+
                       v.point)
            if op != 's' or op != 'S':
                lista()
            else:
                archivo = input("Nombre del archivo"+v.point)
                if exists(archivo):
                    fs.copiar_eXFILESYS_a_FILESYS(archivo)
                    fs.listar_contenido()
                else:
                    print("Error, verifique el nombre del archivo")
        elif opt == "4":
            arch = input("¿Qué quiere eliminar?")
            fs.delete(arch)
        elif opt == "5":
            print("Desfragmentado...")
            fs.desfragmentar()
        elif opt == "q":
            print("Bye")
            fs.exit=True
        else:
            print("Opcion invalida")

