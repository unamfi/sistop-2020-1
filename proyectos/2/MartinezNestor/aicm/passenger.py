from enum import Enum

class Passenger():

	def __init__(self, name, age, origin, destiny, passenger_type):
		self.name = name
		self.age = age 
		self.origin = origin 
		self.destiny = destiny
		self.passenger_type = passenger_type


class PassengerType(Enum):
	child = "Child"
	adult = "Adult"
	old = "Old"