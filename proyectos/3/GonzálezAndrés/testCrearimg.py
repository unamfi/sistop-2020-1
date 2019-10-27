import os
from fiunamfs import FIUNAMFS
from tabulate import tabulate

fsimg_path = os.path.join('.', 'fiunamfs v0.8.img')

FIUNAMFS.crearimg(filename = fsimg_path, label='Andres')