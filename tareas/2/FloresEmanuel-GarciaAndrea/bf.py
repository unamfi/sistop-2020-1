# -*- coding: utf-8 -*-
import sys
import random
import time
import os
from tqdm import tqdm
class Hilo():
        def __init__(self, thread_id, tiempot, prioridad):
            self.thread_id = thread_id   
            self.tiempo_total = tiempot
            #Indica en que momento comenzo su ejecución        
            self.t_0 = 0
            #Indica en que momento termino su ejecución
            self.t_fin = 0
            self.t_espera = 0
            self.t_ejecucion = 0
            self.prioridad = prioridad
            self.barra_p = None
    
class FB():
        def __init__(self):
            self.cola0 = []
            self.cola1 = []
            self.cola2 = []
            self.cola3 = []
            self.listaexec = []
            self.executed = []
            self.t_global = 0
            self.barra_t = 0

        def despachador(self):
        #Elige la cola de mayor prioridad
            cola = self.cola0
            if len(self.cola0) == 0:
                cola = self.cola1
                if len(self.cola1) == 0:
                    cola = self.cola2
                    if len(self.cola2) == 0:
                        cola = self.cola3
                        if len(self.cola3) == 0:
                            cola = -1
            return cola



        def suma_tespera(self,colas):
            #Le suma 1 a la espera de los otros procesos
            for cola in colas:
                for proceso in cola:
                    proceso.t_espera += 1

        def estadisticas(self):
            ejecutados = ""
            sumat_espera = 0
            suma_prom = 0
            suma_ttot = 0
            num_procesos = 0
            for proceso in self.listaexec:
                ejecutados += proceso
            print("El orden de los procesos fue el siguiente: %s" % (ejecutados))
            print('\n{:10} {:<10} {:10} {:10} {:10} {:10}'.format("Proceso", "Inicio", "Fin", "Total" ,"Espera", "Prom"))
            print('_____________________________________________________________')
            for proceso in self.executed:
                num_procesos += 1
                sumat_espera += proceso.t_espera
                suma_ttot += proceso.tiempo_total
                promedio = (proceso.t_fin - proceso.t_0)/proceso.tiempo_total
                suma_prom += promedio            
                print('{:10}|{:<10}|{:<10}|{:<10}|{:<10}|{:<10.4f}'.format(proceso.thread_id, proceso.t_0, proceso.t_fin,proceso.tiempo_total, proceso.t_espera, promedio))
            print('{:40.3f}{:10.3f}{:10.3f}'.format(suma_ttot/num_procesos, sumat_espera/num_procesos, suma_prom/num_procesos))           

        #Añade a la lista de prioridad correspondiente
        def agregaLP(self, proceso):
            p = proceso.prioridad
            if p == 0:
                self.cola0.append(proceso)
            elif p == 1:
                self.cola1.append(proceso)
            elif p == 2:
                self.cola2.append(proceso)
            else:
                self.cola3.append(proceso)

        #Recorre cada cola e imprime los procesos que hay en ella
        def imprime_Prioridad(self,colas):
            num_cola = 0
            for cola in colas:
                for proceso in cola:
                    print("Cola %d" %(num_cola))
                    print("Proceso: %s \t Prioridad: %d \n" % (proceso.thread_id,proceso.prioridad))
                num_cola += 1
                    

        def planifica(self, procesos):       
            #Crea la cantidad de progress bar de procesos que tenemos
            for proceso in procesos:
                proceso.barra_p = tqdm(total = proceso.tiempo_total,leave = False, desc = "Proceso %s" % (proceso.thread_id))
            #--------------------------------------------
            #El despachador elige la cola de mayor prioridad            
            sig_proceso = self.despachador()
            inicia = 0
            #Mientras haya procesos en las colas
            while sig_proceso != -1:
                #Se saca el proceso de la cola de mayor prioridad
                proceso = sig_proceso.pop(0)
                #Se crea una lista con todas las colas
                tmp = [self.cola0, self.cola1, self.cola2, self.cola3] 
                #Duración del quantum  
                #Agrega el proceso a la lista de los que se han ejecutado       
                self.listaexec.append(proceso.thread_id)
                while inicia < 5:
                    time.sleep(0.5)
                    #Si el proceso aún tiene ejecuciones pendientes
                    if proceso.t_ejecucion < proceso.tiempo_total:
                        if proceso.t_ejecucion == 0:
                            proceso.t_0 = self.t_global
                        os.system('clear')
                        self.imprime_Prioridad(tmp)
                        #Actualiza el progress bar del proceso en ejecución
                        proceso.barra_p.update(1)
                        proceso.t_ejecucion += 1
                    else: 
                        if proceso.t_fin == 0:
                            proceso.t_fin = self.t_global
                        pass
                                
                    self.suma_tespera(tmp)
                    inicia +=1
                    self.t_global += 1
                inicia = 0
                #Si el proceso no ha terminado de ejecutarse se disminuye o "aumenta" su prioridad
                if proceso.t_ejecucion != proceso.tiempo_total:
                    if proceso.prioridad < 3:
                        proceso.prioridad += 1
                    self.agregaLP(proceso)
                else:
                    if proceso.t_fin == 0:
                        proceso.t_fin = self.t_global
                    #Se agrega a la lista de procesos que terminaron su ejecución
                    self.executed.append(proceso)
                sig_proceso = self.despachador()
            os.system('clear')
            self.estadisticas()

if __name__ == '__main__':
    #Para asociar el numero de proceso a una letra
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    
    l_process =[]
    fb = FB()
    #Recupera el valor de numero de procesos de los argumentos
    num_procesos = int(sys.argv[1])
    #Genera la cantidad de hilos que le indicamos
    for i in range(num_procesos):        
        t_process = random.randrange(1,15)   
        prioridad = random.randrange(0,4)
        #Proceso con un tiempo y prioridad aleatorio     
        proceso = Hilo(letras[i], t_process, prioridad)
        l_process.append(proceso)
        fb.agregaLP(proceso)

    fb.planifica(l_process)
