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

//Funcion que extrae el tamanio en
//bytes dek archivo a extraer del encabezado
//char *m_head: arreglo del encabezado
//const unsigned short pos = 16: posicion relativa donde esta la data
//const unsigned short n_tam = 8: tamanio del
size_t extractSize(char *m_head, const unsigned short pos = 16, const unsigned short n_tam = 8)
{
	size_t num_bytes{ 0 };

	for(size_t i{ pos }, t{ static_cast<size_t>(std::pow(10.0f, n_tam - 1)) }; i < (pos + n_tam); ++i)
	{
		char loc = m_head[i];
		num_bytes += std::atoi(&loc) * t;

		t /= 10;
	}

	return num_bytes;
}

//Funcion que compacta el arreglo del nombre
//en base al retorno de cleanName() obtenemos
//la nueva longitud del nombre
//char *m_nom_s: aqui va el nombre compacto
//char *m_nom: aqui entra el nombre anterior
//const unsigned short new_num: el nuevo numero de caracteres deseados
void compactName(char *m_nom_s, char *m_nom, const unsigned short new_num)
{
	for(size_t f{ 0 }; f < new_num; ++f)
	{
		m_nom_s[f] = m_nom[f];
	}
}

//Funcion que limpia el arreglo del nombre,
//como cuando lo leemos viene precedido de espacios,
//hay que reordenarlo, mover el nombre hasta el principio
//char *m_nom: arreglo que contiene el nombre
//const unsigned short n_nom = 15: El tamanio maximo del nombre en bytes
//retorna el numero de caracteres que no son espacios vacios.
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
			}

			break;
		}
	}

	return n_nom - k;
}

//Funcion que lee el nombre del archivo de la cabeza
//char *head: El arreglo de la cabeza
//char *m_nom: El arreglo donde vamos a guardar el nombre
//const unsigned short n_nom = 15: El tamanio maximo del nombre en bytes
void extractName(char *head, char *m_nom, const unsigned short n_nom = 15)
{
	if(head != nullptr && m_nom != nullptr)
	{
		for(size_t p{ 0 }; p < n_nom; ++p)
		{
			m_nom[p] = head[p];
		}
	}
}

//Funcion que lee el encabezado,
//std::ifstream *m_archiv: es un apuntador al archivo que contiene el sistema de archivos
//char *head: en donde guardaremos el encabezado
//const unsigned short n_dir = 64: tamanio del encabezado en bytes
//const unsigned short n_pos = 1024: tamanio del offset absoluto del sistema de archivos en bytes
void readHead(std::ifstream *m_archiv, char *head, const unsigned short n_dir = 64, const unsigned short n_pos = 1024)
{
	if(m_archiv->is_open())							//Solo si el archivo esta abierto
	{
		m_archiv->seekg(n_pos, std::ios::beg);		//nos ubicamos en la posicion correcta
		m_archiv->read(head, n_dir);				//leemos
		m_archiv->seekg(0, std::ios::beg);			//regresamos la posicion al inicio
	}
}

int main(int argc, char* argv[])
{
	const unsigned short num_mag{ 8 };			//tamanio del numero magico
	const unsigned short num_nom{ 15 };			//tamanio del nombre del archivo
	const unsigned short dir{ 64 };				//cada directorio mide 64 bytes_f
	const unsigned short pos{ 1024 };			//posicion absoluta donde inicia el encabezado
	const unsigned short offset{ 5120 };		//fin del superbloque y el encabezado
	const std::string mag_def{ "FiUnamFS" };	//numero magico esperado
	std::string mag;							//numero magico leido
	std::string fname{ "res/fiunamfs.img" };	//nombre y ubicacion default del sistema de archivos
	std::ifstream archiv;						//archivo de entrada que contiene el sistema de archivos
	std::ofstream archiv_out;					//archivo para las salidas

	size_t tam{ 0 };							//tamanio total del sistema de archivos

	char tmp[num_mag];							//arreglo para leer el numero magico
	char nom_2[num_nom];						//arreglo para leer el nombre del archivo dentro del sistema de archivos
	char cabeza[dir];							//arreglo para leer el encabezado

	if(argc > 1)
	{
		fname = argv[1];
	}

	std::cout << std::endl << "\tVamos a abrir " << fname << std::endl;

	archiv.open(fname, std::ios::binary | std::ios::in);

	if(!archiv.is_open())
	{
		std::cout << std::endl << "\tError al abrir el archivo: " << fname << std::endl << std::flush;

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

	std::cout << std::flush << std::endl <<"\tVamos a extraer todos los archivos de " << fname << std::endl << std::endl;

	readHead(&archiv, cabeza);

	extractName(cabeza, nom_2);

	size_t new_num_nom{ cleanName(nom_2) };

	char *nom_small{ new char[new_num_nom] };

	compactName(nom_small, nom_2, new_num_nom);

	size_t bytes_archiv_out{ extractSize(cabeza) };

	char *out_d{ new char[bytes_archiv_out] };

	std::cout << std::endl << "\tVamos a exportar a: " << nom_small << ", " << "logo.png, mensajes.png" << std::flush;

	archiv_out.open(nom_small, std::ios::binary | std::ios::out);

	if(!archiv_out.is_open())
	{
		std::cout << std::endl << "\tError al abrir el archivo: " << nom_small << std::endl << std::flush;

		return 2;
	}

	archiv.seekg(offset, std::ios::beg);

	archiv.read(out_d, bytes_archiv_out);

	archiv_out.write(out_d, bytes_archiv_out);

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


