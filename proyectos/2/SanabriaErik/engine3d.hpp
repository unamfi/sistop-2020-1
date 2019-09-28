/*
 * engine3d.hpp
 *
 *  Created on: Sep 28, 2019
 *      Author: Erik Sanabria
 */

#ifndef ENGINE3D_HPP_
#define ENGINE3D_HPP_

#include "consolegameengine.hpp"
#include <vector>

struct vec3d
{
	float x;
	float y;
	float z;
};

struct triangulo
{
	vec3d p[3];
};

struct mesh
{
	std::vector<triangulo> tris;
};

struct mat4
{
	float m[4][4] = { 0 };
};

class Engine3D : public ConsoleGameEngine
{
public:
	Engine3D();

	bool OnUserCreate() override;

	bool OnUserUpdate(float tiem = 0);

private:

	void multMatrizVector(vec3d &a, vec3d &b, mat4 &m);

	mesh m_meshCube;
	mat4 m_matProj;
	float m_theta;
};

#endif /* ENGINE3D_HPP_ */
