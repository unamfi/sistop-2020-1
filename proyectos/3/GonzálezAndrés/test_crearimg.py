import os
from fiunamfs import FIUNAMFS, EntradaDir, format_date
from tabulate import tabulate
import math

# fsimg_path = os.path.join('.', 'fiunamfs backup.img')
# FIUNAMFS.crearimg(filename = fsimg_path, label='Backup')

fsimg_path = os.path.join('.', 'fiunamfs.img')
FIUNAMFS.crearimg(filename = fsimg_path, label='Andres')

fs = FIUNAMFS(fsimg_path)
fs.montar()

# Subimos los archivos en el orden que los subió el profesor
fs.subir(os.path.join('ArchivosParaSubir', 'README.org'), 'README.org')
fs.subir(os.path.join('ArchivosParaSubir', 'logo.png'), 'logo.png')

# Agregamos manualmente otro, en una localidad lejana
path_img = os.path.join('ArchivosParaSubir', 'mensajes.png')
cluster_inicial = 355

try:
    f = open(path_img, 'rb') # Abrimos el archivo en modo lectura
    bytes_archivo = f.read()
    tam_archivo = len(bytes_archivo)
    clusters_requeridos = math.ceil(tam_archivo / fs.tam_cluster)
    #print('Tamaño de "%s": %i bytes, %i clusters' % (path_img, tam_archivo, clusters_requeridos))
    f.close()
except IOError as ioerr:
    print('IOError: %s' % ioerr)

ent1 = EntradaDir('mensajes.png', tam_archivo, cluster_inicial)
fs.agregarEntDir(ent1, bytes_archivo)

lEntDir = fs.scandir()
encabezados = ['Cluster\nde inicio', 'Nombre', 'Tamaño', 'Fecha de creación', 'Fecha de modificación']
tabla = []
for entDir in lEntDir:
    tabla.append([
        entDir.cluster_inicial, 
        entDir.nombre, 
        '%i bytes' % entDir.tam_archivo, 
        format_date(entDir.f_creacion), 
        format_date(entDir.f_modif)
    ])
print('\n', tabulate(tabla, encabezados), '\n')