/*Tarea 2: Programa para comparar planificadores
creado por Luis Moreno y Angel Ramírez Ceseña */

#include <stdio.h>
#include <stdlib.h>
#include <windows.h>


int numProceso=0;

struct procesos
{
	char identificador; //identifica el proceso
	int tiempoLlegada; //tiempo en que llega cada proceso
	int tiempoEjecucion; //tiempo que tarda en ejecutarse cada proceso
};


void crearProceso( struct procesos * ptrP1) //Inicializo mis procesos
{

	int i;
	
	for (i=0;i<5;i++)
	{
		ptrP1[i].identificador = 'X'; //asigno un id temporal a mi estructura
		ptrP1[i].tiempoLlegada = (rand() % 10) + 1; // asigno un tiempo de llegada random
		ptrP1[i].tiempoEjecucion = (rand() % 15) + 1; //asigno un tiempo de ejecucion Random
		
	}	

	//printf("\n\t %d, %d, %d", ptrP1.identificador, ptrP1.tiempoLlegada, ptrP1.tiempoEjecucion );
	
	//return ptrP1;	
}



void AcomodarCola(struct procesos *cola)  // funcion que acomoda mi arreglo de estructura de menor a mayor, por su tiempo de llegada
{
	struct procesos aux;
	int i, j, burbuja;
	
	for( burbuja=0;burbuja<5;burbuja++)
	{
		for(i=0; i<4; i++)
		{
			for(j=i+1; j<5; j++)
			{
				if(cola[i].tiempoLlegada > cola[j].tiempoLlegada)
				{
					aux=cola[i];
					cola[i]=cola[j];
					cola[j]=aux;
				}
			}
		}
	}
	

	cola[0].identificador = 'A'; //asigno un numero id a mis estructuras
	cola[1].identificador = 'B'; 
	cola[2].identificador = 'C';
	cola[3].identificador = 'D'; 
	cola[4].identificador = 'E'; 

}





void FCFS(struct procesos *cola) // algoritmo FCFS
{
	int tT= cola[0].tiempoEjecucion + cola[1].tiempoEjecucion + cola[2].tiempoEjecucion + cola[3].tiempoEjecucion + cola[4].tiempoEjecucion;  //Tiempo total
	int contador= cola[0].tiempoLlegada;
	int i;
	int tE= cola[0].tiempoLlegada;  //sumador de tiempos para ir moviendo el arreglo
	int T=0;	//Suma de T
	int t=0;	//Tiempo de Respuesta
	int E=0;	//Suma de E
	int e=0;	//Tiempo de Espera
	float P=0;	//Suma de P
	float p=0;	//Proporcion de Penalizacion
	
	printf("\n\n\t FCFS: ");
	for(i=0; i<5; i++)
		{
			tE= tE + cola[i].tiempoEjecucion;
			
			do{	 //Imprimimos nuestra ejecución
				
				contador++;
				printf("%c",cola[i].identificador);
			}while (tE > contador );
			
			
			t=(tE - cola[i].tiempoLlegada);
			//printf("-%d,",t);
			T= T + t;                      //suma de todas las T
			e= (t - cola[i].tiempoEjecucion);
			//printf("%d,",e);
			E= E + e;						//suma de todas las E
			p=(float) t/cola[i].tiempoEjecucion;
			//printf("%.2f-",p);
			P= P + p;						//suma de todas las P
			
		}
	

	float PT= (float)T/5; //promedio de T
	float PE= (float)E/5; //promedio de E
	float PP= (float)P/5; //promedio de P
	


	printf("\n\t FCFS: T= %.2f, E= %.2f, P=%.2f \n\n", PT, PE, PP);

}



