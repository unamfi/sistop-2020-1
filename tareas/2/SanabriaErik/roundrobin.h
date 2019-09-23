#ifndef ROUNDROBIN_H_
#define ROUNDROBIN_H_

#include <vector>
#include <stdexcept>

#include "proc.h"

class RoundRobin
{
public:
	RoundRobin(size_t n, size_t nProcs);
	virtual ~RoundRobin();

	void run();

	void add(const Proc& proc);

	void remove(const Proc& proc);

	Proc& siguitente();

private:

	//Funcion que genera numeros aleatorios
	//estos van a representar los tiempos
	size_t randomN();

	const size_t m_tiem_a{ 5 };
	size_t m_num_proc;

	std::vector<Proc> m_procs;
	std::vector<Proc>::iterator m_it_pos;
};

#endif /* ROUNDROBIN_H_ */
