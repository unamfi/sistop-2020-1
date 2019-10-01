from enum import Enum

class LandingTrack():

	def __init__(self,id):
		self.id = id 


class LandingPriority(Enum):
	normal = 0
	urgent = 1