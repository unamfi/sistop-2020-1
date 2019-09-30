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

//vector tridimensional
struct vec3d
{
	float x;
	float y;
	float z;
};

//un triangulo consiste en tres puntos
//de tipo vector tridimensional
struct triangulo
{
	vec3d p[3];
};

//un mesh es un conjunto de triangulos
struct mesh
{
	std::vector<triangulo> tris;
};

//una matriz de 4 por 4
//inicializada con ceros
struct mat4
{
	float m[4][4] = { 0 };
};

//herencia de la clase principal
class Engine3D : public ConsoleGameEngine
{
public:
	//constructor
	Engine3D();

	//vamos a implementar estas dos funciones
	bool OnUserCreate() override;

	bool OnUserUpdate(float tiem = 0);

private:

	//multiplicar matriz por vector
	//a: referencia a vector
	//b: referencia a vector de resultado
	//c: referencia a matriz a la cual se multiplica
	void multMatrizVector(vec3d &a, vec3d &b, mat4 &m);

	mesh m_meshCube;		//cubo
	mat4 m_matProj;			//matriz de proyeccion
	float m_theta;			//angulo de rotacion
};

#endif /* ENGINE3D_HPP_ */
