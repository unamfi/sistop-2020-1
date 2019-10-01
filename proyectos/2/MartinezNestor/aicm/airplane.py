from threading import Thread
from aicm.landing_track import LandingPriority

""" Class that represents the implementation of an Airplane. """
class Airplane(Thread):
	"""__init__(self, ): """
	def __init__(self, origin, destination, airline, flight_no, fuel_percentage, passengers, priority):
		Thread.__init__(self)
		self.origin = origin 
		self.destination = destination
		self.airline = airline 
		self.flight_no = flight_no
		self.fuel_percentage = fuel_percentage
		self.passengers = passengers
		self.download_time = -1
		self.landing_track = -1 
		self.landing_priority = priority

	def run(self):
		print(self)

	def __str__(self):
		return "No: " + self.flight_no + " Airline: " + self.airline + " Origin: " + self.origin + " Destination: " + self.destination + " Fuel percentage: " + str(self.fuel_percentage) + "% Passengers: " + str(len(self.passengers))

