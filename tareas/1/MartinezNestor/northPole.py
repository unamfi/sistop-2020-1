#!/usr/bin/python3

from threading import Thread, Semaphore
from time import sleep
from random import randint 

#Signal pattern to control Santa Claus' operation
santa = Semaphore(0)

#Barrier pattern. One barrier for the elves and another for the reindeer
elves = Semaphore(1)
reindeerReturning = Semaphore(1)

#Mutex pattern to protect the access to shared variables
mutex = Semaphore(1)
problems = 0
problematicElves = []
reindeer = 0
reindeerReady = []

# Function that wakes up Santa Claus once all reindeer have returned from vacations
# or 3 elves have a problem. Or, puts Santa Claus to sleep if neither reindeer have returned
# nor there are 3 elves with problems.
def santaClaus():
	global problems, reindeer
	while True:
		santa.acquire()
		print("\nSanta is now ready to work.")
		with mutex:
			if reindeer == 9:
				print("\t\tNow leaving the North Pole to deliver gifts...")
				reindeer = 0
				sleep(randint(2,3))
				print("Now entering the Nort Pole to sleep. Reindeer going on vacations\n")
				sleep(2)
				reindeerReturning.release()
			elif problems == 3:
				print("\t\t\tNow helping elves: %s" % problematicElves)
				problems = 0	
				del problematicElves[0:3]
				sleep(randint(2,3))
				print("Finished helping elves.\n\tRemaining elves to help: %d\n" % len(problematicElves))
				sleep(2)
				elves.release()

# Function that makes elves work based on a barrier. 
# The first thread will be able to enter the lines of code to determine if it has a problem. 
# The other threads will go to sleep and wake up if then number of problems != 3. 
def elvesWorking(id):
	global problems
	while True:
		elves.acquire()
		print("Elf #%d working" % id)
		sleep(1)
		if randint(0,500) <= 250:	
			print("\t\t\t this elf has a problem.")
			with mutex:
				problematicElves.append(id)
				problems += 1
				if problems == 3:
					print("Now there are 3 elves with problems")
					sleep(1.5)
					santa.release()
				else:
					elves.release()
		else:
			elves.release()
		sleep(2)
	
# Function that makes reindeer work based on a barrier.
# Similar to the elvesWorking() function, this function will wake up Santa only if 9 reindeer have returned from vacation. 
# Otherwise, they will wake up the next thread that is asleep and add the current reindeer to the array. 
def reindeerLeaving(id):
	global reindeer
	while True:
		reindeerReturning.acquire()
		if randint(20,40) <= 30:
			print("\t\t\t\t\t\tReindeer ready!")	
			with mutex:
				reindeer += 1
				if reindeer == 9:
					print("\t\t\t\t\t\t\t\t9 reindeer ready to work!")
					sleep(1.5)
					santa.release()
				else:
					reindeerReturning.release()
		else: 
			reindeerReturning.release()
		sleep(3)


#Start of the program. We have only 1 Santa Claus, n elves (in this case 40) and 9 reindeer.
Thread(target=santaClaus, args=[]).start()
for i in range(40):
	Thread(target=elvesWorking, args=[i]).start()
for i in range(9):
	Thread(target=reindeerLeaving, args=[i]).start()
