from fslib.filemanager import FileManager

class CommandManager():
	
	def __init__(self):
		f_m = FileManager()
		self.super_block = f_m.build_sb()

	def ls(self):
		print("List")
		print(self.super_block.name)

	def cpi(self, file):
		print("Copy inside", file)

	def cpo(self, file):
		print("Copy outside", file)

	def rm(self, file):
		print("remove ", file)

	def defrag(self):
		print("defrag")
	
		