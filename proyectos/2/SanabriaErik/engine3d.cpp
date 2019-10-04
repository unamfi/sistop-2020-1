/*
 * engine3d.cpp
 *
 *  Created on: Sep 28, 2019
 *      Author: Erik Sanabria
 */

#include "engine3d.hpp"

Engine3D::Engine3D()
{
	m_appnom = L"Proyecto SISTOP";
}

bool Engine3D::OnUserCreate()
{

	//definiendo un cubo
	m_meshCube.tris =
	{
		{0.0f, 0.0f, 0.0f, 		0.0f, 1.0f, 0.0f, 		1.0f, 1.0f, 0.0f},
		{0.0f, 0.0f, 0.0f, 		1.0f, 1.0f, 0.0f, 		1.0f, 0.0f, 0.0f},

		{1.0f, 0.0f, 0.0f, 		1.0f, 1.0f, 0.0f, 		1.0f, 1.0f, 1.0f},
		{1.0f, 0.0f, 0.0f, 		1.0f, 1.0f, 1.0f, 		1.0f, 0.0f, 1.0f},

		{1.0f, 0.0f, 1.0f, 		1.0f, 1.0f, 1.0f,		0.0f, 1.0f, 1.0f},
		{1.0f, 0.0f, 1.0f, 		0.0f, 1.0f, 1.0f,		0.0f, 0.0f, 1.0f},

		{0.0f, 0.0f, 1.0f, 		0.0f, 1.0f, 1.0f,		0.0f, 1.0f, 0.0f},
		{0.0f, 0.0f, 1.0f, 		0.0f, 1.0f, 0.0f,		0.0f, 0.0f, 0.0f},

		{0.0f, 1.0f, 0.0f, 		0.0f, 1.0f, 1.0f,		1.0f, 1.0f, 1.0f},
		{0.0f, 1.0f, 0.0f, 		1.0f, 1.0f, 1.0f,		1.0f, 1.0f, 0.0f},

		{1.0f, 0.0f, 1.0f, 		0.0f, 0.0f, 1.0f,		0.0f, 0.0f, 0.0f},
		{1.0f, 0.0f, 1.0f, 		0.0f, 0.0f, 0.0f,		1.0f, 0.0f, 0.0f}
	};

	//los ejes x, y son la pantalla, para que sea tridimensional agregamos la z
	//la z entra a la pantalla
	float fNear{ 0.0f };			//el plano en z cercano
	float fFar{ 1000.0f };			//el plano en z lejano
	float fFOV{ 90.0f };			//el angulo de field of view
	//el tamaño de la pantalla
	float fAspectRatio{ static_cast<float>(getHeight()) / static_cast<float>(getWidth()) };

	//tamaño del plano lejano
	float fFovRad{ 1.0f / tanf(fFOV * 0.5f / 180.0f * 3.14159f) };	//convirtiendo a radianes

	//definiendo la matriz de proyeccion
	m_matProj.m[0][0] = fAspectRatio * fFovRad;
	m_matProj.m[1][1] = fFovRad;
	m_matProj.m[2][2] = fFar / (fFar - fNear);
	m_matProj.m[3][2] = (-fFar * fNear) / (fFar - fNear);
	m_matProj.m[2][3] = 1.0f;
	m_matProj.m[3][3] = 0.0f;

	return true;
}

