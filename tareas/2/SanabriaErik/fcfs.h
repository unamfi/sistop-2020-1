#ifndef FCFS_H_
#define FCFS_H_

#include <queue>
#include <memory>

#include "proc.h"

class FCFS
{
public:
	FCFS();
	void enqueu(Proc p1);

	virtual ~FCFS();

	void run();

private:
	std::unique_ptr<std::queue<Proc>> m_procptr = std::make_unique<std::queue<Proc>>();
	//std::queue<Proc> m_proc;
};

#endif /* FCFS_H_ */
