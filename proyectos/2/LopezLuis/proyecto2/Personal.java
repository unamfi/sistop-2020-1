/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package proyecto2;
/**
 *
 * @author deida
 */

import java.util.concurrent.Semaphore;

public class Personal extends Thread{
 public static int empleadostot=0;
 public String nombre;

 static int pizza; //Totales: variables donde accederan los hilos
 static int bebidas;
 static int postre;
 public static int cuenta;
 
 
 static Semaphore sem = new Semaphore(1); //semaforo que lleva la sincronizacion principal
 static Semaphore sempit = new Semaphore(1); // semaforo para que un hilo no genere items cuando otros generen 
 static Semaphore sempost = new Semaphore(1); //
 static Semaphore re = new Semaphore(1); 
 static Semaphore counting = new Semaphore(1); //semaforo para llevar la cuenta
 Cliente gen = new Cliente();
 public Personal() {
	gen.orden1[0]=0;
 }
 public Personal(String nombre, Cliente gen) {
	 empleadostot++;
	 this.nombre=nombre;
	 this.gen=gen;
 }
 
 
 public static void generarPizzas() {
	 try {
		sempit.acquire();
		pizza++;
		sempit.release();
	} catch (InterruptedException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
	 
 }
 
 public static void generarPostres() {
	 try {
		sempost.acquire();
		postre++;
		sempost.release();
	} catch (InterruptedException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
	 
 }
 public static void restock() {
	 try {
		re.acquire();
		bebidas++;
		re.release();
	} catch (InterruptedException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
	 
 }
 public static void cuenta(Cliente nu) {
	 try {
		
		int count;
		 count=nu.orden1[0]*80;
		 count=count+(nu.orden1[1]*10);
		 System.out.println("Su cuenta a pagar "+count);
		 counting.acquire();
		 cuenta=cuenta+count;
		 System.out.println("Ganancias Totales "+cuenta);
		 counting.release();
		 
	} catch (InterruptedException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
	 
 }
 public void run() {
	 
	if(gen.orden1[0]==0){//si no hay clientes genera items
		//System.out.println("Soy el mesero "+nombre+", no hay clientes");
		if(pizza<=10) {
			System.out.println("Se hizo una pizza");
			Personal.generarPizzas();
		}	
		if(postre<=10) {
			System.out.println("Se hizo un postre");
			Personal.generarPostres();
		}		
		if(bebidas<=10) {
			System.out.println("Se realizo un restock de bebidas");
			Personal.restock();
			System.out.println();
		}		
	}
	 if(Cliente.Clientes>0) {//si hay despacha
		 System.out.println("Soy el mesero "+nombre+", estare atendiendo su orden");
		 if(gen.orden1[0]>0 || gen.orden1[1]>0 ) {
			 try {		
				System.out.println("La orden de "+gen.nombre+" es "+gen.orden1[0]+" pizzas "+gen.orden1[1]+" refrescos" );
				
				int requeridas=gen.orden1[0];
				if(pizza<requeridas) {
					int pizzasdispo=pizza;
					gen.orden1[0]=requeridas-pizzasdispo;
					int bebidasreq=gen.orden1[1];
					if(bebidasreq>bebidas) {
						while(bebidas<bebidasreq) {
							Personal.restock();// si hacen falta bebidas se hace restock
						}
						
					}
					 sem.acquire();//se resta el numero total de bebidas, se usa un semaforo para sincronizar la variable 
					bebidas=bebidas-gen.orden1[1];
					sem.release();
					System.out.println("Hola "+gen.nombre+" Te sirvo "+pizzasdispo+" pizzas y "+ gen.orden1[1] +" bebidas  te faltan "+gen.orden1[0]+" pizzas");
					System.out.println("Tendras que esperar un momento");
					while(gen.orden1[0]>=pizza) {
						Personal.generarPizzas();
						
					}
					//System.out.println("pizzas "+pizza);
					sem.release();
					pizza=pizza-gen.orden1[0];//se sincroniza para evitar perdida de pizzas
					System.out.println("Le traemos sus "+gen.orden1[0]+" pizzas faltantes y un postre de regalo");
					if(postre<0) {
						Personal.generarPostres();
					}
					postre--;
					Personal.cuenta(gen);
					Cliente.Clientes--;
					sem.release();
					System.out.println();
					
					
				}
				
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		 }
		 
	 }
	 
	 
 }
 }
