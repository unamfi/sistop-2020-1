from threading import Thread,Semaphore
from aicm.airport_generator import AirportGenerator
from time import sleep

g = AirportGenerator()
#Signal pattern to wake up control tower operators 
wake_up = Semaphore(0)
mutex = Semaphore(1)


class ControlTower(Thread):

	operators = []

	def __init__(self,num_planes,num_ops):
		Thread.__init__(self)
		self.num_planes = num_planes
		self.num_ops = num_ops	

	def run(self):
		self.initialize_operators()	

	def detect_airplanes(self):
		print("Control tower looking for airplanes...")
		sleep(2)
		print("Airplanes detected: %d" % self.num_planes)		
		return g.generate_planes(self.num_planes)		

	def initialize_operators(self):
		self.operators = g.generate_operators(self.num_ops)
		for o in self.operators:
			wake_up.acquire()
			o.start()

	def wake_up_operators(self):
		print("\t\t\tIn the meantime, let's wake up the operators:")
		sleep(1)
		for o in self.operators:
			wake_up.release()

	def assign_planes(self,planes):
		for o in self.operators:
			if o.with_plane():
				print("\t\t\tOperator %d is busy with airplane %d" % (o.id, o.plane.id))
			else:
				if len(planes) > 0:
					self.assign_plane(planes,o)

	def assign_plane(self,planes,operator):
		with mutex:
			p = planes.pop()
			sleep(1.5)
			operator.receive_plane(p)
			print("\t\t\t\tRemaining planes in the air: %d" % len(planes))
