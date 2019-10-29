# -*- coding: utf-8 -*-
import mmap
import os # para conocer los metadatos de archivos a ingresar con la fx cpin()
import math
import os.path, time
class SuperBlock :
    """
        El superbloque para este sistema de archivos ocupa el primer cluster
        del mismo, es decir, ocupa 2048
    """

    f = open('fiunamfs.img','r+b')
    fs_map = mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)

    # Información de superbloque
    name            = fs_map[0:8].decode('utf-8')         # FiUnamFS
    version         = fs_map[10:13].decode('utf-8')       # 0.4
    tagv            = fs_map[20:35].decode('utf-8')       # Mi Sistema
    size_cluster    = int(fs_map[40:45].decode('utf-8'))  # 2048
    numdir_cluster  = int(fs_map[47:49].decode('utf-8'))  # 04
    total_cluster   = int(fs_map[52:60].decode('utf-8'))  # 00000720
    size_dentry     = 64                                  # size dir entry

    f.close()
    fs_map.close()

class DIRENTRY :
    """
        De hecho, estrictamente esta clase no es un inode ya que estamos
        guardando el nombre del archivo en él y eso no pasa en los verdaderos
        inodes y obviamente tampoco estamos guardando
        permisos ni propietarios porque NO los tenemos
    """
    offset_fname  = 15
    offset_fsize = 8
    offset_fcluster = 5
    offset_fcreated = 14
    offset_fmodif = 14

    fname = ""         # 0-15
    fsize = 0          # 16-24
    finit_cluster = 0  # 25-30
    fcreated = ""      # 31-45
    fmodif = ""        # 46-60
    numdir = -1        # numero entre 0-63
                       # por las especificaciones

    def __init__(self, dir_entry):
        self.fname = dir_entry[0:15].decode('utf-8').lstrip()
        self.fsize = int(dir_entry[16:24].decode('utf-8'))
        self.finit_cluster = int(dir_entry[25:30].decode('utf-8'))
        self.fcreated = dir_entry[31:45].decode('utf-8')
        self.fmodif = dir_entry[46:60].decode('utf-8')
        

