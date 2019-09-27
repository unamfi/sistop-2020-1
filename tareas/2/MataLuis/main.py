from fifo import ff
from rond import rr
from alea import aleatorios
import time

tiempos = [['A', 'B', 'C', 'D', 'E'],[0,0,0,0,0],[0,0,0,0,0]]
resultados = [['A', 'B', 'C', 'D', 'E'],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

tiempos = aleatorios(tiempos)
for i in range(5):
        print("Proceso: %s llega en %d y se ejecutara por %d"%(tiempos[0][i],tiempos[1][i],tiempos[2][i]))


ff(tiempos, resultados)
rr(tiempos, resultados, 1)
rr(tiempos, resultados, 4)

