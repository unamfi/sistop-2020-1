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
			if len(reindeerReady) == 9:
				print("\t\tSanta leaving the North Pole to deliver gifts... (ignoring for now the elves with problems)")
				del reindeerReady[:] 
				sleep(randint(2,3))
				print("\t\t Santa entering the North Pole and will solve the elves problems (if there are any). \n\t\t\tReindeer going on vacations\n")
				sleep(2)
				reindeerReturning.release()
			elif problems == 3:
				print("\t\tSanta helping elves: %s" % problematicElves)
				problems = 0	
				del problematicElves[0:3]
				sleep(randint(2,3))
				print("\t\tSatna finished helping elves.\n\t\tRemaining elves to help: %d\n" % len(problematicElves))
				sleep(2)
				elves.release()

# Function that makes elves work based on a barrier. 
# The first thread will be able to enter the lines of code to determine if it has a problem. 
# The other threads will go to sleep and wake up if then number of problems != 3. 
def elvesWorking(id):
	global problems
	while True:
		# Only the first elf will be able to enter the following lines of code, all the other elves go to sleep.
		elves.acquire() 
		# --- 
		print("Elf #%d working" % id)
		sleep(1)
		if randint(0,500) <= 250:	# generate a random integer to determine if the current elf will have a problem. 
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
		if randint(20,40) <= 30: # generate a random integer to determine if certain raindeer will return from vacations.
			with mutex:
				# We have to make this comparisson to make sure that all 9 reindeer are different. 
				# Otherwise, it might me possible that Santa ends up with less than 9 reindeer thinkin that he has 9. 
				if id in reindeerReady:
					reindeerReturning.release()
				else:
					reindeerReady.append(id)
					print("\t\t\t\t\t\tReindeer %d ready!" % id)	
					if len(reindeerReady) == 9:
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
