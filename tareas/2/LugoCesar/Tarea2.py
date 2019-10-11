import random #Importamos random para porder generar números aleatorios que se ocupan en el programa

def generate_process_list():

    num_of_processes = 5

    arrival = 0

    diccionary = {0:'A',1:'B',2:'C',3:'D',4:'E'} #Diccionario con los procesos que se van a utilizar

    processes = [] #Arreglo vacio para guardar los procesos

    for i in range(num_of_processes): #Hacemos un barrido de nuestros procesos
        duration = random.randint(1,8) #Se establece una duracion aleatoria para cada proceso
        processes.append([diccionary[i],arrival,duration]) #Finalmente de ponen en el arreglo los elementos que constituyen a cada uno de los procesos
        arrival += random.randint(0,duration-1) #Se establece el orden de llegada de cada uno romando en cienta la longitud de la duracion
    return processes #Endalmete retornamos los procesos

def FCFS(process_queue): #Implementación del primer algoritmo que es el FCFS (First Come First Serve)

    l = len(process_queue) #Almacenamos la longitud de nuesto arreglo de procesos

    t = [process_queue[i][2] for i in range(l)] #Es el tiempo total que dura el proceso

    # Cada una de estas variables que nos representan el tiempo de ,respuesta,espera y la proporción de penalización (T,E,P respectivamente)
    #Se toma un rango de 0 hasta el valor máximo l que es la longitud del nuúmero de procesos
    T = [0 for i in range(l)]
    E = [0 for i in range(l)]
    P = [0 for i in range(l)]

    End = [0 for i in range(l)] #Fin del proceso

    output = '' #Cadena vacía para guardar la salida

    for i in range(l):

        if i == 0:
            End[i] = process_queue[i][2]
        else:
            if process_queue[i][1] <= End[i-1]:
                End[i] = process_queue[i][2] + End[i-1]
            else:
                End[i] = process_queue[i][1] + process_queue[i][2]

        T[i] = End[i] - process_queue[i][1]
        E[i] = T[i] - process_queue[i][2]
        P[i] = T[i]/ process_queue[i][2]

    #Apartir de aqui se comienza a calcular los promedios de T,E y P
    auxT = 0

    for i in range(l):
        auxT += T[i]

    averageT = auxT / l

    auxE = 0

    for i in range(l):
        auxE += E[i]

    averageE = auxE / l

    auxP = 0

    for i in range(l):
        auxP += P[i]

    averageP = auxP / l

    print ('FCFS:   T = %.2f' % averageT,'\t', 'E = %.2f' % averageE,'\t', 'P = %.2f' % averageP) #Imprime la tabla con el formato y los valores que regresa son los promedios

    for i in range(l):
        for j in range(t[i]):
            output += process_queue[i][0]

    print(output) #Se imprime la salida de los procesos de acuerdo a como funciona el algoritmo

def RR1(process_queue):

    l = len(process_queue) #Almacenamos la longitud de nuesto arreglo de procesos

    queue_processes = []

    t = [ process_queue[i][2] for i in range(l) ]


    T = [ 0 for i in range(l) ]
    E = [ 0 for i in range(l) ]
    P = [ 0 for i in range(l) ]

    begin = [ process_queue[i][1] for i in range(l) ]

    End = [ 0 for i in range(l) ]


    output = ''

    current_time = 0 #Se utiliza para que los processes entren en el tiempo que les toca.

    while any(time != 0 for time in t):
        for i in range(len(t)):
            if t[i] >= 1 and current_time >= begin[i]:
                queue_processes.append(process_queue[i][0])
                output += process_queue[i][0]
                t[i] -= 1
                current_time += 1

    for i in range(l):
        aux = [ j for j in range(len(queue_processes)) if queue_processes[j] == process_queue[i][0] ]
        End[i] = aux[::-1][0] + 1 #Se voltea la lista y se obtiene el primer elemento que es el mayor, es decir, la ultima vez que aparece
        T[i] = End[i] - process_queue[i][1]
        E[i] = T[i] - process_queue[i][2]
        P[i] = T[i]/ process_queue[i][2]

    auxT = 0

    for i in range(l):
        auxT += T[i]
    averageT = auxT / l

    auxE = 0

    for i in range(l):
        auxE += E[i]
    averageE = auxE / l

    auxP = 0

    for i in range(l):
        auxP += P[i]
    averageP = auxP / l

    print ('RR1:    T = %.2f' % averageT,'\t', 'E = %.2f' % averageE,'\t', 'P = %.2f' % averageP)

    print(output)

def RR4(process_queue):

    l = len(process_queue)#Almacenamos la longitud de nuesto arreglo de procesos

    queue_processes = []

    t = [ process_queue[i][2] for i in range(l) ]

    T = [ 0 for i in range(l) ]
    E = [ 0 for i in range(l) ]
    P = [ 0 for i in range(l) ]

    begin = [ process_queue[i][1] for i in range(l) ]
    End = [ 0 for i in range(l) ]

    output = ''

    current_time = 0 #Definimos el tiempo para que entre en cuanto sea su turno


    while any(time != 0 for time in t):
        for i in range(len(t)):
            if t[i] >= 4 and current_time >= begin[i]:  #Como estamos tranajando elRR4 cada quantum debe der = a 4 por eso manejamos estas condiciones
                for j in range(4):
                    queue_processes.append(process_queue[i][0])
                    output += process_queue[i][0]
                current_time += 4
                t[i] -= 4
            elif t[i] < 4 and t[i] > 0 and current_time >= begin[i]:
                for j in range(t[i]):
                    queue_processes.append(process_queue[i][0])
                    output += process_queue[i][0]
                current_time += t[i]
                t[i] = 0

    for i in range(l):

        aux = [ j for j in range(len(queue_processes)) if queue_processes[j] == process_queue[i][0] ]
        End[i] = aux[::-1][0] + 1 #Se le da vuelta la lista para obtener el primer elemento, que es el mayor
        T[i] = End[i] - process_queue[i][1]
        E[i] = T[i] - process_queue[i][2]
        P[i] = T[i]/ process_queue[i][2]

    auxT = 0

    for i in range(l):
        auxT += T[i]
    averageT = auxT / l

    auxE = 0

    for i in range(l):
        auxE += E[i]
    averageE = auxE / l

    auxP = 0

    for i in range(l):
        auxP += P[i]
    averageP = auxP / l

    print ('RR4:    T = %.2f' % averageT,'\t', 'E = %.2f' % averageE,'\t', 'P = %.2f' % averageP)

    print(output)

#Me falto el algoritmo de SPN no acudi a esa clase y no comprendo muy bien como implementarlo TTmTT


rondas = random.randint(1,20)   #Nos da un numero aleatorio entre 1 y 20 para el numero de rondas de cada proceso

for i in range (rondas):

    process_queue = generate_process_list()

    print ('Ronda:', i+1 )
    string = str(process_queue)
    string2 = string.replace("[" , " ")
    str1 = string2.replace("]" , " ")
    #print ('Proceso:', string.strip('[]'))
    print ('Proceso:', str1)
    FCFS(process_queue)
    RR1(process_queue)
    RR4(process_queue)
