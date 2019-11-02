import argparse
from string import ascii_uppercase
from memoria import Memoria

LETRAS = set(ascii_uppercase)

parser = argparse.ArgumentParser()
parser.add_argument("unidades", help="Unidades de memoria que tiene el sistema", 
                                type=int, 
                                nargs='?',
                                default=30)
args = parser.parse_args()

print('Simulación de asignación y liberación de procesos en memoria.')
print('Tamaño: %i unidades.' % args.unidades)
operacion = -1
mem = Memoria(args.unidades)
while not operacion == 2:
    print('\nEstado actual: \n\t', end='')
    mem.imprime_mem()
    operacion = int(input('Operación a realizar (0 : asignar, 1 : liberar, 2: salir): '))
    if(operacion == 0):
        lista_procesos = sorted(LETRAS-set(mem.procesosEnMemoria)) # Quitamos las letras que ya usamos
        proceso = lista_procesos[0]
        u_requeridas = int(input('Nuevo proceso (%s): ' % proceso))
        mem.asignar(proceso, u_requeridas)
    elif(operacion == 1):
        strpem = ''.join(mem.procesosEnMemoria) # Cadena de procesos en memoria
        proceso = str(input('Eliminar proceso (%s): ' % strpem))
        mem.liberar(proceso)
    elif(operacion==2):
        print('Adiós :D')
    else:
        print('¡Opción inválida!')