"""
	memory.py -> program that assigns or removes memory units to different processes
	and compacts the memory map when needed.
"""
import os
import sys
from random import randint, getrandbits
from boring import BoringHelper

class MemoryManager(object):
	"""
		MemoryManager

		Class that handles:
			1. Creation of random processes.
			2. Assigning/removing memory units from a process
			3. Compacting the memory map when needed. 
	"""

	#List that represents the current memory map
	memorymap = []
	units_available = 0
	procs = []
	b_helper = None

	def __init__(self, units, strategy=0):
		"""
			Class initializer 

			units: number of memory units the disk has
			strategy: strategy that the OS follows to assign memory units to a process
				- 0: 'mejor ajuste'
				- 1: 'primer ajuste' (not implemented yet)
				- 2: 'peor ajuste' (not implemented yet)
		"""
		self.units = units
		self.strategy = strategy
		self.memorymap = []


	def start(self, num_procs):
		"""
			This function starts the simulation:
				1. Generates 'n' number of initial processes.
					Each process has: 
						1. Letter id.
						2. Number of memory units needed
				2. Assigns the 'n' number of process to the memory map
				3. Presents the menu to the user:
					3.1 Assign memory to a new process
					3.2 Remove memory from an existing process 
		"""
		os.system('clear')
		if num_procs > self.units:
			print("Error: more processes requested than can be assigned.")
			sys.exit()
		self.b_helper = BoringHelper(num_procs=num_procs)
		self.procs = self.b_helper.generate_procs()
		self.__mmap__(procs=self.procs)
		self.__print_mmap__()
		r = ""
		while r is not "2":
			r = self.b_helper.showmenu()
			if r == "0":
				self.__assign__()
			elif r == "1":
				self.__liberate__()
		os.system('clear')

	
	"""
		Protected functions
	"""	
	def __mmap__(self, procs):
		"""
			Builds a list representing the memory map
			given a list of processes
		"""
		units_occupied = 0
		index = 0
		for proc in procs:
			units_occupied += proc.units
			if units_occupied > self.units:
				print("From proc \'%s\' until the end, there is no more memory\n" % proc.letter_id)
				self.procs = procs[0:index]
				units_occupied -= proc.units
				break
			index += 1
		self.units_available = self.units - units_occupied
		units_av = self.units_available
		#print("Disk units: %d. Oc: %d. Av: %d" % (self.units, units_occupied, self.units_available))
		for proc in self.procs:
			if units_av > 0:
				space = bool(getrandbits(1))
				if space:
					duration = randint(1, units_av)
					units_av -= duration
					self.__proc_in_mmap__(proc=None, nil=True, times=duration)
			self.__proc_in_mmap__(proc)
		self.__complete_mmap__()


	def __proc_in_mmap__(self, proc, nil=False, times=0):
		"""
			Append to the memory map 'number of units' letter_id from the process
		"""
		if nil and times > 0:
			for _ in range(times):
				self.memorymap.append('-')
		else:
			for _ in range(proc.units):
				self.memorymap.append(proc.letter_id)

	def __complete_mmap__(self):
		"""
			Adds the required '-' character to ensure memory maps has 
			'n' disk units slots.
		"""
		current = len(self.memorymap)
		if current < self.units:
			diff = self.units - current
			for _ in range(diff):
				self.memorymap.append('-')

	def __print_mmap__(self):
		""" 
			Deals with printing nicely the memory map.
		"""
		print("Asignacion actual:")
		index = 0
		for entry in self.memorymap:
			end_c = ' '
			if index == len(self.memorymap)-1:
				end_c = "\n"
			print(entry, end=end_c)
			index += 1

	def __compact__(self):
		"""
			Compacts the memory map when requested
		"""	
		self.memorymap = []
		for proc in self.procs:
			self.__proc_in_mmap__(proc)
		self.__complete_mmap__()

	def __liberate__(self):
		"""
			Liberates a process from memory.
		"""		
		sinput = input("Proceso a liberar (%s): " % self.__procs_n__())
		if sinput.isdigit() or len(sinput) < 1 or len(sinput) > 1:
			print("Solo puedo aceptar una letra")
		else:
			proc = self.__findproc__(sinput.upper())
			if proc is None:
				print("El proceso que elegiste no existe.")
			else:
				self.__removeproc__(proc=proc)
				self.__print_mmap__()


	def __assign__(self):
		"""
			Assigns disk units to a new process.
		"""
		if self.units_available < 1:
			print("No hay unidades disponibles. Intenta liberar (1) memoria.")
		else:
			nextkey = self.b_helper.nextkey(self.procs)
			uinput = input("Nuevo proceso (%s): " % nextkey)
			if uinput.isdigit():
				units = int(uinput)
				print(units)
			else:
				print("Solo puedo aceptar enteros.")

	def __findproc__(self, letter):
		"""
			Finds a process given a letter.
		"""
		for proc in self.procs: 
			if proc.letter_id == letter:
				return proc
		return None

	def __procs_n__(self):
		"""
			Returns the processes in a nicely way.
		"""
		proc_string = ""
		for proc in self.procs:
			proc_string += (proc.letter_id)
		return proc_string

	def __removeproc__(self, proc):
		"""
			Removes 'proc' process from the memory map.
		"""
		index = 0
		for p in self.procs:
			if p == proc:
				break
			index += 1
		del self.procs[index]
		index = 0
		for entry in self.memorymap:
			if entry == proc.letter_id:
				self.memorymap[index] = "-"
				self.units_available += 1
			index += 1

if __name__ == "__main__":
	#Change this parameters to modify the execution of the program
	MEM = MemoryManager(units=30, strategy=0)
	MEM.start(num_procs=5)
