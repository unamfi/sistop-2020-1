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

void *comer(pthread_t* m)
{
	const size_t tiempo = num_rand(2, 5);
	
	printf("\n\tComiendo... \n\tAhora durmiendo por %zu segundos.\n", tiempo);
	sleep(tiempo);
	
}

void *gato_come(void *argv)
{
	Argv *m_argv = argv;
	size_t t = ((rand() % (10 - 1 + 1)) + 1);
	printf("\n\tGato %zu comiendo en Thread ID: %ld durmiendo: %zu\n", m_argv->m_num, m_argv->m_id, t);
	sleep(t);
	printf("\n\tGato %zu despertando\n", m_argv->m_num);
}

void *raton_come(void *argv)
{
	Argv *m_argv = argv;
	size_t t = ((rand() % (15 - 1 + 1)) + 1);
	printf("\n\tRaton %zu comiendo en Thread ID: %ld y durmiendo: %zu\n", m_argv->m_num, m_argv->m_id, t);
	sleep(t);
	printf("\n\tRaton %zu despertando\n", m_argv->m_num);
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
		printf("\n\ti: %zu", i);
		pthread_create(&a_gatos[i].id, NULL, gato_come, (void*)argum);
		argum->m_id = a_gatos[i].id;
		printf("\n\tGato: argum m_num: %zu m_id: %ld\tId real: %ld\n", argum->m_num, argum->m_id, a_gatos[i].id);
		free(argum);
	}
	
	for(size_t j = 0; j < raton; ++j)
	{
		printf("\n\tj: %zu", j);
		Argv* argum_2 = (Argv*)calloc(1, sizeof(Argv));
		argum_2->m_num = j;
		pthread_create(&a_ratones[j].id, NULL, raton_come, (void*)argum_2);
		argum_2->m_id = a_ratones[j].id;
		printf("\n\tRaton: argum_2 m_num: %zu m_id: %ld\n", argum_2->m_num, a_ratones[j].id);
		free(argum_2);
	}

	/*for(size_t k = 0; k < gatos; ++k)
	{
		printf("\n\tUniendo hilo %zu: %d", k, a_gatos[k].id);
		pthread_join(&a_gatos[k].id, NULL);
	}*/
	
	free(a_gatos);
	free(a_ratones);
	free(a_platos);
	pthread_exit(NULL);
	
	return 0;
}
