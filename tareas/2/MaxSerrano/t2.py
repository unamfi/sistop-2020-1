from random import randint
procesos=[]

def Proceso():
    procesos.append(['A',0,randint(1,10)])
    procesos.append(['B',randint(1,10),randint(1,10)])
    procesos.append(['C',randint(1,10),randint(1,10)])
    procesos.append(['D',randint(1,10),randint(1,10)])
    procesos.append(['E',randint(1,10),randint(1,10)])

def impDatosPro():
    global digito
    for digito in procesos:
        datos= digito[0]+" : "+str(digito[1])+", t="+str(digito[2])
        print ("imprime los  datos", datos)

def calProm(tT,tE,p):
    PTTotal=0
    PTEspera=0
    PPena=0
    T=0
    E=0
    P=0

    for i in tT:
        T = T + i

    for i in tE:
        E = E + i

    for i in p:
        P = P + i

    PTTotal = T/5.0
    PTEspera = E/5.0
    PPena = P/5.0
    prom="T="+str(PTTotal)+", E="+str(PTEspera)+", P="+str(PPena)
    print ("imprime promedios", promedios)

def FIFO(procesos):
    ordenProc=[]
    fin=[]
    TTotal=[]
    TEspera=[]
    Penalizacion=[]
    procesoA=0
    Tiempo=procesos[procesoA][2]
    while(procesoA<10):
        if Tiempo > 0:
            ordenProc.append(procesos[procesoA][0])
            Tiempo = Tiempo - 1
        else:
            if procesoA != 5:
                if procesoA == 0:
                    fin.append(procesos[procesoA][2])
                    TTotal.append(procesos[procesoA][2])
                    TEspera.append(0)
                    Penalizacion.append(TTotal[procesoA]/procesos[procesoA][2])
                else:
                    TEspera.append(fin[procesoA-1] - procesos[procesoA][1])
                    TTotal.append(TEspera[procesoA]+procesos[procesoA][2])
                    Penalizacion.append(TTotal[procesoA]/procesos[procesoA][2])
                    fin.append(fin[procesoA-1]+procesos[procesoA][2])
                procesoA = procesoA + 1
                Tiempo = procesos[procesoA][2]
            else:
                procesoA = procesoA + 1
    print ("FIFO")
    calProm(TTotal,TEspera,Penalizacion)
    print ("orden de procesos: ", ordenProc)

def main():
    global procesos
    numRondas = 0
    while(numRondas < 10):
        print ("Ronda " + str(numRondas+1))
        Proceso()
        impDatosPro()
        FIFO(procesos)
        numRondas = numRondas +1
        procesos[:]=[]


main()