from math import floor

class Memoria:
    CHAR_ULIBRE = '-' # Identificador de unidad libre
    def __init__(self, unidades):
        self.unidades = unidades
        self.__u_libres = unidades
        self.memoria = ['-' for i in range(unidades)]
        self.__mapmem = []
        self.u_min = 1 # Unidades mínimas asignables
        self.u_max = floor(unidades/2) # Unidades máximas asignables

    @property
    def procesosEnMemoria(self):
        pem = [] # Procesos en memoria
        for emm in self.__mapmem:
            pem.append(emm.nombre)
        return pem
    
    def liberar(self, proceso):
        if self.__mapmem:
            resultado = list(filter( lambda emm: emm.nombre == proceso, self.__mapmem)) # Buscamos si hay algún proceso con el mismo nombre
            if not resultado:
                print('No existe el proceso en memoria')
                return False
            eem_del = resultado.pop()
            self.__mapmem.remove(eem_del)
            self.memoria[eem_del.direccion : eem_del.direccion + eem_del.u_ocupadas] = [self.CHAR_ULIBRE for _ in range(eem_del.u_ocupadas)]
            self.__u_libres += eem_del.u_ocupadas
            print('Proceso %s liberado' % proceso)
            return True

    def compactar(self):
        procesos_mov = 0 # Contador para indicar los procesos que fueron movidos durante la compactación
        if self.__mapmem:
            direccion = 0 # 
            u_libres = self.__u_libres # Suponemos que tenemos todo el espacio
            clusters_usados = 0 # Al inicio suponemos que no hay archivos ocupando el cluster

            self.__mapmem = sorted(self.__mapmem, key=lambda ed: ed.direccion) # Ordenamos la lista de entradas con base en el cluster donde inician

            for i, emm in enumerate(self.__mapmem): # emm : entrada de mapa de memoria
                u_libres = emm.direccion - direccion # Vemos cuantas unidades tenemos disponibles entre procesos

                if u_libres > 0: # Si hay espacio entre procesos...

                    dir_in_antigua = emm.direccion
                    dir_fin_antigua = dir_in_antigua + emm.u_ocupadas # Dirección de fin                    
                    proceso_por_mover = self.memoria[dir_in_antigua : dir_fin_antigua] # Guardar los datos del archivo
                    self.memoria[dir_in_antigua : dir_fin_antigua] = [self.CHAR_ULIBRE for _ in range(emm.u_ocupadas)]
                    
                    dir_fin_nueva = direccion + emm.u_ocupadas # Dirección nueva de fin

                    emm.direccion = direccion # Le actualizamos su dirección de inicio
                    self.memoria[direccion : dir_fin_nueva] = proceso_por_mover # Movemos el proceso
                    procesos_mov += 1

                direccion = emm.direccion+emm.u_ocupadas # y actualizamos la dirección de inicio
        print('Compactación terminada, %i procesos movidos.' % procesos_mov)
        return procesos_mov>0

    def asignar(self, proceso, unidades_req=2, tipo_ajuste=0):
        """Asigna una cantidad de unidades de memoria a un proceso
        Parámetros:
            proceso - nombre del proceso
            unidades_req - el número de unidades que pide el proceso
            tipo_ajuste - 0: Primer ajuste. 1: Mejor ajuste, 2: Peor ajuste
        """
        # self.imprime_mem()
        if unidades_req > self.__u_libres:
            print('No se pueden asignar %i unidades, memoria sin espacio disponible' % unidades_req)
            return
        if unidades_req < self.u_min or unidades_req > self.u_max:
            print('No se puede asignar menos de %i unidad ni más de %i unidades' % (self.u_min, self.u_max))
            return
        
        # Vemos si hy espacio en memoria entre procesos
        direccion = 0 # Iniciamos en la primer dirección de memoria
        u_libres = self.__u_libres # Suponemos que tenemos todo el espacio

        if self.__mapmem:
            resultado = list(filter( lambda emm: emm.nombre == proceso, self.__mapmem)) # Buscamos si hay algún proceso con el mismo nombre
            if resultado:
                print('Ya existe el proceso en memoria')
                return False

            self.__mapmem = sorted(self.__mapmem, key=lambda ed: ed.direccion) # Ordenamos la lista de entradas con base en la dirección del proceso
            for emm in self.__mapmem: # eem : Entrada del mapa de memoria
                u_libres = emm.direccion - direccion # Vemos cuanto espacio tenemos disponible
                if u_libres > unidades_req: # Si hay espacio...
                    break # Rompemos el ciclo                    
                direccion = emm.direccion+emm.u_ocupadas # Dirección del proceso = direccón del proceso que está en lista más su tamaño
        
        urestantes_fin = self.unidades - direccion - 1 # unidades restantes al final de la memoria
        
        if urestantes_fin < unidades_req: # Si no queda espacio...
            print('No hay espacio contiguo suficiente. La unidad necesita compactarse') # Significa que la unidad requiere compactarse
            self.compactar()
            direccion = self.unidades - self.__u_libres 
            print('Nueva situación: \n\t', end='')
            self.imprime_mem()

        print('Asignando %s en direccion %i' % (proceso, direccion))
        emm_nueva = EntrMapMem(direccion, nombre=proceso, u_ocupadas=unidades_req)
        self.__mapmem.append(emm_nueva)
        self.memoria[direccion:direccion+unidades_req] = [proceso for _ in range(unidades_req)]
        self.__u_libres -= unidades_req
        return True
    
    def imprime_mem(self):
        print(''.join(self.memoria))

class EntrMapMem: # Entrada del mapa de memoria
    def __init__(self, direccion, nombre, u_ocupadas):
        self.direccion = direccion
        self.nombre = nombre
        self.u_ocupadas = u_ocupadas