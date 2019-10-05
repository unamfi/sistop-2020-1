#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>
#include "sprites.h"

#include <thread>
#include <mutex>
#include <condition_variable>

#define maxClientes 10 //El numero máximo de clientes que vamos a simular

char pantalla [47][28];
int numClientes = 0; //Para llevar la cuenta de los clientes creados
int numClientesDespachados = 0; //Para saber cuantos clientes han sido atendidos en su totalidad
char flagMeseroA = 'n'; //Bandera para saber si llamamos o no al mesero
char flagMeseroB = 'n';
char flagCocineroA ='n'; //Bandera para saber el cocinero esta ocupado o no
char flagCajero = 'n'; //Bandera para saber si mi cajero esta ocupado o no
short int mesas[6] = {0,0,0,0,0,0} ; //Banderas para saber que mesa esta ocupada(1) o libre (0)
short int comidaEnMesas[6]={0,0,0,0,0,0} ;//Banderas para saber si hay (1) o no (0) comida en las mesas
short int genteFormada=0; //Clientes formados fuera
short int genteSentada=0; //Clientes en el restaurante
short int pedidoA = 0; //Que mesa le pide algo al mesero A
short int pedidoB = 0; //que mesa le pide algo al mesero B

std::mutex puerta; //Sólo un cliente puede entrar por la puerta
std::mutex caja; //Sólo un cliente puede estar pagando en la caja

std::mutex meseroAtiendeA; //El mesero atiende a un cliente o cocinero a la vez
std::mutex meseroAtiendeB; //y hay dos meseros

std::mutex cocineroA;//Hay 3 cocineros
std::mutex cocineroB;
std::mutex cocineroC;

std::condition_variable afuera; //Afuera habrá una fila de máx 5 personas esperando 
std::mutex semAfuera; 			// para lograrlo usaremos un semáforo

std::condition_variable restaurant; //Máximo hay 6 personas dentro del restaurante
std::mutex semRestaurante; 			//para lograrlo usaremos un semáforo

std::condition_variable clienteEsperaPedirA; //Para que el cliente espere si el meseroA esta ocupado
std::mutex esperaPedirA;

std::condition_variable clienteEsperaPedirB; //Para que el cliente espere si el meseroB esta ocupado
std::mutex esperaPedirB;

std::condition_variable meseroVenA; //Para que el mesero A pueda esperar mientras llegan pedidos
std::mutex meseroEsperaA;

std::condition_variable meseroVenB; //Para que el mesero B pueda esperar mientras llegan pedidos
std::mutex meseroEsperaB;

std::condition_variable meseroEncarga; //Para estar al pendiente de los cocineros, cuando se desocupen el mesero encarga un pedido 
std::mutex noEncarges;

std::condition_variable cociLibreA; //Para que el cocinero A pueda esperar mientras llegan pedidos
std::mutex cociEsperaA;

std::condition_variable esperandoComida; //La uso para que los clientes revisen si hay comida en sus mesas

std::mutex quieroPagar; //Para la caja

std::condition_variable despiertaCajero; //Para que el cajero espere a que gente quiera pagar
std::mutex mDespiertaCajero;

std::mutex dinero; //Para sincronizar la transacción entre cliente y cajero

struct cliente
{
	short int numMesa; //En que mesa se sienta
};

struct mesero
{
	short int colaPedidos [3]={0,0,0}; //Guarda la mesa que le hizo el pedido en el orden que fueron pidiendo
	short int entrega; //A que mesa va a entregar la comida
};

struct cocinero
{
	short int pedido; //Sabe que mesa le hizo el pedido que cocina
};

