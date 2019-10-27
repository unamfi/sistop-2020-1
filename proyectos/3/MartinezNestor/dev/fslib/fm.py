"""docstring"""
from fslib.sb import SuperBlock
from mmap import mmap
from os import path


class FileManager():
    """docstring for FileManager"""
    def __init__(self):
        self.data = self.read_fs()

        fs_name = self.data[0:8].decode()
        version = self.data[10:13].decode()
        label = self.data[20:35].decode()
        cluster_size = self.data[40:45].decode()
        num_clusters_dir = self.data[47:49].decode()
        num_clusters_unit = self.data[52:60].decode()

        if fs_name == 'FiUnamFS':
        	self.super_block = SuperBlock(name=fs_name, version=version, label=label, cluster_size=cluster_size, num_clusters_dir=num_clusters_dir, num_clusters_unit=
        		num_clusters_unit)
        else:
        	self.super_block = None
        	raise(IOError, 'No se puede abrir el sistema de archivos')

    def read_fs(self):
        filename = 'fiunamfs.img'
        if not path.isfile(filename):
            raise(IOError, 'El archivo %s no existe' % filename)
        f_h = open(filename, 'r+')
        return  mmap(f_h.fileno(), 0)

    def build_sb(self):
    	if self.super_block is not None:
    		return self.super_block

    def get_fs_data(self):
    	if self.super_block is not None:
    		return self.data 