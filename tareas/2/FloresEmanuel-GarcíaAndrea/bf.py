import sys
import random
import time
import os
from tqdm import tqdm
class Hilo():
        def __init__(self, thread_id, tiempot):
            self.thread_id = thread_id   
            self.tiempo_total = tiempot
            #Indica en que momento comenzó su ejecución        
            self.t_0 = 0
            #Indica en que momento terminó su ejecución
            self.t_fin = 0
            self.t_espera = 0
            self.t_ejecucion = 0
            self.prioridad = 0
            #self.barra_p = 0
    
class FB():
        def __init__(self, procesos, t):
            self.cola0 = procesos
            self.cola1 = []
            self.cola2 = []
            self.cola3 = []
            self.listaexec = []
            self.executed = []
            self.t_global = 0
            #Si se ocupa el progress bar
            self.t_total = t
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
            print("El tiempo total que tardaron en ejecutarse fue %d", (self.t_global))
            for proceso in self.listaexec:
                ejecutados += proceso
            print("El orden de los procesos fue el siguiente: %s" % (ejecutados))
            print("Tiempo total %d", self.t_global)
            for proceso in self.executed:
                print("Proceso "+ proceso.thread_id + "\n" + "Tiempo total " + str(proceso.tiempo_total) + "\n" + "Tiempo espera "
                + str(proceso.t_espera) + "\n" + "Tiempo de inicio " + str(proceso.t_0) + "\n" + "Tiempo fin " + str(proceso.t_fin) + "\n")

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


        def imprime_Prioridad(self,colas):
            num_cola = 0
            for cola in colas:
                
                for proceso in cola:
                    print("Cola %d" %(num_cola))
                    print("Proceso: %s \t Prioridad: %d \n" % (proceso.thread_id,proceso.prioridad))
                num_cola += 1
                    

        def planifica(self):       
            for proceso in self.cola0:
                proceso.barra_p = tqdm(total = proceso.tiempo_total,leave = False, desc = "Proceso %s" % (proceso.thread_id))
            #--------------------------------------------            
            sig_proceso = self.despachador()
            inicia = 0
            while sig_proceso != -1:
                proceso = sig_proceso.pop(0)
                #Se crea una lista con todas las colas
                tmp = [self.cola0, self.cola1, self.cola2, self.cola3] 
                #Duración del quantum  
                #self.imprime_Prioridad(tmp)             
                self.listaexec.append(proceso.thread_id)
                while inicia < 5:
                    time.sleep(0.5)
                    #Proceso sacado de la lista en ejecución
                    if proceso.t_ejecucion < proceso.tiempo_total:
                        if proceso.t_ejecucion == 0:
                            proceso.t_0 = self.t_global
                        
                        os.system('clear')
                        self.imprime_Prioridad(tmp)
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
                    self.executed.append(proceso)
                sig_proceso = self.despachador()
            os.system('clear')
            self.estadisticas()

if __name__ == '__main__':
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    
    l_process =[]
    #Para saber cuanto debe tardar la ejecución
    t_total = 0
    #Recupera el valor de los argumentos
    num_procesos = int(sys.argv[1])
    for i in range(num_procesos):
        t_process = random.randrange(1,15)   
        prioridad = random.randrange(0,3)     
        proceso = Hilo(letras[i], t_process)
        l_process.append(proceso)
        t_total += t_process

    fb = FB(l_process, t_total)
    fb.planifica()