short int eligeMesa(void)
{	
	if(mesas[0]==0) //Si la 0 esta desocupada
	{
		mesas[0]=1; //Marcala ocupada
		return 0;     //Regresa el numero de mesa
	}
	
	if(mesas[1]==0)
	{
		mesas[1]=1;
		return 1;
	}
	
	if(mesas[2]==0)
	{
		mesas[2]=1;
		return 2;
	}
	
	if(mesas[3]==0)
	{
		mesas[3]=1;
		return 3;
	}
	
	if(mesas[4]==0)
	{
		mesas[4]=1;
		return 4;
	}
	
	if(mesas[5]==0)
	{
		mesas[5]=1;
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
	
	if (paquito->numMesa < 3) //Si me sente el las primeras 3 mesas, me corresponde el mesero A
	{
		std::unique_lock<std::mutex> noComasAnsias(esperaPedirA);
		while(flagMeseroA != 'n')	//Mientras el mesero NO este desocupado
		{
			clienteEsperaPedirA.wait(noComasAnsias);	//el cliente espera antes de llamarlo para hacer un pedido
		}
		
		meseroAtiendeA.lock(); //Ocupo a mi mesero
		printf("\nww Pide %d",paquito->numMesa);
		pedidoA = paquito->numMesa;
		flagMeseroA = 't'; //Pongo al mesero en modo "toma pedido"
		meseroVenA.notify_all(); //Despierto a mi mesero
		Sleep(100);//En lo que anota mi pedido
		meseroAtiendeA.unlock();//suelto a mi mesero
		
	}else //De lo contrario, llamo al meseroB
	{
		std::unique_lock<std::mutex> noComasAnsias(esperaPedirB);
		while(flagMeseroB != 'n')	//Mientras el mesero NO este desocupado
		{
			clienteEsperaPedirB.wait(noComasAnsias);	//el cliente espera antes de llamarlo para hacer un pedido
		}
		
		meseroAtiendeB.lock(); //Lo mismo pero con el mesero B
		printf("\nww Pide %d",paquito->numMesa);
		pedidoB = paquito->numMesa;
		flagMeseroB = 't'; 
		meseroVenB.notify_all(); 
		Sleep(100);
		meseroAtiendeB.unlock();
	}
	
}

void saleDelRestaurante(struct cliente * paquito)
{
	genteSentada--; //Hay un cliente menos dentro
	printf("\n°°°Soy %d y sali",paquito->numMesa);
	restaurant.notify_all(); //Le aviso a quien quería entrar
	
}

void nvoCliente(void)
{
	//short int nombreCliente;
	struct cliente *paquito;
	
	std::mutex esperaComida; //Mutex local para quedarme en la mesa esperando mi comida

	
	//nombreCliente = numClientes;
	
	paquito = (struct cliente*) malloc (sizeof(struct cliente));
	
	printf("\tHola =D");
	//Sleep(1000);
	
	entraAlRestaurante(paquito);
	pideComida(paquito);
	
	//Espero a que llegue mi comida
	
	std::unique_lock<std::mutex> paciencia(esperaComida);
	while( comidaEnMesas[paquito->numMesa]!=1 )	//Mientras no haya comida en mi mesa
	{
		esperandoComida.wait(paciencia);	//espero
	}
	
	printf("\n...Soy %d y estoy comiendo\n",paquito->numMesa);
	Sleep(500); //Como
	comidaEnMesas[paquito->numMesa] = 0; //Ya no hay comida en la mesa
	
	//Acabe, así que voy a pagar =)
//	Sleep(6000);
	
	quieroPagar.lock();
	mesas[paquito->numMesa]=0; //La mesa del cliente ahora esta libre
	printf("\n\nxx %d da dinero",paquito->numMesa);
	flagCajero='o'; //me pongo frente al cajero
	despiertaCajero.notify_all(); //le digo al cajero que aquí estoy
	dinero.lock();//Sólo me avanzo cuando el cajero recibe mi dinero
	printf("\nzzz %d gracias",paquito->numMesa) ;
	quieroPagar.unlock();
	

	saleDelRestaurante(paquito); //Salgo y le aviso al 1ro de la fila que puede entrar
	
	
	//if (nombreCliente == maxClientes) //Si mi ultimo cliente salio del restaurante, despierto a mi mesero para que salga de su función
	//{
	//	flagMeseroA='m';
	//	meseroVenA.notify_all();//desbloqueo a mi mesero para que termine
	//}
	
	free(paquito);//libero memoria
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
		printf("\n==Creo Cliente %d",numClientes);
	//	printf("\n tiempo: %d %d",tiempo, rand());
		Sleep(500+tiempo); //Espero antes de crear un hilo
		
	}while(numClientes<maxClientes); //Repite hasta crear el máximo de clientes simulados
	
//	printf("\n**Se acabaron los clientes");
}

