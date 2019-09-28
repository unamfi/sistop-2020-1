/*
 * consolegameengine.cpp
 *
 *  Created on: Sep 27, 2019
 *      Author: Erik Sanabria
 */

#include "consolegameengine.hpp"

ConsoleGameEngine::ConsoleGameEngine()
{
	m_sw = 0;
	m_sh = 0;
}

void ConsoleGameEngine::exec()
{
	m_batom = true;

	std::thread t0 = std::thread(&ConsoleGameEngine::Game, this);

	t0.join();
}

void ConsoleGameEngine::Game()
{
	SDL_Init(SDL_INIT_VIDEO | SDL_INIT_EVENTS);

	//Nombre de la aplicacion
	char buffnom[256];

	wcstombs(buffnom, m_appnom.c_str(), 256);

	m_window = SDL_CreateWindow(buffnom, SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, m_sw * m_fw, m_sh * m_fh, SDL_WINDOW_SHOWN);

	m_render = SDL_CreateRenderer(m_window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_TARGETTEXTURE);

	m_screen = SDL_CreateTexture(m_render, SDL_PIXELFORMAT_ABGR8888, SDL_TEXTUREACCESS_TARGET, m_sw * m_fw, m_sh * m_fh);

	CargaFonts("./fonts.bmp");

	if(!OnUserCreate())
	{
		m_batom = false;
	}

	auto tp1{ std::chrono::system_clock::now() };
	auto tp2{ std::chrono::system_clock::now() };

	while(m_batom)
	{
		while(m_batom)
		{
			tp2 = std::chrono::system_clock::now();

			std::chrono::duration<float> tiempas = tp2 - tp1;	//tiempo pasado

			tp1 = tp2;

			float tiemp{ tiempas.count() };

			SDL_Event evento;

			while(SDL_PollEvent(&evento))
			{
				switch(evento.type)
				{
				case SDL_QUIT:
					{
						m_batom = false;
						break;
					}

				default:
					continue;
				}
			}

			if(!OnUserUpdate(tiemp))
			{
				m_batom = false;
			}

			char titulo[256];

			snprintf(titulo, 256, "Erik Sanabria - %s - FPS: %3.2f", buffnom, 1.0f / tiemp);

			SDL_SetWindowTitle(m_window, titulo);

			CHAR_INFO *buff_v;		//buffer viejo
			CHAR_INFO *buff_n;		//buffer nuevo

			buff_n = m_buffer[m_buffactual];
			buff_v = m_buffer[(m_buffactual + 1) % 2];

			SDL_SetRenderTarget(m_render, m_screen);

			for(size_t cx{ 0 }; cx < m_sw; ++cx)
			{
				for(size_t cy{ 0 }; cy < m_sh; ++cy)
				{
					size_t k{ cy * m_sw + cx };

					if((buff_n[k].color != buff_v[k].color) || (buff_n[k].glyph != buff_v[k].glyph))
					{
						int cell_x{ buff_n[k].glyph % 64 };
						int cell_y{ buff_n[k].glyph / 64 };


						//dibujando primer plano
						int pplano{ (buff_n[k].color & 0x00F) >> 4 };//primer plano

						SDL_Rect src_bg = { pplano * 16, 0, 16, 16 };
						SDL_Rect dst = { cx * m_fw, cy * m_fh, m_fw, m_fh };

						SDL_SetTextureColorMod(m_ff, 255, 255, 255);
						SDL_SetTextureAlphaMod(m_ff, 255);

						SDL_RenderCopy(m_render, m_ff, &src_bg, &dst);

						//establecer el color y los fonts
						SDL_Color col = color_T[buff_n[k].color & 0x000F];

						SDL_SetTextureColorMod(m_ff, col.r, col.g, col.b);
						SDL_SetTextureAlphaMod(m_ff, col.a);

						SDL_Rect src_fg = { cell_x * 16, cell_y * 16, 16, 16 };
						SDL_RenderCopy(m_render, m_ff, &src_fg, &dst);
					}
				}
			}

			//presentar los buffers
			SDL_SetRenderTarget(m_render, nullptr);
			SDL_RenderCopy(m_render, m_screen, nullptr, nullptr);
			SDL_RenderPresent(m_render);

			//flip de los buffers
			m_buffactual = (m_buffactual + 1) % 2;


		}

		if(OnUserDestroy())
		{
			SDL_DestroyTexture(m_ff);
			SDL_DestroyRenderer(m_render);
			SDL_DestroyWindow(m_window);
			SDL_Quit();

			delete[] m_buffer[0];
			delete[] m_buffer[1];

			m_gamefin.notify_one();

		}
		else
		{
			m_batom = true;
		}
	}
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

//inicializando las variables static
std::atomic<bool> ConsoleGameEngine::m_batom(false);
std::condition_variable ConsoleGameEngine::m_gamefin;
//std::mutex ConsoleGameEngine::m_muxgame;
