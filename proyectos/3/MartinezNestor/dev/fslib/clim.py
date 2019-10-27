from fslib.fm import FileManager
from fslib.de import DirectoryEntry

class CommandManager():

	root_dir = []
	
	def __init__(self):
		f_m = FileManager()
		self.super_block = f_m.build_sb()
		self.fs_data = f_m.get_fs_data()

	def ls(self):
		print("List")


	def cpi(self, file):
		print("Copy inside", file)

	def cpo(self, file):
		print("Copy outside", file)

	def rm(self, file):
		print("remove ", file)

	def defrag(self):
		print("defrag")
	
		