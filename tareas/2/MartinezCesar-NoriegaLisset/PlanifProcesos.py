from Proceso import Proceso, crea_procesos, medias_procesos
from RoundRobin import RoundRobin
from FCFS import FCFS	
from SPN import SPN

"""
Programa principal de los algoritmos de planificacion de procesos

"""


def prueba():
  lista = []
  p1 = Proceso(0,3,"A")
  p2 = Proceso(1,5,"B")
  p3 = Proceso(3,2,"C")
  p4 = Proceso(9,5,"D")
  p5 = Proceso(12,5,"E")
  lista.append(p1)
  lista.append(p2)
  lista.append(p3)
  lista.append(p4)
  lista.append(p5)
  return lista

def revive_procesos(lista_procesos):
	for proceso in lista_procesos:
		proceso.reset()


lista_cuantums = []
while(True):
	cuantum = int(input("Introduzca un cuantum para RoundRobin, introduzca 0 para detenerse: "))
	if(cuantum == 0):
		break
	lista_cuantums.append(cuantum)

rondas = int(input("Numero de rondas: "))
for i in range(1,rondas+1):
	lista = crea_procesos(3)
	print(f"-----------------------RONDA:{i}----------------------")
	for proceso in lista:
		proceso.imprime_proceso()
	print(" ")

	FCFS(lista)
	revive_procesos(lista)

	for j in range(0,len(lista_cuantums)):
		RoundRobin(lista,lista_cuantums[j])
		revive_procesos(lista)
	SPN(lista)



