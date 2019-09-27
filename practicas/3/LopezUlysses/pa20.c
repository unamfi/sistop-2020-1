/*
	Program practice advance 20
	By Stephan Mario Olivares
	Threads 2 and structures
*/

#include <stdio.h>
#include <pthread.h>
#include <string.h>
#include <stdlib.h>

typedef struct fields{
	int a;
	float b;
	char name[32];
}Fields;

void *printMessage(void *);

int main(void){

	Fields *lol = (Fields *)malloc(sizeof(Fields));

	pthread_t thr;

	strcpy(lol->name, "Hello There");
	lol->a = 1;

	printf("\nSoy el hilo principal\n");

	pthread_create(&thr, NULL, printMessage, (void *)lol);

	pthread_join(thr, NULL);

	free(lol);
	return 0x0;
}//End of main

void *printMessage(void *param){

	Fields *p = (Fields *)param;

	printf("\nEl hilo principal dice: %s \nAnd we are number %i\n", p->name, p->a);

	pthread_exit(NULL);
}//End of printMessage
