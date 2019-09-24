#include "roundrobin.h"

RoundRobin::RoundRobin(size_t n)
{
	m_num_proc = n;
}

void RoundRobin::run()
{

	size_t prev{ 0 };

	std::cout << "\n\tNumero de procesos: " << m_num_proc << std::endl << std::flush;

	for(size_t a{ 0 }; a < m_num_proc; ++a)
	{
		sleep(5);

		size_t tiem{ randomN() };

		Proc A(tiem, a, 0);

		//prev += tiem;

		m_procs.push(A);
	}

	prev = 0;

	size_t f{ m_tiem_a };		//cuanto falta, empieza como maximo tiempo posible
	size_t acper{ 0 };			//tiempo acumulado perdido

	std::cout << std::endl <<"::run() f: " << f << std::endl << std::flush;

	for(size_t a{ 0 }; a < m_num_proc, a < m_procs.size(); ++a)
	{
		Proc A = m_procs.front();

		A.exec(m_tiem_a, &f);

		//no termino de ejecutarse
		if(f > 0)
		{
			//reordenalo al principio
			m_procs.push(A);

			//y
		}
		else if(f == 0)
		{
			//si ya no le falta nada quitalo.
			m_procs.pop();
		}

		std::cout << std::endl << "\ta: " << a << " m_num_proc: " << m_num_proc << " size: " << m_procs.size() << " f: " << f << std::flush;
	}

}

size_t RoundRobin::randomN()
{
	srand(time(NULL));

	//generando numero aleatorio entre 2 y 10
	size_t m = ((rand() % (10 - 2 + 1)) + 4);

	return m;
}


