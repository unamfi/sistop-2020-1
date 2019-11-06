from time import time 
from random import randint

pross = {0:'A', 1:'B', 2:'C', 3:'D',4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 24:'X', 25:'Y', 26:'Z'}

opcion = '1'
procesosAsignados = 0
mapaMemoria = ''
suma = 0
desechados = []

def compactar():
    global mapaMemoria
    global suma
    aux = mapaMemoria.count('-')
    if aux > 0:
        suma = suma - aux
        mapaMemoria = mapaMemoria.replace('-','')
        print ("Espacio utilizado: " + str(suma))
        print("Nueva situacion")
        print(mapaMemoria)
        return True
    else:
        print("No se puede compactar mas, sera necesario liberar algun proceso")

def asignar(solicitado, idProceso):
    global mapaMemoria
    global suma
    suma = suma + solicitado
    if (suma <= 30):
        print ("Espacio utilizado: " + str(suma))
        for i in range(solicitado):
            mapaMemoria = mapaMemoria + idProceso
    else:
        suma = suma - solicitado
        print("Ese proceso ya no cabe.")  
        print("Se tratara de compactar")
        if (compactar()):
            asignar(solicitado,idProceso)
    print(mapaMemoria)

def liberar(proceso):
    global mapaMemoria
    global suma
    global desechados
    aux = mapaMemoria.count(proceso)
    print(aux)
    print ("Espacio utilizado: " + str(suma))
    reemplazar = '-'
    mapaMemoria = mapaMemoria.replace(proceso, reemplazar)
    print("El espacio fue liberado se recomienda compactar")
    desechados.append(proceso)
    print(mapaMemoria)



while(opcion != 's' and opcion != 'S'):
    print("1: Agregar proceso \n2: Liberar proceso\n3: Compactar")    
    opcion = raw_input("-> ")
    if opcion == '1':
        print("Asigne un espacio entre 2 y 15")
        espacio = raw_input("Proceso[%s]: " %pross[procesosAsignados])
        if int(espacio) >= 2 and int(espacio) <= 15:
            solicitado = int(espacio)
            asignar(solicitado, pross[procesosAsignados])
            procesosAsignados += 1
        else:
            print("No es un espacio entre 2 y 15")
    elif opcion == '2':
        asig = ' '
        for i in range(procesosAsignados):
            if pross[i] in desechados:
                pass
            else:
                asig = (asig + pross[i]).strip(" ")
        proc = raw_input("Liberar [%s]: " %asig)
        liberar(proc)
    elif opcion == '3':
        compactar()



        
    
    
