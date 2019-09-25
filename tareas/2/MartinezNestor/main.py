from foundations import * 
from rr1 import *

#Main method
f = Foundation()

def main():
	procs = generateTest()
	f.printProcesses(procs)
	rr1(procs)

#generateTest() generates a hard coded data set of processes
def generateTest():
	a = Process("A",0,3)
	b = Process("B",1,5)
	c = Process("C",3,2)
	d = Process("D",9,5)
	e = Process("E",12,5)
	return [a,b,c,d,e]



#---------------------------
if __name__ == '__main__':
	main()
#---------------------------