from os import path
from mmap import mmap
filename = '/tmp/cuac'
if not path.isfile(filename):
    raise(IOError, 'El archivo %s no existe!' % filename)
fh = open(filename, 'r+')
datos = mmap(fh.fileno(), 0)
datos[50:74] = 'Escribiendo directamente'
print(datos[0:100])
