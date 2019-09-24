#%%
import numpy as np
import string

#%%
nombre_procesos = np.array(list(string.ascii_uppercase))
#%%
tiempo_llegada = np.sort(np.random.randint(low='0', high='50', size=26))
#%%
tiempo_requerido = np.random.randint(low='0', high='8', size=26)
#%%
lista_procesos = np.array([nombre_procesos, tiempo_llegada, tiempo_requerido]).transpose()