class DirectoryEntry():
	"""docstring for Dir"""
	def __init__(self, file_name, file_size, cluster, creation, last_modif, non_used_space):
		self.file_name = file_name
		self.file_size = file_size
		self.cluster = cluster
		self.creation = creation
		self.last_modif = last_modif
		self.non_used_space = non_used_space