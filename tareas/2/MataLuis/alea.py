import random 

def aleatorios(tiempos):
    ##Generacion de numeros aleatorios para llegadas
    for i in range(5): 
        num = round(random.uniform(1,10),2)
        tiempos[1][i] = num
    ##Generacion de numeros aleatorios para tiempo de ejecucion 
    for i in range(5): 
        num = round(random.uniform(1,10),2)
        tiempos[2][i] = num
    return tiempos
