from foundations import *

f = Foundation()
#proc_ready: queue of processes that are ready
proc_ready = Queue()
#proc_waiting: queue of processes that are waiting to be executed
proc_waiting = Queue()
i = 0
#array of results
results = []
#rr1(procs: [Process]): round Robin with quantum = 1
def rr4(procs,q):
	global proc_ready, proc_waiting,c,results
	#a: list of arrival times
	#t: list of ticks 
	(a,t) = f.gen_arrivals_ticks(procs) 
	#a_l: counter to indicate what process has arrived
	a_l = 0 
	#sum_t: indicates the total number of ticks the O.S. should execute
	sum_t = sum(t)
	#c: counter to indicate the current tick
	c = 0 
	while c <= sum_t:
		if a_l < len(a) and c >= a[a_l]:
			p = procs[a_l]
			a_l += 1
			if proc_ready.isEmpty() and proc_waiting.isEmpty():
				proc_ready.enqueue(p)
			else:
				proc_waiting.enqueue(p)
				process_w(proc_waiting, proc_ready)
		else:
			if proc_waiting.isEmpty():
				pass 
			else:
				process_w(proc_waiting,proc_ready)
		process_r(proc_ready, proc_waiting,q,c)
		c += 1 
	f.handle_results(procs,"RR4",results)

#process_w(waiting: Queue, ready: Queue): move a process from the waiting queue to the ready queue
def process_w(waiting, ready):
	if waiting.isEmpty():
		pass
	else:
		if ready.isEmpty():
			p = waiting.dequeue()
			ready.enqueue(p)

#process_r(ready: Queue, waiting: Queue, c: Int): works with the process in the queue of processes that are ready 
def process_r(ready, waiting,q,c):
	global results, i
	if ready.isEmpty():
		pass
	else:
		p = ready.dequeue()
		if p.ticks_aux == p.ticks:
			p.beginning = c 
		results.append(p.name)
		p.ticks_aux -= 1
		if i < q:
			if p.ticks_aux > 0:
				ready.enqueue(p)
			else:
				p.end = c + 1
				i = 0
			i += 1
		else:
			i = 1
			if p.ticks_aux > 0:
				waiting.enqueue(p)

