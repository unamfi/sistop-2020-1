class DirectoryEntry():
	"""docstring for Dir"""
	def __init__(self, name, size, cluster, creation, last_modif, non_used_space):
		self.name = name
		self.size = size
		self.cluster = cluster
		self.creation = creation
		self.last_modif = last_modif
		self.non_used_space = non_used_space