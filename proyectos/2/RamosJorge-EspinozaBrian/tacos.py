import threading
import time
import random
import math 

def descargando(semaforo):
    global activasTacos
    global activasTortas
    global activasGorditas
    nombre = threading.current_thread().getName()
    # print('Esperando para ser atendido:', nombre)
    with semaforo:
        ###para generar los numeros aleatorios
        ran=random.randint(1,10)
        nombreint=int(nombre) 
        print("*"*50,'llego el hilo: ',nombreint) 
        if(nombreint%2==0):
            n=ran*2
            print('Esperando para ser atendido:', nombreint)
            if (n>1 and n<=3):
                    activasTacos.append(nombre)
                    print('personas en espera de su orden de tacos', activasTacos)
                    print('...Preparando orden de persona:', nombre)
                    time.sleep(n)
                    activasTacos.remove(nombre)
                    print('orden de la persona', nombre,' entregada')
            elif(n>3 and  n<=7):
                    activasTortas.append(nombre)
                    print('personas en espera de su orden de tortas', activasTortas)
                    print('...Preparando orden de persona:', nombre)
                    time.sleep(n)
                    activasTortas.remove(nombre)
                    print('orden de la persona', nombre,' entregada')
            elif (n>7):
                    activasGorditas.append(nombre)
                    print('personas en espera de su orden gorditas', activasGorditas)
                    print('...Preparando orden de persona:', nombre)
                    time.sleep(n)
                    activasGorditas.remove(nombre)
                    print('orden de la persona', nombre,' entregada')
        elif(nombreint%2==1):
            n=ran
            print('Esperando para ser atendido:', nombreint)
            if (n>1 and n<=3):
                    activasTacos.append(nombre)
                    print('personas en espera de su orden de tacos', activasTacos)
                    print('...Preparando orden de persona:', nombre)
                    time.sleep(n)
                    activasTacos.remove(nombre)
                    print('orden de la persona', nombre,' entregada')
            elif (n>3 and  n<=7):
                    activasTortas.append(nombre)
                    print('personas en espera de su orden de tortas', activasTortas)
                    print('...Preparando orden de persona:', nombre)
                    time.sleep(n)
                    activasTortas.remove(nombre)
                    print('orden de la persona', nombre,' entregada')
            elif (n>7):
                    activasGorditas.append(nombre)
                    print('personas en espera de su orden gorditas', activasGorditas)
                    print('...Preparando orden de persona:', nombre)
                    time.sleep(n)
                    activasGorditas.remove(nombre)
                    print('orden de la persona', nombre,' entregada')
        # activas.append(nombre)
        # print('personas en espera de su orden', activas)
        # print('...Preparando orden de persona:', nombre)
        # time.sleep(n)
        # activas.remove(nombre)
        # print('orden de la persona', nombre,' entregada')

NUM_DESCARGAS_SIM = 4
#activas = []
activasTacos = []
activasTortas = []
activasGorditas = []
semaforo = threading.Semaphore(NUM_DESCARGAS_SIM)
for indice in range(1,10):
    hilo = threading.Thread(target=descargando,
                            name=indice,
                            args=(semaforo,),)
    hilo.start()




