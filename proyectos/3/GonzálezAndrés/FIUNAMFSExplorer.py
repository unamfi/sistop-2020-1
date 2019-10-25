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
    # print('%i %s %i bytes %s %s' % (entDir.cluster_inicial, 
    #                                 entDir.nombre, 
    #                                 entDir.tam_archivo, 
    #                                 entDir.f_creacion, 
    #                                 entDir.f_modif))
print(tabulate(tabla, encabezados))
fs.descargar('README.org', 'README.org')
fs.descargar('logo.png')
fs.descargar('mensajes.png')
fs.desmontar()
fs.desmontar()