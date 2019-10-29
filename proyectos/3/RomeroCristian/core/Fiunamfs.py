#!/usr/bin/python
# -*- coding: utf-8 -*-

import mmap, os, datetime, time

from datetime import datetime
from math import ceil


class Fiunamfs:
    ##  Este metodo inicializa un nuevo FILESYS creando su superbloque y llenando el indice de directorio
    @staticmethod
    def crear_fs(raiz, nvol):
        if nvol == None:
            nvol = "NUEVO_VOL"
            size_nvol = len(nvol)
            sobrante_nvol = (35 - 20) - size_nvol if size_nvol < 35 - 20 else 0
        with open(raiz,"w+") as f:
            f.write(("\x00"*(512*1440)))
            filesys = mmap.mmap(f.fileno(),0)
            filesys[0:8] = "FiUnamFS".encode('ascii')
            filesys[10:13] = "0.7".encode('ascii')
            filesys[20:35] = str(("0"*sobrante_nvol)+nvol).encode('ascii')
            filesys[40:45] = "00512".encode('ascii')
            filesys[47:49] = "04".encode('ascii')
            filesys[52:60] = "00001440".encode('ascii')
            for i in range(64):
                FiUnamFS.escribir_indir(filesys,i)
            filesys[512*5:] = str("\x00"*(512*1435)).encode('ascii')
            f.close()
    
    ## Este metodo escribe una entrada en el indice de directorio del FILESYS persistente
    def escribir_indir(FILESYS, id,name_file="AQUI_NO_VA_NADA",size_file="",inicluster="",cdate="",mdate="",no_use=""):
        byte = 512
        tamanno_indir = 64
        id = int(id)
        try:
            FILESYS[byte+(tamanno_indir*id):byte+(tamanno_indir*id)+15] =\
                ((" "*(15-len(str(name_file))))+str(name_file)).encode('ascii')
        except:
            print("Nombre no valido")
            return False
        FILESYS[byte+(tamanno_indir*id)+16:byte+(tamanno_indir*id)+24] =\
            ("0"*(8-len(str(size_file)))+str(size_file)).encode('ascii')
        FILESYS[byte+(tamanno_indir*id)+25:byte+(tamanno_indir*id)+30] =\
            ("0"*(5-len(str(inicluster)))+str(inicluster)).encode('ascii')
        FILESYS[byte+(tamanno_indir*id)+31:byte+(tamanno_indir*id)+45] =\
            ("0"*(14 - len(str(cdate)))+str(cdate)).encode('ascii')
        FILESYS[byte+(tamanno_indir*id)+46:byte+(tamanno_indir*id)+60] =\
            ("0"*(14 - len(str(mdate)))+str(mdate)).encode('ascii')
        FILESYS[byte+(tamanno_indir*id)+61:byte+(tamanno_indir*id)+64] =\
            ("\x00"*(3 - len(str(no_use)))+str(no_use)).encode('ascii')
        return True





    # Este metodo lee del FILESYS persistente el indice de directorio y lo asigna a memoria principal
    def analizar_dir(self):
        for input_dir in range(self.num_input_dir):
            name_dir = self.map[512+(64*input_dir):512+
                                (64*input_dir)+15].decode('ascii').replace(" ","")
            tam_archivo = int(self.map[512+(64*input_dir)+
                                       16:512+(64*input_dir)+24])
            cluster_inicial = int(self.map[512+(64*input_dir)+
                                           25:512+(64*input_dir)+30])
            fecha_creacion = int(self.map[512+(64*input_dir)+
                                          31:512+(64*input_dir)+45])
            fecha_modificacion = int(self.map[512+(64*input_dir)+
                                              46:512+(64*input_dir)+60])
            # Crea diccionario que sera añadido al array del indice de directorio
            self.inputs_dir.append(dict(id=input_dir,name_dir=name_dir,
                                        size_file=tam_archivo,
                                        inicluster=cluster_inicial,
                                        file_creation = fecha_creacion,
                                        file_mod = fecha_modificacion))
    # Inicializa el FILESYS y valida que sea un FILESYS valido
    def __init__(self, raiz):
        super(FiUnamFS, self).__init__()
        self.raiz = raiz
        self.void_entrada_dir = "AQUI_NO_VA_NADA"
        # Valida que el FILESYS sea archivo valido para inicializar 
        if os.path.isfile(self.raiz):
            with open(self.raiz,"r+") as f:
                self.map = mmap.mmap(f.fileno(),0)
                try:
                    self.nombre_FILESYS = self.map[0:8].decode('ascii')
                except:
                    print("el sistema de archivos no es valido")
                    exit()
                # Se valida que sea no sea otro FILESYS
                if self.nombre_FILESYS != 'FiUnamFS':
                    print("el sistema de archivos no es valido")
                    exit()
                # Añado datos del superbloque a variable
                self.version_FILESYS = self.map[10:13].decode('ascii')
                self.etiqueta_vol = self.map[20:35].decode('ascii')
                self.size_of_cluster_FILESYS = int(self.map[40:45].decode('ascii'))
                self.num_of_cluster_dir_FILESYS = int(self.map[47:49].decode('ascii'))
                self.num_of_cluster_total_FILESYS = int(self.map[52:60].decode('ascii'))
                self.files = {}
                dcluster_byte=512
                tamanno_indir = 64
                # Se calcula el numero de entradas en directorio
                self.num_input_dir = int(self.size_of_cluster_FILESYS/tamanno_indir * self.num_of_cluster_dir_FILESYS)
                self.inputs_dir = []
            self.analizar_dir()
        else:
            exit()
    # Obtiene una lista de los indices que contiene un nombre pasado por argumento
    def get_index_dir(self,name,key_out='id'):
        try:
            lista = []
            for elem in self.inputs_dir:
                if elem['name_dir'] == name:
                    lista.append(elem[key_out])
            return lista
        except:
            return -1

    def get_index_not_dir(self,name):
        try:
            lista = []
            for elem in self.inputs_dir:
                if elem['name_dir'] != name:
                    lista.append(elem['id'])
            return lista
        except:
            return -1
    
    # Escribe en el archivo persistente el indice del directorio que esta en memoria principal
    def write_index_dir(self):
        dcluster_byte=512
        tamanno_indir = 64
        for input_dir in self.inputs_dir:
            FiUnamFS.escribir_indir(self.map,input_dir['id'],
                                     input_dir['name_dir'],input_dir['size_file'],
                                     input_dir['inicluster'],
                                     input_dir['file_creation'],
                                     input_dir['file_mod'])
        return True
    
     # Lista el contenido del FILESYS
    def listar_contenido(self):
        print("\033[36mNombre\t\033[35mCluster inicial\t\033[34mtamaño en" +
              "bytes\033[33m\tFecha Creacion\t\033[32m Fecha modificacion\033[0m")
        for input_dir in self.inputs_dir:
            if input_dir["name_dir"] != self.void_entrada_dir:
                print("\033[31m{0}\t\033[32m{1}\t\033[33m{2\t\033[34m{3}\t" +
                      "\033[35m{4}\033[0m".\
                      format(input_dir["name_dir"],input_dir['inicluster'],
                             input_dir['size_file'],input_dir['file_creation'],
                             input_dir['file_mod']))
    
    # regresa los datos del archivo por su nombre
    def read(self,name):
        index = self.get_index_dir(name)
        if index != []:
            index = index[0]
            input_dir = self.inputs_dir[index]
            inicluster = input_dir['inicluster']
            size_file =  input_dir['size_file']
            return self.map[self.size_of_cluster_FILESYS*inicluster:self.size_of_cluster_FILESYS*inicluster+size_file]
        return False

    ### Escribe un nuevo archivo y escribe su entrada en el directorio
    def write(self,name,data,create_date):
        if name not in self.get_index_dir(name,'name_dir'):
            index = self.get_index_dir(self.void_entrada_dir)
            if index != []:
                index = index[0]
                input_dir = self.inputs_dir[index]
                size_file =  len(data)
                inputs_dir = list(filter(lambda x: x['name_dir'] not in self.void_entrada_dir,self.inputs_dir))
                inputs_dir = sorted(inputs_dir, key = lambda x:x['inicluster'], reverse=True)
                if inputs_dir != []:
                    inicluster = self.get_cluster_final(inputs_dir[0]) + 1
                else:
                    inicluster = 5
                input_dir = dict(inicluster=inicluster, size_file=size_file)
                cluster_final = self.get_cluster_final(input_dir)
            if (cluster_final < 1440):
                self.set_data(inicluster,size_file,data)
                self.inputs_dir[index]['name_dir'] = name
                self.inputs_dir[index]['inicluster'] = inicluster
                self.inputs_dir[index]['size_file'] = size_file
                self.inputs_dir[index]['file_mod'] = self.time_to_formatFILESYS(time.time())
                self.inputs_dir[index]['file_creation'] = self.time_to_formatFILESYS(create_date)
                self.write_index_dir()
                return True
            else:
                print("Ya no hay espacio para meter este archivo")
        else:
            print("ya existe un archivo con el mismo nombre")
        return False
    
    # Convierte una ruta absoluta y obtiene el nombre del archivo
    def parse_ruta_a_nombre_archivo(self,path):
        path = path.split("/")
        return path[len(path)-1]

    #copia del FILESYS a un FILESYS externo
    def copiar_FILESYS_a_eXFILESYS(self,source,dest):
        data = self.read(source)
        # valida que el destino no sea un directorio
        # Es obligatorio asignar un nombre al archivo que sera copiado al sistema externo
        if not os.path.isdir(dest):
            with open(dest,"wb+") as f:
                f.write(data)
                return True
        return False
    
    
    #copia del FILESYS externo al FILESYS
    def copiar_eXFILESYS_a_FILESYS(self,source):
        if os.path.isfile(source):
            with open(source,"r+") as f:
                name = self.parse_ruta_a_nombre_archivo(source)
                if name not in self.get_index_dir(name,'name_dir'):
                    filesys = mmap.mmap(f.fileno(),0)
                    data = filesys.read()
                    create_date = os.path.getctime(source)
                    return self.write(name,data,create_date)
                else:
                    print("Este archivo ya existe en el sistema de archivos")
                    return False
        print("No es un archivo valido")
        return False
    
    # Desfragmenta el FILESYS 
    def desfragmentar(self):
        self.inputs_dir
        indexes = self.get_index_not_dir(self.void_entrada_dir)
        cluster_nuevo = 5
        for index in indexes:
            cluster_inicial = self.inputs_dir[index]['inicluster']
            size_bits = self.inputs_dir[index]['size_file']
            data = self.get_data(cluster_inicial,size_bits)
            cluster_final = self.get_cluster_final(self.inputs_dir[index])
            tam_clusters = len(self.get_list_range(cluster_inicial,cluster_final))
            cluster_inicial = cluster_nuevo
            self.set_data(cluster_inicial,size_bits,data)
            self.inputs_dir[index]['inicluster'] = cluster_inicial
            cluster_nuevo = cluster_inicial + tam_clusters
        return self.write_index_dir()

    # Obtiene los datos binarios de una entrada en el FILESYS
    def get_data(self,cluster_inicial,size_bits):
        return self.map[self.size_of_cluster_FILESYS*cluster_inicial:self.size_of_cluster_FILESYS*cluster_inicial+size_bits]
    
    # Escribe los datos a una entra den el FILESYS
    def set_data(self,cluster_inicial,size_bits,data):
        try:
            self.map[self.size_of_cluster_FILESYS*cluster_inicial:self.size_of_cluster_FILESYS*cluster_inicial+size_bits] = data
            return True
        except Exception as e:
            print(e)
            return False
    
    # Obtiene el cluster final de una entrada en el directorio
    def get_cluster_final(self,input_dir):
        tam = ceil(input_dir['size_file']/512) + 1
        return input_dir['inicluster'] + tam

    # Obtiene una lista de numeros por medio de un numero inicial y final
    # Este metodo es usado para "mapear" numero de clusters
    def get_list_range(self,init,end):
        lista = []
        for i in range(init,end+1):
            lista.append(i)
        return lista
    # Convierte un timestamp a una cadena con el formato del FILESYS
    def time_to_formatFILESYS(self,time):
        date_time = datetime.datetime.fromtimestamp(time)
        return date_time.strftime("%Y%m%d%H%M%S")

    # Elimina una entrada del indice de directorios dejandola libre
    # No elimina datos pero al no estar mapeados en el indice se consideran basura
    # Al final se desfragmenta de manera implicita
    def elimina(self,name):
        index = self.get_index_dir(name)
        if index != []:
            index = index[0]
            input_dir = self.inputs_dir[index]
            inicluster = input_dir['inicluster']
            size_file =  input_dir['size_file']
            self.inputs_dir[index]['name_dir'] = "AQUI_NO_VA_NADA"
            self.inputs_dir[index]['size_file'] = "0"
            self.inputs_dir[index]['inicluster'] = "0"
            self.inputs_dir[index]['file_creation'] = "0"
            self.inputs_dir[index]['file_mod'] = "0"
            return self.desfragmentar()
        return False        
