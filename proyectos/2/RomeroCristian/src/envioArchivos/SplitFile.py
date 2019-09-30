#!/usr/bin/python3
# -*- coding: utf-8 -*-

from threading import Thread, Semaphore, Lock
from os import getcwd, remove
from os.path import basename
from time import sleep

class SplitFile:

    def __init__(self, archivo: str, num_splits=4, dest_dir=getcwd()):
        self.archivo = open(archivo, "rb").read()
        self.nombre = archivo
        self.num_splits = num_splits
        self.dest_dir = dest_dir
        print(self.dest_dir)
        self.list_gen = list()

    def start_split(self, mutex: Semaphore, num_s, split_max=4):

        mutex.acquire()
        self.num_splits = num_s
        print('Semaforo abajo S', mutex)
        sleep(0.1)
        tamanio = len(self.archivo)
        splits = list()
        while split_max > 0:
            splits.append(tamanio//split_max)
            split_max -= 1
        ini = cont = 0
        while splits:
            popper = splits.pop(0)
            self.split((ini, popper), cont)
            ini += 1
            cont += 1
        print('Semaforo Arriba', mutex)
        mutex.release()


    def split(self, rango: tuple, num_split: int):
        """
        :param rango: Recibe el rango de corte del archivo (inicio, fin)
        """
        ext = ".{}.part".format(num_split)
        self.list_gen.append("{}{}".format(self.dest_dir+'/.'+basename(self.nombre), ext))
        print("{}{}".format(self.dest_dir+'/.'+basename(self.nombre), ext))
        archivo_p = open("{}{}".format(self.dest_dir+'/.'+basename(self.nombre), ext), "wb+")

        bina = self.archivo
        archivo_p.write(bina[rango[0]:rango[1]])
        print(archivo_p)
        archivo_p.close()


    def clean_part(self, mutex: Semaphore):
        with mutex:
            [remove(i) for i in self.list_gen]

if __name__=='__main__':

    mut = Semaphore(1)
    sp = SplitFile('UNAM_INGENIERIA-eps-converted-to.pdf', mut)
    sp.start_split(mut)
