#include <stdio.h>
#include <windows.h>
#include "sprites.h"

char pantalla [47][28];

int main(void)
{
	short int x,y;
	
	limpia(pantalla);
	
	mesa(pantalla,22,3,3);
	mesa(pantalla,22,7,2);
	mesa(pantalla,22,11,1);
	mesa(pantalla,22,15,0);
	mesa(pantalla,22,19,0);
	mesa(pantalla,22,23,0);
	
//	estufa(pantalla,37,7,'s');
	estufa(pantalla,37,14,'n');
//	estufa(pantalla,37,21,'s');
	
	persona(pantalla,9,10,'n'); //cajero
	persona(pantalla,13,10,'n');
	
	
	persona(pantalla,18,3,'n');//en la mesa
	persona(pantalla,18,7,'n');
	persona(pantalla,18,11,'n');
	persona(pantalla,18,15,'n');
	pedido(pantalla,18,15,2);
	persona(pantalla,18,19,'n');
//	persona(pantalla,18,23,'n');
	
	persona(pantalla,2,12,'n');//En fila
	persona(pantalla,2,9,'n');
	persona(pantalla,2,6,'n');
	persona(pantalla,2,3,'n');
	persona(pantalla,2,0,'n');
	
//	persona(pantalla,7,13,'n'); //entra
//	persona(pantalla,7,16,'n'); //sale
	
//	persona(pantalla,40,6,'n'); //cocineros
//	persona(40,13,'s');
//	persona(pantalla,40,20,'n');
	
//	persona(pantalla,25,3,'n');//meseros en la mesa
//	persona(pantalla,25,7,'n');
//	persona(pantalla,25,11,'n');
	persona(pantalla,25,15,'n');
//	persona(pantalla,25,19,'n');
//	persona(pantalla,25,23,'n');
	
	//persona(pantalla,31,4,'n');//meseros en barra
	persona(pantalla,31,11,'n');
	//persona(pantalla,31,18,'n');

	
	
	persona(pantalla,37,11,'s'); //cocinero en barra
	
	paga(pantalla);
	
	restaurante(pantalla);
	
	pedido(pantalla,31,11,0); //mesera a cocinero
	
	for(y=0;y<28;y++)
	{
		for(x=0;x<47;x++)
		{
			printf("%c",pantalla[x][y]);
		}
		printf("\n");//Al terminar, salta de línea
	}
	
	printf("\t    ===Simulador de restaurante===");
	
	//sleep();
	return 0;
}
