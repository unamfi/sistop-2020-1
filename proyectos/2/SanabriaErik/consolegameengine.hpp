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

//tabla de colores
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
	//constructor
	ConsoleGameEngine();

	//destructor
	virtual ~ConsoleGameEngine() {}

	//metodo padre
	void exec();

	//para ser implementada en la herencia
	//funcion que crea y asigna variables
	virtual bool OnUserCreate() = 0;

	//para ser implementada en la herencia
	//fundion para actualizar las matrizes
	//float tiem: tiempo que llevamos corriendo
	virtual bool OnUserUpdate(float tiem = 0) = 0;

	virtual bool OnUserDestroy()
	{
		return true;
	}

	//hilo principal
	void Game();

	//asigna la memoria para los buffers de pantalla
	//w: ancho de pantalla
	//h: altura de pantalla
	//fonh: altura de fonts
	//fonw: ancho de fonts
	bool CreaConsola(int w, int h, int fonh, int fonw);

	//dibuja un punto en el buffer de la pantalla
	//x: coordenada x
	//y: coordenada y
	//c: color
	//col: color
	virtual void Dibuja(int x, int y, unsigned short c = 0x2588, unsigned short col = 0x000F)
	{
		//si esta dentro de la ventana dibujalo
		if((x >= 0) && (x < m_sw) && (y >= 0) && (y < m_sh))
		{
			m_buffer[m_buffactual][(y * m_sw) + x].glyph = c;
			m_buffer[m_buffactual][(y * m_sw) + x].color = col;
		}
	}

	//dibujar una linea en base a dos puntos
	//x1: coordenada x del primer punto
	//y1: coordenada y del primer punto
	//x2: coordenada x del segundo punto
	//y2: coordenada y del segundo punto
	void DibujaLinea(int x1, int y1, int x2, int y2);

	//dibujar triangulo en base a tres puntos
	//x1: coordenada x del primer punto
	//y1: coordenada y del primer punto
	//x2: coordenada x del segundo punto
	//y2: coordenada y del segundo punto
	//x3: coordenada x del tercer punto
	//y3: coordenada y del tercer punto
	void DibujaTriangulo(int x1, int y1, int x2, int y2, int x3, int y3);

	//llena la ventana
	void Llena(int x1, int y1, int x2, int y2, unsigned short c, unsigned short col);

	//si un punto x, y esta fuera de la ventana
	//regresalo al rango de la ventana
	//x: referencia a coordenada x
	//y: referencia a coordenada y
	void Clip(int& x, int& y);

	//obtener ancho de ventana
	int getWidth();

	//obtener altura de ventana
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
