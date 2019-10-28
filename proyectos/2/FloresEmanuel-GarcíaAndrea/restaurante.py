import threading 
import sys
import random
#------------------------Filas de espera
meserosDisp =[]
filaEspera =[]
#---------------------------------Mutex para acceder la fila espera y a los meseros disponibles
mutex_fe = threading.Semaphore(1)
mutex_md = threading.Semaphore(1)
mutex_nmd = threading.Semaphore(1)
#---------------------------------Número de mesas, meseros y clientes (Definidos por el usuario)
num_mesas = int(sys.argv[1])
num_meseros = int(sys.argv[2])
num_clientes = int(sys.argv[3])
#---------------------------------Multiplex para evitar que se ocupen más mesas o meseros de los disponibles
mesas = threading.Semaphore(num_mesas)
meseros = threading.Semaphore(num_meseros)
#----------------------------------------------------------------------------------------------
class Color:
    def __init__(self):
        self.opciones_texto = ['\033[30m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m']    
        self.opciones_fondo = ['\033[40m', '\033[41m', '\033[42m', '\033[43m', '\033[44m', '\033[45m', '\033[46m', '\033[47m']
        self.FIN = '\033[0m'

    def elegirColores(self):
        numt = random.randrange(0,len(self.opciones_texto))
        texto = self.opciones_texto[numt]
        numf = random.randrange(0,len(self.opciones_fondo))
        while numf == numt:
           numf = random.randrange(0,len(self.opciones_fondo))         
        return [texto, self.opciones_fondo[numf]]

