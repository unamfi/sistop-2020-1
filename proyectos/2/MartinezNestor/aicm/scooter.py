from aicm.transport import Transport, TransportType
from threading import Thread

class Scooter(Transport,Thread):	
	def __init__(self,id):
		Thread.__init__(self)
		self.id = id
		self.transport_type = TransportType.scooter
		super(Scooter,self)
		
	def run(self):
		print(self)

	def __str__(self):
		return "\t\tScooter #" + str(self.id+1) + " ready"