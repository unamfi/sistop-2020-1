from aicm.transport import Transport, TransportType
from threading import Thread

class Bus(Transport,Thread):	
	def __init__(self,id):
		Thread.__init__(self)
		self.id = id
		self.transport_type = TransportType.bus
		super(Bus,self)

	def run(self):
		print(self)

	def __str__(self):
		return "\t\tBus #" + str(self.id+1) + " ready"		
			
		