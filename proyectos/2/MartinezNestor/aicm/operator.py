from threading import Thread,Semaphore
from time import sleep
from random import randint
from aicm.general import planes,landing_tracks,track
from aicm.landing_track import LandingTrack

mutex = Semaphore(1)

active_landing_tracks = -1

class Operator(Thread):	
	
	is_busy = False
	plane = None

	def __init__(self,id):
		Thread.__init__(self)
		self.id = id 

	def run(self):	
		global active_landing_tracks
		while len(planes) > 0:
			if self.is_busy:
				self.is_busy = False
			else:
				self.is_busy = True
				with mutex:
					self.plane = planes.pop()
				print("\t\t\tOperator #%d working with plane #%d. [%d] planes in air." % (self.id,self.plane.id,len(planes)+1))
				with mutex:
					if active_landing_tracks < 4:
						active_landing_tracks += 1
					if active_landing_tracks == 4:
						print("Landing tracks are busy, wait...")
						planes.append(self.plane)
					else:
						track.release()
				sleep(2)
				if len(planes) == 0:
					self.is_busy = True

		# print("\t\t\t[%d] planes in air." % (len(planes)))
		# print("\t\t\tOperator #%d working with plane #%d. [%d] planes in air." % (self.id,self.plane.id,len(planes)))
		# print("\t\t\tOperator #%d has finished working..." % self.id)
	

	def assign_plane(self,plane,d):
		self.is_busy = True
		self.plane = plane
		print("\t\t\tOperator #%d working with plane #%d. [%d] planes in air." % (self.id,self.plane.id,len(planes)))
		sleep(d)
		self.plane = None

	def busy(self):
		self.is_busy = False
		print("\t\tOperator #%d busy..." % self.id)

	def receive_plane(self,plane,tracks):
		self.plane = plane
		sleep(0.5)
		print("\n\t\t\tOperator #%d now with airplane %d" % (self.id, self.plane.id))
		with mutex:			
			self.work_with_airplane(plane,tracks)

	def work_with_airplane(self,plane,tracks):
		track = tracks.pop()
		print("\t\t\tAirplane #%d is landing on track #%d" % (plane.id,track.id))
		track.receive_plane(plane)
		self.plane = None
		tracks.append(track)		

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

	def redirect(self,plane):
		print("Redirecting plane")

	def __str__(self):
		return "\t\t\tHello, I'm Operator #" + str(self.id)
