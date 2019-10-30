# -*- coding: utf-8 -*-
from fiUnam import FIFS
import sys


def ls(fs):
    fs.ls()
    return "zero"
 
def rm(fs):
    if len(sys.argv) == 3:
        fs.rm(sys.argv[2])
    else:
        print("rm: falta operador")
    
def cpout(fs):
    if len(sys.argv) == 3:
        fs.cpout(sys.argv[2],"./")
    else:
        print("cpout:falta operandor")
    
def cpin(fs):
    if len(sys.argv) == 3:
        fs.cpin(sys.argv[2])
    else:
        print("cpin: falta operador")
    
def defrag(fs):
    fs.defrag()

def help(fs):
    print("ls        Listado de Archivos")
    print("rm        Remueve archivo    rm  <file name>")
    print("cpout     Copia un archivo del FIunam al exterior   cpout  <file name>")
    print("cpin     Copia un archivo del exterior al FIunam    cpin  <file name>")
    print("defrag     Desfragmenta el sistema de archivos")
    print("help      Ayuda con listados")
    return "help"

switcher = {
        "ls": ls,
        "rm": rm,
        "cpout": cpout,
        "cpin": cpin,
        "defrag" : defrag,
        "help": help
    }

def numbers_to_strings(argument):
    # Get the function from switcher dictionary
    func = switcher.get(argument, "nothing")
    # Execute the function
    return func()
 
def main():
    fs = FIFS()
    # Seguro que existe un método muchisimo mejor para emular swith case
    # Solo falta buscarlo e implementarlo
    if len(sys.argv) > 1:
        # Get the function from switcher dictionary
        if(switcher.get(sys.argv[1]) == None):
            print("Comando Invalido")
        else:
            func = switcher.get(sys.argv[1], "nothing")
            # Execute the function
            func(fs)
    else :
        print("Please enter a command or use help")

    fs.close()

if __name__ == '__main__':
    main()