void meseroAEncarga(struct mesero * mA) //Función Auxiliar de meseroUno, esta al pendiente de los cocineros
{										//si uno esta disponible, va y le hace un pedido

	std::unique_lock<std::mutex> descansa(noEncarges);
		while(flagCocineroA != 'n')	//Mientras el cocinero NO este desocupado...
		{
			meseroEncarga.wait(descansa);	//...el mesero espera para encargarle un pedido
		}
	
	meseroAtiendeA.lock();//Bloqueo a mi mesero porque esta en uso
	
	if(flagCocineroA == 'n') //Si el primer cocinero esta desocupado
	{
		cocineroA.lock(); //Ocupo a mi cocinero 1
		flagCocineroA='p';
		pedidoA = mA->colaPedidos[0]; //Mando el pedido a mi cocinero
		cociLibreA.notify_all(); //Le digo a mi cocinero que tiene un pedido
		cocineroA.unlock(); //lo libero
		
		mA->colaPedidos[0]=mA->colaPedidos[1]; //Recorro mi cola de pedidos
		mA->colaPedidos[1]=mA->colaPedidos[2];
		mA->colaPedidos[2]=0;
	}
	
	meseroAtiendeA.unlock(); //Dejo de usar a mi mesero
	//clienteEsperaPedirA.notify_all();//Veo si hay clientes que deseen pedir algo
}

void meseroUno (void) //Atiende las primeras 3 mesas
{
	struct mesero mA;
	printf("\n-- Naci, mesero 1");
	do
	{
		std::unique_lock<std::mutex> descansa(meseroEsperaA);
		while(flagMeseroA=='n')	//Si nadie llama al mesero...
		{
			meseroVenA.wait(descansa);	//El mesero espera
		}
		
		//De lo contrario ...
		
		switch(flagMeseroA)
		{
			case 't': //En caso de que haya llamado el cliente tomo su pedido
					{
						if(mA.colaPedidos[0]==0) //Si no hay pedidos en la cola
						{
							printf("\n++1er pedido mesa %d",pedidoA);
							mA.colaPedidos[0] = pedidoA; //Guarda el numero de mesa que le hizo un pedido
						}else
						{
							if(mA.colaPedidos[1]==0)//Si había un pedido en la cola
							{
								printf("\n++2do pedido mesa %d",pedidoA);
								mA.colaPedidos[1] = pedidoA;
							}else //Si había dos pedidos en la cola
							{
								printf("\n++3er pedido mesa %d",pedidoA);
								mA.colaPedidos[2] = pedidoA;
							}
						}
						
						std::thread encargalo (meseroAEncarga, &mA); //Hago un hilo para que mi mesero este listo
																	//para encargar los pedidos a los cocineros
						if (encargalo.joinable())
						{
							encargalo.detach();	//y suelto ese hilo para que sea independiente
						}
						flagMeseroA = 'n'; //me desocupo
						clienteEsperaPedirA.notify_all();//Veo si hay clientes que deseen pedir algo
					}
						break;
						
			case 'r': //Si llamo el cocineroA, recojo el pedido
						mA.entrega = pedidoA; //Recibo el pedido
						printf("\n\n\t===Recogo pedido %d",mA.entrega);
						cocineroA.unlock();//Desocupo a mi cocinero
						
						Sleep(200);//Me dirijo a la mesa
						comidaEnMesas[mA.entrega]=1; //Pongo la comida en la mesa
						esperandoComida.notify_all(); //Le notifico a mis clientes que hay comida en una mesa
						
						flagMeseroA = 'n'; //me desocupo
						clienteEsperaPedirA.notify_all();//Veo si hay clientes que deseen pedir algo
						break;	
			default:
						printf("\nAdios");
						printf("\n--%d --%d --%d",mesas[0],mesas[1],mesas[2]);
						Sleep(500);
		} 
		
	}while( (mesas[0]+mesas[1]+mesas[2])!= 0 || numClientes< maxClientes);//Repite mientras mis mesas no esten vacías	y no hayamos cerrado
	
}

