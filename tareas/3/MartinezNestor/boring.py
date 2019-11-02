""" boring.py -> classses needed to complete everything boring """
import sys
from random import randint
from proc import Process

class BoringHelper(object):
	"""
		Class that handles the UI menu and the generation of 'n' random process.
	"""

	alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
	            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
	            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
	            'Y', 'Z']

	def __init__(self, num_procs):
		self.num_procs = num_procs

	def generate(self):
		"""
			Generates 'num_procs' number of processes
		"""
		procs = []
		for i in range(self.num_procs):
			if i > len(self.alphabet)-1:
				print("Maximun number of generated processes has been reached(%d)" % len(self.alphabet))
				sys.exit()

			units = randint(Process.MIN_UNITS, Process.MAX_UNITS)
			letter_id = self.alphabet[i]
			proc = Process(letter_id=letter_id, units=units)
			procs.append(proc)
		return procs

	def print_mmap(self, mmap):
		""" 
			Deals with printing nicely the memory map.
		"""
		index = 0
		for entry in mmap:
			end_c = ' '
			if index == len(mmap)-1:
				end_c = "\n"
			print(entry, end=end_c)
			index += 1


