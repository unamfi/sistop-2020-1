#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import threading
import time

#En esta variable se define en numero de clientes que puede haber conectados al servidor
UsuariosConectados=2
#Se definen los multiplex que nos permiten controlar el flujo en cada direccion
multiplexConsulta = threading.BoundedSemaphore(UsuariosConectados)
multiplexGuardar = threading.BoundedSemaphore(UsuariosConectados)

def esSeguroConsultar():
    if (numUsuariosGuardando - (numUsuariosConsultando + 1)) == 0:
        return False
    return True

def esSeguroGuardar():
    if (numUsuariosConsultando - (numUsuariosGuardando + 1)) == 0:
        return False
    return True

#Estas variables nos permiten decidir si es seguro consultar o guardar. 
numUsuariosConsultando = 0
numUsuariosGuardando = 0
mutexAGuardar = threading.BoundedSemaphore(0)
mutexAConsulta = threading.BoundedSemaphore(0)
sepuedeConsultar = esSeguroConsultar()
sepuedeGuardar = esSeguroGuardar()

def elegirAccion():
        if random.random() < 0.5:
            #1 para Consultar
            return 1
        else:
            #0 para Guardar
            return 0

AConsulta=set()
AGuardar = set()
Lectura = set()
class Usuario():
    
    def __init__(self, nombre):
        global numUsuariosGuardando
        global numUsuariosConsultando
        

        self.nombre = nombre
        self.accionActual = -1
        #print(self.nombre + " está en espera")
        self.isWaiting = True
        Lectura.add(self)

    def __str__(self):
        accion =  "de consulta" if self.accionActual == 1 else "de guardar"
        return self.nombre + " está realizando " + accion
    

    def eventos(self):
        global numUsuariosGuardando
        global numUsuariosConsultando
        global sepuedeGuardar
        global sepuedeConsultar
        """mutexAGuardar.acquire()
        sepuedeConsultar = esSeguroConsultar()
        mutexAGuardar.release()
        mutexAGuardar.acquire()
        sepuedeGuardar = esSeguroGuardar()
        mutexAGuardar.release()"""

        iteracion = 1
        while(True):
            nuevaAccion = elegirAccion()
            if nuevaAccion == self.accionActual:
                tmp =  "de sentido del reloj" if self.accionActual == 1 else "contra reloj"
                
                continue
            if self.isWaiting:
                Lectura.remove(self)
                if nuevaAccion == 1 and iteracion == 1 and sepuedeConsultar:
                     #Quiere decir que la accion que realizaba era consulta
                    multiplexConsulta.acquire()
                    AConsulta.add(self)
                    self.accionActual = 1
                    self.isWaiting = False
                    numUsuariosConsultando+=1
                    #print(self)
                    continue   
                elif nuevaAccion  == 0 and iteracion == 1 and sepuedeGuardar:
                    multiplexGuardar.acquire()
                    AGuardar.add(self)
                    self.accionActual = 0
                    self.isWaiting = False
                    numUsuariosGuardando+=1
                    #print(self)
                    continue

                if nuevaAccion == 1:
                    
                    multiplexGuardar.release()
                    AGuardar.remove(self)

                elif nuevaAccion  == 0:
                    multiplexConsulta.release()
                    AConsulta.remove(self)  


                if nuevaAccion == 1 and sepuedeConsultar:
                     
                    multiplexConsulta.acquire()
                    AConsulta.add(self)
                    self.accionActual = 1
                    self.isWaiting = False
                    numUsuariosConsultando+=1
                    numUsuariosGuardando -= 1
                    #print(self)

                elif nuevaAccion  == 0 and  sepuedeConsultar:
                    multiplexGuardar.acquire()
                    AGuardar.add(self)
                    self.accionActual = 0
                    self.isWaiting = False
                    numUsuariosGuardando+=1
                    numUsuariosConsultando -= 1
                    #print(self)
                else:
                    Lectura.add(self)
                    self.isWaiting = True
                    
    
            elif not self.isWaiting:
                Lectura.add(self)
                self.isWaiting  = True
                #print(self.nombre+" está en el Lectura de la pecera.")
            
            iteracion += 1
            time.sleep(5)
            
                
def getStatus():
    while(True):
        string="************************************\n"
        string += "Usuarios consultando[ " + "*"*len(AConsulta)+" ]\n"
        for Usuario in AConsulta:
            string += "( ͡❛ ͜ʖ ͡❛)  "+Usuario.nombre+"\n"
        string += "Usuarios guardando[ " + "*"*len(AGuardar)+" ]\n\n"
        for Usuario in AGuardar:
            string += "( ͡❛ ͜ʖ ͡❛)  "+Usuario.nombre+"\n"
        time.sleep(5)
        print(string)

def main():
    omar = Usuario("Omar")
   	#mario = Usuario("Mario")
    claudia = Usuario("Claudia")
    daniela = Usuario("Daniela")
    saul = Usuario("Saul")
    ricardo = Usuario("Ricardo")
    gunnar = Usuario("Gunnar")
    cliente=[omar, mario, claudia, daniela, saul, ricardo, gunnar]
    print("*"*30)
    hilos = []
    hilos.append(threading.Thread(target=getStatus))

    for Usuario in cliente:
        hilo = threading.Thread(target=Usuario.eventos)
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

if __name__ =="__main__":
   main()
