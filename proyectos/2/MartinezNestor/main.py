from aicm.airplane import Airplane
from aicm.operator import Operator
from aicm.landing_track import LandingTrack
from threading import Semaphore
from aicm.general import planes,landing_tracks
from time import sleep
from random import randint

operators = []
m = Semaphore(1)

def main():
	global planes, operators
	# a = Airport("AICM: Benito Juárez", "Mexico City", n_tracks=4, n_buses=4, n_scooters=10,num_planes=5,num_operators=3)
	# a.simulate()

	generate_planes()
	generate_operators()
	generate_landing_tracks()

	start(planes)
	start(operators)
	start(landing_tracks)

def generate_planes():
	global planes
	for i in range(5):
		plane = Airplane(i)
		planes.append(plane)

def generate_operators():
	global operators
	for i in range(3):
		operator = Operator(i)
		operators.append(operator)

def generate_landing_tracks():
	global landing_tracks
	for i in range(4):
		l = LandingTrack(i)
		landing_tracks.append(l)

def start(items):
	for i in range(len(items)):
		item = items[i]
		item.start()


if __name__ == "__main__":
	main()