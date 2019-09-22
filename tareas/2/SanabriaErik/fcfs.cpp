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
	//variable para guardar el acumulado del tiempo transcurrido
	size_t prev{ 0 };

	std::cout << "\n\tNumero de procesos: " << m_num_proc << "\n";

	//creando fila de procesos
	for (size_t v{ 0 }; v < m_num_proc; ++v)
	{
		//durmiendo 5 segundos para que
		//los numeros aleatorios que generemos
		//no sean iguales
		sleep(5);

		//a generar los tiempos asignados de los
		//procesos de forma aleatoria
		size_t tiem{ randomN() };

		//creando el proceso
		Proc A(tiem, v, prev);

		//contando el total de espera
		//que se va acumulando
		prev += tiem;

		//agregando el proceso a la cola
		m_proc.push(A);
	}

	//borrando variable por si acaso
	prev = 0;

	//ahora si a ejecutarlos
	for (size_t n{ 0 }; n < m_num_proc; ++n)
	{
		//obtenemos el proceso que esta en frente de la fila
		Proc B = m_proc.front();

		//lo ejecutamos
		B.exec();

		//como ya termino se va de la fila
		m_proc.pop();
	}

	std::cout << "\n\tDone\n";
}

size_t FCFS::randomN()
{
	srand(time(NULL));

	//generando numero aleatorio entre 2 y 10
	size_t m = ((rand() % (10 - 2 + 1)) + 4);

	return m;
}
