import threading
import time
import random 
import os 

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

def cliente(numCliente):    #Cliente es la funcion que manda a cada hilo, aqui se anuncia que el cliente llego y se agrega a la cola general de espera 
    time.sleep(aleatorios(30))   #Espera para llegada de cada cliente 
    colaGeneral.append(numCliente)
    nombre=capitan(numCliente)
    sentarse(numCliente, nombre)  #Cambiar nombre de esta funcion   #Sentarse es la funcion que define el comportamiento de cada hilo 

#Esta funcion busca un elemento en la lista dada 
def buscarCliente(lista, cliente):
    for i in range(len(lista)):
        if(lista[i] == cliente):
            return i

#Lanzmos x cantidad de hilos que representaran a los clientes, el numero sera aleatorio pero sera entre 0 y 10 
def lanzaHilos():
    for i in range(aleatorios(50)):
        threading.Thread(target=cliente, args=[i]).start()
