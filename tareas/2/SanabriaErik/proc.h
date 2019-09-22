#ifndef PROC_H_
#define PROC_H_

#include <iostream>
#include <iomanip>

//objeto proceso
class Proc
{
public:
	Proc();

	//a: tiempo ideal
	//n: numero de proceso
	//m: tiempo que se ha esperado acumulado
	Proc(size_t a, size_t n, size_t m);

	//es la ejecucion del proceso como tal
	void exec();

	//destructor default
	virtual ~Proc();

private:

	const int m_w{ 3 };	//para setw
	size_t m_num;		//numero de proceso
	size_t m_t;			//tiempo ideal
	size_t m_t2;		//tiempo de respuesta
	size_t m_e;			//tiempo en espera
	float m_pen;		//proporcion de penalizacion
	float m_res;		//proporcion de respuesta
};

#endif /* PROC_H_ */
