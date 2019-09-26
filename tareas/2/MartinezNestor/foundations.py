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
		print("\t%s:%d,t=%d; " % (self.name, self.arrival, self.ticks), end=e)

	def show_e(self):
		print("\t%s-> a: %d, t: %d, beg: %d, end: %d, T: %.2f, E: %.2f, P:%.2f" % (self.name, self.arrival, self.ticks, self.beginning, self.end, self.T, self.E, self.P))

	def reset(self):
		self.ticks_aux = self.ticks
		self.beginning = 0
		self.end = 0
		self.T = 0
		self.P = 0
		self.E = 0

#A class with some useful methods 
class Foundation:

	#print_p(procs: [Process]): prints all the processes inside the procs array of Process
	def print_p(self, procs, title):
		print(title)
		for i in range(len(procs)):
			e = ''
			if i == len(procs) -1:
				e = '\n'
			procs[i].show(e)

	#print_p_ext(procs: [Process]): prints all the processes inside the procs array of Process with extra information of T,P, and E parameters
	def print_p_ext(self, procs):
		for i in range(len(procs)):
			procs[i].show_e()

	#handle_results(procs: [Process]): calculates T, E, P parameters based on the modified list of processes once beginning and end parameters of each process are set
	def handle_results(self,procs,n,results):
		self.make_numbers(procs)
		(t_a, T_a, E_a, P_a) = self.get_avgs(procs)
		self.print_avgs(n,t_a, T_a, E_a, P_a)
		for i in range(len(results)):
			if i == 0:
				print("\t\t", end='')
			print(results[i], end=' ')
			if i == (len(results)-1):
				print()
		if n == "SPN":
			print()
		#Uncomment the next line to see a table of all the attributes of each process
		# self.print_p_ext(procs)
		self.clean_procs(procs)

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

	#print_avgs(name, ticks, T,E, P): prints to the console the final results for the 'n' algorithm
	def print_avgs(self,n,t,T,E,P):
		print("\n\t%s: T=%.2f, E=%.2f, P=%.2f" % (n,T,E,P))

	#gen_arrivals_ticks(procs: [Process]): generates a list of the processess' times of arrivals and number of ticks
	def gen_arrivals_ticks(self,procs):
		a = [] #times of arrivals 
		t = [] #number of ticks 
		for i in range(len(procs)):
			a.append(procs[i].arrival)
			t.append(procs[i].ticks_aux)	
		return (a,t)

	def clean_procs(self,procs):
		for i in range(len(procs)):
			procs[i].reset()










