""" proc.py -> Class definition for a Process """ 
class Process(object):
	"""
		Class that represents a simple process conforming just of:
		1. Letter id.
		2. Number of memory units. 
	"""

	#Constants representing the number of minimum and maximum units
	#each process could request. 
	MIN_UNITS = 2
	MAX_UNITS = 15

	def __init__(self, letter_id, units):		
		self.letter_id = letter_id
		self.units = units
