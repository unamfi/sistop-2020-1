import java.util.ArrayList;

public class Autobus {
	
	private int numeroAsientosDisponibles;
	private int asientosOcupados;
	private boolean yaNosVamos=false;
	private ArrayList<Persona> pasajeros;


	public Autobus(){
		this.pasajeros = new ArrayList<>();
	}

	public synchronized void dejarSubir(Persona pasajero){
		pasajeros.add(pasajero);
		asientosOcupados++;
		System.out.println("Un pasajero ha subido, es el número "+ this.asientosOcupados);
		System.out.println("Quedan "+ this.numeroAsientosDisponibles + " asientos disponibles");
		if(asientosOcupados== numeroAsientosDisponibles) {
			yaNosVamos = true;
		}
	}

	public void run() throws InterruptedException {
		while( yaNosVamos == false){
			this.wait();
		}
		System.out.println("El autobus se va");
	}

}
