from mmap import mmap

class FIUNAMFS(object):
    def __init__(self, img_path):
        self.img_path = img_path
        self.mounted = False

    def mount(self):
        try:
            f = open(self.img_path, 'r+b')
        except OSError:
            print('No se puede abrir ', self.img_path)
        else:
            self.__mmfs = mmap(f.fileno(), 0)
            fsname = self.__mmfs[0:8].decode('ascii')
            print(fsname)
            if fsname == 'FiUnamFS':
                self.mounted = True
                print('Sistema de archivos montado')
            else:
                print('No se reconoce el sistema de archivos')
                self.__mmfs.close()
                self.mounted = False

    def umount(self):
        if self.mounted:
            self.__mmfs.close()
            self.mounted = False
            print('Sistema de archivos desmontado')
        else:
            print('No se ha montado el sistema de archivos')