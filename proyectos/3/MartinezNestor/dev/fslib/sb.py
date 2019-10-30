class SuperBlock(object):
	"""docstring for SuperBlock"""
	def __init__(self, name, version, label, cluster_size, num_clusters_dir, num_clusters_unit):
		"""docstring"""
		self.name = name
		self.version = version
		self.label = label
		self.cluster_size = cluster_size
		self.num_clusters_dir = num_clusters_dir
		self.num_clusters_unit = num_clusters_unit