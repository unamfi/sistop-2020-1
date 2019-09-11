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

size_t num_rand(size_t a, size_t b)
{	
	return ((rand() % (b - a + 1)) - 1);
}

void *comer()
{
	const size_t tiempo = num_rand(2, 5);
	
	printf("\n\tComiendo... \n\tAhora durmiendo por %zu segundos.", tiempo);
	sleep(tiempo);
	
}

void *gato_come(pthread_t *n)
{
	//empiezo a comer
	//si veo raton me lo como primero
	//si no hay ratones voy directo a comer
}

void *raton_come(pthread_t *n)
{
	//si no hay gatos como
	//si si huyo
}

int main(void)
{
	srand(time(0));
	pthread_t id;
	pthread_t id_2;
	
	size_t gatos = num_rand(10, 40);
	size_t raton = num_rand(10, 40);
	size_t platos = num_rand(10, 40); //necesitan mutex
	
	size_t *a_gatos = (size_t *)calloc(gatos, sizeof(gatos));
	size_t *a_ratones = (size_t *)calloc(raton, sizeof(raton));
	Plato *a_platos = (Plato *)calloc(platos, sizeof(Plato));
	
	for(size_t i = 0; i < gatos; ++i)
	{
		pthread_create(&id, NULL, gato_come, (void *)&id);
	}
	
	for(size_t j = 0; j < raton; ++j)
	{
		pthread_create(&id_2, NULL, raton_come, (void *)&id);
	}
	
	free(a_gatos);
	free(a_ratones);
	free(a_platos);
	
	pthread_exit(NULL);
	printf("\n\n");
	
	return 0;
}