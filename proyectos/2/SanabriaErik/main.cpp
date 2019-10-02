/*
 * main.cpp
 *
 *  Created on: Sep 27, 2019
 *      Author: Erik Sanabria
 */

#include "engine3d.hpp"

int main()
{
	Engine3D A;

	if(A.CreaConsola(256, 240, 4, 4))
	{
		A.exec();
	}

	return 0;
}




