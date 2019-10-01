from enum import Enum

class Transport(): 
	def __init__(self,t_id, transport_type):
		self.id = t_id
		self.transport_type = transport_type

	def to_landing_track(self,landing_track):
		self.landing_track = landing_track
		print("%s #%d : going to landing track #%d" % (self.transport_type.value,self.id, self.landing_track))

	def to_terminal(self,passengers):
		self.passengers = passengers
		if self.transport_type == TransportType.bus:
			print("Bus #%d : going to terminal with %d passengers" % (self.id, len(self.passengers)))
		elif self.transport_type == TransportType.scooter:
			print("Scooter #" + self.id + ": going to terminal with: " + str(passengers[0]))			
			

class TransportType(Enum):
	bus = "Bus"
	scooter = "Scooter"