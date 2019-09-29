/*
 * consolegameengine.hpp
 *
 *  Created on: Sep 27, 2019
 *      Author: Erik Sanabria
 */

#ifndef CONSOLEGAMEENGINE_HPP_
#define CONSOLEGAMEENGINE_HPP_

#include <SDL2/SDL.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <chrono>
#include <thread>
#include <atomic>
#include <condition_variable>
#include <string>

#undef main

#define __STDC_LIB_EXT1__
#define __STDC_WANT_LIB_EXT1__ 1
#define _CRT_SECURE_NO_WARNINGS
#define UNICODE
#define _UNICODE

struct CHAR_INFO
{
	unsigned short glyph;
	short color;
};

constexpr SDL_Color color_T[] = {
	SDL_Color{ 0,0,0,255 },      // 0
	SDL_Color{ 0,0,127,255 },    // 1
	SDL_Color{ 0,127,0,255 },    // 2
	SDL_Color{ 0,127,127,255 },  // 3
	SDL_Color{ 127,0,0,255 },    // 4
	SDL_Color{ 127,0,127,255 },  // 5
	SDL_Color{ 127,127,0,255 },  // 6
	SDL_Color{ 192,192,192,255 },// 7
	SDL_Color{ 127,127,127,255 },// 8
	SDL_Color{ 0,0,255,255 },    // 9
	SDL_Color{ 0,255,0,255 },    // A
	SDL_Color{ 0,255,255,255 },  // B
	SDL_Color{ 255,0,0,255 },    // C
	SDL_Color{ 255,0,255,255 },  // D
	SDL_Color{ 255,255,0,255 },  // E
	SDL_Color{ 255,255,255,255 },// F
};

class ConsoleGameEngine
{
public:
	ConsoleGameEngine();

	virtual ~ConsoleGameEngine() {}

	void exec();

	virtual bool OnUserCreate() = 0;

	virtual bool OnUserUpdate(float tiem = 0) = 0;

	virtual bool OnUserDestroy()
	{
		return true;
	}

	void Game();

	bool CreaConsola(int w, int h, int fonh, int fonw);

	virtual void Dibuja(int x, int y, unsigned short c = 0x2588, unsigned short col = 0x000F)
	{
		if((x >= 0) && (x < m_sw) && (y >= 0) && (y < m_sh))
		{
			m_buffer[m_buffactual][(y * m_sw) + x].glyph = c;
			m_buffer[m_buffactual][(y * m_sw) + x].color = col;
		}
	}

	void DibujaLinea(int x1, int y1, int x2, int y2);

	void DibujaTriangulo(int x1, int y1, int x2, int y2, int x3, int y3);

	void Llena(int x1, int y1, int x2, int y2, unsigned short c, unsigned short col);

	void Clip(int& x, int& y);

	int getWidth();

	int getHeight();


protected:

	void CargaFonts(const std::string& file)
	{
		SDL_Surface *tmp = SDL_LoadBMP(file.c_str());

		if(tmp == nullptr)
		{
			std::wcout << L"No se encontro el archivo!" << std::endl;

			throw 1;
		}

		SDL_SetColorKey(tmp, SDL_TRUE, SDL_MapRGB(tmp->format, 255, 0, 255));

		m_ff = SDL_CreateTextureFromSurface(m_render, tmp);

		SDL_FreeSurface(tmp);
	}


	std::wstring m_appnom;	//nombre de applicacion
	int m_sw;			//ancho de pantalla
	int m_sh;			//alto de pantalla
	int m_fw;			//ancho de font
	int m_fh;			//altura de font

	CHAR_INFO *m_buffer[2];		//buffer de pantalla
	int m_buffactual{ 0 };	//buffer actual

	static std::atomic<bool> m_batom;			//variable atomica, esta activo?
	static std::condition_variable m_gamefin;	//variable de condicion
	//static std::mutex m_muxgame;				//mutex

private:

	SDL_Window *m_window;		//ventana de SDL
	SDL_Renderer *m_render;		//Renderer de SDL
	SDL_Texture *m_screen;		//Colores de SDL
	SDL_Texture *m_fontf;		//Colores de fonts
	SDL_Texture *m_ff;			//archivo con los fonts
};

//inicializando las variables static
/*std::atomic<bool> ConsoleGameEngine::m_batom(false);
std::condition_variable ConsoleGameEngine::m_gamefin;*/
//std::mutex ConsoleGameEngine::m_muxgame;

#endif /* CONSOLEGAMEENGINE_HPP_ */
