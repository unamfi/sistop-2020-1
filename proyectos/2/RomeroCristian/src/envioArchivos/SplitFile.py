#!/usr/bin/python3
# -*- coding: utf-8 -*-

from threading import Thread, Semaphore
from os import getcwd

class SplitFile:

    def __init__(self, archivo: str, mutex: Semaphore,
                 num_splits=4, dest_dir=getcwd()):
        self.archivo = open(archivo, "rb").read()
        self.nombre = archivo
        self.num_splits = num_splits
        self.dest_dir = dest_dir
        self.mutex = mutex

    def start_split(self, split_max=4):
        tamanio = len(self.archivo)
        splits = list()
        while split_max > 0:
            splits.append(tamanio//split_max)
            split_max -= 1
        ini = cont = 0
        with self.mutex:
            while splits:
                popper = splits.pop(0)
                Thread(target=self.split, args=((ini, popper), cont)).start()
                ini += 1
                cont += 1

    def split(self, rango: tuple, num_split: int):
        """
        :param rango: Recibe el rango de corte del archivo (inicio, fin)
        """
        ext = ".{}.part".format(num_split)
        archivo_p = open("{}{}".format(self.nombre, ext), "wb+")
        archivo_p.write(self.archivo[rango[0]:rango[1]])

if __name__=='__main__':

    mut = Semaphore(1)
    sp = SplitFile('wxglade_out.py', mut)
    sp.start_split()
