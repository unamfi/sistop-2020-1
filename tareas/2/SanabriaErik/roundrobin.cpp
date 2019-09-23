#include "roundrobin.h"

RoundRobin::RoundRobin(size_t n, size_t nProcs)
{
	m_procs.reserve(n);
	m_it_pos = std::begin(m_procs);
	m_num_proc = nProcs;
}

void RoundRobin::run()
{

	size_t prev{ 0 };

	std::cout << "\n\tNumero de procesos: " << m_num_proc << "\n";

	for(size_t a{ 0 }; a < m_num_proc; ++a)
	{
		sleep(5);

		size_t tiem{ randomN() };

		Proc A(tiem, a, prev);

		prev += tiem;

		add(A);
	}

	prev = 0;

	size_t f{ m_tiem_a };		//cuanto falta, empieza como maximo tiempo posible

	for(size_t a{ 0 }; a < m_num_proc, a < m_procs.size(); ++a)
	{
		Proc A = siguitente();

		A.exec(m_tiem_a, &f);

		if(f == 0)
		{
			remove(A);
		}
	}

}

void RoundRobin::add(const Proc& proc)
{
	size_t pos{ m_it_pos - std::begin(m_procs) };

	m_procs.push_back(proc);

	m_it_pos = std::begin(m_procs) + pos;
}

Proc& RoundRobin::siguitente()
{
	if(m_procs.empty())
	{
		throw std::out_of_range("No hay elementos!!!");
	}
	else if(!m_procs.empty())
	{
		//std::vector<Proc>::iterator&
		auto& retornar = *m_it_pos;

		++m_it_pos;

		if(m_it_pos == std::end(m_procs))
		{
			m_it_pos = std::begin(m_procs);
		}

		return retornar;
	}
}

void RoundRobin::remove(const Proc& proc)
{
	std::vector<Proc>::iterator p_it{ std::begin(m_procs) };

	for(/*auto p_it = std::begin(m_procs)*/; p_it != std::end(m_procs); ++p_it)
	{
		if(*p_it == proc)
		{
			int n_pos{ 0 };

			if((m_it_pos == (std::end(m_procs) - 1)) && (p_it == m_it_pos))
			{
				n_pos = 0;
			}
			else if(m_it_pos <= p_it)
			{
				n_pos = m_it_pos - std::begin(m_procs);
			}
			else
			{
				n_pos = m_it_pos - std::begin(m_procs) - 1;
			}

			m_procs.erase(p_it);

			m_it_pos = std::begin(m_procs) + n_pos;

			return;
		}
	}
}

RoundRobin::~RoundRobin()
{
	m_procs.clear();
}

size_t RoundRobin::randomN()
{
	srand(time(NULL));

	//generando numero aleatorio entre 2 y 10
	size_t m = ((rand() % (10 - 2 + 1)) + 4);

	return m;
}


