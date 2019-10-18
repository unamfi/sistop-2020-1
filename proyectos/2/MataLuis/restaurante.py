import threading
import time
import random 
import os 

#Diccionarios para el menu y para un nombre de cada cliente. 
menu = {'0':'Pollo', '1':'Carne', '2':'Pescado', '3':'Sopa', '4':'Ensalada'}
persona = {'0': 'Luis', '1': 'Jorge', '2':'Daniel', '3':'Diana', '4':'Paola', '5':'Laura', '6': 'Saul', '7':'Sarah', '8': 'Alberto', '9': 'Pedro', '10': 'Monse', '11':'Gunnar', '12': 'Beto', '13': 'Carlos', '14': 'Eduardo', '15':'Fabiola', '16':'Hugo', '17': 'Irma', '18': 'Julia', '19': 'Karina', '20': 'Marcos', '21':'Nora', '22':'Omar', '23': 'Quique', '24': 'Roberto', '25':'Tania', '26':'Uriel', '27':'Ander', '28':'Blanca', '29':'Carmen', '30':'Diego', '31':'Eber','32':'Francisca'}

mutexMesero = threading.Semaphore(1)
mutexCapitan = threading.Semaphore(1)
mutexOrden = threading.Semaphore(1)
mutexPrint = threading.Semaphore(1)
colaGeneral = []
barra = []
mesa1 = []
mesa2 = []
mesa3 = []
mesa4 = []

#Imprime mesas, barra y cola de espera, se manda a llamar cada que un cliente se sienta. 
def imprimir():
    mutexPrint.acquire()
    print("\033[1;33mDistribucion de mesas y personas sentadas identificadas con el numero que se les asigno al llegar")
    print("Barra:")
    print(barra)
    print("Mesa 1:")
    print(mesa1)
    print("mesa 2:")
    print(mesa2)
    print("Mesa 3:")
    print(mesa3)
    print("Mesa 4:")
    print(mesa4)
    print("En espera de lugar:")
    print(colaGeneral)
    mutexPrint.release()

#Introduccion para dar a conocer una pequeña parte del programa. 
def introduccion(): 
    i = 25
    while(i>0):
        print("Este programa simula un restaurante.\nAl llegar, cada cliente lo recibe el Capitan.\nEl Capitan debe preguntarle su nombre para que todos lo conozcan")
        print("Ademas debe preguntarle en que lugar le gustaria sentarse\nSi la mesa que elige esta llena, se le indicara al cliente y podra esperar o elegir otra mesa")
        print("Al sentarse un mesero le dira el menu y le tomara su orden\nEl mesero pasara la orden al chef quien por cada platillo tiene un tiempo diferente")
        print("Comenzamos en %d" %i)
        i -= 1
        time.sleep(1)
        os.system("clear")
    lanzaHilos()

def aleatorios(num):        #Esta funcion genera numeros aleatorios para determinar la cantidad de hilos y el tiempo de duraran comiendo cada cliente
    return random.randrange(num)


def cliente(numCliente):    #Cliente es la funcion que manda a cada hilo, aqui se anuncia que el cliente llego y se agrega a la cola general de espera 
    time.sleep(aleatorios(30))   #Espera para llegada de cada cliente 
    colaGeneral.append(numCliente)
    nombre=capitan(numCliente)
    sentarse(numCliente, nombre)  #Cambiar nombre de esta funcion   #Sentarse es la funcion que define el comportamiento de cada hilo 

#Desarrollo real del cliente en el restaurante.
def estancia(nombre):
    imprimir()
    #time.sleep(aleatorios(5))
    mutexMesero.acquire()
    recibirOrden(nombre)
    mutexMesero.release()
    time.sleep(aleatorios(20))
    print("\033[1;37m%s se ah ido" %persona[nombre])

#El chef recibe la orden del mesero de preparar la comida. 
def chef(orden, nombre):
    print("\033[1;34mChef: Anotado y preparando!.. ")
    time.sleep(aleatorios(5))
    print("\033[1;34mChef: Sale %s para %s" %(menu[orden], persona[nombre]))

