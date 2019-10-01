#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, basename, dirname
from re import match
from threading import Thread, Semaphore, Lock


class JoinParts:

    def __init__(self, nombre_archivo: str, ruta_destino='.', work_dir='.'):
        self.work_dir = work_dir
        self.list_dir = list()
        self.nombre = basename(nombre_archivo)
        self.ruta_destino = ruta_destino

    def __expresion_r_lista(self):
        """
        Mediante una expreción regular, lista los archivos
        generados a unir
        """

        swap_list = list()
        for archivo in self.list_dir:
            if match('.+\.[0-9]+\.part', '.'+archivo):
                swap_list.append(self.ruta_destino+'/'+archivo)
        self.list_dir = sorted(swap_list)
        print(self.list_dir)

    def to_list(self):
        tmp_list = list()
        if self.tamanio % 2 == 0:
            for i in range(1, self.tamanio, 2):
                tmp_list.append([self.list_dir[i-1], self.list_dir[i]])
        else:
            i = 0
            print(len(self.list_dir))
            while i < len(self.list_dir):
                print(i, self.list_dir[i])
                if i == len(self.list_dir)-1:
                    tmp_list.append([self.list_dir[i]])
                else:
                    tmp_list.append([self.list_dir[i], self.list_dir[i+1]])
                i += 2
        print(tmp_list)
        return tmp_list

    def join(self, mutex: Semaphore):
        """
        Une los archivos partidos, se añade 2\\ para identificar el nuevo
        :param mutex: El semaforo que da via abierta cuando los archivos
          esten generados
        """

        mutex.acquire()
        print('Semaforo abajo J', mutex, listdir(self.ruta_destino))
        self.list_dir = listdir(self.ruta_destino)
        print(self.list_dir)
        self.__expresion_r_lista()
        self.tamanio = len(self.list_dir)
        list_w = self.to_list()
        if isfile(self.nombre):
            self.nombre = '2\ ' + self.nombre
        print(self.ruta_destino+'/'+self.nombre)
        out = open(self.ruta_destino+'/'+self.nombre, 'ab+')

        for i in list_w:

            if len(i) == 2:
                print('uniendo', i[0], '+', i[1])
                f1, f2 = open(i[0], 'rb'), open(i[1], 'rb')
                out.write(f1.read())
                out.write(f2.read())
                f1.close()
                f2.close()
            else:
                print('uniendo', i[0])
                f1 = open(i[0], 'rb')
                out.write(f1.read())
                f1.close()
        out.close()
        mutex.release()
        print('Semaforo Arriba J', mutex)
#        return self.ruta_destino+'/'+self.nombre


if __name__ == '__main__':
    mut = Semaphore(1)
    j = JoinParts('UNAM_INGENIERIA-eps-converted-to.pdf', mut, '../')
    print(j.join())
