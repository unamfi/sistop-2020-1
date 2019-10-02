from threading import Thread
from enum import Enum
from time import sleep
from aicm.general import landing_tracks,track


class LandingTrack(Thread):

	plane = None

	def __init__(self,id):
		Thread.__init__(self)
		self.id = id 

	def run(self):
		track.acquire()
		print("LR %d" % self.id)
		sleep(1)


	def is_available(self):
		if self.plane == None:
			return True 
		else:
			return False 

	def receive_plane(self,plane):
		if self.plane == None:
			self.plane = plane
		time = plane.time_to_download()
		print("\nLanding track #%d receiving plane %d" % (self.id,plane.id))
		print("Calling a bus")
		print("Plane downloading passengers...")
		plane.passengers = []
		sleep(time)

	def time_to_become_available(self):
		if self.plane != None:
			return self.plane.time_to_download()

	def __str__(self):
		return "\t\tLanding track #" + str(self.id+1) + " ready."


class LandingPriority(Enum):
	normal = 0
	urgent = 1