from test import *

#helper class to set up the test environment
t = Test()
#number of rounds the O.S. should plan: this integer could be any number
num_rounds = 2

def main():
	t.run_algorithms(t.initial_test())
	for i in range(num_rounds):
		t.run_algorithms(t.random_test(i))

#---------------------------
if __name__ == '__main__':
	main()
#---------------------------
