#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>

char memory [31];
void beginmemory()
{
	int i = 0;
	int index = 0;
	while(i<30)
	{
		if(rand()%3==0)
		{
			int sizeSpace = rand()%4+2;
			int j = 0;
			for(j=0;j<sizeSpace;j++)
			{
				memory[i]='*';
				i++;
				if(i>=30) break;
			}
		}
		else
		{
			int sizeMemory = rand()%14+2;
			int j = 0;
			for(j=0;j<sizeMemory;j++)
			{
				memory[i] = 'A'+index;
				i++;
				if(i>=30) break;
			}
			index++;
		}
	}
	memory[30]='\0';
}

char newProcess()
{
	int i,j=0;
	for(i=0;i<30;i++)
	{
		if(memory[i]>j)
		{
			j=memory[i];
		}
	}
	return j+1;
}

int primerAjuste(int size)
{
	int i=0,j=0;
	for(i=0;i<30;i++)
	{
		if(memory[i]=='*')
		{
			j++;
			if(j==size) return i-size+1;
		}
		else
		{
			j=0;
		}
	}
	return -1;
}

void compactMemory()
{
	int i = 0;
	for(i=0;i<30;i++)
	{
		if(memory[i]=='*')
		{
			int j=i;
			while(j<30 && memory[j]=='*')
			{
				j++;
			}
			if(j<30)
			{
				memory[i] = memory[j];
				memory[j]='*';
			}
		}
	}
}

int main()
{
	char answer,end;
	int sizepro;
	srand(time(NULL));
	beginmemory();
	while(end != 'N'|| end != 'n')
	{
		printf("Asignación actual:\n%s\n",memory);
		printf("¿Qué acción desea realizar?\n\nAsignar --> A\t\tLiberar --> L\n\n");
		scanf("%s",&answer);
		if(answer == 'A')
		{
			char nameprocess = newProcess();
			printf("Indique el tamaño del nuevo %c proceso (El valor debe de ser de entre 2 y 15: \n",nameprocess);
			scanf("%i",&sizepro);
			while(sizepro<2 || sizepro>15)
			{
				printf("El tamaño del proceso debe de ser entre 2 y 15, vuelva a indicar el tamaño:\n");
				scanf("%i",&sizepro);
			}
			int placeinmem = primerAjuste(sizepro);
			if(placeinmem != -1)
			{
				int i=0;
				for(i=0;i<sizepro;i++)
				{
					memory[placeinmem+i]=nameprocess;
				}
			}
			else
			{
				compactMemory();
				printf("--Compactación requerida--\n");
				printf("Nueva situación:\n%s\nAsignando a %c\n",memory,nameprocess);
				placeinmem=primerAjuste(sizepro);
				if(placeinmem!=-1)
				{
					int i=0;
					for(i=0;i<sizepro;i++)
					{
						memory[placeinmem+i]=nameprocess;
					}
				}
				else
				{
					printf("No hay espacio suficiente en memoria, se tiene que liberar un proceso para asignar uno nuevo\n");
				}
			}
		}
		else if(answer == 'L')
		{
			char process[2];
			printf("¿Qué proceso desea liberar?\n");
			scanf("%s",process);
			int i =0;
			for(i=0;i<30;i++)
			{
				if(memory[i]==toupper(process[0]))
				{
					memory[i]='*';
				}
			}
		}
		printf("¿Desea continuar?\n");
		scanf("%s",&end);
	}
	return 0x0;
}
