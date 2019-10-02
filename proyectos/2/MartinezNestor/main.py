from threading import Thread, Semaphore 
from random import randint
from time import sleep

#global array to denote the airplanes in the air
planes = []
tracks = []
operators = []

planes_landed = -1
passengersDownloaded = 0

mutex = Semaphore(1)
ops = Semaphore(0)
bus = Semaphore(0)
landingTrack = Semaphore(0)
airplane = Semaphore(1)
busBarrier = Semaphore(0)


class Passenger():
	def __init__(self,id):
		self.id = id 
class Generator():
	def __init__(self):
		pass
	def generatePassengers(self,n):
		ps = []
		for i in range(n):
			p = Passenger(i)
			ps.append(p)
		return ps 
class Plane():
	g = Generator()
	def __init__(self,id):
		self.id = id 
		self.passengers = self.g.generatePassengers(randint(1,8))
		self.fly()
	def fly(self):
		global planes_landed,planes
		while True:
			airplane.acquire()
			print(self)
			sleep(5)
			with mutex:
				if planes_landed < 5:
					planes.append(self)
					ops.release()				
		sleep(2)
	def time_to_download(self):
		time = 0 
		for p in self.passengers:
			time_of_p = 0.4 
			time += (0.2 + time_of_p)
		return time
	def __str__(self):
		return "Plane #" + str(self.id) + " is arriving with " + str(len(self.passengers)) + " passengers."
class Operator():
	def __init__(self,id):
		self.id = id 
		self.isAvailable = True
		self.plane = None
		self.work()
	def work(self):
		global planes,planes_landed
		while True:
			ops.acquire()
			with mutex:
				planes_landed += 1
				p = planes[planes_landed]
			if planes_landed < 4:
				print("Operator is now attending plane #%d" % p.id)
				sleep(2)
				landingTrack.release()
			else:
				print("\tPlane %d must wait until a landing track is available..." % p.id)
				with mutex:
					planes_landed -= 1
			with mutex:
				if planes_landed < 5:
					airplane.release()
class Track():
	def __init__(self,id):
		self.id = id 
		self.receivePlane()
	def receivePlane(self):
		global planes,planes_landed
		while True:
			landingTrack.acquire()
			sleep(2)
			with mutex:
				plane = planes[planes_landed]
			print("\tLanding track %d ready for plane %d's landing" % (self.id,plane.id))
			self.attendPlane(plane)
	def attendPlane(self,plane):
		global planes_landed,passengersDownloaded
		print("\t\t\t\tPassengers are now dowloading from plane %d" % plane.id)
		for i in plane.passengers:
			print("\t\t\t\tPassenger %d is dowloading from plane %d" % (i.id,plane.id))
			sleep(1)
			with mutex:
				passengersDownloaded += 1
			if passengersDownloaded == 10:
				bus.release()

class Bus():
	def __init__(self):
		self.leaveWithPassengers()
	def leaveWithPassengers(self):
		global passengersDownloaded
		while True:
			bus.acquire()
			print("\t\tBus is now leaving. We have %d passengers" % passengersDownloaded)
			sleep(5)
			print("\t\tArriving at terminal. %d passengers are going home." % passengersDownloaded)
			passengersDownloaded = 0



if __name__ == '__main__':
	num_planes = 5
	num_tracks = 4
	Thread(target=Operator,args=[0]).start()
	Thread(target=Bus,args=[]).start()
	for i in range(num_planes):
		Thread(target=Plane,args=[i]).start()
	for i in range(num_tracks):
		Thread(target=Track,args=[i]).start()
