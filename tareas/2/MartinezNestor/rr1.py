from foundations import *

#Round Robin with quantum = 1
f = Foundation()
#proc_ready: queue of processes that are ready
proc_ready = Queue()
#proc_waiting: queue of processes that are waiting to be executed
proc_waiting = Queue()
def rr1(procs):
	global proc_ready, proc_waiting	
	#a: list of arrival times
	#t: list of ticks 
	(a,t) = genArrivalsTicks(procs) 
	#a_l: counter to indicate what process has arrived
	a_l = 0 
	#sum_t: indicates the total number of ticks the O.S. should execute
	sum_t = sum(t)
	#c: counter to indicate the current tick
	c = 0 
	while c <= sum_t:
		if a_l < len(a) and c == a[a_l]:
			p = procs[a_l]
			a_l += 1
			if proc_waiting.size() > 1:
				process_w(proc_waiting, proc_ready)
			proc_ready.enqueue(p)	
		else:
			if proc_ready.isEmpty():
				process_w(proc_waiting, proc_ready)		
		process_r(proc_ready, proc_waiting)
		if c == (sum_t-1) and proc_waiting.size() > 1:
				for i in range(proc_waiting.size()):
					p = proc_waiting.dequeue()
					if p.ticks > 0:
						eat(p)
				proc_waiting.empty()
		c += 1 

def process_w(waiting, ready):
	if waiting.isEmpty():
		pass
	else:
		p = waiting.dequeue()
		ready.enqueue(p)

def process_r(ready, waiting):
	if ready.isEmpty():
		pass
	else:
		# ready.show()
		p = ready.dequeue()
		# print("dequeueing %s" % p.name, end=' ')
		if p.ticks > 0:
			eat(p, waiting)
			# waiting.show()
			# print()

#eat(process): decrements the number of ticks and prints the process' name 
def eat(process, waiting):
	process.ticks -= 1
	print(process.name, end=' ')
	if process.ticks > 0:
		waiting.enqueue(process)

#genArrivalsTicks(procs): generates a list of the processess' times of arrivals and number of ticks
def genArrivalsTicks(procs):
	a = [] #times of arrivals 
	t = [] #number of ticks 
	for i in range(len(procs)):
		a.append(procs[i].arrival)
		t.append(procs[i].ticks)
	return (a,t)