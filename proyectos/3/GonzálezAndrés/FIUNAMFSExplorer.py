import os
from fiunamfs import FIUNAMFS

fsimg_path = os.path.join('..', 'fiunamfs.img')

fs = FIUNAMFS(fsimg_path)
fs.montar()
l_archivos = fs.listdir()
print(l_archivos)
fs.desmontar()
fs.desmontar()