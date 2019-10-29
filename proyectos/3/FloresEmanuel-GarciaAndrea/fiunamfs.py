# -*- encoding: utf-8

import mmap
import os, os.path
import time

class FSInit:
    # Iniciar el sistema de archivos
    def __init__(self, ):
        with open("fiunamfs.img", 'r+') as f:
            fs_mmap = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

            self.fs_nombre = fs_mmap[:8].decode('utf-8')
            self.version = fs_mmap[10:13].decode('utf-8')
            self.volumen_tag = fs_mmap[20:35].decode('utf-8')
            self.cluster_size = fs_mmap[40:45].decode('utf-8')
            self.num_cluster_dir = fs_mmap[47:49].decode('utf-8')
            self.num_cluster_total = fs_mmap[52:60].decode('utf-8')

            fs_mmap.close()

            # Validamos que sea el sistema de archivos correcto
            if self.fs_nombre != 'FiUnamFS':
                print('[-] Error: Sistema de Archivos Incorreto')

            exit(-1)

        


    