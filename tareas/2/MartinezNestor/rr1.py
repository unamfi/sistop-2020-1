from foundations import *

f = Foundation()
#proc_ready: queue of processes that are ready
proc_ready = Queue()
#proc_waiting: queue of processes that are waiting to be executed
proc_waiting = Queue()
#array of results
results = []
#rr1(procs: [Process]): round Robin with quantum = 1
def rr1(procs):
	global proc_ready, proc_waiting, c, results
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
			a_time = c
			if proc_waiting.size() > 1:
				process_w(proc_waiting, proc_ready)
				a_time += 1
			proc_ready.enqueue(p)	
			p.beginning = a_time
		else:
			if proc_ready.isEmpty():
				process_w(proc_waiting, proc_ready)		
		process_r(proc_ready, proc_waiting, c)
		c += 1 
	f.handle_results(procs,"RR1",results)
	results = []

#process_w(waiting: Queue, ready: Queue): move a process from the waiting queue to the ready queue
def process_w(waiting, ready):
	if waiting.isEmpty():
		pass
	else:
		p = waiting.dequeue()
		ready.enqueue(p)
#process_r(ready: Queue, waiting: Queue, c: Int): works with the process in the queue of processes that are ready 
def process_r(ready, waiting, c):
	if ready.isEmpty():
		pass
	else:
		p = ready.dequeue()
		if p.ticks_aux > 0:
			eat(p, waiting, c)

#eat(process: Process, waiting: Queue, c: Integer): decrements the number of ticks and prints the process' name 
def eat(process, waiting, c):
	global results 
	process.ticks_aux -= 1
	results.append(process.name)	
	if process.ticks_aux > 0:
		waiting.enqueue(process)
	else:
		process.end = c + 1
