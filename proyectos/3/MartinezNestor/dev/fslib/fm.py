"""docstring"""
import sys
from fslib.de import DirectoryEntry
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
        	print('img name does not correspond to \'FiUnamFS\'')

    def read_fs(self):
        filename = 'fiunamfs.img'
        if not path.isfile(filename):
            print('No such file or directory:  \'%s\'' % filename)
            sys.exit()
        file_system = open(filename, 'r+')
        data = mmap(file_system.fileno(), 0)
        file_system.close()
        return  data

    def build_sb(self):
    	if self.super_block is not None:
    		return self.super_block

    def get_fs(self):
    	if self.super_block is not None:
    		return self.read_fs()

    def direntry(self, data, dir_entry_id):
        name = data[0:15]
        size = data[16:24]
        cluster = data[25:30]
        creation = data[31:45]
        last_modif = data[45:60]
        non_used_space = data[61:64]
        return DirectoryEntry(name=name, size=size, cluster=cluster, creation=creation, last_modif=last_modif, non_used_space=non_used_space, dir_entry_id=dir_entry_id) 
