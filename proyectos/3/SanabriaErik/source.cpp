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

void compactName(char *m_nom_s, char *m_nom, const unsigned short new_num, const unsigned short n_nom = 15)
{

}

size_t cleanName(char *m_nom, const unsigned short n_nom = 15)
{
	size_t k{ 0 };

	for(size_t m{ 0 }; k < n_nom; ++k)
	{
		if((m_nom[k] != 0x20) && (m == 0))
		{
			m = k;

			for(size_t h{ 0 }; h < n_nom; ++h, ++m)
			{
				if(m < n_nom)
				{
					m_nom[h] = m_nom[m];
				}
				else if(m >= n_nom)
				{
					m_nom[h] = 0x20;
				}

//				std::cout << std::endl << "\tnom[" <<  std::setw(3) << h << "]: " << m_nom[h] << "\tM[" << std::setw(3) << m << "]: " << m_nom[m] << std::flush;
			}

			break;
		}
	}

	return n_nom - k;
}

void extractName(char *head, char *m_nom, const unsigned short n_dir = 64, const unsigned short n_nom = 15)
{
	if(head != nullptr && m_nom != nullptr)
	{
		for(size_t p{ 0 }; p < n_nom; ++p)
		{
			m_nom[p] = head[p];
		}
	}
}

void readHead(std::ifstream *m_archiv, char *head, const unsigned short n_dir = 64, const unsigned short n_pos = 1024)
{
	if(m_archiv->is_open())
	{
		m_archiv->seekg(n_pos, std::ios::beg);
		m_archiv->read(head, n_dir);
		m_archiv->seekg(0, std::ios::beg);
	}
}

int main(int argc, char* argv[])
{
	const unsigned short num_mag{ 8 };			//tamanio del numero magico
	const unsigned short num_tam{ num_mag };	//tamanio del numero de bytes_f del archivo
	const unsigned short num_nom{ 15 };			//tamanio del nombre del archivo
	const unsigned short dir{ 64 };				//cada directorio mide 64 bytes_f
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
	char nom_2[num_nom];
	char sizeb[num_tam];
	char cabeza[dir];

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

	std::cout << std::flush << std::endl << std::endl;

	readHead(&archiv, cabeza);

/*	for(size_t H{ 0 }; H < dir; ++H)
	{
		std::cout << "\n\tcabeza[" << std::setw(2) << H << "]:\t" << std::setw(4) << cabeza[H] << std::flush;
	}*/

	extractName(cabeza, nom_2);

	size_t new_num_nom{ cleanName(nom_2) };

	char *nom_small{ new char[new_num_nom] };

	for(size_t H{ 0 }; H < num_nom; ++H)
	{
		std::cout << "\n\tnom_2[" << std::setw(2) << H << "]:\t" << std::setw(4) << nom_2[H] <<"\t" << new_num_nom << std::flush;
	}

	std::cout << std::flush << std::endl << std::endl << std::flush;

	for(size_t H{ 0 }; H < new_num_nom; ++H)
	{
		std::cout << "\n\tnom_2[" << std::setw(2) << H << "]:\t" << std::setw(4) << nom_small[H] << std::flush;
	}


	std::cout << std::flush << std::endl << std::endl << std::flush;

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



	archiv.seekg(5120, std::ios::beg);

	archiv.read(out_d, bytes_f);

	archiv_out.write(out_d, bytes_f);

	archiv_out.close();

	//=======================================================================================================================

	archiv_out.open("logo.png", std::ios::binary | std::ios::out);

	const size_t n{ 170173 };

	char data_out[n];

	archiv.seekg(0x4400, std::ios::beg);

	archiv.read(data_out, n);

	archiv_out.write(data_out, n);

	archiv_out.close();

	//=======================================================================================================================

	archiv_out.open("mensajes.png", std::ios::binary | std::ios::out);

	const size_t nam{ 1337 };

	char data_out_2[nam];

	archiv.seekg(0x58400, std::ios::beg);

	archiv.read(data_out_2, nam);

	archiv_out.write(data_out_2, nam);

	//=======================================================================================================================

	delete [] nom_small;
	delete [] out_d;

	archiv_out.close();

	archiv.close();

	std::cout << std::endl << std::flush;

	return 0;
}


