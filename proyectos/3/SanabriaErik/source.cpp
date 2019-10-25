/*
 * source.cpp
 *
 *  Created on: Oct 24, 2019
 *      Author: erik
 */

#include <iostream>
#include <string>
#include <fstream>

int main(int argc, char* argv[])
{
	std::string fname{ "res/fiunamfs.img" };
	std::ifstream in_f;

	const char *mag_def = "FiUnamFS";

	if(argc > 1)
	{
		fname = *argv[1];
	}

	in_f.open(fname, std::ios::binary | std::ios::in);

	char mag[8];

	in_f.read(mag, 8);

	if(mag != mag_def)
	{
		std::cout << std::endl << "El archivo no es valido..." << mag << std::endl;
		return 1;
	}

	std::cout << std::endl << "Data:\t" << mag << std::endl;

	in_f.close();

	return 0;
}


