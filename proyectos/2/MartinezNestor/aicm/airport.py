from time import sleep
from os import system, name
from threading import Thread,Semaphore
from aicm.airplane import Airplane
from aicm.airport_generator import AirportGenerator
from aicm.control_tower import ControlTower
from aicm.landing_track import LandingTrack,LandingPriority
from aicm.scooter import Scooter
from aicm.bus import Bus



g = AirportGenerator()
mutex = Semaphore(1)

class Airport(Thread): 

	planes = []
	passengers = []
	landing_tracks = []
	buses = []
	scooters = []

	def __init__(self,name,city,n_tracks,n_buses,n_scooters,num_planes,num_operators):
		global landing_tracks, buses, scooters
		Thread.__init__(self)
		self.name = name
		self.city = city		
		self.tower = ControlTower(num_planes,num_operators)
		self.landing_tracks = g.generate_landing_tracks(n_tracks)
		self.buses = g.generate_buses(n_buses)
		self.scooters = g.generate_scooters(n_scooters)

	def run(self):
		global planes 
		# self.start_simulation()
		self.tower.start()
		with mutex:
			self.planes = self.tower.detect_airplanes()
			self.tower.wake_up_operators()
			while len(self.planes) > 0:
				sleep(2)
				print("\nAirplanes in the air waiting for landing track: %d" % len(self.planes))
				self.show_planes()
				if len(self.planes) > 1:
					sleep(1)
					print("\n\t\t\tAssigning airplanes to operators...")
					sleep(2)
					self.tower.assign_planes(self.planes,self.landing_tracks)
				sleep(5)

			
	def show_planes(self):
		for p in self.planes:
			sleep(1)
			print(p)

	def start_simulation(self):
		print("Starting simulation...")
		sleep(1)
		for i in range(3,0,-1):
			print("%d ..." % (i))
			sleep(1)
		if name == 'nt':
			_ = system('cls')
		else:
			_ = system('clear')
		print(self)

	def __str__(self):
		return "Welcome to " + self.city + "'s international airport " + self.name + "\n"

