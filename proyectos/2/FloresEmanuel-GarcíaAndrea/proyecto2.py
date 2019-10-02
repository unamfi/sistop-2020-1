
import threading
import sys
import random
from colores import Colores
#-------------------------------------------Datos generales, se recuperan de los argumentos
num_mesas = 6
num_meseros = 3
#------------------------------------------------------------------------------------------
#Multiplex con los que se garantiza que no se ocupen más mesas o meseros de los que tenemos
mesas = threading.Semaphore(num_mesas)
meseros = threading.Semaphore(num_meseros)
#------------------------------------------------------------------------------------------
#-------------------------------------------------------Para saber que meseros están libres
meserosDisp = []
mutexmd = threading.Semaphore(1)
#------------------------------------------------------------------------------------------
#Para saber cuando cierra el restaurante
clientes_res = 0
mutex_cr = threading.Semaphore(1)
#---------------------------------------

class Mesa:
    #Variables para implementar la barrera cuando todos quieran ordenar
    cuenta = 0
    mutex = threading.Semaphore(1)
    barrera = threading.Semaphore(0)
    #------------------------------------------------------------------

    def __init__(self,num_cliente,num_invitados):
        self.num_cliente = num_cliente
        self.num_invitados = num_invitados

    class Cliente:
        def __init__(self,num_cliente,num_invitados):
            self.num_cliente = num_cliente
            self.num_invitados = num_invitados
            self.esperarMesa()

        #Función desde el inicio de la estadía en el restaurante al fin
        def esperarMesa(self):
            global mesas
            mesas.acquire()
            self.llamarMesero("mesa")
            self.conseguirMesa()
            self.llamarMesero("carta")
            self.ordenarM()
            self.llamarMesero("comida")
            self.llamarMesero("cuenta")
            print("La mesa del cliente %d ha sido desocupada" % (self.num_cliente))
            mesas.release()
        #---------------------------------------------------------------

        #--------------Se llama a un mesero y se le pasa la acción para la cual lo requieren
        def llamarMesero(self, accion):
            global meserosDisp, meseros
            esperarMesero = True
<<<<<<< HEAD
            print(meserosDisp) 
=======
>>>>>>> f3a737d79a69ddf959c07233a998d11ec9af8565
            print(Colores.F_NEGRO + Colores.T_BLANCO + "La mesa del cliente %d esta buscando un mesero" % (self.num_cliente) + Colores.FIN)
            #-----------Revisar si hay meseros disponibles
            while esperarMesero:
                mutexmd.acquire()
                tam = len(meserosDisp)
                mutexmd.release()
                if tam > 0:
                    mutexmd.acquire()
                    mesero = meserosDisp.pop(0)
                    mutexmd.release()
                    esperarMesero = False 
            #---------------------------------------------
            #Se despierta al mesero que se saco de la lista de meseros disponibles
            mesero.despertar(accion,self.num_cliente)
<<<<<<< HEAD
            #Después de realizar la acción vuelve a estar disponible para otras mesas     
=======
            #Después de realizar la acción vuelve a estar disponible para otras mesas
            #meseros.release()
            #---------------------------------------------
            #mutexmd.acquire()
            #print("Se desocupo el mesero %d" % (self.num_cliente))            
            #meserosDisp.append(mesero)             
            #mutexmd.release()               
>>>>>>> f3a737d79a69ddf959c07233a998d11ec9af8565
        #------------------------------------------------------------------------------------

        def conseguirMesa(self):
            print(Colores.F_CIAN + Colores.T_NEGRO + "El cliente %d ha conseguido una mesa para %d personas" % (self.num_cliente, self.num_invitados+1) + Colores.FIN)

        def revisaCarta(self):
            print(Colores.F_CIAN + Colores.T_NEGRO + "El cliente número %d está revisando la carta" % (self.num_cliente) + Colores.FIN)

        def decidirOrden(self):        
            Mesa.mutex.acquire()
            print(Colores.F_CIAN + Colores.T_NEGRO + "El cliente número %d está listo para ordenar" % (self.num_cliente) + Colores.FIN)        
            Mesa.cuenta += 1       
            Mesa.mutex.release()

        def ordenarM(self):              
            self.revisaCarta()
            self.decidirOrden()
            salir = True
            num_hilos = self.num_invitados + 1
            #-------------------------------------------------------------Crea los hilos de sus acompañantes
            for i in range (self.num_invitados):
                threading.Thread(target = Mesa.Invitado, args= [self.num_cliente,i]).start()
                            
            #-----------------------------------------------------------------------------------------------
            while salir:
                if Mesa.cuenta == num_hilos:
                    Mesa.barrera.release()
                    salir = False
            Mesa.barrera.acquire()
            Mesa.barrera.release()

            print(Colores.F_VERDE + Colores.T_NEGRO + "La mesa del cliente número %d ha realizado su orden" % (self.num_cliente) + Colores.FIN)

    class Invitado:
        def __init__(self,num_cliente,num_invitado):
            self.num_cliente = num_cliente
            self.num_invitado = num_invitado
            self.revisaCarta()
            self.decidirOrden()                                 

        def revisaCarta(self):
            print(Colores.F_PURPURA + Colores.T_NEGRO + "El acompañante número %d del cliente %d está revisando la carta" % (self.num_invitado , self.num_cliente) + Colores.FIN)

        def decidirOrden(self):   
            Mesa.mutex.acquire()   
            print(Colores.F_ROJO + Colores.T_NEGRO + "El acompañante número %d del cliente %d ha decidido que ordenar" % (self.num_invitado, self.num_cliente) + Colores.FIN)        
            Mesa.cuenta += 1
            Mesa.mutex.release()

        #--------------------------------
    def iniciarCena(self):
        threading.Thread(target = Mesa.Cliente , args= [self.num_cliente, self.num_invitados]).start()
                

