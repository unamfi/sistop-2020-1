#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>

#define LOOP 1000
static void * sumando_1(void* arg);
static void * sumando_2(void* arg);
static int contador = 0;

sem_t *sem1;

int main(void){
	pthread_t hilo_1 , hilo_2;
	
	sem_open("/sem1",O_CREAT,0644,1);
	
	pthread_create(&hilo_1, NULL, *sumando_1 ,NULL);
	pthread_create(&hilo_2, NULL, *sumando_2 ,NULL);
	
	pthread_join(hilo_1, NULL);
	pthread_join(hilo_2, NULL);
	
	printf("Valor del contador %d \n", contador);

	return 0;
}


static void * sumando_1(void* arg)
{
	for(int i = 0 ; i < LOOP ; i++)
	{
		sem_close(sem1);
		contador += 1 ;
		sem_unlink("/sem1");
	}	
}

static void * sumando_2(void* arg)
{       
        for(int i = 0 ; i < LOOP ; i++)
        {	
		sem_close(sem1);
                contador -= 1 ;
                sem_unlink("/sem1");
	}
}