class Cliente:
    def __init__(self,num_cliente,num_invitados, texto, fondo, fin):
        self.num_cliente = num_cliente
        self.num_invitados = num_invitados
        self.lista_inv = []
        #..........................Para la barrera de ordenar
        self.cuenta = 0
        self.mutex = threading.Semaphore(1)
        self.barrera = threading.Semaphore(0)
        #....................................................
        #-----------------------Para la impresión con colores
        self.colorT = texto
        self.colorF = fondo
        self.colorf = fin
        #....................................................
        #----------------------------Para la barrera de comer
        self.cuentam = 0
        self.mutexm = threading.Semaphore(1)
        self.barreram = threading.Semaphore(0)
        #----------------------------------------------------
        self.esperarMesa()


    def esperarMesa(self):
        global mesas, mutex_fe, filaEspera
        #Adquiere una mesa, a partir del patrón multiplex
        mesas.acquire()
        #Sí logra adquirir una mesa...
        mutex_fe.acquire()
        #Se saca de la lista de espera, el primero en llegar es el primero en salir
        filaEspera.pop(0)
        mutex_fe.release() 
        #--------------------------------------------------------------------------
        self.llamarMesero("mesa")
        self.conseguirMesa()
        self.llamarMesero("carta")
        self.ordenarM()
        self.llamarMesero("comida")
        self.comer()
        self.llamarMesero("cuenta")
        self.salir()        
        mesas.release()
        
    def crearInvitado(self,i):
        return threading.Thread(target = Cliente.Invitado, args= [self, i]).start()

    #--------------Se llama a un mesero y se le pasa la acción para la cual lo requieren
    def llamarMesero(self, accion):
        global meserosDisp, meseros, mutex_md, num_meseros
        print(self.colorF + self.colorT+ "La mesa del cliente %d esta buscando un mesero" % (self.num_cliente) + self.colorf)
        #-----------Sí aún hay meseros disponibles...
        meseros.acquire()
        mutex_md.acquire()
        mesero = meserosDisp.pop(0)
        mutex_md.release()
        #Se despierta al mesero que se saco de la lista de meseros disponibles
        mesero.despertar(accion,self.num_cliente)
        #Después de realizar la acción vuelve a estar disponible para otras mesas     
        meseros.release()
    #--------------------------------------------------------------------------------------

    def conseguirMesa(self):
        print(self.colorF + self.colorT+ "El cliente %d ha conseguido una mesa para %d personas" % (self.num_cliente, self.num_invitados+1)+ self.colorf)
        #self.ordenarM()

    def revisaCarta(self):
        print(self.colorF + self.colorT+ "El cliente número %d está revisando la carta" % (self.num_cliente) + self.colorf)

    def decidirOrden(self):        
        self.mutex.acquire()
        print( self.colorF + self.colorT+ "El cliente número %d está listo para ordenar" % (self.num_cliente) + self.colorf)        
        self.cuenta += 1       
        self.mutex.release()

    def ordenarM(self):              
        self.revisaCarta()
        self.decidirOrden()
        salir = True
        num_hilos = self.num_invitados + 1
        #-------------------------------------------------------------Crea los hilos de sus acompañantes
        for i in range (self.num_invitados):
            self.crearInvitado(i) 
       
        #-----------------------------------------------------------------------------------------------  
        #---------------------------------------------------------------------------------Patrón barrera
        while salir:     
            if self.cuenta == num_hilos:
                self.barrera.release()
                salir = False
        self.barrera.acquire()
        self.barrera.release()
        #------------------------------------------------------------------------------------------------        
        print(  self.colorF + self.colorT+"La mesa del cliente número %d ha decidido realizar su orden" % (self.num_cliente) + self.colorf)
        self.mutex.acquire()
        self.mutex.release()


    def comer(self):
        num_hilos = self.num_invitados + 1
        salir = True
        print( self.colorF + self.colorT+"El cliente número %d ha comenzado a comer" % (self.num_cliente) + self.colorf)
        print( self.colorF + self.colorT+"El cliente número %d ha terminado de comer" % (self.num_cliente) + self.colorf)
        self.mutexm.acquire()
        self.cuentam = self.cuentam + 1
        self.mutexm.release()
        #-----------------------------------Indica a los invitados que comiencen a comer
        for invitado in self.lista_inv:
            invitado.comer()
        #-------------------------------------------------------------------------------
        #---------------------------------------------------------------------------------Patrón barrera
        while salir:     
            if self.cuentam == num_hilos:
                self.barreram.release()
                salir = False
        self.barreram.acquire()
        self.barreram.release()
        #------------------------------------------------------------------------------------------------        
        print(  self.colorF + self.colorT+"La mesa del cliente número %d ha terminado de comer" % (self.num_cliente) + self.colorf)
        self.mutexm.acquire()
        self.mutexm.release()
        


    def salir(self):
        print(  self.colorF + self.colorT+"La mesa del cliente número %d ha salido del restaurante" % (self.num_cliente) + self.colorf)   
     
    class Invitado():
        def __init__(self, cliente ,num_invitado):
            self.cliente = cliente
            self.num_invitado = num_invitado
            self.revisaCarta()
            self.decidirOrden()                                 

        def revisaCarta(self):
            print(self.cliente.colorF + self.cliente.colorT + "El acompañante número %d del cliente %d está revisando la carta" % (self.num_invitado , self.cliente.num_cliente) + self.cliente.colorf)

        def decidirOrden(self):    
            self.cliente.mutex.acquire()   
            print(self.cliente.colorF + self.cliente.colorT + "El acompañante número %d del cliente %d ha decidido que ordenar" % (self.num_invitado, self.cliente.num_cliente) + self.cliente.colorf)        
            self.cliente.cuenta += 1
            self.cliente.mutex.release()
            self.cliente.lista_inv.append(self)

        def comer(self):
            print(self.cliente.colorF + self.cliente.colorT + "El acompañante número %d del cliente %d ha comenzado a comer" % (self.num_invitado, self.cliente.num_cliente) + self.cliente.colorf)  
            self.cliente.mutexm.acquire()   
            print(self.cliente.colorF + self.cliente.colorT + "El acompañante número %d del cliente %d ha terminado de comer" % (self.num_invitado, self.cliente.num_cliente) + self.cliente.colorf)        
            self.cliente.cuentam += 1
            self.cliente.mutexm.release()
            
