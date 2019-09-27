import java.util.ArrayList;
import java.util.*;

public class RoundRobin {
	private int ronda=0;
	
	public static void main(String[] args) {
		RoundRobin robin = new RoundRobin();
		robin.nuevaRonda();
		
	}
	
	public void nuevaRonda(){
		ronda += 1;
		System.out.println("Ronda "+ ronda);
		Quantum q = new Quantum(2);
		ArrayList<Proceso> listaProcesos = new ArrayList<Proceso>();
		Proceso p1 = new Proceso((int)(Math.random()*10), q,"A");
		Proceso p2 = new Proceso((int)(Math.random()*10), q,"B");
		Proceso p3 = new Proceso((int)(Math.random()*10), q,"C");
		listaProcesos.add(p1);
		listaProcesos.add(p2);
		listaProcesos.add(p3);
		q.recorrerProcesos(listaProcesos);
		this.nuevaRonda();
	}

}

class Quantum{
	public int valor;
	private boolean sacarProceso;
	private int tiempoTotal= 0;
	private ArrayList<String> orden = new ArrayList<>();
	
	
	
	public Quantum(int valor) {
		this.valor = valor;
		
	}
	
	public void recorrerProcesos(ArrayList<Proceso> listaProcesos) {
			this.tiempoTotal = 0;
			
			
		while(listaProcesos.isEmpty() == false) {
		for(int i = 0; i< listaProcesos.size(); i++){
			//System.out.println("Se entró al bucle ");
			System.out.println("Está trabajando el proceso "+ listaProcesos.get(i).getNumeroProceso());
			if(listaProcesos.get(i).getRafaga() - listaProcesos.get(i).getComparador() < this.valor ) {
				try {
					Thread.sleep((listaProcesos.get(i).getRafaga() - listaProcesos.get(i).getComparador())*1000);
					System.out.println("Duró menos de un quantum completo, es decir: "+ (listaProcesos.get(i).getRafaga() - listaProcesos.get(i).getComparador()) +" segundos");
					this.tiempoTotal+= listaProcesos.get(i).getRafaga() - listaProcesos.get(i).getComparador();
					System.out.println("Han pasado "+ this.tiempoTotal + " segundos");
					listaProcesos.get(i).setComparador(listaProcesos.get(i).getRafaga() - listaProcesos.get(i).getComparador());
					//listaProcesos.get(i).setTiempo(this.tiempoTotal);
					//System.out.println("El proceso "+ listaProcesos.get(i).getNumeroProceso() + " tardó "+ this.tiempoTotal +" segundos en concluir" );
					orden.add(listaProcesos.get(i).getNumeroProceso());
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}		//Fin de la comprobación sobre si el proceso acabará antes de completar un quantum
			else {
			try {
				Thread.sleep(listaProcesos.get(i).getValorQuantum()*1000);
				System.out.println("Durmió después de un quantum completo, es decir: "+ this.valor +" segundos");
				this.tiempoTotal+= listaProcesos.get(i).getValorQuantum();
				System.out.println("Han pasado "+ this.tiempoTotal + " segundos");
				orden.add(listaProcesos.get(i).getNumeroProceso());
				listaProcesos.get(i).setComparador(listaProcesos.get(i).getValorQuantum());
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			}		//Fin del caso donde sí se completa un quantum antes de que acabe el proceso
			//sacarProceso = listaProcesos.get(i).estaTerminado();
			if(listaProcesos.get(i).getComparador() == listaProcesos.get(i).getRafaga()){
				
				System.out.println("Se terminó el proceso "+ listaProcesos.get(i).getNumeroProceso() + " en "+ this.tiempoTotal + " segundos, y su ráfaga es de "+ listaProcesos.get(i).getRafaga());
				listaProcesos.remove(i);
				if(listaProcesos.isEmpty() == false) {
					i--;
				}
				
			}
			
			
		}
		
		}
		System.out.println("El orden fue ");
		for(int i = 0; i<this.orden.size();i++) {
			System.out.print(orden.get(i));
		}
		System.out.println("El tiempo total fue: "+ this.tiempoTotal);
		
		System.out.println("\n\n");
		
		
	}
}

class Proceso{
	private int rafaga;
	private int comparador;
	private int valorQuantum;
	private int tiempo;
	private String numeroProceso;
	
	
	public Proceso(int rafaga, Quantum valor, String numeroProceso) {
		super();
		this.rafaga = rafaga;
		this.comparador = 0;
		this.valorQuantum = valor.valor;
		this.numeroProceso = numeroProceso;
		
	}
	
	public String getNumeroProceso() {
		return this.numeroProceso;
	}
	
	public int getValorQuantum() {
		return valorQuantum;
	}
	
	public void setComparador(int valor) {
		this.comparador += valor;
	}
	
	public boolean estaTerminado() {
		if(this.rafaga <= comparador) {
			return true;
		}
		else {
			return false;
		}
	}
	
	public int getRafaga() {
		return this.rafaga;
	}
	
	public int getComparador() {
		return this.comparador;
	}
	
	public void setTiempo(int tiempo) {
		this.tiempo = tiempo;
	}
	
	public int getTiempo() {
		return this.tiempo;
	}
	
	
}	//Fin clase Proceso