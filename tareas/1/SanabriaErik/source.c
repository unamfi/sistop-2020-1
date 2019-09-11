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
	return ((rand() % (b - a + 1)) - 1);
}

bool *obtener_plato()
{
	return true;
}

void *comer(pthread_t* m)
{
	const size_t tiempo = num_rand(2, 5);
	
	printf("\n\tComiendo... \n\tAhora durmiendo por %zu segundos.", tiempo);
	fflush(stdout);
	sleep(tiempo);
	
}

void *gato_come(Argv* argv/*pthread_t* n, size_t num, void(*comer)(pthread_t* m)*/)
{
	size_t num = argv->m_num;
	pthread_t n = argv->m_id;
	printf("\n\tGato %zu comiendo en Thread ID: %d", num, n);
	fflush(stdout);
	
	//comer(n);
	//empiezo a comer
	//si veo raton me lo como y sigo comiendo
	//si no hay ratones voy directo a comer
}

void *raton_come(Argv* argv/*pthread_t* n, size_t num, void(*comer)(pthread_t* m)*/)
{
	size_t num = argv->m_num;
	pthread_t n = argv->m_id;	
	printf("\n\tRaton %zu comiendo en Thread ID: %d", num, n);
	fflush(stdout);
	//comer(n);
	//si no hay gatos como
	//si si huyo
}

int main(void)
{
	srand(time(0));
	
	const size_t gatos = num_rand(10, 40);
	const size_t raton = num_rand(10, 40);
	const size_t platos = num_rand(10, 40); //necesitan mutex
	
	Animal *a_gatos = (Animal*)calloc(gatos, sizeof(Animal));
	Animal *a_ratones = (Animal*)calloc(raton, sizeof(Animal));
	Plato *a_platos = (Plato*)calloc(platos, sizeof(Plato));
	
	printf("\n\tCreando %zu gatos, %zu ratones y %zu platos.\n", gatos, raton, platos);
	fflush(stdout);
	
	for(size_t i = 0; i < gatos; ++i)
	{
		Argv* argum = (Argv*)calloc(1, sizeof(Argv));
		argum->m_num = i;
		pthread_create(&(a_gatos[i].id), NULL, gato_come, (void*)&(argum));
		argum->m_id = a_gatos[i].id;
		free(argum);
	}
	
	for(size_t j = 0; j < raton; ++j)
	{
		Argv* argum_2 = (Argv*)calloc(1, sizeof(Argv));
		argum_2->m_num = j;
		pthread_create(&(a_ratones[j].id), NULL, raton_come, (void *)&(argum_2));
		argum_2->m_id = a_ratones[j].id;
		free(argum_2);
	}
	
	free(a_gatos);
	free(a_ratones);
	free(a_platos);
	
	pthread_exit(NULL);
	
	printf("\n\n\n");
	fflush(stdout);
	
	return 0;
}