#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

size_t num_rand()
{
	const size_t a = 10;	//minimo
	const size_t b = 50;	//maximo
	
	return ((rand() % (b - a + 1)) - 1);
}

void comer()
{
	const size_t tiempo = 6;
	
	printf("\n\tComiendo... \n\tAhora durmiendo por %zu segundos.", tiempo);
	sleep(tiempo);
	
}

void gato_come()
{
	//empiezo a comer
	//si veo raton me lo como primero
	//si no hay ratones voy directo a comer
}

void raton_come()
{
	//si no hay gatos como
	//si si huyo
}

int main(void)
{
	srand(time(0));
	
	size_t gatos = num_rand();
	size_t raton = num_rand();
	size_t platos = num_rand(); //necesitan mutex
	
	printf("\n\n");
	
	return 0;
}