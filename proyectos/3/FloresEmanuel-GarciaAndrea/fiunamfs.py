import mmap
import os, os.path
import time

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
        self.nombre_archivo = entrada[0:15].decode('ascii').strip()
        self.archivo_size = entrada[16:24].decode('ascii')
        self.cluster_inicial = entrada[25:30].decode('ascii')
        self.creacion_archivo = entrada[31:45].decode('ascii')
        self.modificacion_archivo = entrada[40:60].decode('ascii')
        self.num_entrada = -1

class FSUnamFI:
    # Elementos que se estarán utilizando en la mayoría de las funciones
    f = open('fiunamfs.img','a+b')
    fs_mmap = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    sb = Superbloque()
    entrada_size = 64

    def obtenerEntradas(self):
        entradas = []
        # Se recorrera el directorio de entradas, cada entrada mide 64 bytes
        # El tamaño del directorio es: 2048 * 4 = 8192
        # La cantidad de entradas serán 8192/64 = 128
        for num_entrada in range(128):
            p_entrada = self.sb.cluster_size + num_entrada * ENT_DIR.entrada_size
            entrada = ENT_DIR(self.fs_mmap[p_entrada:p_entrada + ENT_DIR.entrada_size])

            if entrada.nombre_archivo != ENT_DIR.entrada_sin_usar:
                entrada.num_entrada = num_entrada
                entradas.append(entrada)

        return entradas

    def listar(self):
        entradas = self.obtenerEntradas()
        
        print('{:15} {:10} {:15} {:15}'.format("Nombre", "Tamaño", "Creacion", "Modificación"))
        for entrada in entradas:
            print('{:15} {:10} {:15} {:15}'.format(entrada.nombre_archivo, entrada.archivo_size, entrada.creacion_archivo, entrada.modificacion_archivo))

    #def copiar_a_pc():

    #def copiar_a_fs():

    #def eliminar_archivo():

    #def desfragmentar():


fs = FSUnamFI()
fs.listar()

        

