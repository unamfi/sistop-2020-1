#My own implementation of the queue class 
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

#My own implementation of a process 
class Process: 

	def __init__(self, name, arrival, ticks):
		self.name = name 
		#Time of arrival 
		self.arrival = arrival 
		#Number of ticks to complete its execution
		self.ticks = ticks 
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


#A class with some useful methods 
class Foundation:

	def printProcesses(self, procs):
		for i in range(len(procs)):
			e = ''
			if i == len(procs) -1:
				e = '\n'
			procs[i].show(e)










