"""docstring"""
import os
from datetime import datetime
from random import randint
from fslib.fm import FileManager


class CommandManager():

	f_m = FileManager()

	root_dir = []
	root_dir_entry_size = 64
	root_dir_empty_entry = "Xx.xXx.xXx.xXx."

	available_dir_entries = []
	
	def __init__(self):
		self.super_block = self.f_m.build_sb()
		self.file_system = self.f_m.get_fs()

		self.cluster_size = int(self.super_block.cluster_size)
		self.root_dir_clusters = int(self.super_block.num_clusters_dir)
		self.first_data_cluster = self.root_dir_clusters + 1
		
		(self.root_dir, self.available_dir_entries, self.occupied_data_clusters) = self.get_dir_entries()

	def ls_(self):
		self.root_dir = self.get_dir_entries(only_root=True)
		self.__print__root(dir=self.root_dir)

	def cpi(self, file):
		if self.search(file) is None:
			data = open(file,'rb').read()
			data_size = len(data)
			dir_entry_id = self.available_dir_entries.pop(0)

			name = file
			size = data_size
			cluster = self.get_next_cluster()

			ctime = os.path.getmtime(file)
			mtime = os.path.getmtime(file)
			creation = datetime.fromtimestamp(ctime).strftime('%Y%m%d%H%M%S')
			last_modif = datetime.fromtimestamp(mtime).strftime('%Y%m%d%H%M%S')

			index = self.cluster_size + (dir_entry_id * self.root_dir_entry_size)

			self.file_system[index:index+15] = ('%15s' % name).encode()
			self.file_system[index+16:index+24] = ('%08d' % size).encode()
			self.file_system[index+25:index+30] = ('%05d' % cluster).encode()
			self.file_system[index+31:index+45] = ('%014s' % creation).encode()
			self.file_system[index+46:index+60] = ('%014s' % last_modif).encode()

			start_index = cluster * self.cluster_size
			end_index = start_index + data_size
			self.file_system[start_index:end_index] = data
		else:
			print("i: FiUnamFS/%s and %s are identical (not copied)." % (file,file))

	def cpo(self, file):
		print("Copy outside", file)

	def rm(self, file):
		f = self.search(file)
		if f is None:
			print('r: %s: No such file or directory' % file)
		else:
			print(f.name.decode())

	def defrag(self):
		print("defrag")

	def get_dir_entries(self, only_root=False):
		dir_entries = []
		av_dir_entries = []
		oc_data_clusters = []
		for cluster in range(self.root_dir_clusters):
			_c = 0
			for entry in range(0,self.cluster_size,64):
				_a = ((cluster+1)*self.cluster_size) + (_c*64)
				_b = _a + 64
				_c += 1
				dir_entry_data = self.file_system[_a:_b]
				file = self.f_m.get_de(data=dir_entry_data, dir_entry_id=_c-1)
				if file.name == self.root_dir_empty_entry.encode():
					av_dir_entries.append(_c-1)
				else:
					oc_data_clusters.append(int(file.cluster))
					dir_entries.append(file)
		if only_root:
			return dir_entries
		else:
			return (dir_entries, av_dir_entries, oc_data_clusters)

	def get_next_cluster(self):
		cluster = randint(self.first_data_cluster,int(self.super_block.num_clusters_unit))
		while cluster in self.occupied_data_clusters:
			cluster = randint(self.first_data_cluster,int(self.super_block.num_clusters_unit))
		return cluster

	def search(self, file):
		if self.root_dir == []:
			(self.root_dir, self.available_dir_entries, self.occupied_data_clusters) = self.get_dir_entries()		
		for f in self.root_dir:
			if f.name.decode().strip() == file:
				return f
		return None

	def __print__root(self, dir):
		for file in dir:
			print("%s" %(file.name.decode()))
