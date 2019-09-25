#Implementation of the queue 
class Queue: 

	def __init__(self):
		self.queue = []

	def enqueue(self, item):
		self.queue.append(item)

	def dequeue(self):
		if len(self.queue) < 1:
			return None 
		return self.queue.pop(0)

	def isEmpty(self):
		return len(self.queue) < 1 

	def show(self):
		for i in range(len(self.queue)):
			print("...%s" % (self.queue[i].name))

	def empty(self):
		t = len(self.queue)
		for i in range(t):
			self.dequeue()

	def size(self):
		return len(self.queue)


#Some tests 
# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# queue.show()
# print("----")
# p = queue.dequeue()
# print(p)
# print("----")
# queue.show()
# print("----")
# queue.empty()
# print(queue.isEmpty())

#Implementation of a process 
class Process: 

	def __init__(self, name, arrival, ticks):
		self.name = name 
		#Time of arrival 
		self.arrival = arrival 
		#Number of ticks to complete its execution
		self.ticks = ticks 
		#Aux variable that also denotes ticks 
		self.ticks_aux = ticks 
		#Moment in time where the process begins its execution
		self.beginning = 0
		#Moment in time where the process ends its execution
		self.end = 0
		#Response time: T = end - arrival
		self.T = 0 
		#Wait time: E = T - ticks  
		self.E = 0
		#Response ratio: P = T / ticks 
		self.P = 0

	def show(self, e=''):
		print("%s: %d, t=%d;" % (self.name, self.arrival, self.ticks), end=e)

	def show_e(self):
		print("%s-> a: %d, t: %d, beg: %d, end: %d, T: %.2f, E: %.2f, P:%.2f" % (self.name, self.arrival, self.ticks, self.beginning, self.end, self.T, self.E, self.P))


#A class with some useful methods 
class Foundation:

	def print_p(self, procs):
		for i in range(len(procs)):
			e = ''
			if i == len(procs) -1:
				e = '\n'
			procs[i].show(e)

	def print_p_ext(self, procs):
		print()
		for i in range(len(procs)):
			procs[i].show_e()

	#make_numbers(procs: [Process]): calculates the T, E, P parameters of each process
	def make_numbers(self,procs):
		for i in range(len(procs)):	
			p = procs[i]
			p.T = p.end - p.arrival
			p.E = p.T - p.ticks
			p.P = p.T / p.ticks 

	#get_avgs(procs: [Process]) -> (t,T,E,P): calculates the avergaes for the T, E, P parameters of all the processeses 
	def get_avgs(self,procs):
		l = len(procs)
		sum_t = t = sum_T = T = sum_E = E = sum_P = P = 0
		for i in range(l):
			p = procs[i]
			sum_t += p.ticks
			sum_T += p.T
			sum_E += p.E
			sum_P += p.P
		return ((sum_t/l), (sum_T/l), (sum_E/l), (sum_P/l))


	#print_avgs(name, ticks, T, E, P): prints to the console the final results for the 'name' algorithm
	def print_avgs(self,n,t,T,E,P):
		print("%s: T=%.2f, E=%.2f, P=%.2f" % (n,T,E,P))









