from aicm.airport_helpers.helper import AirportGenerator
from time import sleep

g = AirportGenerator()

class ControlTower():

	def __init__(self,num_planes,num_ops):
		self.planes_detected = num_planes
		self.operators = g.generate_operators(num_ops)

	def detect_airplanes(self):
		print("Detecting airplanes...")
		sleep(2)
		print("Airplanes detected: %d" % self.planes_detected)
		planes = g.generate_planes(self.planes_detected)
		for p in planes:
			sleep(1)
			p.start()
		print()
		return planes

	def show_operators(self):
		for i in self.operators:
			print(i)