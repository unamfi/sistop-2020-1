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
		self.passengers = self.g.generatePassengers(randint(1,5))
		self.fly()
	def fly(self):
		global planes
		while True:
			airplane.acquire()
			print(self)
			sleep(1)
			with mutex:
				if len(planes) < 5:
					planes.append(self)
					ops.release()
				else:
					airplane.release()
		sleep(2)
	def time_to_download(self):
		time = 0 
		for p in self.passengers:
			time_of_p = 0.4 
			time += (0.2 + time_of_p)
		return time
	def __str__(self):
		return "Plane #" + str(self.id) + " with " + str(len(self.passengers)) + " passengers."
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
				print("\tOperator is now attending plane #%d" % p.id)
				landingTrack.release()
			else:
				print("\tPlane %d must wait until a landing track is available..." % plane.id)
				with mutex:
					planes_landed -= 1
			with mutex:
				if planes_landed < 5:
					airplane.release()
class Bus():
	def __init__(self):
		self.leaveWithPassengers()
	def leaveWithPassengers(self):
		global passengersDownloaded
		while True:
			bus.acquire()
			print("\t\t\tBus is now leaving. We have %d passengers" % passengersDownloaded)
			passengersDownloaded = 0
			sleep(5)
			print("\t\t\tArriving at terminal")
class Track():
	def __init__(self,id):
		self.id = id 
		self.receivePlane()
	def receivePlane(self):
		global planes,planes_landed
		while True:
			landingTrack.acquire()
			with mutex:
				plane = planes[planes_landed]
			print("\t\t\tLanding track %d ready for plane %d's landing" % (self.id,plane.id))
			self.attendPlane(plane)
			planes_landed -= 1
	def attendPlane(self,plane):
		global passengersDownloaded
		print("Passengers are now dowloading from plane %d" % plane.id)
		for i in plane.passengers:
			print("\tPassenger %d is dowloading from plane %d" % (i.id,plane.id))
			# plane.passengers.remove(i)
			sleep(0.4)
			with mutex:
				passengersDownloaded += 1
			if passengersDownloaded == 30:
				print("\t\t\tasfasdfasd")
				bus.release()




if __name__ == '__main__':
	num_planes = 5
	num_tracks = 4
	Thread(target=Operator,args=[0]).start()
	Thread(target=Bus,args=[]).start()
	for i in range(num_planes):
		Thread(target=Plane,args=[i]).start()
	for i in range(num_tracks):
		Thread(target=Track,args=[i]).start()
