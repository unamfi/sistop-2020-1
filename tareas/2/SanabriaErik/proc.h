#ifndef PROC_H_
#define PROC_H_

#include <iostream>
#include <iomanip>
#include <unistd.h>

//objeto proceso
class Proc
{
public:
	//a: tiempo ideal
	//n: numero de proceso
	//m: tiempo que se ha esperado acumulado
	Proc(size_t a, size_t n, size_t m);

	//es la ejecucion del proceso como tal
	void exec();

	//es la ejecucion del proceso para
	//round robin
	//tn: tiempo maximo asignado
	//fal: cuanto tiempo falta
	void exec(size_t tn, size_t *fal);

	bool falta(void);

	//destructor default
	~Proc() = default;

	bool operator==(const Proc& rhs)
	{
		return m_num == rhs.m_num;
	}

private:

	int m_w{ 3 };		//para setw
	size_t m_falta;		//cuanto le falta
	size_t m_num;		//numero de proceso
	size_t m_t;			//tiempo ideal
	size_t m_t2;		//tiempo de respuesta
	size_t m_e;			//tiempo en espera
	float m_pen;		//proporcion de penalizacion
	float m_res;		//proporcion de respuesta
};

#endif /* PROC_H_ */
