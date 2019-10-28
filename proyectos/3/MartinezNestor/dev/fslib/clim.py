from fslib.fm import FileManager
from fslib.de import DirectoryEntry

class CommandManager():

	f_m = FileManager()

	root_dir = []
	root_dir_entry_size = 64
	root_dir_empty_entry = "Xx.xXx.xXx.xXx."

	first_data_cluster = 5

	available_dir_entries = []
	
	def __init__(self):
		self.super_block = self.f_m.build_sb()
		self.cluster_size = int(self.super_block.cluster_size)
		self.root_dir_clusters = int(self.super_block.num_clusters_dir)
		self.file_system = self.f_m.get_fs()
		self.available_dir_entries = self.get_dir_entries(available=True)

	def ls(self):
		self.root_dir = self.get_dir_entries()
		self.__print__root(dir=self.root_dir)

	def cpi(self, file):
		data = open(file,'rb').read()
		dir_entry_id = self.available_dir_entries.pop(0)
		cluster = self.get_next_cluster(cluster=first_data_cluster)
		dir_entry = DirectoryEntry(name=file, size=size, cluster=cluster, creation=creation, last_modif=last_modif, non_used_space=non_used_space, dir_entry_id=dir_entry_id)

	def cpo(self, file):
		print("Copy outside", file)

	def rm(self, file):
		print("remove ", file)

	def defrag(self):
		print("defrag")

	def get_dir_entries(self, available=False):
		dir_entries = []
		av_dir_entries = []
		for cluster in range(self.root_dir_clusters):
			_c = 0
			for entry in range(0,self.cluster_size,64):
				_a = ((cluster+1)*self.cluster_size) + (_c*64)
				_b = _a + 64
				_c += 1
				dir_entry_data = self.file_system[_a:_b]
				dir_entry = self.f_m.get_de(data=dir_entry_data, dir_entry_id=_c)
				if dir_entry.name == self.root_dir_empty_entry.encode():
					av_dir_entries.append(_c)
				else:
					dir_entries.append(dir_entry)
		if available:
			return av_dir_entries
		else:
			return dir_entries

	def get_next_cluser(self, cluster):
		pass


	def __print__root(self, dir):
		for file in dir:
			print("%s" %(file.name.decode()))
