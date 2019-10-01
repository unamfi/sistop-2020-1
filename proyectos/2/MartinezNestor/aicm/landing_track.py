from threading import Thread
from enum import Enum

class LandingTrack(Thread):

	plane = None

	def __init__(self,id):
		Thread.__init__(self)
		self.id = id 

	def run(self):
		print(self)

	def is_available(self):
		if self.plane == None:
			return True 
		else:
			return False 

	def receive_plane(self,plane):
		if self.plane == None:
			self.plane = plane
		print("receivin plane")

	def time_to_become_available(self):
		if self.plane != None:
			return self.plane.time_to_download()

	def __str__(self):
		return "\t\tLanding track #" + str(self.id+1) + " ready."


class LandingPriority(Enum):
	normal = 0
	urgent = 1