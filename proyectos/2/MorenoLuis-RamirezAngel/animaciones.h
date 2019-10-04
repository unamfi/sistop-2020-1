#include "sprites2.h"

void limpia (char (*pantalla)[28]) //Hace que todo mi arreglo este lleno de saltos de línea
{
	short int x,y;
	
	for(y=0;y<28;y++)
	{
		for(x=0;x<47;x++)
		{
			pantalla[x][y]=32;
		}
	}
}

void dibujaRestaurante(char (*pantalla)[28], short int comida[6])
{
	mesa(pantalla,22,3,comida[0]);
	mesa(pantalla,22,7,comida[1]);
	mesa(pantalla,22,11,comida[2]);
	mesa(pantalla,22,15,comida[3]);
	mesa(pantalla,22,19,comida[4]);
	mesa(pantalla,22,23,comida[5]);
	persona(pantalla,9,10,'n'); //cajero
	estufa(pantalla,37,14,'s');
	restaurante(pantalla);
}

void dibujaFila (char (*pantalla)[28], int genteFormada)
{
	switch(genteFormada)
	{
		case 0:
			break;
		case1:
			persona(pantalla,2,12,'n');//En fila
			break;
		case2:
			persona(pantalla,2,12,'n');//En fila
			persona(pantalla,2,9,'n');
			break;
		case3:
			persona(pantalla,2,12,'n');//En fila
			persona(pantalla,2,9,'n');
			persona(pantalla,2,6,'n');
			break;
		case4:
			persona(pantalla,2,12,'n');//En fila
			persona(pantalla,2,9,'n');
			persona(pantalla,2,6,'n');
			persona(pantalla,2,3,'n');
			break;
		case5:
			persona(pantalla,2,12,'n');//En fila
			persona(pantalla,2,9,'n');
			persona(pantalla,2,6,'n');
			persona(pantalla,2,3,'n');
			persona(pantalla,2,0,'n');
			break;
		default:
			break;
	}
}

void dibujaGenteMesas (char (*pantalla)[28], short int mesas[6])
{
	if (mesas[0]==1)
	{
		persona(pantalla,18,3,'n');//en la mesa
	}
	if (mesas[1]==1)
	{
		persona(pantalla,18,7,'n');
	}
	if (mesas[2]==1)
	{
		persona(pantalla,18,11,'n');
	}
	if (mesas[3]==1)
	{
		persona(pantalla,18,15,'n');
	}
	if (mesas[4]==1)
	{
		persona(pantalla,18,19,'n');
	}
	if (mesas[5]==1)
	{
		persona(pantalla,18,23,'n');
	}
}

void dibujaGenteCaja (char (*pantalla)[28], char cajero)
{
	if (cajero != 'n')
	{
		persona(pantalla,13,10,'n');
	}
}

void dibujaMeseroA (char (*pantalla)[28], int posicion)
{
	switch(posicion)
	{
		case 0://mesas
			persona(pantalla,25,3,'n');//meseros en la mesa
			break;
		case 1:
			persona(pantalla,25,7,'n');
			break;
		case 2:
			persona(pantalla,25,11,'n');
			break;
		case 3: //barra
			persona(pantalla,31,11,'n');
			break;
		case 4: //descansando
			persona(pantalla,31,4,'n');
			break;
		default:
			persona(pantalla,31,4,'n');
			
	}
}

void dibujaMeseroB (char (*pantalla)[28], int posicion, char comida) //comida 'n' = no, 's' = sí
{
	switch(posicion)
	{
		case 0://barra
			persona(pantalla,25,3,comida);//meseros en la mesa
			break;
		case 1://descansando
			persona(pantalla,25,7,comida);
			break;
		case 3: //mesas
			persona(pantalla,25,15,comida);
			break;
		case 4: 
			persona(pantalla,25,19,comida);
			break;
		case 5: 
			persona(pantalla,25,23,comida);
			break;
		default:
			persona(pantalla,25,7,comida);
	}
}

void dibujaCocinero (char (*pantalla)[28], int posicion,char comida)
{
	switch(posicion)
	{
		case 0://en barra
				persona(pantalla,37,11,comida);
				break;
		case 1://en estufa
				persona(pantalla,40,13,comida);
				break;
		default:
			persona(pantalla,37,11,'n');
	}
}

void imprimePantalla(char (*pantalla)[28])
{
	short int x,y;
	for(y=0;y<28;y++)
	{
		for(x=0;x<47;x++)
		{
			printf("%c",pantalla[x][y]);
		}
		printf("\n");//Al terminar, salta de línea
	}
	
	printf("\t    ===Simulador de restaurante===");
}
