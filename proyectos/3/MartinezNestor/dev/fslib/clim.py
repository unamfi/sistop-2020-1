"""docstring"""
import os
from datetime import datetime
from random import randint
from fslib.fm import FileManager


class CommandManager():

	f_m = FileManager()

	root_dir = []
	root_dir_entry_size = 64
	rootdir_empty_entry = "Xx.xXx.xXx.xXx."

	unused_dir_entries = []
	occupied_data_clusters = {}
	
	def __init__(self):
		self.super_block = self.f_m.build_sb()
		self.file_system = self.f_m.get_fs()

		self.cluster_size = int(self.super_block.cluster_size)
		self.root_dir_clusters = int(self.super_block.num_clusters_dir)
		self.first_data_cluster = self.root_dir_clusters + 1
		
		(self.root_dir, self.unused_dir_entries) = self.__readdir__()

	def ls_(self):	
		self.__print__root(dir=self.root_dir)

	def cpi(self, file):
		if self.__search__(file) is None:
			data = open(file,'rb').read()
			data_size = len(data)
			dir_entry_id = self.unused_dir_entries.pop(0)

			name = file
			size = data_size
			cluster = self.__nxtcluster__(size)

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

			self.__update_datac__(rdentry_cluster=cluster, rdentry_size=size)
		else:
			print("i: FiUnamFS/%s and %s are identical (not copied)." % (file,file))

	def cpo(self, file):
		file_to_copy = self.__search__(file)		
		exists_in_current_dir = False
		cpodir_name = 'cpo_files'
		cpodir = './%s' %cpodir_name
		if not os.path.exists(cpodir):
			os.makedirs(cpodir)

		if file_to_copy is None: 
			print('o: %s: No such file or directory' % file)
		else:
			ftc_title = file_to_copy.name.decode().strip()
			currentdir = os.listdir('./%s' % cpodir_name)
			for file in currentdir:			
				root = ('./%s/' % cpodir_name)	
				if root + ftc_title == root + file:
					exists_in_current_dir = True 
					break
			if exists_in_current_dir:
				print("o: %s and FiUnamFS/%s are identical (not copied)." % (root + file,file))
			else:
				ftc_cluster = int(file_to_copy.cluster.decode())
				ftc_size = int(file_to_copy.size.decode())
				start_index = ftc_cluster*self.cluster_size
				end_index = start_index + ftc_size
				ftc_data = self.file_system[start_index:end_index].decode()

				path = './%s/%s' % (cpodir_name, ftc_title)
				newfile = open(path,'w')
				newfile.write(ftc_data)
				newfile.close()

	def rm(self, file):
		f = self.__search__(file)
		if f is None:
			print('r: %s: No such file or directory' % file)
		else:
			dir_entry_id = f.dir_entry_id
			self.unused_dir_entries.append(dir_entry_id)
			start_index = int(f.cluster.decode()) * self.cluster_size
			end_index = start_index + int(f.size.decode())
			index = self.cluster_size + (dir_entry_id * self.root_dir_entry_size)
			self.file_system[index:index+15] = ('%15s' % self.rootdir_empty_entry).encode()
			self.file_system[index+16:index+24] = ('%08d' % 0).encode()
			self.file_system[index+25:index+30] = ('%05d' % 0).encode()
			self.file_system[index+31:index+45] = ('%014d' % 0).encode()
			self.file_system[index+46:index+60] = ('%014d' % 0).encode()
			for i in range(start_index,end_index,2):
				self.file_system[i:i+1] = ('%01d' % 0).encode()

	def defrag(self):
		print("Current dir distribution")
		self.track()
		print("\nNew dir distribution\n")

		odc = sorted(self.occupied_data_clusters.keys())
		nxtcluster = self.__nxtcluster__(random=True, odc=odc)

		# self.track()

	def track(self):
		self.__print__root(dir=self.root_dir, track=True)


	"""
		Protected functions

	"""

	def __readdir__(self, only_root=False, update_dc=False):
		"""
			__readdir__ 

				only_root: Bool
					flag to return only the root dir entries 

				update_dc: Bool
					flag that makes __readdir__ returns nothing.
					This flag is used to update the data clusters.

				-> dir_entries: <List>
					list of the current entries on FiUnamFS's root dir.
								
				-> unused_dir_entries: <List>
					list of the unused entries on FiUnamFS's root dir.

			Reads through FiUnamFS's root dir clusters (1-4 version 0.7) 
			in order to get the entries of the root dir and the unused
			dir entries.
		"""
		dir_entries = []
		unused_dir_entries = []

		for cluster in range(self.root_dir_clusters):
			dir_entry_id = 0
			for _ in range(0,self.cluster_size,64):
				start_index = ((cluster+1)*self.cluster_size) + (dir_entry_id*64)
				end_index = start_index + 64
				dir_entry_id += 1

				data = self.file_system[start_index:end_index]

				dir_entry = self.f_m.direntry(data=data, dir_entry_id=dir_entry_id-1)

				if dir_entry.name == self.rootdir_empty_entry.encode():
					unused_dir_entries.append(dir_entry_id-1)
				else:
					rde_cluster = int(dir_entry.cluster)
					rde_size = int(dir_entry.size.decode())

					self.__update_datac__(rdentry_cluster=rde_cluster, rdentry_size=rde_size)
					dir_entries.append(dir_entry)

		if only_root:
			return dir_entries
		elif update_dc:
			return None
		return (dir_entries, unused_dir_entries)

	def __update_datac__(self, rdentry_cluster, rdentry_size):
		"""
			__update_datac__

				rdentry_cluster: Int 
					root dir entry initial cluster

				rdentry_size: Int
					root dir entry file size

			Updates occupied data cluster dictionary. If a
			root dir entry has a value of 'c' as it's inital
			data cluster and a value of 's' as it's file size,
			then, this function updates the occupied data 
			cluster dictionary to add the necesary keys (each
			key in the dictionary represents a cluser) that the
			root dir entry needs to occupy the necessary 'n' 
			clusters determined by it's size 's'.

		"""
		needed_clusters = rdentry_size // self.cluster_size
		for i in range(needed_clusters):
			self.occupied_data_clusters[rdentry_cluster+i] = self.cluster_size

		remaning_bytes = rdentry_size - (needed_clusters * self.cluster_size)
		if remaning_bytes > 0:			
			self.occupied_data_clusters[rdentry_cluster + needed_clusters] = remaning_bytes
		

	def __nxtcluster__(self, size=0, random=False, odc=None):
		"""
			__nxtcluster__

				size: Int
					Size of an 'f' file.

				random: Bool
					Flag to indicate if the returned cluster should be a 
					random integer withing the superblock's data clusters.

				odc: <List>
					List of the occupied data clusters.

				-> cluster: Int
					Available data cluster. 


			Returns an available data cluster based on the current list 
			of the occupied data clusters and the file size.

		"""
		self.__readdir__(update_dc=True)

		if size == 0 and random and odc is not None:
			for i in range(1, len(odc) - 1):
				if odc[i] - odc[i-1] > 1:				
					return i + self.first_data_cluster
		else:
			cluster = randint(self.first_data_cluster, int(self.super_block.num_clusters_unit))
			clusters = []
			_r = size / self.cluster_size
			if _r > 1:
				_r = size // self.cluster_size
				for i in range(_r+1):
					clusters.append(i)
			elif _r == 1:
				clusters.append(0)

			for _c in clusters:
				while (cluster+_c) in self.occupied_data_clusters.keys():
					cluster = randint(self.first_data_cluster, int(self.super_block.num_clusters_unit))
			return cluster

	def __search__(self, file):
		if self.root_dir == []:
			(self.root_dir, self.unused_dir_entries, self.occupied_data_clusters) = self.__readdir__()		
		for f in self.root_dir:
			if f.name.decode().strip() == file:
				return f
		return None

	def __print__root(self, dir, track=False):
		for file in dir:
			if track:
				print("%s \tcluster: %d \tsize: %d bytes" %(file.name.decode(), int(file.cluster.decode()), int(file.size.decode())))
			else:
				print("%s" %(file.name.decode()))

