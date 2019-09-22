#ifndef FCFS_H_
#define FCFS_H_

#include <queue>
#include <ctime>
#include <unistd.h>

#include "proc.h"

//First Come Sirst Serve
class FCFS
{
public:
	//constructor estandar
	FCFS();

	//Constructor, n es numero de procesos
	FCFS(size_t n);

	//destructor default
	virtual ~FCFS();

	//Funcion principal para simular
	void run();

private:

	//Funcion que genera numeros aleatorios
	//estos van a representar los tiempos
	size_t randomN();

	//numero de procesos
	size_t m_num_proc;

	//cola de procesos
	std::queue<Proc> m_proc;
};

#endif /* FCFS_H_ */
