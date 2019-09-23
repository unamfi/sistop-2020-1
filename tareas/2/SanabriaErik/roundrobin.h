#ifndef ROUNDROBIN_H_
#define ROUNDROBIN_H_

#include <vector>

#include "proc.h"

class RoundRobin
{
public:
	RoundRobin(size_t n);
	virtual ~RoundRobin();

	void run();

	void add(const Proc& proc);

	void remove(const Proc& proc);

private:
	std::vector<Proc> m_procs;
	std::vector<Proc>::iterator m_it_pos;
};

#endif /* ROUNDROBIN_H_ */
