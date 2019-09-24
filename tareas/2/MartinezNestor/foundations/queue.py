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
			print(self.queue[i])

	def empty(self):
		t = len(self.queue)
		for i in range(t):
			self.dequeue()


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