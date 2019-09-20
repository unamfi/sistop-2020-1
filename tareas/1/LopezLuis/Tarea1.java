import java.util.LinkedList;
import java.util.concurrent.*;
public class New extends Thread{
	static Semaphore Mutex= new Semaphore(1);
	static Semaphore Sleep= new Semaphore(0);
	static CyclicBarrier barrera = new CyclicBarrier(4);
	boolean band=false;
	static int Hackers = 0;
	static int Serfs = 0;	
	static int Cuenta=0;
	 String queEs="";
	 public New(String queEs) {
		 this.queEs=queEs;
	 }
	public void run() {
		 try {
			 
			if(queEs.equals("Hacker")) {
				Mutex.acquire();
				Hackers++;
				Mutex.release();
		
			}else {
					Mutex.acquire();
					Serfs++;
					Mutex.release();
				
				}
				
			System.out.println(" y Soy "+queEs);			 
			System.out.println(Hackers);
			System.out.println(Serfs);
			if((Hackers==3 && Serfs==1) ||(Serfs==3 && Hackers==1)) {
				System.out.println("Espera tu turno");
			//	System.out.println("Dormido");
				Sleep.acquire();
			//	System.out.println("Despierto");
				band=true;
			}else {
			barrera.await();
			//System.out.println("Barrera abierta");
			System.out.println("Avanzamos");
			}
			
			if(band==false) {
			if(queEs.equals("Hacker")) {
				Hackers--;
			}else if(queEs.equals("Serfs")) {
				Serfs--;
			}
			
			}
			if(band==true ||Hackers==4 ||Serfs==4) {
				Sleep.release();
				if(queEs.equals("Hacker")) {
					Hackers--;
				}else if(queEs.equals("Serfs")) {
					Serfs--;
				}
			//	System.out.println("Otra barrera abierta");
				barrera.await();
				System.out.println("Avanzamos");
			}
			Sleep.release();
			Mutex.acquire();
			band=false;
			Mutex.release();
		   } catch (Exception e) {
		      
		   }		 
	}
	public static void main(String[]args) throws InterruptedException{
		LinkedList<String> clase2 = new LinkedList<String>();
		LinkedList<Thread> espera = new LinkedList<Thread>();
		clase2.add("Hacker");
		clase2.add("Serfs");
		while(true) {
		
		 int numero = Man.generaNumeroAleatorio(0, 1) ;
		String clase=clase2.get(numero);
		Thread hilo = new New(clase);
		espera.add(hilo);
		hilo.start();
		System.out.println("Soy el hilo "+hilo.getName());
		TimeUnit.SECONDS.sleep(1);
		}
	}
	
}
