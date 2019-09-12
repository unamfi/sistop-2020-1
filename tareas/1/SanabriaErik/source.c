#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
#include <pthread.h>
#include <stdbool.h>

typedef struct
{
	pthread_t m_id;
	size_t m_num;
	//function pointer
}Argv;

typedef struct
{
	size_t n;
	size_t total;
	bool en_uso;
}Plato;

typedef struct
{
	pthread_t id;
	bool comiendo;
}Animal;

size_t num_rand(size_t a, size_t b)
{	
	return ((rand() % (b - a + 1)) + a);
}

bool *obtener_plato()
{
	return true;
}

void *comer(pthread_t* m)
{
	const size_t tiempo = num_rand(2, 5);
	
	printf("\n\tComiendo... \n\tAhora durmiendo por %zu segundos.", tiempo);
	sleep(tiempo);
	
}

void *gato_come(pthread_t* n)
{
	size_t num = 5;//argv->m_num;
	//pthread_t n = argv->m_id;
	printf("\n\tGato %zu comiendo en Thread ID: %d", num, *n);
}

void *raton_come(Argv* argv)
{
	size_t num = argv->m_num;
	pthread_t n = argv->m_id;	
	printf("\n\tRaton %zu comiendo en Thread ID: %d", num, n);
}

int main(void)
{
	srand(time(0));
	
	const size_t gatos = num_rand(10, 40);
	const size_t raton = num_rand(10, 40);
	const size_t platos = num_rand(10, 40); //necesitan mutex
	//https://www.cs.cmu.edu/afs/cs/academic/class/15492-f07/www/pthreads.html
	
	Animal *a_gatos = (Animal*)calloc(gatos, sizeof(Animal));
	Animal *a_ratones = (Animal*)calloc(raton, sizeof(Animal));
	Plato *a_platos = (Plato*)calloc(platos, sizeof(Plato));
	
	printf("\n\tCreando %zu gatos, %zu ratones y %zu platos.\n", gatos, raton, platos);
	
	for(size_t i = 0; i < gatos; ++i)
	{
		Argv* argum = (Argv*)calloc(1, sizeof(Argv));
		argum->m_num = i;
		pthread_create(&a_gatos[i].id, NULL, gato_come, (void*)&(a_gatos[i].id));
		argum->m_id = a_gatos[i].id;
		free(argum);
	}
	
	/*for(size_t j = 0; j < raton; ++j)
	{
		Argv* argum_2 = (Argv*)calloc(1, sizeof(Argv));
		argum_2->m_num = j;
		pthread_create(&(a_ratones[j].id), NULL, raton_come, (void*)&argum_2);
		argum_2->m_id = a_ratones[j].id;
		free(argum_2);
	}*/
	

	
	for(size_t k = 1; k < gatos; ++k)
	{
		printf("\n\tUniendo hilo %zu: %d", k, a_gatos[k].id);
		pthread_join(&a_gatos[k].id, NULL);
	}
	
	free(a_gatos);
	free(a_ratones);
	free(a_platos);
	
	printf("\n\n\n");
	
	return 0;
}