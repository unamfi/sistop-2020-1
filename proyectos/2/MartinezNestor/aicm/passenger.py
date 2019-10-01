from enum import Enum

class Passenger():

	def __init__(self, name, age, origin, destiny, passenger_type):
		self.name = name
		self.age = age 
		self.origin = origin 
		self.destiny = destiny
		self.passenger_type = passenger_type

	def time_to_download():
		if self.passenger_type == PassengerType.child:
			return 0.3
		elif self.passenger_type == PassengerType.adult:
			return 0.1
		else:
			return 0.5


class PassengerType(Enum):
	child = "Child"
	adult = "Adult"
	old = "Old"