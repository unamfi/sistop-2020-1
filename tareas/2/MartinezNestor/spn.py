from foundations import * 

f = Foundation()
#proc_ready: queue of processes that are ready
proc_ready = Queue()
#proc_waiting: queue of processes that are waiting to be executed
proc_waiting = Queue()
#q: denotes the ticks per process 
q = 0
#i: counter to keep track of the current tick
i = 0
results = []
#spn(procs: [Process]): algorithm that planifies procesesses based on Shortest Process Next strategy
def spn(procs):
	global proc_ready, proc_waiting,results
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
				if proc_waiting.isEmpty():
					proc_waiting.enqueue(p)
				else:
					proc_waiting.enqueue(p)
					arranged_q = sort_waiting_q(proc_waiting)
					for i in range(len(arranged_q)):
						proc_waiting.enqueue(arranged_q[i])
				process_w(proc_waiting, proc_ready)
		else:
			if proc_waiting.isEmpty():
				pass
			else:
				process_w(proc_waiting,proc_ready)
		process_r(proc_ready,c)
		c += 1
	f.handle_results(procs,"SPN",results)
	results = [] 

#process_w(waiting: Queue, ready: Queue): move a process from the waiting queue to the ready queue
def process_w(waiting, ready):
	if waiting.isEmpty():
		pass
	else:
		if ready.isEmpty():
			p = waiting.dequeue()
			ready.enqueue(p)

#process_r(ready: Queue, c: Int): works with the process in the queue of processes that are ready 
def process_r(ready,c):
	global results,i,q
	if ready.isEmpty():
		pass
	else:
		p = ready.dequeue()
		if p.ticks_aux == p.ticks:
			p.beginning = c 
		results.append(p.name)
		q = p.ticks
		p.ticks_aux -= 1
		if i < q:
			if p.ticks_aux > 0:
				ready.enqueue(p)
				i += 1
			else:
				p.end = c + 1
				i = 0
				q = 0 
#determine_next_short(waiting: Queue): when the waiting queue contains two or more processes, this function will return a list of the procesess sorted by number of ticks. 
def sort_waiting_q(waiting):
	if waiting.size() < 2:
		return [waiting.dequeue()]
	else:
		pcs = []
		for i in range(waiting.size()):
			pcs.append(waiting.dequeue())
		pcs.sort(key=lambda x: x.ticks)
		return pcs 
