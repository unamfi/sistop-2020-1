from aicm.transport import Transport, TransportType

class Bus(Transport):	
	def __init__(self, t_id):
		self.id = t_id 
		self.transport_type = TransportType.bus
		super(Bus,self)
		