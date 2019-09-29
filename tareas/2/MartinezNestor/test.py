from random import randint
from foundations import *
from fcfs import *
from rr1 import *
from rr4 import *
from spn import *

#Helper class 
f = Foundation()

#Custom class to provide different processess implementations 
class Test:

	def __init__(self):
		#low and high are integer variables used to determine random values: they can be any "small" integer value except 0.
		self.low = 1
		self.high = 5
	
	#initial_test(): generates a the first data set of problems from Chapter4 of "Fundamentos de Sistemas Operativos" by Gunnar Wolf
	def initial_test(self):
		a = Process("A",0,3)
		b = Process("B",1,5)
		c = Process("C",3,2)
		d = Process("D",9,5)
		e = Process("E",12,5)
		return self.t_procs(0,[a,b,c,d,e])		

	#random_tests(): generates data sets with a random amount of arrival times and number of ticks per process. 
	def random_test(self,id):
		low = self.low
		high = self.high
		a = Process("A",0,randint(low,high))
		b = Process("B",randint(low,high),randint(low,high))
		c = Process("C",randint(low,high),randint(low,high))
		d = Process("D",randint(low,high),randint(low,high))
		e = Process("E",randint(low,high),randint(low,high))
		return self.t_procs(id+1,[a,b,c,d,e])

	#t_procs(round_id: Int, procs: [Process]): transforms the generated list of Process into a list ready to process
	def t_procs(self, round_id, procs):
		total = 0
		for i in range(len(procs)):
			total += procs[i].ticks
		f.print_p(procs,"Ronda %d: -> total(%d)" % (round_id,total))
		procs.sort(key=lambda x: x.arrival)
		return procs 

	#run_algorithms(procs: [Process]): 
	def run_algorithms(self,procs):
		#First Come First Served
		fcfs(procs)
		#Round Robin with quantum = 1
		rr1(procs)
		#Round Robin with quantum = 4
		rr4(procs,4)
		#Shortest Process Next 
		spn(procs)