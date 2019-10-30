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
	middle_clusters = {}
	#List of DirectoryEntry representing all the root dir 
	#entries that are not in their correct positions
	wanderers = [] 
	direntry_tomove = None

	used_dataclusters = []
	
	def __init__(self):
		self.superblock = self.f_m.build_sb()
		self.file_system = self.f_m.get_fs()

		self.cluster_size = int(self.superblock.cluster_size)
		self.root_dir_clusters = int(self.superblock.num_clusters_dir)
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

			(self.root_dir, self.unused_dir_entries) = self.__readdir__()
			self.__update_dc_()
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
			cluster = int(f.cluster.decode())
			dir_entry_id = f.dir_entry_id
			self.unused_dir_entries.append(dir_entry_id)
			start_index = cluster * self.cluster_size
			end_index = start_index + int(f.size.decode())
			index = self.cluster_size + (dir_entry_id * self.root_dir_entry_size)
			self.file_system[index:index+15] = ('%15s' % self.rootdir_empty_entry).encode()
			self.file_system[index+16:index+24] = ('%08d' % 0).encode()
			self.file_system[index+25:index+30] = ('%05d' % 0).encode()
			self.file_system[index+31:index+45] = ('%014d' % 0).encode()
			self.file_system[index+46:index+60] = ('%014d' % 0).encode()
			for i in range(start_index,end_index,2):
				self.file_system[i:i+1] = ('%01d' % 0).encode()
			(self.root_dir, self.unused_dir_entries) = self.__readdir__()
			self.used_dataclusters.remove(cluster)

	def defrag(self):
		print("Current dir distribution")
		self.track()
		print("\nNew dir distribution\n")
		self.__update_dc_()
		something = self.__findhole__()
		while something is not None:
			top = something[0]
			nxt = something[1]
			direntry = self.__fetch_direntry__(nxt)
			self.__move__(direntry=direntry, to=top+1)
			(self.root_dir, self.unused_dir_entries) = self.__readdir__()
			something = self.__findhole__()			
		self.track()
		

	def __fetch_direntry__(self, entryid):
		for entry in self.root_dir:
			if int(entry.cluster.decode()) == entryid:
				return entry
				break
		print("No direntry with %d id" % entryid)


	def track(self):
		self.__print__root(dir=self.root_dir, track=True)


	"""
		CommandManager's protected functions

	"""
	def __readdir__(self, only_root=False):
		"""
			__readdir__ 

				only_root: Bool
					flag to return only the root dir entries 

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
					dir_entries.append(dir_entry)

		self.__update_dc_()
		if only_root:
			return dir_entries
		return (dir_entries, unused_dir_entries)

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
		if size == 0 and random and odc is not None:
			for i in range(1, len(odc) - 1):
				if odc[i] - odc[i-1] > 1:				
					return i + self.first_data_cluster
		else:
			cluster = randint(self.first_data_cluster, int(self.superblock.num_clusters_unit))
			clusters = []
			_r = size / self.cluster_size
			if _r > 1:
				_x = size // self.cluster_size
				for i in range(_x+1):
					clusters.append(i)
			else:
				clusters.append(0)

			for _c in clusters:
				while (cluster+_c) in self.occupied_data_clusters.keys():
					cluster = randint(self.first_data_cluster, int(self.superblock.num_clusters_unit))
			return cluster

	def __update_dc_(self):
		dataclusters = []
		for entry in self.root_dir:
			offset = int(entry.cluster.decode())
			currentcluster = 0
			for cluster in range(entry.needed_clusters(self.cluster_size)):
				dataclusters.append(offset + currentcluster)
				currentcluster += 1
		self.used_dataclusters = sorted(dataclusters)

	def __findhole__(self):
		"""
			Finds available disk space and returns a tuple.
		"""
		space = None
		for i in range(1,len(self.used_dataclusters)):
			current_cluster = self.used_dataclusters[i]
			prev_cluster = self.used_dataclusters[i-1]
			diff = current_cluster - prev_cluster
			if diff > 1:
				return (prev_cluster, current_cluster)
		return space 

	def __move__(self, direntry, to):
		data_to_move = self.__fetch__(direntry)
		self.__update__rootdir__(direntry=direntry, newcluster=to)
		start_index = int(direntry.cluster.decode()) * self.cluster_size
		end_index = start_index + (len(data_to_move))		
		self.file_system[start_index:end_index] = data_to_move

	def __fetch__(self, direntry):
		initial_cluster = int(direntry.cluster.decode())
		start_index = initial_cluster * self.cluster_size
		end_index = start_index + int(direntry.size.decode())
		return self.file_system[start_index: end_index]

	def __update__rootdir__(self, direntry, newcluster):
		found = False
		for entry in self.root_dir:			
			if entry.name == direntry.name:
				entry.update_cluster(newcluster)
				index = self.cluster_size + (direntry.dir_entry_id * self.root_dir_entry_size)
				self.file_system[index+25:index+30] = ('%05d' % newcluster).encode()
				found = True
		if not found:
			print("Invalid directory entry")

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