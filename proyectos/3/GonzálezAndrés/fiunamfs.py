from mmap import mmap

class FIUNAMFS(object):
    def __init__(self, ruta_img):
        self.ruta_img = ruta_img
        self.montado = False

    def montar(self):
        try:
            f = open(self.ruta_img, 'r+b')
        except OSError:
            print('No se puede abrir %s' % self.ruta_img)
        except IOError as e:
            print('IOError %s' % e)
        else:
            self.__mmfs = mmap(f.fileno(), 0)
            nombrefs = self.__mmfs[0:8].decode('ascii')
            # print(nombrefs)
            if nombrefs == 'FiUnamFS':
                self.montado = True

                self.nombre = nombrefs
                print('Nombre del sistema de archivos: %s' % self.nombre)

                self.version = self.__mmfs[10:13].decode('ascii').strip()
                print('Versión: %s' % self.version)
                
                self.etiqueta = self.__mmfs[20:35].decode('ascii').strip()
                print('Etiqueta del volumen: %s' % self.etiqueta)
                
                self.tam_cluster = int(self.__mmfs[40:45].decode('ascii').strip())
                print('Tamaño del cluster: %i bytes' % self.tam_cluster)

                self.tam_dir = int(self.__mmfs[47:49].decode('ascii').strip())
                print('Tamaño del directorio: %i clusters' % self.tam_dir)

                self.tam_unidad = int(self.__mmfs[52:60].decode('ascii').strip())
                print('Tamaño de la unidad: %i clusters' % self.tam_unidad)

                self.tam_entradadir = 64

                print('Sistema de archivos montado')
            else:
                print('No se reconoce el sistema de archivos')
                self.__mmfs.close()
                self.montado = False

    def desmontar(self):
        if self.montado:
            self.__mmfs.close()
            self.montado = False
            print('Sistema de archivos desmontado')
        else:
            print('No se ha montado el sistema de archivos')
    
    def listdir(self):
        ldir = []
        if self.montado:
            inicio = self.tam_cluster
            fin = self.tam_cluster*self.tam_dir+self.tam_cluster
            paso = self.tam_entradadir
            # cluster_actual = 1
            for i in range(inicio,fin,paso):
                entdir = self.__mmfs[i:i+paso]
                nombre = entdir[0:15].decode('ascii').strip()
                
                # if (i % self.tam_cluster) == 0:
                #     print('Cluster actual: %i' % cluster_actual)
                #     cluster_actual+=1

                # if nombre == '\0'*15:
                #     cadena = 'Xx.xXx.xXx.xXx.'.encode('ascii')
                #     print(len(cadena), cadena)
                #     print(len(self.__mmfs[i:i+15]), self.__mmfs[i:i+paso])
                #     try:
                #         self.__mmfs[i:i+15] = cadena
                #     except IndexError as ierr:
                #         print('indexerror')
                    
                if nombre not in('Xx.xXx.xXx.xXx.', '\0'*15):
                    #print(nombre)
                    ldir.append(nombre)
        else: 
            print('No se ha montado el sistema de archivos')
        return ldir
class EntradaDir(object):
    def __init__(self, nombre_arch, tam_archivo, cluster_i, f_creacion, f_modif):
        pass