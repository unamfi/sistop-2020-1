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

void ConsoleGameEngine::DibujaLinea(int x1, int y1, int x2, int y2)
{
	int x{ 0 };
	int y{ 0 };
	int dx{ x2 - x1 };
	int dy{ y2 - y1 };
	int dx1{ abs(dx) };
	int dy1{ abs(dy) };
	int px{ 2* dy1 - dx1 };
	int py{ 2 * dx1 - dy1 };
	int xe{ 0 };
	int ye{ 0 };

	if(dy1 <= dx1)
	{
		if(dx >= 0)
		{
			x = x1;
			y = y1;
			xe = x2;
		}
		else
		{
			x = x2;
			y = y2;
			xe = x1;
		}

		Dibuja(x, y);

		while(x < xe)
		{
			++x;

			if(px < 0)
			{
				px = px +2 * dy1;
			}
			else
			{
				if(((dx < 0) && (dy > 0)) || ((dx > 0) && (dy > 0)))
				{
					y = y + 1;
				}
				else
				{
					y = y - 1;
				}

				px = px + 2 * (dy1 - dx1);
			}

			Dibuja(x, y);
		}
	}
	else
	{
		if(dy >= 0)
		{
			x = x1;
			y = y1;
			ye = y2;
		}
		else
		{
			x = x2;
			y = y2;
			ye = y1;
		}

		Dibuja(x, y);

		while(y < ye)
		{
			++y;

			if(py <= 0)
			{
				py = py + 2 * dx1;
			}
			else
			{
				if(((dx < 0) && (dy < 0)) || ((dx > 0) && (dy > 0)))
				{
					x = x + 1;
				}
				else
				{
					x = x -1;
				}

				py = py + 2 * (dx1 - dy1);
			}

			Dibuja(x, y);
		}
	}
}

void ConsoleGameEngine::DibujaTriangulo(int x1, int y1, int x2, int y2, int x3, int y3)
{
	DibujaLinea(x1, y1, x2, y2);
	DibujaLinea(x2, y2, x3, y3);
	DibujaLinea(x3, y3, x1, y1);
}

size_t ConsoleGameEngine::getWidth()
{
	return m_sw;
}

size_t ConsoleGameEngine::getHeight()
{
	return m_sh;
}
