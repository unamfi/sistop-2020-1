#-*- encoding: utf-8
import mmap
import os, os.path
import time, math
import sys

class Superbloque:
    # Se leen los datos del superbloque
    def __init__(self):
        with open('fiunamfs.img', 'r+b') as f:
            fs_mmap = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

            self.fs_nombre         = fs_mmap[0:8].decode('ascii')           # FiUnamFS
            self.version           = fs_mmap[10:13].decode('ascii')         # 0.7
            self.volumen_tag       = fs_mmap[20:35].decode('ascii')         # Mi Sistema
            self.cluster_size      = int(fs_mmap[40:45].decode('ascii'))    # 2048
            self.num_cluster_dir   = int(fs_mmap[47:49].decode('ascii'))    # 4
            self.num_cluster_total = int(fs_mmap[52:60].decode('ascii'))    # 720

            fs_mmap.close()

            # Validamos que sea el sistema de archivos correcto
        if self.fs_nombre != 'FiUnamFS':
            print('[-] Error: Sistema de Archivos Incorreto')
            exit(-1)

# Clase para las ENTradas del DIRectorio
class ENT_DIR:
    entrada_sin_usar = 'Xx.xXx.xXx.xXx.'
    entrada_size = 64

    def __init__(self, entrada):
        self.nombre_archivo       = entrada[0:15].decode('ascii').strip()
        self.archivo_size         = entrada[16:24].decode('ascii')
        self.cluster_inicial      = entrada[25:30].decode('ascii')
        self.creacion_archivo     = entrada[31:45].decode('ascii')
        self.modificacion_archivo = entrada[46:60].decode('ascii')
        self.num_entrada = -1

