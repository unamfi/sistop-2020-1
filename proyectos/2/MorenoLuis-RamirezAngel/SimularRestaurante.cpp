#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>
#include "sprites.h"

#include <thread>
#include <mutex>
#include <condition_variable>

char pantalla [47][28];
short int mesas[6] = {'0','0','0','0','0','0'} ; //Bandera para saber que mesa esta ocupada(0) o libre (1)
short int genteFormada=0; //Clientes formados fuera
short int genteSentada=0; //Clientes en el restaurante

std::mutex puerta; //Sólo un cliente puede entrar por la puerta
std::mutex caja; //Sólo un cliente puede estar pagando en la caja
std::mutex mesero1; //El mesero atiende a un cliente a la vez
std::mutex mesero2; //y hay dos meseros
std::mutex cocinero1;//Hay 3 cocineros
std::mutex cocinero2;
std::mutex cocinero3;

std::condition_variable afuera; //Afuera habrá una fila de máx 5 personas esperando 
std::mutex semAfuera; 			// para lograrlo usaremos un semáforo

std::condition_variable restaurant; //Máximo hay 6 personas dentro del restaurante
std::mutex semRestaurante; 			//para lograrlo usaremos un semáforo




struct cliente
{
	short int numMesa; //En que mesa se sienta
};

struct mesero
{
	short int colaPedidos [3]; //Guarda la mesa que le hizo el pedido en el orden que fueron pidiendo
	short int entrega; //A que mesa va a entregar la comida
};

struct cocinero
{
	short int pedido; //Sabe que mesa le hizo el pedido que cocina
};

short int eligeMesa(void)
{	
	if(mesas[0]=='0') //Si la 0 esta desocupada
	{
		mesas[0]='1'; //Marcala ocupada
		return 0;     //Regresa el numero de mesa
	}
	
	if(mesas[1]=='0')
	{
		mesas[1]='1';
		return 1;
	}
	
	if(mesas[2]=='0')
	{
		mesas[2]='1';
		return 2;
	}
	
	if(mesas[3]=='0')
	{
		mesas[3]='1';
		return 3;
	}
	
	if(mesas[4]=='0')
	{
		mesas[4]='1';
		return 4;
	}
	
	if(mesas[5]=='0')
	{
		mesas[5]='1';
		return 5;
	}
	
	return 9; //Mi codigo de error
}

void entraAlRestaurante(struct cliente* paquito)
{
	puerta.lock();//Sólo una persona entra por la puerta a la vez
	std::unique_lock<std::mutex> espera(semRestaurante);
	while(genteSentada>5)	//Cuando no haya mesas vacías en el restaurante
	{
		restaurant.wait(espera);	//Dejo a los demás esperando afuera
	}
	genteSentada++; //Si entra, hay un cliente más en el restaurante
	
	paquito->numMesa = eligeMesa(); //El cliente elige una mesa
	
	printf("\n\tEstoy en mesa %d",paquito->numMesa); //Va a la mesa
	puerta.unlock(); //Se aleja de la puerta
	
	genteFormada--; //Hay una persona menos en la fila
	afuera.notify_all(); //Notifico que ya puede formarse otra persona
}

void pideComida(struct cliente *paquito)
{
	
}

void saleDelRestaurante(struct cliente * paquito)
{
	genteSentada--; //Hay un cliente menos dentro
	mesas[paquito->numMesa]='0'; //La mesa del cliente ahora esta libre
	printf("\n\t\tsali mesa %d",paquito->numMesa);
	restaurant.notify_all(); //Le aviso a quien quería entrar
	
}

void nvoCliente(void)
{
	struct cliente *paquito;
	
	paquito = (struct cliente*) malloc (sizeof(struct cliente));
	
	printf("\tHola =D");
	//Sleep(1000);
	
	entraAlRestaurante(paquito);
	pideComida(paquito);
	//comeComida(paquito);
	//pagaComida(paquito);
	Sleep(6000);
	saleDelRestaurante(paquito);
	
	free(paquito);
}

void formaAlCliente (void)
{
	std::unique_lock<std::mutex> espera(semAfuera);
	while(genteFormada>4)	//Cuando hay 5 personas en la fila
	{
		afuera.wait(espera);	//Dejan de llegar clientes porque la fila es muy larga
	}
	genteFormada++; //Si no había 5, te formas
}

void funcionMadre (void)
{
	int tiempo;
	int numClientes = 0;
	
	srand( time(NULL) );//Uso el tiempo para randomizar mis numeros
	do
	{
		formaAlCliente(); //Ves si hay menos de 5 clientes en la fila
	
		std::thread cliente(nvoCliente); //Lanzo el hilo de mi cliente
		numClientes++;
		
		if(cliente.joinable()) //Si el hilo aún le pertenece a este proceso...
    	{
        	cliente.detach(); //No voy a esperar a que el hilo termine su ejecución, así que lo hago independiente
    	}
		
		//tiempo = rand() %1500;
		tiempo=0;
		
		printf("\n tiempo: %d %d",tiempo, rand());
		Sleep(500+tiempo); //Espero antes de crear un hilo
		
	}while(numClientes<100); //Repite hasta crear 100 clientes
}

void prinx (void)
{
	while (true)
	{
		printf("\n\tHay %d clientes afuera",genteFormada);
		Sleep(1000);
	}
	
}


int main(void)
{	
	
	std::thread madre (funcionMadre);	
	std::thread imprime (prinx);
	
	imprime.detach();
	madre.join();
	
	return 0;
}
