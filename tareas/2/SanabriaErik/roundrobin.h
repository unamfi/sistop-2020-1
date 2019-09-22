#ifndef ROUNDROBIN_H_
#define ROUNDROBIN_H_

#include <vector>

#include "proc.h"

class RoundRobin
{
public:
	RoundRobin(size_t n);
	virtual ~RoundRobin();

	void crea_Procs();

	void run();

private:
	std::vector<Proc> m_procs;
};

#endif /* ROUNDROBIN_H_ */
