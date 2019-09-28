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

	virtual bool OnUserUpdate(unsigned float tiem = 0);

	bool CreaConsola(size_t w, size_t h, size_t fonh, size_t fonw);

	size_t getWidth();

	size_t getHeight();


protected:


	size_t m_sw;		//ancho de pantalla
	size_t m_sh;		//alto de pantalla


private:


};

#endif /* CONSOLEGAMEENGINE_HPP_ */
