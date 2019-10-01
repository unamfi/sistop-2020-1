from aicm.transport import Transport, TransportType

class Scooter(Transport):	
	def __init__(self, t_id):
		self.id = t_id 
		self.transport_type = TransportType.scooter
		super(Scooter,self)
		