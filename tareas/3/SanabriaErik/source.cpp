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
	std::cout << "\n\n\tContenidos de la memoria:\n\t" << std::flush;

	for(size_t i{ 0 }; i < n; ++i)
	{
		std::cout << data[i];
	}

	std::cout << std::endl;
}

size_t asigMem(char *data, char newData, size_t newDataSize, size_t n = 30)
{
	for(size_t k{ 0 }; k < n; ++k)
	{
		if((data[k] == '-') && ((n - k) >= newDataSize))
		{
			for(size_t h{ k }; h < (newDataSize + k); ++h)
			{
				data[h] = newData;

				std::cout << "\n\t[" << h <<"]: " << data[h];
			}

			return 0;
		}
		else if(data[k] != '-')
		{
			std::cout << "\n\t[" << k << "]: Buscando...";

			continue;
		}
	}

	return 1;
}

int main()
{
	size_t mem{ 30 };
	size_t numprocs{ 0 };
	size_t tam{ 0 };

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

	std::cout << "\n\tIngrese el numero de procesos deseados entre 1 y " << mem << ": " << std::flush;
	std::cin >> numprocs;

	if((numprocs <= 0) || (numprocs > mem))
	{
		std::cout << std::endl <<"\n\tEl numero " << numprocs << " es mayor a " << mem << "! Terminando!" << std::flush;

		delete [] arr_mem;

		return 2;
	}

	std::cout << std::endl << std::flush;

	char let{ 0x41 };

	for(size_t h{ 0 }; h < numprocs; ++h, ++let)
	{
		std::cout << "\n\tIngresa el tamanio del proceso " << let << " entre 2 y 15: ";
		std::cin >> tam;

		if((tam > 15) || (tam < 2))
		{
			std::cout <<"\tEl valor (" << tam << ") ingresado para " << let << " es invalido!" << std::flush;

			--h;
			--let;
		}
		else if((tam >= 2) && (tam <= 15))
		{
			std::cout << "\n\tVamos a ingresar el proceso " << let << std::flush;

			if(!asigMem(arr_mem, let, tam, mem))
			{
				std::cout << "\n\tLa asignacion de " << let << " con tamanio " << tam << " fue exitosa!" << std::flush;

				printMem(arr_mem, mem);
			}
			else
			{
				std::cout << "\\n\tEl proceso " << let <<" ya no cabe!" << std::endl << std::flush;

				printMem(arr_mem, mem);

				break;
			}
		}
	}

	delete [] arr_mem;

	return 0;
}
