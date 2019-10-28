/*
 * source.cpp
 *
 *  Created on: Oct 24, 2019
 *      Author: erik
 */

#include <iostream>
#include <iomanip>
#include <string>
#include <fstream>

int main(int argc, char* argv[])
{
	const unsigned short num_mag{ 8 };			//tamanio del numero magico
	const unsigned short num_nom{ 15 };			//tamanio del nombre del archivo
	const unsigned short dir{ 64 };				//cada directorio mide 64 bytes
	const std::string mag_def{ "FiUnamFS" };
	std::string mag;
	std::string fname{ "res/fiunamfs.img" };
	std::ifstream archiv;
	std::ofstream archiv_out;

	size_t tam{ 0 };
	size_t tam_out{ 0 };
	char tmp[num_mag];
	char nom[num_nom];
	char header[dir];

	if(argc > 1)
	{
		fname = argv[1];
	}

	std::cout << std::endl << "\tVamos a abrir " << fname << std::endl;

	archiv.open(fname, std::ios::binary | std::ios::in);

	if(!archiv.is_open())
	{
		std::cout << std::endl << "\tError al abrir el archivo!" << std::endl;

		return 2;
	}

	archiv.read(reinterpret_cast<char*>(tmp), num_mag);

	mag = tmp;

	if(mag_def != mag)
	{
		std::cout << std::endl << "\tEl archivo no es valido...\t" << mag << std::endl;

		archiv.close();

		return 1;
	}

	std::cout << std::endl << "\tData:\t" << mag << std::endl;

	archiv.seekg(0, std::ios::end);
	tam = archiv.tellg();

	archiv.seekg(0, std::ios::beg);

	std::cout << std::endl <<"\tTamanio del archivo: " << tam << " bytes.";

	archiv.seekg(1024, std::ios::beg);

//	archiv.read(reinterpret_cast<char*>(nom), num_nom);
	archiv.read(reinterpret_cast<char*>(header), dir);

	for(size_t a{ 0 }; a < dir; ++a)
	{
		if(a < num_nom)
		{
			std::cout << std::endl << "\tH[" <<  std::setw(3) <<a << "]: " << header[a] << std::flush;
			nom[a] = header[a];
		}
	}

	std::cout << std::endl << std::endl << std::flush;

	for(size_t k{ 0 }, m{ 0 }; k < num_nom; ++k)
	{
		if((nom[k] != 0x20) && (m == 0))
		{
			m = k;

			std::cout << k << std::endl;

			for(size_t h{ 0 }; h < num_nom; ++h, ++m)
			{
				if(m < num_nom)
				{
					nom[h] = nom[m];
				}
				else if(m >= num_nom)
				{
					nom[h] = 0x20;
				}

				std::cout << std::endl << "\tH[" <<  std::setw(3) << h << "]: " << nom[h] << "\tM[" << std::setw(3) << m << "]: " << nom[m] << std::flush;
			}

			break;
		}
	}



	std::cout << std::endl << "\tNombre: " << std::setw(20) << nom << std::flush;

	archiv_out.open(nom);

	if(!archiv_out.is_open())
	{
		std::cout << std::endl << "\tError al abrir el archivo!" << std::endl;

		return 2;
	}

	const size_t n{ 4776 };

	archiv.seekg(5120, std::ios::beg);

	char data_out[n];

	archiv.read(reinterpret_cast<char*>(data_out), n);

	archiv_out.write(reinterpret_cast<char*>(data_out), n);




	/*for(size_t a{ 1 }; a <= tam; ++a)
	{
		archiv.read(&b, 1);

		std::cout << std::setw(10) << std::hex << static_cast<int>(b) << std::flush;

		if((a % 10) == 0)
		{
			std::cout << std::endl;
		}
	}*/


	archiv_out.close();

	archiv.close();

	return 0;
}


