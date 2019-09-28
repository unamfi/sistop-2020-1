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
	m_fw = fonw;
	m_fh = fonh;

	//alocando memoria para el buffer de pantalla
	m_buffer[0] = new CHAR_INFO[m_sw * m_sh];
	m_buffer[1] = new CHAR_INFO[m_sw * m_sh];

	//llenando con ceros al buffer
	memset(m_buffer[0], 0, m_sw * m_sh * sizeof(CHAR_INFO));
	memset(m_buffer[1], 0, m_sw * m_sh * sizeof(CHAR_INFO));

	m_buffactual = 0;

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
