import mmap
import os, os.path
import time, math

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

    def obtener_entradas(self):
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
        entradas = self.obtener_entradas()
        
        print('{:15} {:10} {:20} {:20}'.format("Nombre", "Tamaño", "Creación", "Modificación"))
        for entrada in entradas:
            print('{:15} {:10} {:20} {:20} {:5}'.format(entrada.nombre_archivo, entrada.archivo_size, self.convertir_fecha(entrada.creacion_archivo), self.convertir_fecha(entrada.modificacion_archivo), entrada.num_entrada))

    # Para imprimir la fecha de una manera más adecuada al usuario
    def convertir_fecha(self, fecha):
        anio = fecha[:4]
        mes = fecha[4:6]
        dia = fecha[6:8]
        hora = fecha[8:10]
        min = fecha[10:12]
        seg = fecha[12:14]
        return dia + '/' + mes + '/' + anio + ' ' + hora + ':' + min + ':' + seg

    # La función buscar será fundamental, ya que sabremos si existe una entrada y su ubicación
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
        cluster_inicial = self.calcular_cluster(entradas)
        p_entrada_nueva = self.sb.cluster_size + (entradas[-1].num_entrada + 1) * 64
        entrada_nueva = ' ' * (15 - len(nombre))
        entrada_nueva += nombre
        entrada_nueva += '0' * (9-len(str(size))) + str(size)
        entrada_nueva += '0' * (6-len(str(cluster_inicial))) + str(cluster_inicial) + '0'
        entrada_nueva += fecha_creacion + '0'
        entrada_nueva += fecha_modificacion
        entrada_nueva += ' ' * 4

        self.fs_mmap[p_entrada_nueva:p_entrada_nueva + ENT_DIR.entrada_size] = entrada_nueva.encode('ascii')
        
        self.cargar_contenido(contenido, cluster_inicial)

    def cargar_contenido(self, contenido, cluster_inicial):
        clusters = math.ceil(len(contenido)/self.sb.cluster_size) * 2048
        self.fs_mmap[cluster_inicial*2048:cluster_inicial*2048 + clusters] = contenido + ('0' * (clusters - len(contenido))).encode('ascii')
        
    def calcular_cluster(self, entradas):
        return math.ceil((int(entradas[-1].cluster_inicial) * 2048 + int(entradas[-1].archivo_size)) / 2048)

    def eliminar_archivo(self, archivo):
        entrada = self.buscar_entrada(archivo)

        if entrada != None:
            p_entrada = self.sb.cluster_size + ENT_DIR.entrada_size * entrada.num_entrada
            self.fs_mmap[p_entrada:p_entrada+15] = bytes(ENT_DIR.entrada_sin_usar.encode('ascii'))
            print('[+] El archivo se ha eliminado correctamente')
        else:
            print('[-] El archivo no existe, vuelva a intentarlo')

    #def desfragmentar():

fs = FSUnamFI()
fs.listar()
fs.copiar_a_pc('mensajes.png', './')