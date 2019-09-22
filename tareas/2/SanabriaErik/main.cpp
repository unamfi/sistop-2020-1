#include <iostream>

#include "fcfs.h"

int main(void)
{
	srand(time(NULL));
	size_t num{ static_cast<size_t>((rand() % (8 - 4 + 1)) + 4) };
	std::cout << std::endl;

	FCFS P(num);
	P.run();

	return 0;
}
