#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <time.h>

size_t g = 0;
  
void *m_Fun(void *argv) 
{ 
	int *m_id = (int *)argv;

	static size_t s = 0; 
 
	++s;
	++g;

	printf("ID: %d, Static: %lu, Global: %lu\n", *m_id, ++s, ++g);
} 
  
int main() 
{ 
	pthread_t id;

	for (size_t i = 0; i < 3; i++) 
	{
		pthread_create(&id, NULL, m_Fun, (void *)&id);
	}

	sleep(5);

	printf("\n\tTerminando.\n\n");

	pthread_exit(NULL);
	return 0; 
} 
