from threading import Thread, Semaphore
from aicm.landing_track import LandingPriority
from time import sleep
from aicm.airport_generator import AirportGenerator
from aicm.general import planes

g = AirportGenerator()

""" Class that represents the implementation of an Airplane. """
class Airplane(Thread):
	"""__init__(self, ): """
	# def __init__(self,p_id, origin, destination, airline, flight_no, fuel_percentage, passengers, priority):
	# 	Thread.__init__(self)
	# 	self.id = p_id
	# 	self.origin = origin
	# 	self.destination = destination
	# 	self.airline = airline 
	# 	self.flight_no = flight_no
	# 	self.fuel_percentage = fuel_percentage
	# 	self.passengers = passengers
	# 	self.download_time = -1
	# 	self.landing_track = -1 
	# 	self.landing_priority = priority
	def __init__(self,id):
		Thread.__init__(self)
		self.id = id
		self.landed = False
		self.origin = g.generate_origin()
		self.destination = "CDMX"
		self.fuel_percentage = g.generate_fuel_percentage()
		self.passengers = g.generate_passengers(self.origin,self.destination)

	def run(self):
		pass
		# while self.landed == False:
		# 	with mutex:
		# 		if self.landed == False:
		# 			print("\t" + str(self))
		# 	sleep(10)

	def __str__(self):
		# return "Airplane #" + str(self.id) + " No: " + self.flight_no + " Airline: " + self.airline + " Origin: " + self.origin + " Destination: " + self.destination + " Fuel percentage: " + str(self.fuel_percentage) + "% Passengers: " + str(len(self.passengers))
		return "Airplane #" + str(self.id)

	def time_to_download(self):
		#0.2 seconds per passengers
		time = 0 
		for p in self.passengers:
			time_of_p = 0.4 #p.time_to_download()
			time += (0.2 + time_of_p)
		return time