class FSUnamFI:
    # Elementos que se estar��n utilizando en la mayor��a de las funciones
    f = open('fiunamfs.img','a+b')
    fs_mmap = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    sb = Superbloque()
    entrada_size = 64

    def obtener_entradas(self):
        entradas = []
        # Se recorrera el directorio de entradas, cada entrada mide 64 bytes
        # El tama�0�9o del directorio es: 2048 * 4 = 8192
        # La cantidad de entradas ser��n 8192/64 = 128
        for num_entrada in range(128):
            p_entrada = self.sb.cluster_size + num_entrada * ENT_DIR.entrada_size
            entrada = ENT_DIR(self.fs_mmap[p_entrada:p_entrada + ENT_DIR.entrada_size])

            if entrada.nombre_archivo != ENT_DIR.entrada_sin_usar:
                entrada.num_entrada = num_entrada
                entradas.append(entrada)

        return entradas

    def listar(self):
        entradas = self.obtener_entradas()
        
        print('{:15} {:10} {:20} {:20} {:10}'.format("Nombre", "Tamaño", "Creación", "Modificación", "Clúster"))
        for entrada in entradas:
            print('{:15} {:10} {:20} {:20} {:10}'.format(entrada.nombre_archivo, entrada.archivo_size, self.convertir_fecha(entrada.creacion_archivo), self.convertir_fecha(entrada.modificacion_archivo), entrada.cluster_inicial))

    # Para imprimir la fecha de una manera m��s adecuada al usuario
    def convertir_fecha(self, fecha):
        anio = fecha[:4]
        mes = fecha[4:6]
        dia = fecha[6:8]
        hora = fecha[8:10]
        min = fecha[10:12]
        seg = fecha[12:14]
        return dia + '/' + mes + '/' + anio + ' ' + hora + ':' + min + ':' + seg

    # La funci��n buscar ser�� fundamental, ya que sabremos si existe una entrada y su ubicaci��n
    def buscar_entrada(self, nombre_buscar):
        for num_entrada in range(128):
            p_entrada = self.sb.cluster_size + num_entrada * ENT_DIR.entrada_size
            entrada = ENT_DIR(self.fs_mmap[p_entrada:p_entrada + ENT_DIR.entrada_size])

            if nombre_buscar == entrada.nombre_archivo:
                entrada.num_entrada = num_entrada
                return entrada
        return None

    def copiar_a_pc(self, archivo, ruta):
        entrada = self.buscar_entrada(archivo)
        if entrada != None and os.path.exists(ruta):
            cluster = int(entrada.cluster_inicial) * self.sb.cluster_size
            with open(ruta + '/' + archivo, 'w+b') as nuevo_archivo:
                nuevo_archivo.write(self.fs_mmap[cluster: cluster+int(entrada.archivo_size)])
                print('[+] El archivo se copió correctamente')
        else:
            print('[-] Archivo o ruta no encontrado')

    def copiar_a_fs(self, archivo):
        if os.path.isfile(archivo):
            if self.buscar_entrada(archivo) != None:
                print('[-] El archivo ya existe, cambie el nombre o borre el archivo')
            else:
                self.crear_entrada(archivo)
        else:
            print('[-] No se ha encontrado el archivo')


    # Cuando se copia una archivo externo debemos generar los metadatos
    def crear_entrada(self, archivo):
        nombre = archivo[:]
        with open(archivo) as f:
            f_mmap = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY)
            size = len(f_mmap)
            contenido = f_mmap.read()
        
        fecha_creacion = time.strftime("%Y%m%d%H%M%S")
        fecha_modificacion = time.strftime("%Y%m%d%H%M%S")

        entradas = self.obtener_entradas()

        if entradas:
            p_entrada_nueva = self.sb.cluster_size + (entradas[-1].num_entrada + 1) * 64
        else:
            p_entrada_nueva = self.sb.cluster_size 

        cluster_inicial = self.calcular_cluster(entradas)
        entrada_nueva = ' '.encode('ascii') * (15 - len(nombre)) 
        entrada_nueva += nombre.encode('ascii')
        entrada_nueva += bytes(1) + ('0' * (8-len(str(size))) + str(size)).encode('ascii')
        entrada_nueva += bytes(1) + ('0' * (5-len(str(cluster_inicial))) + str(cluster_inicial)).encode('ascii')
        entrada_nueva += bytes(1) + fecha_creacion.encode('ascii') 
        entrada_nueva += bytes(1) + fecha_modificacion.encode('ascii')
        entrada_nueva += bytes(4)

        self.fs_mmap[p_entrada_nueva:p_entrada_nueva + ENT_DIR.entrada_size] = entrada_nueva
        
        if(self.cargar_contenido(contenido, cluster_inicial)):
            print('[+] Se ha guardado el archivo correctamente')
        else:
            print('[-] Error al agregar contenido, espacio no suficiente')
            self.eliminar_archivo(archivo)

    def cargar_contenido(self, contenido, cluster_inicial):
        clusters = math.ceil(len(contenido)/self.sb.cluster_size)
        if (cluster_inicial + clusters) < self.sb.num_cluster_total:
            clusters *= self.sb.cluster_size
            cluster_inicial *= self.sb.cluster_size
            self.fs_mmap[cluster_inicial:cluster_inicial + clusters] = contenido + ('0' * (clusters - len(contenido))).encode('ascii')
            return True
        else:
            return False

    def calcular_cluster(self, entradas):
        if entradas:
            cluster_inicial = int(entradas[-1].cluster_inicial)
            archivo_size = int(entradas[-1].archivo_size)
        else:
            cluster_inicial = 5
            archivo_size = 0
        return math.ceil((cluster_inicial * self.sb.cluster_size + archivo_size) / self.sb.cluster_size)

    def eliminar_archivo(self, archivo):
        entrada = self.buscar_entrada(archivo)

        if entrada != None:
            p_entrada = self.sb.cluster_size + ENT_DIR.entrada_size * entrada.num_entrada
            self.fs_mmap[p_entrada:p_entrada+15] = bytes(ENT_DIR.entrada_sin_usar.encode('ascii'))
            print('[+] El archivo se ha eliminado correctamente')
        else:
            print('[-] El archivo no existe, vuelva a intentarlo')

    def desfragmentar(self):
        
        entradas = self.obtener_entradas()
        tam_cluster = self.sb.cluster_size
        clusters = {}
        #El primer clúster a partir del cual podemos definir información ya que del 0 - 4 tenemos el superbloque y el directorio 
        clus_init = 5
        #Se genera un diccionario de la forma clusters{ cluster_inicial : [nom_arch , tam_arch]}
        for entrada in entradas:    
            tmp = [int(entrada.archivo_size.strip('0')), entrada.num_entrada]
            clusters[int(entrada.cluster_inicial.strip('0'))] = tmp
        print(clusters)
        #Por cada entrada del diccionario se verifica si se puede mover un elemento
        for cluster in range(len(clusters)):
            clus_min = min(clusters)
            if(clus_min > clus_init):
                 inicio = tam_cluster * clus_min
                 #N��mero de clusters que ocupa el archivo
                 fin = math.ceil(clusters.get(clus_min)[0]/tam_cluster)
                 #Recupera el archivo
                 archivo = self.fs_mmap[inicio : inicio + (fin*tam_cluster)]
                 #Lo cambia de lugar
                 self.fs_mmap[clus_init * tam_cluster : (clus_init * tam_cluster) + (fin * tam_cluster)] = archivo
            #Se actualiza el diccionario
            tmp = clusters.get(clus_min)
            del clusters [clus_min]
            #Se deben actualizar los metadatos
            i_metadatos = 2048 + (tmp[1] * 64)
            self.fs_mmap[i_metadatos + 25 : i_metadatos + 30] = str(clus_init).zfill(5).encode('ascii')
            #Se actualiza el valor del cluster inicial
            num_clusters_arch = math.ceil(tmp[0] / tam_cluster)
            clus_init += num_clusters_arch
           
def main():
    fs = FSUnamFI()
    ins_no_param = {'ls' : fs.listar, 'dfg' : fs.desfragmentar}
    ins_param = {'cp_out' : fs.copiar_a_pc, 'cp_in' : fs.copiar_a_fs, 'rm' : fs.eliminar_archivo}    
    num_oper = len(sys.argv)
 
    if(num_oper == 2):
          instruccion = sys.argv[1]
          if instruccion in ins_no_param:
                ins_no_param[instruccion]()
          else:
                print ("Instruccion no válida, intentalo de nuevo :(")   
    elif(num_oper == 3):
          instruccion = sys.argv[1]
          if instruccion in ins_param:
                if((instruccion == "rm" or instruccion == "cp_in") and len(sys.argv) == 3):
                    ins_param[instruccion](sys.argv[2])
                else:
                    print("Los parámetros no coinciden :(")
          else: 
                print ("Instruccion no válida, intentalo de nuevo :(")   
    elif(num_oper == 4):
          instruccion = sys.argv[1]
          if instruccion in ins_param and instruccion == "cp_out":
                fs.copiar_a_pc(sys.argv[2], sys.argv[3])
          else:
                print ("Instrucción no válida, intentalo de nuevo :(")
             
    else:
          print("Faltan o sobran argumentos D: Consulta la documentación para introducir los datos correctamente (:")


if __name__ == '__main__':
    main()
