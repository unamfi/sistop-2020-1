from __future__ import print_function
import random
import sys

#Menu incial
def main(): 
	print('ASIGNACION DE MEMORIA !!')
	print('***En caso de salir agrege -1 en unidades de memoria ***')
	print('(No se permiten mas de 1000 unidades de memoria)')
	noUnidades = int(input('Ingrese numero de unidades de memoria : '))
	if(noUnidades == -1 || noUnidades > 1000): 
		return 	
	mapeo(noUnidades)


#Genera aleatoriamente el mapeo de memoria, con los procesos y sus unidades de procesos tambien generadas de forma aleatoria 
def mapeo(unidadesMemoria):
	alpha = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
	mapeo = []
	procesos = []
	while(len(mapeo)<= unidadesMemoria):
		temp = alpha[random.randrange(24)]
		try:
			mapeo.index(temp)
		except:
			if(len(mapeo)<= unidadesMemoria):
				procesos.append(temp)
			uniProceso = random.randrange(15)
			for n in range(uniProceso):
				mapeo.append(temp)
				if(len(mapeo)>= unidadesMemoria):
					break
			if(random.randint(0,1) == 1):
				empty = random.randint(0,4)
				for n in range(empty):
					mapeo.append('-')
					if(len(mapeo)>= unidadesMemoria):
						break
	asignacionActual(mapeo, procesos)


#Muestra lo que hay que hacer si liberar procesos o agregar uno nuevo
def asignacionActual(mapeo, procesos):
	print('Asiganacion Actual:')
	print(' ')
	for n in range(len(mapeo)):
		print(mapeo[n],end="")
	print('\n')
	opc = int(input('Asignar (0) o liberar (1) : '))
	if opc == 0:
		nProceso = nuevoProceso(mapeo)
		tamProceso = int(input("Nuevo proceso (%s): " %(nProceso)))
		nuevaAsignacion(mapeo, procesos, nProceso, tamProceso)
		try: 
			mapeo.index(nProceso)
			print("Nueva Asigancion: ")
			for n in range(len(mapeo)):
				print(mapeo[n],end="")
			print('\n')
		except:
			print("**Compactacion requerida**")
			print("Nueva situacion: ")
			compactacion(mapeo)
			for n in range(len(mapeo)):
				print(mapeo[n],end="")
			print('\n')
			nuevaAsignacion(mapeo, procesos, nProceso, tamProceso)
			try:
				mapeo.index(nProceso)
				print("Asignando a %c:" %(nProceso))
				for n in range(len(mapeo)):
					print(mapeo[n],end="")
				print('\n')
				asignacionActual(mapeo, procesos)
			except:
				print("**El proceso no puede ser ingresado**")
	elif opc == 1:
		procesoLib = raw_input("Proceso a liberar (%s) :" %(','.join(procesos)))
		liberar(mapeo, procesos, procesoLib)
		asignacionActual(mapeo, procesos)
	else:
		print('---Ingresa un numero valido----')
		asignacionActual(mapeo, procesos)


#Genera un nuevo proceso aleaotrio sin repetir 
def nuevoProceso(procesos):
	alpha = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
	temp = alpha[random.randrange(24)]
	try:
		procesos.index(temp)
		return nuevoProceso(procesos)
	except:
		return temp

#La nueva asignacion primer ajuste
def nuevaAsignacion(mapeo, procesos, nProceso, tamProceso):
	cont = 0 
	procesos.append(nProceso)
	for n,i in enumerate(mapeo):
 		if i=='-':
 			if cont == 0: 
 				inicio = n 
			cont += 1
		else:
			cont = 0  
		if cont == tamProceso:
			for i in range(inicio , inicio+tamProceso):
				mapeo[i] = nProceso
			break

#Funcion que fompata los proeceso dejando la parte vacia hasta el final 
def compactacion(mapeo):
	ban = True
	cont = 0
	while(ban):
		try:
			mapeo.remove('-')
			cont += 1
		except:
			ban = False
	for i in range(0, cont):
		mapeo.append('-') 


#Libera el mapeo del elemento y lo elimina de la lista de procesos
def liberar(mapeo, procesos, procesoLib):
	 for n,i in enumerate(mapeo):
 		 if i==procesoLib:
			mapeo[n]= '-'
	 procesos.remove(procesoLib)

main()