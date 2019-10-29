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
    entrada_libre = 'Xx.xXx.xXx.xXx.'

    def __init__(self, entrada):
        self.nombre_archivo = entrada[0:15].decode('ascii').strip()
        self.tam_archivo = entrada[16:24].decode('ascii')
        self.cluster_inicial = entrada[25:30].decode('ascii')
        self.creacion_archivo = entrada[31:45].decode('ascii')
        self.modificacion_archivo = entrada[40:60].decode('ascii')
        self.num_entrada = -1

class FSUnamFI:
    # Elementos que se estarán utilizando en la mayoría de las funciones
    f = open('fiunamfs.img','a+b')
    fs_mmap = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    superbloque = Superbloque()
    tam_entrada = 64

    def obtenerEntradas(self):
        entradas = []
        # Se recorrera el directorio de entradas, cada entrada mide 64 bytes
        # El tamaño del directorio es: 2048 * 4 = 8192
        for p_entrada in range(0, 8192, 64):
            entrada = ENT_DIR(self.fs_mmap[p_entrada:p_entrada + self.tam_entrada])

            if entrada.nombre_archivo != ENT_DIR.entrada_libre:
                entrada.num_entrada = p_entrada//64
                entradas.append(entrada)

        return entradas

fs = FSUnamFI()
for i in fs.obtenerEntradas():
    print(i.nombre_archivo, i.num_entrada)

        

