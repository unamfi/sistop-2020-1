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
#include <cmath>
#include <cstdlib>

int main(int argc, char* argv[])
{
	const unsigned short num_mag{ 8 };			//tamanio del numero magico
	const unsigned short num_tam{ num_mag };	//tamanio del numero de bytes_f del archivo
	const unsigned short num_nom{ 15 };			//tamanio del nombre del archivo
//	const unsigned short dir{ 64 };				//cada directorio mide 64 bytes_f
	const unsigned short pos{ 1024 };
	const std::string mag_def{ "FiUnamFS" };
	std::string mag;
	std::string fname{ "res/fiunamfs.img" };
	std::ifstream archiv;
	std::ofstream archiv_out;

	size_t bytes_f{ 0 };
	size_t tam{ 0 };							//tamanio total del sistema de archivos
	//size_t tam_out{ 0 };
	char tmp[num_mag];
	char nom[num_nom];
	char sizeb[num_tam];

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

	archiv.seekg(pos, std::ios::beg);

	archiv.read(reinterpret_cast<char*>(nom), num_nom);
	//archiv.read(reinterpret_cast<char*>(header), dir);

/*	for(size_t a{ 0 }; a < num_nom; ++a)
	{
		if(a < num_nom)
		{
			nom[a] = header[a];
			std::cout << std::endl << "\tH[" << std::setw(3) << a << "]: " << header[a] << "\tnom[" << a << std::setw(3) <<"]: " << nom[a] << std::flush;
		}
	}*/

	std::cout << std::endl << std::endl << std::flush;

	for(size_t k{ 0 }, m{ 0 }; k < num_nom; ++k)
	{
		if((nom[k] != 0x20) && (m == 0))
		{
			m = k;

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

				std::cout << std::endl << "\tnom[" <<  std::setw(3) << h << "]: " << nom[h] << "\tM[" << std::setw(3) << m << "]: " << nom[m] << std::flush;
			}

			break;
		}
	}

	std::cout << std::endl << "\tNombre: " << std::setw(20) << nom << std::flush;

	archiv_out.open(nom, std::ios::binary | std::ios::out);

	if(!archiv_out.is_open())
	{
		std::cout << std::endl << "\tError al abrir el archivo!" << std::endl;

		return 2;
	}

	archiv.seekg(pos + num_nom + 1, std::ios::beg);

	archiv.read(reinterpret_cast<char*>(sizeb), num_tam);

//	std::cout << std::endl << std::flush <<"\tBytes: "  << std::hex << sizeb << std::setw(8) << sizeof(sizeb)/sizeof(char);

	for(size_t i{ 0 }, t{ static_cast<size_t>(std::pow(10.0f, num_tam - 1)) }; i < num_tam; ++i)
	{
		char loc = sizeb[i];
		bytes_f += std::atoi(&loc) * t;

		std::cout << std::endl <<"\tb: " << std::setw(10) << bytes_f << "\tsizeb: " << std::setw(5) << sizeb[i] << "\tt: " << std::setw(10) << t;

		t /= 10;
	}

	char *out_d{ new char[bytes_f] };

	const size_t n{ 4776 };

	archiv.seekg(5120, std::ios::beg);

	char data_out[n];

//	archiv.read(reinterpret_cast<char*>(data_out), n);
//
//	archiv_out.write(reinterpret_cast<char*>(data_out), n);

	archiv.read(out_d, bytes_f);

	archiv_out.write(out_d, bytes_f);

	/*for(size_t a{ 1 }; a <= tam; ++a)
	{
		archiv.read(&b, 1);

		std::cout << std::setw(10) << std::hex << static_cast<int>(b) << std::flush;

		if((a % 10) == 0)
		{
			std::cout << std::endl;
		}
	}*/

	delete [] out_d;

	archiv_out.close();

	archiv.close();

	std::cout << std::endl << std::flush;

	return 0;
}