class Mesero:
    def __init__(self, num_mesero, texto, fondo, fin):
        self.num_mesero = num_mesero
        self.dormidor = threading.Semaphore(0)
        #-----------------------Para la impresión con colores
        self.colorT = texto
        self.colorF = fondo
        self.colorf = fin
        #....................................................
        self.iniciar()
        
    def iniciar(self):
        global meserosDisp
        mutex_md.acquire()
        meserosDisp.append(self)        
        mutex_md.release()  
        
    #Un sólo será despertado cuando sea requerido que realice una acción
    def despertar(self, accion , num_cliente):
        global mutex_md, meserosDisp, sign
        self.dormidor.release()
        if accion == "mesa":
             self.llevarMesa(num_cliente)
        elif accion == "carta":
             self.mostrarCarta(num_cliente)
        elif accion == "comida":
             self.traerPlatillo(num_cliente)
        elif accion == "cuenta":
             self.traerCuenta(num_cliente)
        print( self.colorF + self.colorT+  "Se desocupo el mesero %d" % (self.num_mesero) + self.colorf)
        self.iniciar()             
        
    def llevarMesa(self, num_cliente):
        print( self.colorF + self.colorT+ "El mesero número %d esta llevando al cliente %d a su mesa" % (self.num_mesero,num_cliente) + self.colorf)

    def mostrarCarta(self, num_cliente):
        print(self.colorF + self.colorT+ "El mesero número %d ha entregado las cartas a la mesa del cliente %d" % (self.num_mesero, num_cliente) + self.colorf) 

    def traerPlatillo(self, num_cliente):
        print(self.colorF + self.colorT+ "El mesero número %d está llevando la orden de la mesa %d" %(self.num_mesero, num_cliente) + self.colorf)
        print(self.colorF + self.colorT+ "Los platillos de la mesa %d se están preparando" % (num_cliente)+ self.colorf)
        print(self.colorF + self.colorT+ "El mesero número %d ha servido los platillos a la mesa del cliente %d" % (self.num_mesero, num_cliente)+ self.colorf)

    def traerCuenta(self, num_cliente):
        print(self.colorF + self.colorT+ "El mesero número %d ha llevado la cuenta a la mesa del cliente %d" % (self.num_mesero, num_cliente) + self.colorf)      
            
   
class Restaurante:
    def __init__(self, num_meseros, num_clientes):
        global filaEspera, meserosDisp
        self.num_meseros = num_meseros
        self.num_clientes = num_clientes
        color = Color()
        letra = ''
        fondo = ''
        fin = color.FIN
        #-------------------------------------------Creamos los hilos de los meseros
        for m in range(self.num_meseros):
            colores = color.elegirColores()
            letra = colores[0]
            fondo = colores[1]
            threading.Thread(target = Mesero, args=[m, letra, fondo, fin]).start()
        #---------------------------------------------Creamos los hilos de clientes
        for i in range(self.num_clientes):
            #Generamos el número de acompañantes de manera aleatoria
            num_invitados = random.randrange(0,9)
            #Generamos los colores para el texto
            colores = color.elegirColores()
            letra = colores[0]
            fondo = colores[1]
            #Se crean los clientes y se añaden a la lista de espera
            mutex_fe.acquire()            
            filaEspera.append(threading.Thread(target = Cliente , args= [i , num_invitados, letra, fondo, fin]).start())
            mutex_fe.release()    
        #--------------------------------------------------------------------------

if __name__ == '__main__':
    print("Para esta corrida del restaurante, se definió lo siguiente\n Número de meseros: %d \n Número de mesas: %d \n Número de clientes: %d \n" % (num_meseros, num_mesas, num_clientes))
    restaurante = Restaurante(num_meseros,num_clientes)
