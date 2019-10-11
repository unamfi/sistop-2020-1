from Proceso import Proceso, crea_procesos, medias_procesos, llega_proceso

"""
Algoritmo de Planificacion Ronda(Round Robin)
 
"""


def RoundRobin(lista_procesos, cuantum):
  print(f"RoundRobin{cuantum}: ")
 
  t_sistema = 0
  # El numero de procesos que deben ser atendidos
  num_procesos = len(lista_procesos)
  #El proceso actual en ejecucion
  proceso_actual = None
  cola_procesos = []
  # El numero de ticks a los cuales se le cede al ejecucion a otro proceso
  max_quantum = cuantum
  quantum = 0
  while(num_procesos != 0):
   cola_llegada = llega_proceso(lista_procesos, t_sistema)
   #Si la cola de llegadas no esta vacia:
   if(len(cola_llegada) != 0):
     #El primer proceso que llega sera agregado a la cola de #ejecucion y ejecutado inmediatamente
     if(len(cola_procesos)==0):
       p = cola_llegada.pop(0)
       cola_procesos.append(p)
       proceso_actual = cola_procesos[0]
       proceso_actual.ejecucion = True
       quantum = 0
       for p in cola_llegada:
          cola_procesos.append(p)
     else:
       for p in cola_llegada:
          cola_procesos.append(p)
   if(len(cola_procesos) != 0 ):
    #En caso de que llegue un neuvo proceso este estara al principio de la cola de espera
    #Si el cuantum ya es maximo se le sede la ejecucion a este
     if(quantum == max_quantum):
       proceso_actual.ejecucion = False
       quantum = 0
       if(proceso_actual.terminado == False):
         cola_procesos.append(proceso_actual)
         cola_procesos.pop(0)
       if(len(cola_procesos) != 0):
         proceso_actual = cola_procesos[0]
         proceso_actual.ejecucion = True    
      # Se ponen a trabajar a todos los procesos, en caso de no tener la ejecucion, estos descansan
     for proceso in cola_procesos:
       proceso.trabaja()
      # Se aumenta el cuantum despues de cada trabajo
     quantum += 1
      # Si el proceso en ejecucion ya acabo se le cede la ejecucion al siguente proceso en la cola
      # y se pone quantum a 0
     if(proceso_actual.terminado == True):
       cola_procesos.pop(0)
       num_procesos -= 1
       quantum = 0
       if(len(cola_procesos) != 0):
         proceso_actual = cola_procesos[0]
         proceso_actual.ejecucion = True

    # Sigue pasando el tiempo en el sistema
   t_sistema += 1
  medias = medias_procesos(lista_procesos)
  print("")
  print(medias)
  