#Falta definir cuando los meseros dejan de trabajar
class Mesero:
    def __init__(self, num_mesero):
        self.num_mesero = num_mesero
        self.dormir = threading.Semaphore(0)
        self.iniciar()

    def iniciar(self):
        global meserosDisp
        mutexmd.acquire()
        meserosDisp.append(self)
        print(meserosDisp)
        mutexmd.release()
        #self.dormirSiesta()
   
    #def dormirSiesta(self):
        #self.dormir.acquire()

    #Un sólo será despertado cuando sea requerido que realice una acción
    def despertar(self, accion , num_cliente):
        #self.dormir.release()
        if accion == "mesa":
             self.llevarMesa(num_cliente)
        elif accion == "carta":
             self.mostrarCarta(num_cliente)
        elif accion == "comida":
             self.traerPlatillo(num_cliente)
        elif accion == "cuenta":
             self.traerCuenta(num_cliente)
        print(Colores.F_AMARILLO + Colores.T_NEGRO + "Se desocupo el mesero %d" % (self.num_mesero) + Colores.FIN)
<<<<<<< HEAD
        
        mutexmd.acquire()
        meserosDisp.append(self)        
        mutexmd.release()
        #self.iniciar()
=======
        self.iniciar()
>>>>>>> f3a737d79a69ddf959c07233a998d11ec9af8565
        
    def llevarMesa(self, num_cliente):
        print(Colores.F_BLANCO + Colores.T_NEGRO + "El mesero número %d esta llevando al cliente %d a su mesa" % (self.num_mesero,num_cliente) + Colores.FIN)

    def mostrarCarta(self, num_cliente):
        print(Colores.F_BLANCO + Colores.T_NEGRO + "El mesero número %d ha entregado las cartas a la mesa del cliente %d" % (self.num_mesero, num_cliente)+ Colores.FIN) 

    def traerPlatillo(self, num_cliente):
        print(Colores.F_BLANCO + Colores.T_NEGRO + "El mesero número %d está llevando la orden de la mesa %d" %(self.num_mesero, num_cliente) + Colores.FIN)
        print(Colores.F_AZUL + Colores.T_NEGRO + "Los platillos de la mesa %d se están preparando" % (num_cliente) + Colores.FIN)
        print(Colores.F_BLANCO + Colores.T_NEGRO + "El mesero número %d ha servido los platillos a la mesa del cliente %d" % (self.num_mesero, num_cliente)+ Colores.FIN)

    def traerCuenta(self, num_cliente):
        print("El mesero número %d ha llevado la cuenta a la mesa del cliente %d" % (self.num_mesero, num_cliente))

class Restaurante:
    def __init__(self, num_meseros, num_clientes):
        self.num_meseros = num_meseros
        self.num_clientes = num_clientes
       
    def recepcion(self):
        #Creamos los hilos de meseros y se agregan a la lista de meseros disponibles
        for i in range(self.num_meseros):
            threading.Thread(target = Mesero, args= [i]).start()
       
        #Creamos los hilos de clientes
        for i in range(self.num_clientes):
            #Generamos el número de acompañantes de manera aleatoria
            num_invitados = random.randrange(0,9) 
            Mesa(i,num_invitados).iniciarCena()
                   

if __name__ == '__main__':
    # Recupera el valor de los argumentos
    num_clientes = 3
    restaurante = Restaurante(num_meseros,num_clientes)
    restaurante.recepcion()