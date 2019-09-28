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
#include <vector>
#include <list>
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

class ConsoleGameEngine
{
public:
	ConsoleGameEngine();

	virtual ~ConsoleGameEngine() {}

	virtual bool OnUserCreate() = 0;

	virtual bool OnUserUpdate(float tiem = 0) = 0;

	bool CreaConsola(size_t w, size_t h, size_t fonh, size_t fonw);

	virtual void Dibuja(size_t x, size_t y, wchar_t c = 0x2588, unsigned short col = 0x000F)
	{
		if((x >= 0) && (x < m_sw) && (y >= 0) && (y < m_sh))
		{
			m_buffer[m_buffactual][(y * m_sw) + x].glyph = c;
			m_buffer[m_buffactual][(y * m_sw) + x].color = col;
		}
	}

	size_t getWidth();

	size_t getHeight();


protected:


	std::wstring m_appnom;	//nombre de applicacion
	size_t m_sw;			//ancho de pantalla
	size_t m_sh;			//alto de pantalla
	size_t m_fw;			//ancho de font
	size_t m_fh;			//altura de font

	CHAR_INFO *m_buffer[2];		//buffer de pantalla
	size_t m_buffactual{ 0 };	//buffer actual

	static std::atomic<bool> m_batom;			//variable atomica
	static std::condition_variable m_gamefin;	//variable de condicion
	static std::mutex m_muxgame;				//mutex

private:




	SDL_Window *m_window;		//ventana de SDL
	SDL_Renderer *m_render;		//Renderer de SDL
	SDL_Texture *m_screen;		//Colores de SDL
	SDL_Texture *m_fontf;		//Colores de fonts
};

//inicializando las variables static
std::atomic<bool> ConsoleGameEngine::m_batom(false);
std::condition_variable ConsoleGameEngine::m_gamefin;
std::mutex ConsoleGameEngine::m_muxgame;

#endif /* CONSOLEGAMEENGINE_HPP_ */