void rondaUno (struct procesos * cola)
{
	int timer = 0; //Para llevar la cuenta de cuantos ticks he ejecutado en total
	int ticks[5]; //Respaldo de los ticks a ejecutar de cada proceso
	int i;
	int termina[5];
	short int NOP = 1; //Bandera que en 1 indica que no se realizo ninguna operacion
	
	int T=0;
	int E=0;
	float P=0, PT, PE, PP;
	
	
	for(i=0;i<5;i++)
	{
		ticks[i]=cola[i].tiempoEjecucion; //Guardo el numero de ticks que tiene cada proceso
	}
	
	do
	{
		
		
		if (timer >= cola[0].tiempoLlegada && ticks[0]>0) //Si ya llego mi proceso y aun tiene ticks por ejecutar
		{	
			printf("A"); //Ejecuto mi proceso 1 vez
			ticks[0]--; //y ahora tiene 1 tick menos que ejecutar
			
			if(ticks[0] == 0) //Si ya no hay ticks
			{
				termina[0] = timer; //Guardo el momento en que termino mi proceso
			}
			
			timer++;	//esto me llevo 1 tick en ejecutarse
			NOP = 0;	//Pongo en 0 m bandera porque ya hice una operación
		}
		
		if (timer >= cola[1].tiempoLlegada && ticks[1]>0) //lo mismo que el IF de arriba pero para el 2do proceso
		{	
			printf("B");
			ticks[1]--;
			
			if(ticks[1] == 0)
			{
				termina[1] = timer;
			}
			
			timer++;
			NOP = 0;	
		}
		
		if (timer >= cola[2].tiempoLlegada && ticks[2]>0) //Ahora el 3ro
		{	
			printf("C");
			ticks[2]--;
			
			if(ticks[2] == 0)
			{
				termina[2] = timer;
			}
			
			timer++;
			NOP = 0;	
		}
		
		
		if (timer >= cola[3].tiempoLlegada && ticks[3]>0) //4to
		{	
			printf("D");
			ticks[3]--;
			
			if(ticks[3] == 0)
			{
				termina[3] = timer;
			}
			
			timer++;
			NOP = 0;	
		}
		
		if (timer >= cola[4].tiempoLlegada && ticks[4]>0) //5to
		{	
			printf("E");
			ticks[4]--;
			
			if(ticks[4] == 0)
			{
				termina[4] = timer;
			}
			
			timer++;
			NOP = 0;	
		}
		
		if( NOP == 1) //Si no se realizo ninguna operación
		{
			timer++; //aumenta el timer (para no caer en un loop infinito)
		}
		NOP = 1; //reseteo mi bandera
		
	}while( (ticks[0]+ticks[1]+ticks[2]+ticks[3]+ticks[4]) != 0 );
	
	for( i=0;i<5;i++) //Calculo los valores de mi ronda
	{
		T = T + (termina[i]-cola[i].tiempoLlegada);
		E = E + (termina[i]-cola[i].tiempoLlegada) - cola[i].tiempoEjecucion;
		P = P + (float) (termina[i]-cola[i].tiempoLlegada)/cola[i].tiempoEjecucion;
	}
	
	
	PT= (float)T/5; //promedio de T
	PE= (float)E/5; //promedio de E
	PP= (float)P/5; //promedio de P
	


	printf("\n\t Ronda1: T= %.2f, E= %.2f, P=%.2f \n\n", PT, PE, PP);
	
}


void rondaCuatro (struct procesos * cola) //igual a la funcion RondaUno, sólo tiene un loop para repetir 4 veces las instrucciones en cada if
{
	int timer = 0; //Para llevar la cuenta de cuantos ticks he ejecutado en total
	int ticks[5]; //Respaldo de los ticks a ejecutar de cada proceso
	int i,x;
	int termina[5];
	short int NOP = 1; //Bandera que en 1 indica que no se realizo ninguna operacion
	
	int T=0;
	int E=0;
	float P=0, PT, PE, PP;
	
	
	for(i=0;i<5;i++)
	{
		ticks[i]=cola[i].tiempoEjecucion; //Guardo el numero de ticks que tiene cada proceso
	}
	
	do
	{
		
		
		if (timer >= cola[0].tiempoLlegada && ticks[0]>0) //Si ya llego mi proceso y aun tiene ticks por ejecutar
		{	
			x=0;
			do
			{
				printf("A"); //Ejecuto mi proceso 1 vez
				ticks[0]--; //y ahora tiene 1 tick menos que ejecutar
			
				if(ticks[0] == 0) //Si ya no hay ticks
				{
					termina[0] = timer; //Guardo el momento en que termino mi proceso
				}
			
				timer++;	//esto me llevo 1 tick en ejecutarse
				NOP = 0;	//Pongo en 0 m bandera porque ya hice una operación
				x++;
				
			}while(x<4 && ticks[0] >0); //Repito todo 4 veces o hasta que se me acaben los ticks del proceso
		}
		
		if (timer >= cola[1].tiempoLlegada && ticks[1]>0) //lo mismo que el IF de arriba pero para el 2do proceso
		{	
			x=0;
			do
			{
				printf("B");
				ticks[1]--;
			
				if(ticks[1] == 0)
				{
					termina[1] = timer;
				}
			
				timer++;
				NOP = 0;	
				x++;
				
			}while(x<4 && ticks[1] >0); //Repito todo 4 veces o hasta que se me acaben los ticks del proceso
		}
		
		if (timer >= cola[2].tiempoLlegada && ticks[2]>0) //Ahora el 3ro
		{	
			x=0;
			do
			{
				printf("C");
				ticks[2]--;
			
				if(ticks[2] == 0)
				{
					termina[2] = timer;
				}
			
				timer++;
				NOP = 0;	
				x++;
				
			}while(x<4 && ticks[2] >0); //Repito todo 4 veces o hasta que se me acaben los ticks del proceso
		}
		
		
		if (timer >= cola[3].tiempoLlegada && ticks[3]>0) //4to
		{	
			x=0;
			do
			{
				printf("D");
				ticks[3]--;
			
				if(ticks[3] == 0)
				{
					termina[3] = timer;
				}
			
				timer++;
				NOP = 0;
				x++;
				
			}while(x<4 && ticks[3] >0); //Repito todo 4 veces o hasta que se me acaben los ticks del proceso	
		}
		
		if (timer >= cola[4].tiempoLlegada && ticks[4]>0) //5to
		{
			x=0;
			do
			{
				printf("E");
				ticks[4]--;
			
				if(ticks[4] == 0)
				{
					termina[4] = timer;
				}
			
				timer++;
				NOP = 0;
				x++;
					
			}while(x<4 && ticks[4] >0); //Repito todo 4 veces o hasta que se me acaben los ticks del proceso		
		}
		
		if( NOP == 1) //Si no se realizo ninguna operación
		{
			timer++; //aumenta el timer (para no caer en un loop infinito)
		}
		NOP = 1; //reseteo mi bandera
		
	}while( (ticks[0]+ticks[1]+ticks[2]+ticks[3]+ticks[4]) != 0 );
	
	for( i=0;i<5;i++) //Calculo los valores de mi ronda
	{
		T = T + (termina[i]-cola[i].tiempoLlegada);
		E = E + (termina[i]-cola[i].tiempoLlegada) - cola[i].tiempoEjecucion;
		P = P + (float) (termina[i]-cola[i].tiempoLlegada)/cola[i].tiempoEjecucion;
	}
	
	
	PT= (float)T/5; //promedio de T
	PE= (float)E/5; //promedio de E
	PP= (float)P/5; //promedio de P
	


	printf("\n\t Ronda4: T= %.2f, E= %.2f, P=%.2f \n\n", PT, PE, PP);
	
}


