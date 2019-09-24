#include "proc.h"

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
	std::cout << "\tEmpezando a ejecutar el proceso P" << m_num << " con un tiempo esperado de ejecucion de " << m_t << " llevamos esperando " << m_e << std::endl << std::flush;
	std::cout << "\tResultados de P" << m_num << "\tT:" << std::setw(m_w) << m_e << "\tE:" << std::setw(m_w) << m_e
			<< "\tP:" << std::setw(m_w) << m_pen << "\tR:" << std::setw(m_w) << m_res
			<< std::endl << std::endl << std::flush;
}

void Proc::exec(size_t tn, size_t *fal)
{
	if(*fal == 0)
	{
		std::cout << std::endl << "\tTerminando P" << m_num << std::endl << std::flush;

		return;
	}
	else if(tn < m_t)
	{
		std::cout << std::endl << "\tP" << m_num <<" tiempo requerido m_t: " << m_t << " quantum tn: " << tn << " falta: " << *fal << std::endl << std::flush;

		*fal = (m_t - tn);

		std::cout << std::endl << "\tP" << m_num << " fal: " << *fal << std::endl << std::flush;
	}

	for (size_t a{ 0 }; a < tn, a < m_t; ++a)
	{
		if(*fal >0 )
		{
			--*fal;
		}
		else
		{
			*fal = 0;
			break;
		}

		std::cout << "\n\tProcesando P" << m_num << " por " << tn << " segundos... m_t: " << m_t << " falta: " << *fal << std::endl << std::flush;
		sleep(tn);
	}

	*fal = 0;

	std::cout << std::endl << "\tTerminando P" << m_num << std::endl << std::flush;
}

