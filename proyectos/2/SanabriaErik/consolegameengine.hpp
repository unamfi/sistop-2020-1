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

class ConsoleGameEngine
{
public:
	ConsoleGameEngine();

	virtual ~ConsoleGameEngine() {}

protected:


private:

};

#endif /* CONSOLEGAMEENGINE_HPP_ */
