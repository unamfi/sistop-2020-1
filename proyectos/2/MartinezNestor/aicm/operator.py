from threading import Thread,Semaphore
from time import sleep
from random import randint

mutex = Semaphore(1)

class Operator(Thread):

	plane = None

	def __init__(self,id):
		Thread.__init__(self)
		self.id = id 

	def run(self):
		print(self)

	def receive_plane(self,plane,tracks):
		self.plane = plane
		sleep(0.5)
		print("\t\t\tOperator #%d now with airplane %d" % (self.id, self.plane.id))
		with mutex:			
			self.work_with_airplane(plane,tracks)

	def work_with_airplane(self,plane,tracks):
		track = tracks.pop()
		print("\t\t\tAirplane #%d is landing on track #%d" % (plane.id,track.id))
		track.receive_plane(plane)
		self.plane = None

	def with_plane(self):
		if self.plane == None:
			return False 
		else:
			return True 			

	def landing_tracks_available(self,landing_tracks):
		with mutex:
			if len(landing_tracks) > 0:
				return True 
			return False 

	def __str__(self):
		return "\t\t\tHello, I'm Operator #" + str(self.id)
