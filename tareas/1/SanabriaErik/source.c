#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <pthread.h>
#include <stdbool.h>

typedef struct
{
	size_t n;
	bool en_uso;
	
}Plato;

typedef struct
{
	pthread_t id;
	bool comiendo;
	void* func;
}Animal;

size_t num_rand(size_t a, size_t b)
{	
	return ((rand() % (b - a + 1)) - 1);
}

void *comer(pthread_t* m)
{
	const size_t tiempo = num_rand(2, 5);
	
	printf("\n\tComiendo... \n\tAhora durmiendo por %zu segundos.", tiempo);
	sleep(tiempo);
	
}

void *gato_come(pthread_t* n, void(*comer)(pthread_t* m))
{
	printf("\n\tGato comiendo en Thread ID: %d", *n); 
	//empiezo a comer
	//si veo raton me lo como primero
	//si no hay ratones voy directo a comer
}

void *raton_come(pthread_t* n, void(*comer)(pthread_t* m))
{
	printf("\n\tRaton comiendo en Thread ID: %d", *n); 
	//si no hay gatos como
	//si si huyo
}

int main(void)
{
	srand(time(0));
	
	size_t gatos = num_rand(10, 40);
	size_t raton = num_rand(10, 40);
	size_t platos = num_rand(10, 40); //necesitan mutex
	
	Animal *a_gatos = (Animal*)calloc(gatos, sizeof(Animal));
	Animal *a_ratones = (Animal*)calloc(raton, sizeof(Animal));
	Plato *a_platos = (Plato*)calloc(platos, sizeof(Plato));
	
	printf("\n\tCreando %zu gatos, %zu ratones y %zu platos.\n", gatos, raton, platos);
	
	for(size_t i = 0; i < gatos; ++i)
	{
		pthread_create(&(a_gatos[i].id), NULL, gato_come, (void*)&(a_gatos[i].id));
	}
	
	for(size_t j = 0; j < raton; ++j)
	{
		pthread_create(&(a_ratones[j].id), NULL, raton_come, (void *)&(a_ratones[j].id));
	}
	
	free(a_gatos);
	free(a_ratones);
	free(a_platos);
	
	pthread_exit(NULL);
	fflush(stdout);
	printf("\n\n");
	
	return 0;
}