class FIFS:
    
    f = open('fiunamfs.img','a+b')
    fs_map = mmap.mmap(f.fileno(),0,access=mmap.ACCESS_WRITE)

    sb = SuperBlock()

    dentry_notused ='Xx.xXx.xXx.xXx.'

    # Función interna
    def inodes(self):
        # usamos del 1-4 clusters, es decir 2048*4 = 4096
        # las entradas miden 64 por lo tanto 4096/64 = 128, entonces el rango
        # del for 0-128
        inodes = []
        for j in range(0,128):

            # El directorio se encuentra en los cluster de 1-4 y cada cluster
            # mide 2048 por lo tanto debemo ir en 2048, el cluser 0 es el
            # superblock

            prtb = self.sb.size_cluster + j*self.sb.size_dentry
            i = DIRENTRY(self.fs_map[prtb:prtb + self.sb.size_dentry])
            if self.dentry_notused != i.fname:
                i.numdir = j
                inodes.append(i)
        return inodes

    def search(self,fe):
        for j in range(0,128):
            prtb = self.sb.size_cluster + j*self.sb.size_dentry
            i = DIRENTRY(self.fs_map[prtb:prtb + self.sb.size_dentry])
            if fe == i.fname:
                i.numdir = j
                return i
        return None

    def registerFile(self,fe,cluster):
        for j in range(0,128):
            prtb = self.sb.size_cluster + j*self.sb.size_dentry
            i = DIRENTRY(self.fs_map[prtb:prtb + self.sb.size_dentry])
            if self.dentry_notused == i.fname:
                # tener cuidado con longitud de nombres
                spaces = i.offset_fname - len(fe)
                self.fs_map[prtb:prtb + i.offset_fname] = bytes(fe.rjust(len(fe)+spaces)).encode('utf-8')

                fe_size = str(os.stat(fe).st_size)
                size_zeros = i.offset_fsize - len(fe_size)
                new_ptrb = prtb + i.offset_fname + 1
                self.fs_map[new_ptrb :new_ptrb + i.offset_fsize] = bytes(fe_size.zfill(len(fe_size)+size_zeros)).encode('utf-8')

                fe_cluster = str(cluster)
                cluster_zeros = i.offset_fcluster - len(fe_cluster)
                new_ptrb += i.offset_fsize + 1
                self.fs_map[new_ptrb:new_ptrb + i.offset_fcluster] = bytes(fe_cluster.zfill(len(fe_cluster)+cluster_zeros)).encode('utf-8')

                fe_date_create= time.strftime('%Y%m%d%H%M%S', time.gmtime(os.path.getctime(fe)))
                new_ptrb += i.offset_fcluster + 1
                self.fs_map[new_ptrb:new_ptrb + i.offset_fcreated] = bytes(fe_date_create).encode('utf-8')

                fe_date_modif=time.strftime('%Y%m%d%H%M%S', time.gmtime(os.path.getmtime(fe)))
                new_ptrb += i.offset_fcreated+ 1
                self.fs_map[new_ptrb:new_ptrb + i.offset_fmodif] = bytes(fe_date_modif).encode('utf-8')

                break

    def cpint(self,inode,clustdest):
        ptrb=self.sb.size_cluster*inode.finit_cluster
        buffer=self.fs_map[ptrb:ptrb+inode.fsize]
        ptrbdest=self.sb.size_cluster*clustdest
        self.fs_map[ptrbdest:ptrbdest+inode.fsize]=buffer

    def close(self):
        self.fs_map.close()
        self.f.close()

    def ls(self):
        for i in self.inodes():
            f=self.date_format(i.fmodif)
            print("%s\t%d\t%d\t%s" %(i.fname,i.finit_cluster,i.fsize,f))

    def rm(self,fe):
        #Primero buscar si el archivo existe,
        #si existe, perdemos la ref hacia él
        i = self.search(fe)
        if i is None :
            print("rm: " + fe + " : No such file ")
        else :
            prtb = self.sb.size_cluster + self.sb.size_dentry*i.numdir
            self.fs_map[prtb:prtb + i.offset_fname] = bytes(self.dentry_notused).encode('utf-8')


    def date_format(self,date):
        months={'01':'Jan','02':'Feb','03':'March','04':'Apr','05':'May',
            '06':'Jun','07':'Jul','08':'Aug','09':'Sept','10':'Oct','11':'Nov','12':'Dec'}
        a=date[0:4]
        m=months.get(date[4:6])
        d=date[6:8]
        hh=date[8:10]
        mm=date[10:12]
        ss=date[12:14]
        return m+'\t'+d+'\t'+a+'\t'+hh+':'+mm+':'+ss


    def cpout(self,fe,dir):
        #Primero buscar si el archivo existe,
        #si existe, lo copiamos al directorio especificado
        i = self.search(fe)
        if i is None :
            print("cpout: " + fe + " : No such file ")
        else :
            prtb = self.sb.size_cluster + self.sb.size_dentry*i.numdir
            # VERIFICAR QUE EXISTA EL ARCHIVO
            filecp = open(fe,"a+b")
            cluster = self.sb.size_cluster*i.finit_cluster
            # operacion : 2048*inicio_cluster_del_archivo_a_copiar
            filecp.write(self.fs_map[cluster:cluster + i.fsize])
            filecp.close()

    def cpin(self,fe):
        # Buscar si no hay un archivo con el nombre recibido
        # Si no entonces
        #   buscar un lugar donde quepa el archivo
        #   sino hay lugar, desfragmentamos
        #   si despues de desfragmentar no hay lugar
        #       mandar error

        # cargando todos los dentry que no tenga la cadena 'AQUI NO VA'
        # mediante la funcion inodes()
        #PRIMERO VALIDAR SI EL ARCHIVO EXISTA

        if os.path.isfile(fe):
            if len(fe)<15:
                if self.search(fe)!=None:
                    print('Ya existe un archivo con el mismo nombre, renombrar')
                else:
                   self.cp(fe)
            else:
                print("cpin: " + fe + ": file name too large")
        else:
            print("cpin: " + fe + ": file not found")

    def defrag(self):
        inodes=self.inodes()
        if(len(inodes)!=0):
            if inodes[0].finit_cluster != 5:
                self.cpint(inodes[0],5)
                self.over(inodes[0],5)
                inodes[0].finit_cluster=5


            for j in range(0,len(inodes)-1):

                i_lastcluster = inodes[j].finit_cluster + math.ceil(inodes[j].fsize/self.sb.size_cluster)
                self.cpint(inodes[j+1],i_lastcluster+1)
                self.over(inodes[j+1],i_lastcluster+1)
                inodes[j].finit_cluster=i_lastcluster+1


    def over(self,inode,newcluster):
        fe_cluster = str(newcluster)
        cluster_zeros = inode.offset_fcluster- len(fe_cluster)
        ptrb = self.sb.size_cluster + inode.numdir*self.sb.size_dentry+25
        self.fs_map[ptrb:ptrb+inode.offset_fcluster]=bytes(fe_cluster.zfill(len(fe_cluster)+cluster_zeros),'utf-8')

    def cp(self,fe): 
        inodes = self.inodes()
        inodes.sort(key=lambda x: x.finit_cluster)
        fe_size = os.stat(fe).st_size
        fe_numclusters = math.ceil(fe_size/self.sb.size_cluster)

        if len(inodes) == 0:
            i_lastcluster = 4
            cluster_space = self.sb.total_cluster - i_lastcluster
            if fe_numclusters <= cluster_space :
                f = open(fe,"rb")
                fe_prtb = self.sb.size_cluster*(i_lastcluster + 1)
                fe_prtt = fe_prtb + fe_size
                self.fs_map[fe_prtb:fe_prtt] = f.read()
                self.registerFile(fe,i_lastcluster+1)
                f.close()
            else:
                print("cpin: " + fe + ": file too large")

        elif len(inodes) == 1:
            self.defrag()
            i_lastcluster = inodes[0].finit_cluster + math.ceil(inodes[0].fsize/self.sb.size_cluster)
            cluster_space = self.sb.total_cluster - i_lastcluster
            if fe_numclusters <= cluster_space :
                f = open(fe,"rb")
                fe_prtb = self.sb.size_cluster*(i_lastcluster + 1)
                fe_prtt = fe_prtb + fe_size
                self.fs_map[fe_prtb:fe_prtt] = f.read()
                self.registerFile(fe,i_lastcluster+1)
                f.close()
            else:
                print("cpin: " + fe + ": file too large")
        else:        
            sucess = False
            for j in range(0,len(inodes)-1):
                i_lastcluster = inodes[j].finit_cluster + math.ceil(inodes[j].fsize/self.sb.size_cluster)
                # espacio en clusters entre archivos
                cluster_space = inodes[j+1].finit_cluster - i_lastcluster
                # Usando el algoritmo FIFO, guardamos nuestro archivo en el
                # primer bloque en el que quepa
                if fe_numclusters <= cluster_space :
                    f = open(fe,"rb")
                    # vamos a escribir en i_lastcluster + 1 nuestra info
                    fe_prtb = self.sb.size_cluster*(i_lastcluster + 1)
                    fe_prtt = fe_prtb + fe_size
                    self.fs_map[int(fe_prtb):int(fe_prtt)] = f.read()
                    # hacer registro de metadatos
                    self.registerFile(fe,i_lastcluster+1)
                    f.close()
                    sucess = True
                    break

            if not sucess:
                i_lastcluster = inodes[len(inodes)-1].finit_cluster + math.ceil(inodes[len(inodes)-1].fsize/self.sb.size_cluster)
                cluster_space = self.sb.total_cluster - i_lastcluster
                if fe_numclusters <= cluster_space :
                    f = open(fe,"rb")
                    # vamos a escribir en i_lastcluster + 1 nuestra info
                    fe_prtb = self.sb.size_cluster*(i_lastcluster + 1)
                    fe_prtt = fe_prtb + fe_size
                    self.fs_map[int(fe_prtb):int(fe_prtt)] = f.read()
                    # hacer registro de metadatos
                    self.registerFile(fe,i_lastcluster+1)
                    f.close()
                    sucess = True

                if not sucess:
                    print("cpin: " + fe + ": file too largeeee") 