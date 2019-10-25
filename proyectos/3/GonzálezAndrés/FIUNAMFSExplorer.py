import os
from fiunamfs import FIUNAMFS

fsimg_path = os.path.join('..', 'fiunamfs.img')

fs = FIUNAMFS(fsimg_path)
fs.montar()
fs.listdir()
fs.desmontar()
fs.desmontar()