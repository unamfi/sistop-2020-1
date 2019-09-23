#include "roundrobin.h"

RoundRobin::RoundRobin(size_t n)
{
	m_procs.reserve(n);
	m_it_pos = std::begin(m_procs);
}

void RoundRobin::run()
{

}

void RoundRobin::add(const Proc& proc)
{
	size_t pos{ m_it_pos - std::begin(m_procs) };

	m_procs.push_back(proc);

	m_it_pos = std::begin(m_procs) + pos;
}

void RoundRobin::remove(const Proc& proc)
{
	std::vector<Proc>::iterator p_it{ std::begin(m_procs) };

	for(/*auto p_it = std::begin(m_procs)*/; p_it != std::end(m_procs); ++p_it)
	{
		if(*p_it == proc)
		{
			int n_pos;

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

