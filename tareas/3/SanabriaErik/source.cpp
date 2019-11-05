#include <iostream>

//Funcion que imprime los contenido de la memoria
//char *data: arreglo de la memoria
//size_t n: tamanio de la memoria
void printMem(char *data, size_t n = 30)
{
	std::cout << "\n\n\tContenidos de la memoria:\n\t" << std::flush;

	for(size_t i{ 0 }; i < n; ++i)
	{
		std::cout << data[i];
	}

	std::cout << std::endl;
}

//Funcion que asigna memoria
//char *data: arreglo de la memoria
//char newData: el proceso nuevo
//size_t newDataSize: el tamanio del nuevo proceso
//size_t n: tamanio de la memoria
size_t asigMem(char *data, char newData, size_t newDataSize, size_t n = 30)
{
	for(size_t k{ 0 }; k < n; ++k)
	{
		if((data[k] == '-') && ((n - k) >= newDataSize))
		{
			for(size_t h{ k }; h < (newDataSize + k); ++h)
			{
				data[h] = newData;
			}

			return 0;
		}
		else if(data[k] != '-')
		{
			continue;
		}
	}

	return 1;
}

//Funcion que quita procesos
//char *data: arreglo de la memoria
//char let: el proceso nuevo
//size_t n: tamanio de la memoria
size_t remLet(char *data, char let, size_t n = 30)
{
	bool blet{ false };			//se encuentra la letra?

	for(size_t i{ 0 }; i < n; ++i)
	{
		if(data[i] == let)
		{
			blet = true;

			data[i] = '-';
		}
	}

	if(!blet)
	{
		return 1;
	}

	return 0;
}

int main()
{
	size_t mem{ 30 };				//tamanio de la memoria
	size_t numprocs{ 0 };			//numero de procesos deseados
	size_t numprocs_act{ 0 };		//numero actual de procesos
	size_t tam{ 0 };				//tamanio de proceso a ingresar
	char let{ 0x41 };				//letra A en hexadecimal

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

			numprocs_act = h;

			if(!asigMem(arr_mem, let, tam, mem))
			{
				std::cout << "\n\tLa asignacion de " << let << " con tamanio " << tam << " fue exitosa!" << std::flush;

				printMem(arr_mem, mem);
			}
			else
			{
				std::cout << "\n\n\tEl proceso " << let <<" ya no cabe!" << std::endl << std::flush;

				printMem(arr_mem, mem);

				break;
			}
		}
	}

	while(true)
	{
		char res{ 'N' };			//respuesta
		char letra{ 0x41 };			//letra A
		char let_rem{ 0x41 };		//proceso a remover, inicializado con A

		std::cout << std::endl <<"\tDesea borrar algun proceso (Y/N): " << std::flush;
		std::cin >> res;

		if((res == 'N') || (res == 'n'))
		{
			std::cout << std::endl <<"\tTerminando (" << res <<")." << std::flush;

			break;
		}
		else if((res == 'Y') || (res == 'y'))
		{
			std::cout << std::endl <<"\tQue proceso desea remover: (" << std::flush;

			for(size_t a{ 0 }; a <= numprocs_act; ++a, ++letra)
			{
				std::cout << letra << ", " << std::flush;
			}

			std::cout <<")" << std::flush << "\n\tRespuesta: ";
			std::cin >> let_rem;

			std::cout << std::endl << "\tVamos a remover a " << let_rem << std::flush;

			if(!remLet(arr_mem, let_rem, mem))
			{
				std::cout << std::endl << "\t" << let_rem << " se removio con exito!" << std::flush;

				printMem(arr_mem, mem);
			}
			else
			{
				std::cout << std::endl <<"\tEl proceso " << let_rem << " no existe!" << std::flush;

				continue;
			}
		}
		else
		{
			std::cout << std::endl << "\tLa respuesta " << res << " es invalida!" << std::flush;

			continue;
		}
	}

	delete [] arr_mem;

	return 0;
}
