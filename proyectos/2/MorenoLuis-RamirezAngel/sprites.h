/*#include <stdio.h>
#include <windows.h>


char pantalla [47][28];*/

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

void persona (char (*pantalla)[28], short int x, short int y, char comida) //Dibuja una persona en mi arreglo usando coordenadas xy
{
	
	if(comida=='s') //Si trae comida
	{
		pantalla[x][y]=178; //La comida
		pantalla[x+1][y]=218; //La cabeza
		pantalla[x+2][y]=191;
		pantalla[x+3][y]=32;
		
		pantalla[x][y+1]=192; //Línea 2, brazos y torso
		pantalla[x+1][y+1]=219; 
		pantalla[x+2][y+1]=219;
		pantalla[x+3][y+1]=32;
	}else
	{
		pantalla[x][y]=32;
		pantalla[x+1][y]=218; //La cabeza
		pantalla[x+2][y]=191;
		pantalla[x+3][y]=32;
		
		pantalla[x][y+1]=47; //Línea 2, brazos y torso
		pantalla[x+1][y+1]=219; 
		pantalla[x+2][y+1]=219;
		pantalla[x+3][y+1]=92;
	
	}
	
	
	pantalla[x][y+2]=32; //Línea 3, piernas
	pantalla[x+1][y+2]=217;
	pantalla[x+2][y+2]=192;
	pantalla[x+3][y+2]=32;
	
}

void mesa (char (*pantalla)[28], short int x, short int y, short int comida) //Dibuja una mesa en mi arreglo
{
	switch (comida) //Si en la mesa...
	{
		case 0: //No hay comida
			pantalla[x+1][y]=32;
			break;
		case 1:
			pantalla[x+1][y]=176; //Casi se acaba la comida
			break;
		case 2:
			pantalla[x+1][y]=177; //A medio comer
			break;
		case 3:
			pantalla[x+1][y]=178; //Llego la comida
	}
	
	pantalla[x][y+1]=220; //superficie de la mesa
	pantalla[x+1][y+1]=220;
	pantalla[x+2][y+1]=220;
	
	pantalla[x+1][y+2]=223; //La patita de la mesa	
}

void estufa (char (*pantalla)[28], short int x, short int y, char comida) //Dibuja una estufa en mi arreglo
{
	if(comida=='s')
	{
		pantalla[x][y]=219; //Estufa con cacerola
		pantalla[x+1][y]=200;
		pantalla[x+2][y]=188;
		
	}else
	{
		pantalla[x][y]=219; //Estufa vacía
		pantalla[x+1][y]=32;
		pantalla[x+2][y]=32;
	}
	
	
	pantalla[x][y+1]=219; //Cuerpo de la estufa
	pantalla[x+1][y+1]=219;
	pantalla[x+2][y+1]=219;
	
}

void pedido (char (*pantalla)[28], short int x, short int y, short int pedido) //Dibuja un '~' para indicar que se esta diciendo un pedido
{
	short int i;
	
	for(i=0;i<=pedido;i++)
	{
		pantalla[x+3+i][y]=126;
	}
	
}

void paga (char (*pantalla)[28]) //Escribe $$$ al pagar
{
	pantalla[12][9]=36;
	pantalla[13][9]=36;
	pantalla[14][9]=36;
}

void restaurante(char (*pantalla)[28]) // Dibuja las paredes y mostradores de mi restaurante
{
	int i;
	for(i=7;i<47;i++) //Pared norte y sur
	{
		pantalla[i][1]=177;
		pantalla[i][27]=177;
	}
	
	for(i=2;i<13;i++) //Pared este y oeste
	{
		pantalla[7][i]=177; 
		pantalla[46][i]=177;
	}
	
	for(i=19;i<27;i++) //Pared este y oeste 2
	{
		pantalla[7][i]=177;
		pantalla[46][i]=177;
	}
	
	for(i=2;i<27;i++) //Barra
	{
		pantalla[35][i]=176;
		pantalla[36][i]=176;
	}
	
	pantalla[8][12]=177; //Caja
	pantalla[9][12]='C';
	pantalla[10][12]='A';
	pantalla[11][12]='J';
	pantalla[12][12]='A';
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

/*int main(void)
{
	short int x,y;
	
	limpia();
	
	mesa(22,3,3);
	mesa(22,7,2);
	mesa(22,11,1);
	mesa(22,15,0);
	mesa(22,19,0);
	mesa(22,23,0);
	
	estufa(37,7,'s');
	estufa(37,14,'n');
	estufa(37,21,'s');
	
	persona(9,10,'n');
	persona(13,10,'n');
	
	
	persona(18,3,'n');//en la mesa
	persona(18,7,'n');
	persona(18,11,'n');
	persona(18,15,'n');
	pedido(18,15,2);
	persona(18,19,'n');
	persona(18,23,'n');
	
	persona(2,12,'n');//En fila
	persona(2,9,'n');
	persona(2,6,'n');
	persona(2,3,'n');
	persona(2,0,'n');
	
	persona(7,13,'n'); //entra
	persona(7,16,'n'); //sale
	
	persona(40,6,'n'); //cocineros
//	persona(40,13,'s');
	persona(40,20,'n');
	
	persona(25,3,'n');//meseros en la mesa
	persona(25,7,'n');
	persona(25,11,'n');
	persona(25,15,'n');
	persona(25,19,'n');
	persona(25,23,'n');
	
	persona(31,4,'n');//meseros en barra
	persona(31,11,'n');
	persona(31,18,'n');

	
	
	persona(37,11,'s'); //cocinero en barra
	
	paga();
	
	restaurante();
	
	pedido(31,11,0); //mesera a cocinero
	
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
}*/
