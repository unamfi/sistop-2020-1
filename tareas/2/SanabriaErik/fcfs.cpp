#include "fcfs.h"

FCFS::FCFS()
{
	m_num_proc = 0;
}

FCFS::FCFS(size_t n)
{
	m_num_proc = n;
}

FCFS::~FCFS()
{

}

void FCFS::run()
{
	size_t prev{ 0 };

	std::cout << "\n\tNumero de procesos: " << m_num_proc << "\n";

	//creando fila de procesos
	for (size_t v{ 0 }; v < m_num_proc; ++v)
	{
		sleep(5);
		size_t tiem{ randomN() };
		Proc A(tiem, v, prev);

		prev += tiem;

		m_proc.push(A);
	}

	prev = 0;
	//ahora si a ejecutarlos
	for (size_t n{ 0 }; n < m_num_proc; ++n)
	{
		Proc B = m_proc.front();
		B.exec();

		m_proc.pop();
	}

	std::cout << "\n\tDone\n";
}

size_t FCFS::randomN()
{
	srand(time(NULL));

	size_t m = ((rand() % (8 - 4 + 1)) + 4);

	return m;
}
