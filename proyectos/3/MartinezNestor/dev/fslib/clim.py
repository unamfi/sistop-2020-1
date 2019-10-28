from fslib.fm import FileManager
from fslib.de import DirectoryEntry

class CommandManager():

	f_m = FileManager()

	sector_size = 512
	cluster_size = 512 * 4

	root_dir = []
	root_dir_clusters = 4
	root_dir_entry_size = 64
	root_dir_empty_entry = "Xx.xXx.xXx.xXx."
	
	def __init__(self):
		self.super_block = self.f_m.build_sb()
		self.file_system = self.f_m.get_fs()

	def ls(self):
		for cluster in range(self.root_dir_clusters):
			_c = 0
			for entry in range(0,self.cluster_size,64):
				_a = ((cluster+1)*self.cluster_size) + (_c*64)
				_b = _a + 64
				_c += 1
				data = self.file_system[_a:_b]
				dir_entry = self.f_m.get_de(data)
				if dir_entry.name == self.root_dir_empty_entry.encode():
					pass
				else:
					self.root_dir.append(dir_entry)
		self.__print__root(dir=self.root_dir)

	def cpi(self, file):
		print("Copy inside", file)

	def cpo(self, file):
		print("Copy outside", file)

	def rm(self, file):
		print("remove ", file)

	def defrag(self):
		print("defrag")

	def __print__root(self, dir):
		for file in dir:
			print(file.name.decode(), end='\t')
