import java.util.ArrayList;
import java.util.Random;
import java.util.concurrent.Semaphore;

public class Manejador1{
	
	public static void main(String[] args){
		//Semáforo que me dará acceso a los autobuses.
		Paradero paraderoAutobus = new Paradero();
		//Semáforo que me dará acceso al sitio de los autobus 
		Paradero paraderoPersonas = new Paradero();
		//Va generando aleatoriamente autobuses y personas.
		Generador generador = new Generador(paraderoAutobus, paraderoPersonas); 
		//Inicia el generador.
		generador.start(); 	
	}
	
}

class Paradero extends Semaphore { 
	
	public Paradero() {
		super(1);	
	}
}

class Autobus extends Thread{
	private boolean pasajeLleno = false;
	int numeroAsientos = 10;
	int asientosOcupados=0;

	ArrayList<Persona> personas;

	Paradero paraderoAutobus;
	//Indica el autobus que se encuentra delante en la fila.
	Autobus autobusAdelante; 				
	
	public Autobus(Paradero paraderoAutobus, Autobus autobusAdelante) { 
		this.paraderoAutobus = paraderoAutobus;
		this.autobusAdelante = autobusAdelante;
	}

	public void dejarSubir(Persona persona){
		asientosOcupados++;
		persona.sentado = true;
		if(asientosOcupados>= numeroAsientos){
			this.pasajeLleno = true;
		}
		
	}

	public void setPasajeLleno(){
		this.pasajeLleno = true;
	}

	public boolean getPasajeLleno(){
		return this.pasajeLleno;
	}

	public void run() { 
		
		
		//Adquiere un permiso el semáforo
		try {
			paraderoAutobus.acquire();		
			
		} catch (InterruptedException e) {
			System.out.println("El autobus no pudo adquirir permiso");	
		}
		while(pasajeLleno == false){
			
		}
		this.paraderoAutobus.release();
		System.out.println("Se llenó el camión"); 	
		System.out.println("Se va el autobus "+ this.currentThread());
	}
}

class Persona extends Thread{
	boolean sentado = false;
	boolean noHayAutobus = false;	
	Paradero paradero;
	//Indica el animal que se encuentra delante en la fila.
	Persona personaAdelante; 				
	

	public Persona(Paradero paradero, Persona personaAdelante) { 
		this.paradero = paradero;
		//this.personas = personas;
		this.personaAdelante = personaAdelante;
	}

	public void sentarse(Autobus autobus){
		autobus.dejarSubir(this);
	}

	public void setNoHayAutobus(){
		this.noHayAutobus = true;
	}

	public void run(){ 
		//Adquiere un permiso el semáforo
		try {
			paradero.acquire();		
			
		} catch (InterruptedException e) {
			System.out.println("La persona no pudo adquirir permiso para sentarse");	
		}
		
		while(sentado == false || noHayAutobus== true){
			try{
				this.wait();
			}catch(Exception e){}
		}
		this.paradero.release(); 			
		System.out.println("Se ha sentado la persona "+ this.currentThread());
	}
}


class Generador extends Thread{ 
	
	//Filas en donde se formarán los autobuses.
	ArrayList<Autobus> filaAutobus; 			
	//Se usa para comprobar una condición.
	private boolean bandera = true;		
	//Servirá como 1 y 0 al generar autobus o persona.
	private int autobusOPersona;				 
	//Es el semáforo de autobuses para pasarlos.
	Paradero paraderoAutobuses;
	//Es el semaforo de personas para subirse al autobus.	
	Paradero paraderoPersonas;					
	//La lista donde pasan a comer.
	ArrayList<Persona> filaPersonas;	

	public Generador(Paradero paraderoAutobuses, Paradero paraderoPersonas){ 
		filaAutobus = new ArrayList<Autobus>();
		filaPersonas = new ArrayList<Persona>();
		this.paraderoAutobuses = paraderoAutobuses;
		this.paraderoPersonas = paraderoPersonas;
		System.out.println("Se creó el generador");	
		this.filaPersonas = filaPersonas;
	}
	
	public void run() {		
		Random o = new Random(); 
		int i = 0;
		int j=0;
		while(bandera==true) {
			double autobusOPersona = Math.random();
					if(autobusOPersona < 0.500) {  //Genera autobus y lo añade a su respectiva fila
						if(i == 0) {
							Autobus autobus = new Autobus(paraderoAutobuses, null);
							filaAutobus.add(autobus);
							System.out.println("nuevo autobus en posición "+ (i+1));
							
							}else { 			
							Autobus autobus = new Autobus(paraderoAutobuses, filaAutobus.get(i-1));
							filaAutobus.add(autobus);
							System.out.println("nuevo autobus en posición "+ (i+1));					
						}
				i++;
				}
				else {     // Genera persona y lo añade a su respectiva fila. 

					if(j == 0) {
							Persona persona = new Persona(paraderoPersonas, null);
							filaPersonas.add(persona);
							System.out.println("nueva persona en posición "+ (j+1));
							
							}
							else { 			
							Persona persona = new Persona(paraderoPersonas, filaPersonas.get(j-1));
							filaPersonas.add(persona);
							System.out.println("nueva persona en posición "+ (j+1));
							}
				j++;
				}
					
					try {
						this.sleep(10);
					} catch (InterruptedException e) {
						e.printStackTrace();
					}

					if(i>= 100 && j>= 200){
						bandera = false;
					}
	}

	for(int h = 0; h<filaAutobus.size(); h++){
			for(int k = 0; k < filaPersonas.size(); k++){
				try{
					Thread.sleep(2000);
				}catch(Exception e){}
				if(filaAutobus.get(h).getPasajeLleno() == false){
						filaPersonas.get(k).sentarse(filaAutobus.get(h));
						filaPersonas.get(k).start();
				}
				else{	
					filaAutobus.get(h).start();
					if((h+1)< filaAutobus.size()){
						h++;
						k--;
					}
				}
			}
			System.out.println("Ya no hay más personas");
			if(h<filaAutobus.size()){
			filaAutobus.get(h).setPasajeLleno();
			filaAutobus.get(h).start();
			}

		}
	}
	
}

