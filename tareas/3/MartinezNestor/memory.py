"""
	memory.py -> program that assigns or removes memory units to different processes
	and compacts the memory map when needed.
"""
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
		if num_procs > self.units:
			print("Error: more processes requested than can be assigned.")
			sys.exit()
		b_helper = BoringHelper(num_procs=num_procs)
		self.procs = b_helper.generate()
		self.__mmap__(procs=self.procs)
		self.__print_mmap__()
		self.__compact__()
			
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
				procs = procs[0:index]
				units_occupied -= proc.units
				break
			index += 1
		self.units_available = self.units - units_occupied
		units_av = self.units_available
		#print("Disk units: %d. Oc: %d. Av: %d" % (self.units, units_occupied, self.units_available))
		for proc in procs:
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
		print("Asignacion actual:\n\n")
		index = 0
		for entry in self.memorymap:
			end_c = ' '
			if index == len(self.memorymap)-1:
				end_c = "\n"
			print("%s %s" % (entry, end_c))
			index += 1

	def __compact__(self):
		"""
			Compacts the memory map when requested
		"""		
		self.memorymap = []
		for proc in self.procs:
			self.__proc_in_mmap__(proc)
		self.__complete_mmap__()

if __name__ == "__main__":
	#Change this parameters to modify the execution of the program
	MEM = MemoryManager(units=30, strategy=0)
	MEM.start(num_procs=3)