void AcomodarColaDos(struct procesos *cola)  // Ahora acomodamos la cola de menor a mayor, basandonos en el tiempo de ejecucion
{
	struct procesos aux;
	int i, j, burbuja;
	
	for( burbuja=0;burbuja<5;burbuja++)
	{
		for(i=0; i<4; i++)
		{
			for(j=i+1; j<5; j++)
			{
				if(cola[i].tiempoEjecucion > cola[j].tiempoEjecucion)
				{
					aux=cola[i];
					cola[i]=cola[j];
					cola[j]=aux;
				}
			}
		}
	}

}

void SPN(struct procesos *cola) // Reusamos el algoritmo del FCFS, sólo que la cola esta reacomodada para imprimir 1ro el de menor tiempo de Ejecucion
{
	int tT= cola[0].tiempoEjecucion + cola[1].tiempoEjecucion + cola[2].tiempoEjecucion + cola[3].tiempoEjecucion + cola[4].tiempoEjecucion;  //Tiempo total
	int contador= cola[0].tiempoLlegada;
	int i;
	int tE= cola[0].tiempoLlegada;  //sumador de tiempos para ir moviendo el arreglo
	int T=0;	//Suma de T
	int t=0;	//Tiempo de Respuesta
	int E=0;	//Suma de E
	int e=0;	//Tiempo de Espera
	float P=0;	//Suma de P
	float p=0;	//Proporcion de Penalizacion
	
	printf("\n\n\t SPN: ");
	for(i=0; i<5; i++)
		{
			tE= tE + cola[i].tiempoEjecucion;
			
			do{	 //Imprimimos nuestra ejecución
				
				contador++;
				printf("%c",cola[i].identificador);
			}while (tE > contador );
			
			
			t=(tE - cola[i].tiempoLlegada);
			//printf("-%d,",t);
			T= T + t;                      //suma de todas las T
			e= (t - cola[i].tiempoEjecucion);
			//printf("%d,",e);
			E= E + e;						//suma de todas las E
			p=(float) t/cola[i].tiempoEjecucion;
			//printf("%.2f-",p);
			P= P + p;						//suma de todas las P
			
		}
	

	float PT= (float)T/5; //promedio de T
	float PE= (float)E/5; //promedio de E
	float PP= (float)P/5; //promedio de P
	


	printf("\n\t SPN: T= %.2f, E= %.2f, P=%.2f \n\n", PT, PE, PP);

}


int main (void)
{
	
	struct procesos proc[5];
	int i=0,y;
	srand( time(0) );

	printf("\n\t Bienvenido a nuestro programa de COMPARADOR DE PLANIFICADORES");	
	
	for(y=0;y<4;y++)
	{
	
		printf("\n\n\t ==== Pasada %d ====\n\t",y+1);
		
		
		crearProceso(proc); //Inicializo mis procesos
		AcomodarCola(proc); //Los acomodo de menor a mayor de acuerdo a su tiempo de llegada
		
		for(i=0;i<5;i++) //imprimo la información de los procesos creados
		{
			printf(" %c: %d, t= %i;",proc[i].identificador,proc[i].tiempoLlegada, proc[i].tiempoEjecucion);
		}
	
		FCFS(proc);
	
		printf("\n\n\t Ronda1: ");
		rondaUno(proc);

		printf("\n\n\t Ronda4: ");
		rondaCuatro(proc);
	
		AcomodarColaDos(proc); //Reacomodo mi cola para que vaya de menor a mayor de acuerdo a su tiempo de ejecución
		SPN(proc);
	}
	
	printf("\n\n\t Presiona ENTER para terminar...");
	fflush(stdin);
	getchar();
	return 0;
}

