# -*- coding: utf-8 -*-
import os
from fiunamfs import FIUNAMFS
from tabulate import tabulate

fsimg_path = os.path.join('.', 'fiunamfs.img')

fs = FIUNAMFS(fsimg_path)
fs.montar()
fs.montar()

l_archivos = fs.listdir()
print(l_archivos)

lEntDir = fs.scandir()
encabezados = ['Cluster\nde inicio', 'Nombre', 'Tamaño', 'Fecha de creación', 'Fecha de modificación']
tabla = []
for entDir in lEntDir:
    tabla.append([
        entDir.cluster_inicial, 
        entDir.nombre, 
        '%i bytes' % entDir.tam_archivo, 
        entDir.f_creacion, 
        entDir.f_modif
    ])
print(tabulate(tabla, encabezados))

# fs.descargar('README.org', os.path.join('ArchivosDescargados', 'README.org'))
# fs.descargar('logo.png', os.path.join('ArchivosDescargados', 'logo.png'))
# fs.descargar('mensajes.png', os.path.join('ArchivosDescargados', 'mensajes.png'))

fs.subir('README.org', 'OtroMas')
fs.subir('README.org', 'OtroMas\na')
fs.subir('README.org', '')
fs.subir('README.org', 'OtroMás')
fs.subir('README.org', 'Otro Más  ')
fs.subir('README.org', 'Otro mass largo........  ')

fs.desmontar()
fs.desmontar()