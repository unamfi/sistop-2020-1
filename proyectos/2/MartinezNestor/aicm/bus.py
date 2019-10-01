from aicm.transport import Transport, TransportType

class Bus(Transport):	
	def __init__(self,id):
		self.id = id
		self.transport_type = TransportType.bus
		super(Bus,self)
		