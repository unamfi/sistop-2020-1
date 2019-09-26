#ifndef ROUNDROBIN_H_
#define ROUNDROBIN_H_

#include <queue>
#include <stdexcept>

#include "proc.h"

class RoundRobin
{
public:
	RoundRobin(size_t n);

	~RoundRobin() = default;

	void run();

private:

	//Funcion que genera numeros aleatorios
	//estos van a representar los tiempos
	size_t randomN();

	const size_t m_tiem_a{ 3 };					//tiempo permitido, el quantum
	size_t m_num_proc;							//numero de procesos

	std::queue<Proc> m_procs;					//cola de procesos
};

#endif /* ROUNDROBIN_H_ */
