#ifndef PROC_H_
#define PROC_H_

#include <iostream>
#include <iomanip>

class Proc
{
public:
	Proc();
	Proc(size_t a, size_t n, size_t m);

	void exec();

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
