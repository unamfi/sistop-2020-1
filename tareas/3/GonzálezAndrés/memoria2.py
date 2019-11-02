class Memoria:
    CHAR_ULIBRE = '-' # Identificador de unidad libre
    def __init__(self, unidades):
        self.unidades = unidades
        self.__u_libres = unidades
        self.memoria = ['-' for i in range(unidades)]
        self.__mapmem = []
    
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
        pass

    def asignar(self, proceso, unidades_req=2, tipo_ajuste=0):
        """Asigna una cantidad de unidades de memoria a un proceso
        Parámetros:
            proceso - nombre del proceso
            unidades_req - el número de unidades que pide el proceso
            tipo_ajuste - 0: Primer ajuste. 1: Mejor ajuste, 2: Peor ajuste
        """
        if unidades_req > self.__u_libres:
            print('No se pueden asignar %i unidades, memoria sin espacio disponible' % unidades_req)
            return
        if unidades_req < 1 or unidades_req > 15:
            print('No se pueden asignar menos de 1 unidad ni más de 15 unidades')
            return
        # if not self.__mapmem:
        #     emm = EntrMapMem(0, proceso, unidades_req)
        #     self.__mapmem.append(emm)
        #     return
        
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
        
        urestantes_fin = self.unidades - direccion - 1# unidades restantes al final de la memoria
        if urestantes_fin < unidades_req: # Si no queda espacio...
            print('No hay espacio contiguo suficiente. La unidad necesita compactarse') # Significa que la unidad requiere compactarse
            return False

        print('Asignando "%s" en direccion %i' % (proceso, direccion))
        emm_nueva = EntrMapMem(direccion, nombre=proceso, u_ocupadas=unidades_req)
        self.__mapmem.append(emm_nueva)
        self.memoria[direccion:direccion+unidades_req] = [proceso for _ in range(unidades_req)]
        self.__u_libres -= unidades_req
        return True

class EntrMapMem: # Entrada del mapa de memoria
    def __init__(self, direccion, nombre, u_ocupadas):
        self.direccion = direccion
        self.nombre = nombre
        self.u_ocupadas = u_ocupadas

mem = Memoria(30)
print(mem.memoria)
mem.asignar('A')
mem.asignar('A')
mem.asignar('B', 0)
mem.asignar('B', 16)
mem.asignar('B', 5)
mem.asignar('C', 15)
mem.asignar('D', 10)
mem.liberar('B')
mem.asignar('D', 10)
print(mem.memoria)