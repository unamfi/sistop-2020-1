from threading import Thread


class Operator(Thread):

	def __init__(self,id):
		Thread.__init__(self)
		self.id = id 

	def run():
		

	def __str__(self):
		return "Hello, I'm Operator #" + str(self.id)
