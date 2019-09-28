/*
 * consolegameengine.cpp
 *
 *  Created on: Sep 27, 2019
 *      Author: fanny
 */

#include "consolegameengine.hpp"

ConsoleGameEngine::ConsoleGameEngine()
{
	m_sw = 0;
	m_sh = 0;
}

bool ConsoleGameEngine::CreaConsola(size_t w, size_t h, size_t fonh, size_t fonw)
{
	m_sw = w;
	m_sh = h;

	return true;
}

size_t ConsoleGameEngine::getWidth()
{
	return m_sw;
}

size_t ConsoleGameEngine::getHeight()
{
	return m_sh;
}
