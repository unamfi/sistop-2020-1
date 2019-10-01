import threading 
import sys

class Mesa:
    cuenta = 0
    mutex = threading.Semaphore(1)
    barrera = threading.Semaphore(0)

    def __init__(self,num_cliente,num_invitados):
        self.num_cliente = num_cliente
        self.num_invitados = num_invitados

    class Cliente:
        def __init__(self,num_cliente,num_invitados):
            self.num_cliente = num_cliente
            self.num_invitados = num_invitados
            #-----------------Debemos pasar los datos de la barrera
            self.cuenta = 0
            self.mutex = threading.Semaphore(1)
            self.barrera = threading.Semaphore(0)

            #------------------------------------------------------  
            self.conseguirMesa()

        def conseguirMesa(self):
            print("El cliente %d ha conseguido una mesa para %d personas" % (num_cliente, num_invitados+1))
            self.ordenarM()

        def revisaCarta(self):
            print("El cliente número %d está revisando la carta" % (num_cliente))

        def decidirOrden(self):        
            Mesa.mutex.acquire()
            print("El cliente número %d está listo para ordenar" % (num_cliente))        
            Mesa.cuenta += 1       
            Mesa.mutex.release()

        def ordenarM(self):              
            self.revisaCarta()
            self.decidirOrden()
            salir = True
            num_hilos = self.num_invitados + 1
            #-------------------------------------------------------------Crea los hilos de sus acompañantes
            for i in range (num_invitados):
                threading.Thread(target = Mesa.Invitado, args= [num_cliente,i]).start()
            #-----------------------------------------------------------------------------------------------
            while salir:
                if Mesa.cuenta == num_hilos:
                    Mesa.barrera.release()
                    salir = False
            Mesa.barrera.acquire()
            Mesa.barrera.release()
            print("La mesa del cliente número %d ha realizado su orden" % (self.num_cliente))

    class Invitado():
        def __init__(self,num_cliente,num_invitado):
            self.num_cliente = num_cliente
            self.num_invitado = num_invitado
            self.revisaCarta()
            self.decidirOrden()                                 

        def revisaCarta(self):
            print("El acompañante número %d del cliente %d está revisando la carta" % (self.num_invitado , self.num_cliente))

        def decidirOrden(self):   
            Mesa.mutex.acquire()   
            print("El acompañante número %d del cliente %d ha decidido que ordenar" % (self.num_invitado, self.num_cliente))        
            Mesa.cuenta += 1
            Mesa.mutex.release()
        
    def iniciarCena(self):
        threading.Thread(target = Mesa.Cliente , args= [num_cliente, num_invitados]).start()
    

if __name__ == '__main__':
    # Recupera el valor de los argumentos
    num_cliente = 1
    num_invitados = 8
    mesa = Mesa(num_cliente,num_invitados)
    mesa.iniciarCena()