#El capitan le da la bienvenida a cada cliente. 
def capitan(numCliente):
    mutexCapitan.acquire() #Mutex que sirve como torniquete para que los clientes llegen de uno a uno. 
    mutexCapitan.release()
    nombre = str(aleatorios(33))
    print("\033[1;31mCapitan: Bienvenido, Cual es su nombre")
    print("\033[1;32mCliente %d: %s" %(numCliente,persona[nombre]))
    print("\033[1;31mCapitan: Listo, tome asiento, elija cualquier mesa o la barra.")
    return nombre
#Esta funcion se utiliza para asignarle asiento a cada cliente.
def sentarse(numCliente, nombre):
    mesa = aleatorios(5) #Cada cliente decide donde sentarse.
    if(mesa == 0): #Se revisa que el cliente quepa en la mesa que selecciono 
        print("\033[1;37m%s se quiere sentar en la barra" %persona[nombre])
    else:
        print("\033[1;37m%s se quiere sentar en la mesa %d" %(persona[nombre],mesa))
    if(len(barra) < 12 and mesa == 0):
        barra.append(colaGeneral.pop(buscarCliente(colaGeneral, numCliente)))
        estancia(nombre)
        barra.pop(buscarCliente(barra, numCliente))
    elif(len(mesa1) < 4 and mesa == 1):
        mesa1.append(colaGeneral.pop(buscarCliente(colaGeneral, numCliente)))
        estancia(nombre)
        mesa1.pop(buscarCliente(mesa1, numCliente))
    elif(len(mesa2) < 4 and mesa == 2):
        mesa2.append(colaGeneral.pop(buscarCliente(colaGeneral, numCliente)))
        estancia(nombre)
        mesa2.pop(buscarCliente(mesa2, numCliente))
    elif(len(mesa3) < 4 and mesa == 3):
        mesa3.append(colaGeneral.pop(buscarCliente(colaGeneral, numCliente)))
        estancia(nombre)
        mesa3.pop(buscarCliente(mesa3, numCliente))
    elif(len(mesa4) < 4 and mesa == 4):
        mesa4.append(colaGeneral.pop(buscarCliente(colaGeneral, numCliente)))
        estancia(nombre)
        mesa4.pop(buscarCliente(mesa4, numCliente))
    else:        #En caso de que no quepa en las mesas, esperara, y podra elegir otra mesa. 
        print("\033[1;31mCapitan: Esa mesa esta llena, quisiera esperar o seleccionar otra mesa?")
        time.sleep(1)
        sentarse(numCliente, nombre)

#Parte de la conversacion de ordenar por parte del cliente
def ordenar(nombre):
    mutexOrden.release()
    orden = str(aleatorios(5))
    print("\033[1;32m%s: Quisiera ordenar %s" %(persona[nombre], menu[orden]))
    return orden   
    
#Parte de la conversacion de ordenar por parte del mesero 
def recibirOrden(nombre):
    mutexOrden.acquire()
    print("\033[1;35mMesero: En nuestro menu se encuentra: Pollo, Carne, Pescado, Ensalada o Sopa. Desea Ordenar?")
    orden = ordenar(nombre)
    print("\033[1;35mMesero: En seguida y bienvenido")
    preparar(orden, nombre)

#El mesero solicita al chef la preparacion del alimento 
def preparar(orden, nombre):
    print("\033[1;35mMesero: %s para %s" %(menu[orden], persona[nombre]))
    chef(orden, nombre)

#Esta funcion busca un elemento en la lista dada 
def buscarCliente(lista, cliente):
    for i in range(len(lista)):
        if(lista[i] == cliente):
            return i

#Lanzmos x cantidad de hilos que representaran a los clientes, el numero sera aleatorio pero sera entre 0 y 10 
def lanzaHilos():
    for i in range(aleatorios(50)):
        threading.Thread(target=cliente, args=[i]).start()

introduccion()
