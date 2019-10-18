#!/usr/bin/python3
import faker
import os
import time

nombre = '/'.join(['/tmp', faker.Faker().name()])
pid = os.getpid()
print("PID %d; Creando un archivo temporal: %s" % (pid, nombre))

fh = open(nombre, 'w+')
for i in range(100):
    fh.write("Fooooooo!")
fh.flush()
os.system('ls -lh "/proc/%d/fd/"' % pid)
os.unlink(nombre)
print("El archivo está eliminado:")
os.system('ls -lh "/proc/%d/fd/"' % pid)

time.sleep(30)

fh.seek(0)
print(fh.read())
