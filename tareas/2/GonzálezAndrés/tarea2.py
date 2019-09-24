#%%
import numpy as np
import string
from algoritmos_planeacion import fcfs, Proceso

#%%
nombre_procesos = np.array(list(string.ascii_uppercase))
tiempos_llegadas = np.sort(np.random.randint(low='0', high='50', size=26))
tiempos_requeridos = np.random.randint(low='1', high='8', size=26)

lista_procesos = []

num_procesos = 7

for i in range(num_procesos):
    nombre = nombre_procesos[i]
    tiempo_llegada = tiempos_llegadas[i]
    tiempo_requerido = tiempos_requeridos[i]
    lista_procesos.append(Proceso(nombre, tiempo_llegada, tiempo_requerido))
    print("%s: t_llegada=%d, t_requerido=%d." % (nombre, tiempo_llegada, tiempo_requerido))
#%%
[cola_ejecucion, procesos_ejecutados] = fcfs(lista_procesos)
print('FCFS: ', ''.join(cola_ejecucion))

#%%