void meseroBEncarga(struct mesero * mB) //Función Auxiliar de meseroDos, esta al pendiente de los cocineros
{										//si uno esta disponible, va y le hace un pedido
	
	std::unique_lock<std::mutex> descansa(noEncarges);
		while(flagCocineroA != 'n')	//Mientras el cocinero NO este desocupado...
		{
			meseroEncarga.wait(descansa);	//...el mesero espera para encargarle un pedido
		}
	
	meseroAtiendeB.lock();//Bloqueo a mi mesero porque esta en uso
	
	if(flagCocineroA == 'n') //Si el primer cocinero esta desocupado
	{
		cocineroA.lock(); //Ocupo a mi cocinero 1
		flagCocineroA='d'; //Le digo que le habla el meseroDos
		pedidoB = mB->colaPedidos[0]; //Mando el pedido a mi cocinero
		cociLibreA.notify_all(); //Le digo a mi cocinero que tiene un pedido
		cocineroA.unlock(); //lo libero
		
		mB->colaPedidos[0]=mB->colaPedidos[1]; //Recorro mi cola de pedidos
		mB->colaPedidos[1]=mB->colaPedidos[2];
		mB->colaPedidos[2]=0;
	}
	
	meseroAtiendeB.unlock(); //Dejo de usar a mi mesero
}

void meseroDos (void) //Atiende las últimas 3 mesas
{					//Misma función que meseroUno(), pero con las variables creadas para meseroB
	
	struct mesero mB; 
	printf("\n-- Naci, mesero 2");
	do
	{
		std::unique_lock<std::mutex> descansa(meseroEsperaB);
		while(flagMeseroB=='n')	//Si nadie llama al mesero...
		{
			meseroVenB.wait(descansa);	//El mesero espera
		}
		
		//De lo contrario ...
		
		switch(flagMeseroB)
		{
			case 't': //En caso de que haya llamado el cliente tomo su pedido
					{
						if(mB.colaPedidos[0]==0) //Si no hay pedidos en la cola
						{
							printf("\n~~1er pedido mesa %d",pedidoB);
							mB.colaPedidos[0] = pedidoB; //Guarda el numero de mesa que le hizo un pedido
						}else
						{
							if(mB.colaPedidos[1]==0)//Si había un pedido en la cola
							{
								printf("\n~~2do pedido mesa %d",pedidoB);
								mB.colaPedidos[1] = pedidoB;
							}else //Si había dos pedidos en la cola
							{
								printf("\n~~3er pedido mesa %d",pedidoB);
								mB.colaPedidos[2] = pedidoB;
							}
						}
						
						std::thread encargalo (meseroBEncarga, &mB); //Hago un hilo para que mi mesero este listo
																	//para encargar los pedidos a los cocineros
						if (encargalo.joinable())
						{
							encargalo.detach();	//y suelto ese hilo para que sea independiente
						}
						flagMeseroB = 'n'; //me desocupo
						clienteEsperaPedirB.notify_all();//Veo si hay clientes que deseen pedir algo
					}
						break;
						
			case 'r': //Si llamo el cocineroA, recojo el pedido
						mB.entrega = pedidoB; //recibo el pedido
						printf("\n\n\t___Recogo pedido %d",mB.entrega);
						cocineroA.unlock();//Desocupo a mi cocinero
						
						Sleep(200);//Me dirijo a la mesa
						comidaEnMesas[mB.entrega]=1; //Pongo la comida en la mesa
						esperandoComida.notify_all(); //Le notifico a mis clientes que hay comida en una mesa
						
						flagMeseroB = 'n'; //me desocupo
						clienteEsperaPedirB.notify_all();//Veo si hay clientes que deseen pedir algo
						break;	
			default:
						printf("\nAdios2");
						printf("\n--%d --%d --%d",mesas[3],mesas[4],mesas[5]);
						Sleep(500);
		} 
		
	}while( (mesas[3]+mesas[4]+mesas[5])!= 0 || numClientes< maxClientes);//Repite mientras mis mesas no esten vacías	y no hayamos cerrado
	
}


