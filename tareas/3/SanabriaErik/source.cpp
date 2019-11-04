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

void printMem(char *data, size_t n = 30)
{
	std::cout << "\n\tContenidos de la memoria:\n\t" << std::flush;

	for(size_t i{ 0 }; i < n; ++i)
	{
		std::cout << data[i];
	}
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

	//inicializando el arreglo de memoria.
	char *arr_mem{ new char[mem] };

	for(size_t k{ 0 }; k < mem; ++k)
	{
		arr_mem[k] = '-';
	}

	printMem(arr_mem, mem);

	delete [] arr_mem;

	return 0;
}
