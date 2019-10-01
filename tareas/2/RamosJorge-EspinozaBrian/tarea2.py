#Tarea 3
#Lenguaje Python 3

import random


class Tarea2:
    h=0
    procID=str()
    gh=0

    def __init__(self,procID,time):
        self.procID=procID
        self.h=time
    def obtenerprocID(self):
        return self.procID
    def obtenerH(self):
        return self.h
    def tpp(self):
        self.gh+=1
    def isComplete(self):
        return self.gh == self.h -1
    def obtenerGH(self):
        return self.gh
    def setTA(self):
        self.gh=0

#funcion principal 
def main():
    print("Ejemplo de la tarea 2")
    Proc=[(Tarea2('A',3),0),(Tarea2('B',5),1),(Tarea2('C',2),3),(Tarea2('D',5),9),(Tarea2('E',5),12)]
    imprimirLista(Proc)
    Proc2=Proc.copy()
    Proc3=Proc.copy()
    Proc4=Proc.copy()
    generaTablaFCFS(Proc)
    FCFS(Proc)
    Limpiador(Proc2)
    RoundRobin(Proc2,1)
    Limpiador(Proc3)
    RoundRobin(Proc2,4)
    Limpiador(Proc4)

    # generador de numeros aleatorios procesos y rondas
    duracionmax=10
    procesosmax=10
    rondas=5
    for i in range(rondas):
        print('_'*50+" Ronda " + str(i)+'_'*50)
        PR=Aleatorios(procesosmax,duracionmax)
        imprimirLista(PR)
        PRroc2=PR.copy()
        PRroc3=PR.copy()
        PRroc4=PR.copy()        
        generaTablaFCFS(PR)
        FCFS(PR)
        Limpiador(PRroc2)
        RoundRobin(PRroc2,1)
        Limpiador(PRroc3)
        RoundRobin(PRroc2,4)
        Limpiador(PRroc4)
    return ()

#funcion que toma los datos y los imprime
def Impresion(llegada,t,proc,Ini,Fin,T,E,P):
    #imprime tabla
    print('{:<10}{:<12}{:10}{:<10}{:<15}{:<13}{:<15}{:<15.2f}'.format(llegada,t,proc,Ini,Fin,T,E,P))

def generaTablaFCFS(Procesos):
    Inicio=0
    Fin=0
    T=0
    E=0
    P=0
    k=0
    PromTiempo=0
    PromEspera=0
    PromPenalizacion=0
    print('FCFS')
    #imprime tabla
    print('{:10}{:12}{:12}{:10}{:13}{:10}{:15}{:15}'.format('Llegada','Tiempo','Proceso','Inicio','Fin','Tiempo','Espera','Penalizacion'))
    for i in Procesos:
        Fin=Inicio+i[0].obtenerH()
        T=Fin-i[1]
        PromTiempo+=T
        E=T-i[0].obtenerH()
        PromEspera+=E
        P=T/i[0].obtenerH()
        PromPenalizacion+=P
        Impresion(i[1],i[0].obtenerH(),chr(k+65),Inicio,Fin,T,E,P)
        Inicio+=i[0].obtenerH()
        k+=1
    print('_'*90)
    n=len(Procesos)
    print('{:11} {:10} {:13} {:10} {:11}{:<11.2f}{:<11.2f}{:<13.2f}'.format('Promedio','','','','',PromTiempo/n,PromEspera/n,PromPenalizacion/n))
    print("_"*90)
    return ()

def FCFS(Procesos):
    print("_"*90)
    print("Resultados FCFS")
    while(len(Procesos)>0):
        Actual=Procesos[0][0]
        if Actual.isComplete():
            Procesos.pop(0)     
        print(Actual.obtenerprocID(),end='')
        Actual.tpp()
    print()
    print("_"*90)
    return ()


def Indicador(Proceso,Procesos):
    k=0
    for i in Procesos:
        if Proceso is i[0]:
            return k
        k+=1
    return ()


#limpia las copias de las listas de objetos de procesos
def Limpiador(P):
    for i in P:
        i[0].setTA()
    return ()


def RoundRobin(Procesos,Q):
    print("_"*90)
    print("Resultados Round Robin ",Q)
    t=0
    L=list()
    i=1
    L.append(Procesos[0][0])
    CC=True
    T=0
    E=0
    P=0
    while(len(L)>0):
        
   
        if i<len(Procesos) and Procesos[i][1] == t:
            L.append(Procesos[i][0])
            i+=1
            
        Actual=L[0]
        
        if Actual.obtenerGH()% Q == 0 and CC:
            Aux=L.pop(0)
            L.append(Aux)  

        Actual=L[0]
        CC=True
        #metricas
        if Actual.isComplete():
            indice=Indicador(Actual,Procesos)
            TA=((t+1)- Procesos[indice][1] )
            T+=TA
            E+=TA-Actual.obtenerH()
            P+=TA/Actual.obtenerH()
            L.pop(0)
            CC=False

        print(Actual.obtenerprocID(),end='')
        Actual.tpp()
        t+=1
    
    
    print()
    print("T: ",T/len(Procesos),end="")
    print("\tE: ",E/len(Procesos),end="")
    print("\tP: {:.2f}".format(P/len(Procesos)),end="")
    print()
    print("_"*90)
    return ()

    
#Funcion para generar las listas aleatorias 
def Aleatorios(procesomax,duracionmax):
    Procesos=list()

    duracion = random.randrange(2,duracionmax)
    llegada = 0
# se agregan a la lista y la duracion y a los procesos
    Procesos.append( (Tarea2('A',duracion),llegada) )
    llegada_ant=llegada
    for i in range(1,procesomax):
        
        llegada = random.randrange(llegada,llegada+duracion)
        if llegada==llegada_ant:
            llegada+=1
        duracion = random.randrange(1,duracionmax)      
        Procesos.append( (Tarea2(chr(i+65),duracion),llegada) )
        llegada_ant=llegada
    return Procesos
#impime lista
def imprimirLista(Procesos):
    for i in Procesos:
        print(" {}: {}, t={};".format(i[0].obtenerprocID(),i[1],i[0].obtenerH() ),end='' )
    print()
    return ()


#ejecucion de main 
main()


