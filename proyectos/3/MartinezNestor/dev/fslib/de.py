class DirectoryEntry():
	"""docstring for Dir"""
	def __init__(self, filename, filesize, cluster, creation, last_modif):
		self.filename = filename
		self.filesize = filesize
		self.cluster = cluster
		self.creation = creation
		self.last_modif = last_modif
		