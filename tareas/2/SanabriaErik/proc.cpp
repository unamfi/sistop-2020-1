#include "proc.h"

Proc::Proc()
{
	m_num = 0;
	m_e = 0;
	m_pen = 0.0f;
	m_res = 0.0f;
	m_t = 0;
	m_t2 = 1;
}

Proc::Proc(size_t a, size_t n, size_t m)
{
	m_t = a;
	m_num = n;
	m_e = m;
	m_t2 = m + a;
	m_pen = 0.0f;
	m_res = 0.0f;
}

void Proc::exec()
{
	m_pen = m_t2 / m_t;		//Proporcion de penalizacion
	m_res = 1 / m_pen;		//Proporcion de respuesta
	std::cout << "\tEmpezando a ejecutar el proceso P" << m_num << " con un tiempo esperado de ejecucion de " << m_t << " llevamos esperando " << m_e << std::endl;
	std::cout << "\tResultados de P" << m_num << "\tT:" << std::setw(m_w) << m_e << "\tE:" << std::setw(m_w) << m_e
			<< "\tP:" << std::setw(m_w) << m_pen << "\tR:" << std::setw(m_w) << m_res
			<< std::endl << std::endl;
}

Proc::~Proc()
{

}

