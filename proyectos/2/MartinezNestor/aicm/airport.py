from time import sleep
from os import system, name
from threading import Thread
from aicm.airplane import Airplane
from aicm.control_tower import ControlTower
from aicm.landing_track import LandingTrack,LandingPriority
from aicm.scooter import Scooter
from aicm.bus import Bus

planes = []
passengers = []

class Airport(Thread): 
	def __init__(self,name,city,n_tracks,n_buses,n_scooters,num_planes,num_operators):
		global passengers
		Thread.__init__(self)
		self.name = name
		self.city = city
		self.tracks = n_tracks
		self.buses = n_buses
		self.scooters = n_scooters
		self.tower = ControlTower(num_planes,num_operators)
		self.passengers = passengers

	def run(self):
		global planes 
		self.start_simulation()
		planes = self.tower.detect_airplanes() 	

			
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

