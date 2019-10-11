#include "proc.h"

Proc::Proc(size_t a, size_t n, size_t m)
{
	m_t = a;
	m_num = n;
	m_e = m;
	m_t2 = m + a;
	m_pen = 0.0f;
	m_res = 0.0f;
	m_falta = a;
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
	if(m_falta == 0)
	{
		std::cout << std::endl << "\tTerminando P" << m_num << std::endl << std::flush;

		return;
	}
	else if(tn < m_t)
	{
		std::cout << std::endl << "\tP" << m_num << "procesando por "
				<< tn << " segundos... de un tiempo requerido: " << m_t
				<< std::endl << std::flush;

		sleep(tn);
		m_falta -= tn;

		std::cout << std::endl << "\tA P" << m_num << " le faltan: " << *fal  << " segundos y hemos perdido: "
				<< /*m_tperd <<*/ std::endl << std::flush;

		return;
	}
}

bool Proc::falta(void)
{
	if( m_falta > 0 )
	{
		return true;
	}
	else if(m_falta == 0)
	{
		return false;
	}
}

