# -*- coding: utf-8 -*-
import os
from fiunamfs import FIUNAMFS

fsimg_path = os.path.join('..', 'fiunamfs.img')

fs = FIUNAMFS(fsimg_path)
fs.montar()
l_archivos = fs.listdir()
print(l_archivos)
lEntDir = fs.scandir()
for entDir in lEntDir:
    print('%i %s %i bytes %s %s' %
            (entDir.tam_archivo, entDir.nombre, entDir.cluster_inicial, entDir.f_creacion, entDir.f_modif))
fs.desmontar()
fs.desmontar()