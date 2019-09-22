#ifndef FCFS_H_
#define FCFS_H_

#include <queue>
#include <ctime>
#include <unistd.h>

#include "proc.h"

class FCFS
{
public:
	FCFS();
	FCFS(size_t n);

	virtual ~FCFS();

	void run();

private:

	size_t randomN();

	size_t m_num_proc;

	//std::unique_ptr<std::queue<Proc>> m_procptr = std::make_unique<std::queue<Proc>>();
	std::queue<Proc> m_proc;
};

#endif /* FCFS_H_ */
