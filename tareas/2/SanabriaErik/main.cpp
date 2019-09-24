#include <iostream>

#include "fcfs.h"
#include "roundrobin.h"

int main(void)
{
	srand(time(NULL));
	size_t num{ static_cast<size_t>((rand() % (8 - 4 + 1)) + 4) };
	std::cout << std::endl << std::flush;

	FCFS P(num);
	P.run();

	RoundRobin P2(num);
	P2.run();

	return 0;
}