void cocinero (void)
{
	struct cocinero structCocinero;
	do
	{
		std::unique_lock<std::mutex> descansa(cociEsperaA);
		while( flagCocineroA=='n'  )	//Si el cocinero esta desocupado
		{
			cociLibreA.wait(descansa);	//El cocinero espera
		}
		
	
		
		switch(flagCocineroA)
		{
			case 'p'://Si le hizo un pedido meseroA
						structCocinero.pedido = pedidoA;
		
						printf("\nhago pedido %d",structCocinero.pedido);
						Sleep(1000); //Prepara la comida
				
						meseroAtiendeA.lock();
						flagMeseroA = 'r'; //mesero recoge el pedido
						pedidoA = structCocinero.pedido;
						meseroVenA.notify_all(); //Llamo al mesero
						cocineroA.lock();//Me pongo a mi mismo como ocupado
						cocineroA.lock();//Intento ocuparme de nuevo, pero sólo el mesero puede desocuparme, una vez que haya recibido el pedido
						meseroAtiendeA.unlock();//libero al mesero
						
						flagCocineroA='n'; //me desocupo =)
						cocineroA.unlock();//
						meseroEncarga.notify_all(); //Y se lo digo a los meseros
						break;
			case 'd'://Si se lo hizo meseroB
						structCocinero.pedido = pedidoB;
		
						printf("\nhago pedido %d",structCocinero.pedido);
						Sleep(1000); //Prepara la comida
				
						meseroAtiendeB.lock();
						flagMeseroB = 'r'; //mesero recoge el pedido
						pedidoB = structCocinero.pedido;
						meseroVenB.notify_all(); //Llamo al mesero
						cocineroA.lock();//Me pongo a mi mismo como ocupado
						cocineroA.lock();//Intento ocuparme de nuevo, pero sólo el mesero puede desocuparme, una vez que haya recibido el pedido
						meseroAtiendeB.unlock();//libero al mesero
				
						flagCocineroA='n'; //me desocupo =)
						cocineroA.unlock();//
						
						meseroEncarga.notify_all(); //Y se lo digo a los meseros
						break;
			default:
				printf("\n**Von voyage");
				//printf("\nPresiona ENTER para terminar...");
		}
		
		
	}while( (mesas[0]+mesas[1]+mesas[2]+mesas[3]+mesas[4]+mesas[5])!= 0 || numClientes< maxClientes);//Repite mientras mis mesas no esten vacías y no hayamos cerrado
	
}


void miCajero (void)
{
	do
	{
		dinero.lock(); //Para sincronizar la transacción entre cliente y cajero
		
		std::unique_lock<std::mutex> bienvenido(mDespiertaCajero);
		while( flagCajero=='n' )	//Mientras no haya clientes en la caja
		{
			despiertaCajero.wait(bienvenido);	//espero
		}

		printf("\n\n¬¬¬Recibo pago =)\n");
		dinero.unlock(); //doy el cambio
		Sleep(500);
		dinero.unlock(); //desbloqueo a mi cliente
		
		numClientesDespachados++; //Atendi a un cliente más
		flagCajero = 'n'; //Vuelvo a estar desocupado
		
	}while( numClientesDespachados < maxClientes );
	
	
	flagMeseroA='m'; //Le aviso a mi mesero que es hora de terminar
	meseroVenA.notify_all();//desbloqueo a mi mesero para que termine
	
}

int main(void)
{	
	
	
	printf("\n,, LAnzo meseroA");
	std::thread meseA (meseroUno);
	printf("\n,, LAnzo meseroB");
	std::thread meseB (meseroDos);
	printf("\n,, LAnzo Cocinero");
	std::thread cociA (cocinero);
	printf("\n,, LAnzo Madre");
	std::thread madre (funcionMadre);
	std::thread cajerito (miCajero);
	
	madre.join(); //espero a que termine mi hilo creador de hilos
	cajerito.join();//espero a que termine mi hilo cajero
	meseA.join();//espero a que termine mi hilo mesero
	
	flagMeseroB='m';//Le digo a mi meseroB que es hora de terminar
	meseroVenB.notify_all();//desbloqueo a mi mesero para que termine
	meseB.join();//Espero a que termine
	
	flagCocineroA='m';//Le digo a mi cocinero que es hora de acabar
	cociLibreA.notify_all();//Y lo despierto
	cociA.join();//Espero a que mi hilo cocinero termine
	
	return 0;
}
