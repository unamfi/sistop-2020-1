import random
from aicm.airplane import Airplane
from aicm.landing_track import LandingPriority
from aicm.operator import Operator

origin_cities = ["BUD","WSW","PRH","KRW"]
airlines = ["AeroMexico","AirCanada","Lufthansa"]
numbers = ["001","244","981","987","763","124"]
percentages = [10,20,50,60,75,80]

class AirportGenerator():	

	def __init__(self):
		pass

	def generate_planes(self,n):
		global origin_cities,airlines,numbers,percentages
		planes = []
		for i in range(n):
			c = random.randint(0,len(origin_cities)-1)
			a = random.randint(0,len(airlines)-1)
			n = random.randint(0,len(numbers)-1)
			p = random.randint(0,len(percentages)-1)
			city = origin_cities[c]
			airline = airlines[a]
			no = numbers[n]
			percentage = percentages[p]
			p = Airplane(origin=city,destination="CDMX",airline=airline,flight_no=no,fuel_percentage=percentage,passengers=[1,2,3],priority=LandingPriority.normal)
			planes.append(p)
		return planes

	def generate_operators(self,n):
		ops = []
		for i in range(n):
			operator = Operator(i+1)
			ops.append(operator)
		return ops 