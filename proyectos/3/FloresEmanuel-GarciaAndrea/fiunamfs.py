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
        self.nombre_archivo       = entrada[0:15].decode('ascii').strip()
        self.archivo_size         = entrada[16:24].decode('ascii')
        self.cluster_inicial      = entrada[25:30].decode('ascii')
        self.creacion_archivo     = entrada[31:45].decode('ascii')
        self.modificacion_archivo = entrada[46:60].decode('ascii')
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
        
        print('{:15} {:10} {:20} {:20}'.format("Nombre", "Tamaño", "Creación", "Modificación"))
        for entrada in entradas:
            print('{:15} {:10} {:20} {:20}'.format(entrada.nombre_archivo, entrada.archivo_size, self.convertirFecha(entrada.creacion_archivo), self.convertirFecha(entrada.modificacion_archivo)))

    # Para imprimir la fecha de una manera más adecuada al usuario
    def convertirFecha(self, fecha):
        anio = fecha[:4]
        mes = fecha[4:6]
        dia = fecha[6:8]
        hora = fecha[8:10]
        min = fecha[10:12]
        seg = fecha[12:14]
        return dia + '/' + mes + '/' + anio + ' ' + hora + ':' + min + ':' + seg

    # La función buscar será fundamental, ya que sabremos si existe una entrada y su ubicación
    def buscarEntrada(self, nombre_buscar):
        for num_entrada in range(128):
            p_entrada = self.sb.cluster_size + num_entrada * ENT_DIR.entrada_size
            entrada = ENT_DIR(self.fs_mmap[p_entrada:p_entrada + ENT_DIR.entrada_size])

            if nombre_buscar == entrada.nombre_archivo:
                return entrada
        return None

    def copiar_a_pc(self, archivo, ruta):
        entrada = self.buscarEntrada(archivo)
        if entrada != None and os.path.exists(ruta):
            cluster = int(entrada.cluster_inicial) * self.sb.cluster_size
            with open(ruta + '/' + archivo, 'w+b') as nuevo_archivo:
                nuevo_archivo.write(self.fs_mmap[cluster: cluster+int(entrada.archivo_size)])
                print('[+] El archivo se copio correctamente')
        else:
            print('[-] Archivo no encontrado')



    #def copiar_a_fs():

    #def eliminar_archivo():

    #def desfragmentar():

fs = FSUnamFI()
fs.copiar_a_pc('README.org','/home/emanuel/Documents/C-Semestral')

