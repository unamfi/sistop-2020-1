# -*- encoding: utf-8
from mmap import mmap
import os

class fiunamfs:
    """Implementación del sistema de archivos para el proyecto de Sistemas
    de Archivos. Gunnar Wolf, clase de Sistemas Operativos, Facultad
    de Ingeniería, UNAM.

    """

    from datetime import datetime
    def __init__(self, filename, fsname='FiUnamFS', version=1.0,
                 label='No Label', sector_size=512, sect_per_clust=4,
                 dir_clusters=4, tot_clusters=720, empty_dir_str='-----------'):
        """Inicialización de un objeto fiunamfs.

        El único parámetro obligatorio es el nombre del archivo en el
        cual se inicializará elsistema de archivos. Los demás
        parámetros, espero, serán suficientemente autodescriptivos.

        """
        self.filename = filename
        self.fsname = fsname
        self.version = version
        self.label = label
        self.sector_size = sector_size
        self.sect_per_clust = sect_per_clust
        self.dir_clusters = dir_clusters
        self.tot_clusters = tot_clusters
        self.empty_dir_str = empty_dir_str

        self.direntry_size = 64
        self.cluster_size = self.sector_size * self.sect_per_clust
        self.tot_direntries = int(self.cluster_size * self.dir_clusters /
                                  self.direntry_size)
        self.total_size = self.cluster_size * self.tot_clusters

        if not os.path.isfile(filename):
            # Para dimensionar al sistema del tamaño deseado, creamos
            # un archivo vacío, saltamos (seek()) hasta el punto
            # máximo menos un byte, y escribimos un byte (\0). Todo el
            # espacio restante se llena de \0.
            with open(filename, 'w') as out:
                out.seek(self.tot_clusters * self.cluster_size - 1)
                out.write("\0")

        filesize = os.stat(self.filename).st_size
        if filesize != self.total_size:
            raise RuntimeError(('El archivo %s existe, pero es de tamaño ' +
                                'incorrecto (%d != %d)') %
                               (self.filename, self.total_size, filesize))

        self.fh = open(self.filename, 'r+')
        self.data = mmap(self.fh.fileno(), 0)

    def __del__(self):
        """Destructor del objeto (llamado automáticamente)"""
        self.data = None
        if 'fh' in dir(self):
            self.fh.close()

    def format(self):
        """Formatea un volumen / archivo ejemplo como fiunamfs, con los
        parámetros especificados en __init__"""
        self.init_superblock()
        for i in range(self.tot_direntries):
            self.write_dentry(i, self.empty_dir_str, 0, 0, 0, 0)

    def init_superblock(self):
        """Inicializa el "superbloque" (el primer sector) del sistema de
        archivos con los parámetros especificados en __init__"""
        print('Inicializando volumen %s versión %s, etiqueta «%s»' %
              (self.fsname, self.version, self.label))
        print('Tamaño de cluster: %d. Tamaño de directorio: %d clusters' %
              (self.cluster_size, self.direntry_size))
        print('Entradas de directorio: %d. Clusters totales: %d' %
              (self.tot_direntries, self.tot_clusters))

        # Para almacenar datos dentro de un archivo mmap()eado,
        # tenemos que codificar nuestras cadenas de texto de modo
        # que no haya caracteres de ancho diferente a 8 bits
        # (recuerden Unicode...) — encode() convierte un objeto
        # tipo 'str' (cadena Unicode) en bytes (arreglo de
        # caracteres de 8 bits)
        self.data[0:8] = ('%8s' % self.fsname).encode()
        self.data[10:13] = ('%3s' % self.version).encode()
        self.data[20:35] = ('%15s' % self.label).encode()
        self.data[40:45] = ('%05d' % self.cluster_size).encode()
        self.data[47:49] = ('%02d' % self.dir_clusters).encode()
        self.data[52:60] = ('%08d' % self.tot_clusters).encode()

    def write_dentry(self, pos, name, size, cluster, creat, modif):
        """Escribe una entrada de directorio en la posición especificada"""
        print('- Creando entrada de directorio, posición %d: «%s»' %
              (pos, name))
        print('  Primer cluster: %d. Tamaño: %d. Creación: %s, modif: %s' %
              (cluster, size, creat, modif))
        pos = (self.cluster_size) + (pos * self.direntry_size)
        self.data[pos+0:pos+15] = ('%15s' % name).encode()
        self.data[pos+16:pos+24] = ('%08d' % size).encode()
        self.data[pos+25:pos+30] = ('%05d' % cluster).encode()
        self.data[pos+31:pos+45] = ('%014d' % creat).encode()
        self.data[pos+46:pos+60] = ('%014d' % modif).encode()

    # stuff debe ser un objeto bytes, no str
    def filedata(self, start, stuff):
        """Graba los datos correspondientes a un archivo. Ojo, esta función no
        verifica _nada_, sólo hace lo que le pedimos

        """
        print('  Escribiendo %d bytes a partir de %d' % (len(stuff), start))
        st_byte = start * self.cluster_size
        end_byte = st_byte + len(stuff)
        self.data[st_byte:end_byte] = stuff

    def write(self, filename, filedata, dentry=None, start_cluster=None,
              creat=int(datetime.now().strftime('%Y%m%d%H%M%S')),
              modif=int(datetime.now().strftime('%Y%m%d%H%M%S'))):
        """Escribe dentro del fiunamfs el nombre de archivo especificado como
        primer parámetro, registrando los datos de archivo
        especificados como segundo parámetro.

        Los parámetros opcionales dentry (lugar en el directorio donde
        debe escribirse) y start_cluster (primer cluster para el
        archivo) deben ser llenados (no hay "defaults sensatos").

        """

        self.write_dentry(dentry, filename, len(filedata),
                          start_cluster, creat, modif)
        self.filedata(start_cluster, filedata)

if __name__  == '__main__':
    filename = 'fiunamfs.img'
    fs = fiunamfs(filename, fsname='FiUnamFS', version=0.7, label='No Label',
                  sector_size=512, sect_per_clust=4, dir_clusters=4,
                  tot_clusters=720, empty_dir_str='Xx.xXx.xXx.xXx.')
    fs.format()

    # Copiar tres archivos hacia el interior de FiUnamFS
    stuff = open('README.org', 'rb').read()
    fs.write('README.org', stuff, dentry=0, start_cluster=5)

    stuff = open('/tmp/logo.png', 'rb').read()
    fs.write('logo.png', stuff, dentry=2, start_cluster=17)

    stuff = open('/tmp/mensajes.png', 'rb').read()
    fs.write('mensajes.png', stuff, dentry=5, start_cluster=353)