bool Engine3D::OnUserUpdate(float tiem)
{
	//llenar la ventana con el color 0x2222
	Llena(0, 0, getWidth(), getHeight(), 0x2588, 0x2222);

	mat4 matRotZ;		//matriz de rotacion en el eje z
	mat4 matRotX;		//matriz de rotacion en el eje x

	m_theta += 1.0f * tiem;		//el angulo de rotacion cambiara con el tiempo

	//definiendo la matriz de rotacion z
	matRotZ.m[0][0] = cosf(m_theta);
	matRotZ.m[0][1] = sinf(m_theta);
	matRotZ.m[1][0] = -sinf(m_theta);
	matRotZ.m[1][1] = cosf(m_theta);
	matRotZ.m[2][2] = 1;
	matRotZ.m[3][3] = 1;

	//definiendo la matriz de rotacion x
	matRotX.m[0][0] = 1;
	matRotX.m[1][1] = cosf(m_theta * 0.5f);
	matRotX.m[1][2] = sinf(m_theta * 0.5f);
	matRotX.m[2][1] = -sinf(m_theta * 0.5f);
	matRotX.m[2][2] = cosf(m_theta * 0.5f);
	matRotX.m[3][3] = 1;

	//rendering loop
	for(auto i : m_meshCube.tris)
	{
		triangulo triProj;		//triangulos ya proyectados
		triangulo triTran;		//triangulos trasladados
		triangulo triRotZ;		//triangulos rotados en z
		triangulo triRotZX; 	//triangulos rotados en x y z


		//primero rotamos el cubo
		multMatrizVector(i.p[0], triRotZ.p[0], matRotZ);
		multMatrizVector(i.p[1], triRotZ.p[1], matRotZ);
		multMatrizVector(i.p[2], triRotZ.p[2], matRotZ);

		multMatrizVector(triRotZ.p[0], triRotZX.p[0], matRotX);
		multMatrizVector(triRotZ.p[1], triRotZX.p[1], matRotX);
		multMatrizVector(triRotZ.p[2], triRotZX.p[2], matRotX);

		//ahora vamos a transladar el cubo
		triTran = triRotZX;

		triTran.p[0].z = triRotZX.p[0].z + 3.0f;
		triTran.p[1].z = triRotZX.p[1].z + 3.0f;
		triTran.p[2].z = triRotZX.p[2].z + 3.0f;

		//aplicamos la proyeccion para crear un espacio tridimensional
		//en una pantalla bidimensional
		multMatrizVector(triTran.p[0], triProj.p[0], m_matProj);
		multMatrizVector(triTran.p[1], triProj.p[1], m_matProj);
		multMatrizVector(triTran.p[2], triProj.p[2], m_matProj);

		//redimensionar el cubo
		triProj.p[0].x += 1.0f;
		triProj.p[0].y += 1.0f;
		triProj.p[1].x += 1.0f;
		triProj.p[1].y += 1.0f;
		triProj.p[2].x += 1.0f;
		triProj.p[2].y += 1.0f;

		triProj.p[0].x *= 0.5f * static_cast<float>(getWidth());
		triProj.p[0].y *= 0.5f * static_cast<float>(getWidth());
		triProj.p[1].x *= 0.5f * static_cast<float>(getWidth());
		triProj.p[1].y *= 0.5f * static_cast<float>(getWidth());
		triProj.p[2].x *= 0.5f * static_cast<float>(getWidth());
		triProj.p[2].y *= 0.5f * static_cast<float>(getWidth());

		//ahora si podemos dibujarlo
		DibujaTriangulo(triProj.p[0].x, triProj.p[0].y, triProj.p[1].x, triProj.p[1].y, triProj.p[2].x, triProj.p[2].y);
	}

	return true;
}

void Engine3D::multMatrizVector(vec3d &a, vec3d &b, mat4 &m)
{
	b.x = (a.x * m.m[0][0]) + (a.y * m.m[1][0]) + (a.z * m.m[2][0]) + m.m[3][0];
	b.y = (a.x * m.m[0][1]) + (a.y * m.m[1][1]) + (a.z * m.m[2][1]) + m.m[3][1];
	b.z = (a.x * m.m[0][2]) + (a.y * m.m[1][2]) + (a.z * m.m[2][2]) + m.m[3][2];

	float w{ (a.x * m.m[0][3]) + (a.y * m.m[1][3]) + (a.z * m.m[2][3]) + m.m[3][3] };

	if(w != 0.0f)
	{
		b.x /= w;
		b.y /= w;
		b.z /= w;
	}
}
