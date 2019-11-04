#include <iostream>
#include <ctime>
#include <cstdlib>

//Funcion que genera numeros aleatorios
//entre a y b.
//a: el minimo
//b: el maximo
size_t genRand(size_t a, size_t b)
{
	std::srand(std::time(0));
	size_t num{a + (std::rand()%(b - a + 1))};
	return num;
}

int main()
{
	size_t mem{ 30 };

	std::cout <<"\n\tIngrese el numero de unidades de memoria, mayor a 30: ";
	std::cin >> mem;

	if(mem < 30)
	{
		std::cout << std::endl <<"\n\tEl numero " << mem << " es menor a 30! Terminando!" << std::flush;

		return 1;
	}

	for(size_t i{ 0 }; i < 20; ++i)
	{
		size_t A{ 0 };
		size_t B{ 0 };
		std::cout <<"\n\tA: ";
		std::cin >> A;
		std::cout <<"\n\tB: ";
		std::cin >> B;
		std::cout << std::endl <<"\t" << genRand(A, B) << std::flush;
	}

	return 0;
}
