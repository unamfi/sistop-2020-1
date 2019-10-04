
import java.util.ArrayList;
import java.util.Random;
import java.util.concurrent.Semaphore;
import javax.swing.*;
import javax.swing.JPanel;
import java.awt.*;
import java.io.File;
import java.io.IOException;
import javax.imageio.*;
import javax.swing.JPanel;

/**
 *---Proyecto #2---
*@author Anguiano Morales Benjamin y Martín Mancilla Angel Omar
 */

public class Manejador1{
	public static void main(String[] args){
		
		
		Paradero paraderoAutobus = new Paradero(); 
		Paradero paraderoPersonas = new Paradero();
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
	int numeroAsientos = 3;
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
		//Adquiere un permiso del semáforo
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
	//Indica la persona que se encuentra delante en la fila.
	Persona personaAdelante; 				
	
	public Persona(Paradero paradero, Persona personaAdelante) { 
		this.paradero = paradero;
		this.personaAdelante = personaAdelante;
	}

	public void sentarse(Autobus autobus){
		autobus.dejarSubir(this);
	}

	public void setNoHayAutobus(){
		this.noHayAutobus = true;
	}

	public void run(){ 
		//Adquiere un permiso del semáforo para abordar el autobus
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
	public static JFrame interfaz = new JFrame();
	LaminaConBus laminaSoloBus = new LaminaConBus();
	LaminaConPersona laminaConPersona = new LaminaConPersona();
	LaminaSeVaBus laminaSeVaBus = new LaminaSeVaBus();
	ArrayList<Autobus> filaAutobus; 
				
	//Se usa para comprobar una condición.
	private boolean bandera = true;		
	//Servirá como 1 y 0 al generar autobus o persona.
	private int autobusOPersona;				
	//Es el semáforo para autobuses pasen a subir gente.
	Paradero paraderoAutobuses;
	//Semáforo para que la gente aborde de uno en uno el autobus.	
	Paradero paraderoPersonas;					
	
	ArrayList<Persona> filaPersonas;
		
	public Generador(Paradero paraderoAutobuses, Paradero paraderoPersonas){
		filaAutobus = new ArrayList<Autobus>();
		filaPersonas = new ArrayList<Persona>();
		this.paraderoAutobuses = paraderoAutobuses;
		this.paraderoPersonas = paraderoPersonas;
		System.out.println("Se creó el generador");	
		this.filaPersonas = filaPersonas;
		interfaz.setBounds(0, 0, 1920, 1080);
		interfaz.setVisible(true);
		interfaz.setDefaultCloseOperation(interfaz.EXIT_ON_CLOSE);
		interfaz.setResizable(true);
		
	}
	
	public void run() {		
		Random o = new Random(); 
		int i = 0;
		int j=0;
		
		while(bandera==true) {
			double autobusOPersona = Math.random();
			
					if(autobusOPersona < 0.500) { //Genera Autobus y lo añade a su fila
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
				else { //Genera Persona y lo añade a su fila

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
					
					/*try {
						this.sleep(10);
					} catch (InterruptedException e) {
						e.printStackTrace();
					}*/

					if(i>= 1000 && j>= 2000){
						bandera = false;
					}
	}
	for(int h = 0; h<filaAutobus.size(); h++){
			for(int k = 0; k < filaPersonas.size(); k++){
				try{
					this.sleep(2000);
				}catch(Exception e){}
				if(filaAutobus.get(h).getPasajeLleno() == false){
						if(k==0){
							this.interfaz.add(this.laminaConPersona);
							this.interfaz.repaint();
							
							
							try{
								this.sleep(2000);
							}catch(Exception e){}
							
							this.interfaz.remove(laminaConPersona);
							this.interfaz.repaint();
						}
						else{
							
							this.interfaz.add(laminaConPersona);
							this.interfaz.repaint();
							try{
								this.sleep(2000);
							}catch(Exception e){}
							this.interfaz.remove(laminaConPersona);
							this.interfaz.repaint();
						filaPersonas.get(k).sentarse(filaAutobus.get(h));
						filaPersonas.get(k).start();
						
					}
				}
				else{
					this.interfaz.add(laminaSoloBus);
					this.interfaz.repaint();
					
					try{
						this.sleep(1000);
					}catch(Exception e){}
					this.interfaz.remove(laminaSoloBus);
					this.interfaz.repaint();
					try{
						this.sleep(1000);
					}catch(Exception e){}
					this.interfaz.add(laminaSeVaBus);
					this.interfaz.repaint();
					try{
						this.sleep(2000);
					}catch(Exception e){}
					this.interfaz.remove(laminaSeVaBus);
					this.interfaz.repaint();
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





class LaminaConBus extends JPanel{
	private Image imagen;
	 
	public void paintComponent(Graphics g) {
		super.paintComponent(g);
		File miImagen = new File("autobus.jpg");
		try {
		this.imagen = ImageIO.read(miImagen);
		}catch(IOException e) {
			System.out.println("No se encontró la imagen");
		}
		
		
		g.drawImage(imagen, 300, 100, 600, 300, null);
	}
	
	
}

class LaminaSeVaBus extends JPanel{
	private Image imagen;
	 
	public void paintComponent(Graphics g) {
		super.paintComponent(g);
		File miImagen = new File("autobus.jpg");
		try {
		this.imagen = ImageIO.read(miImagen);
		}catch(IOException e) {
			System.out.println("No se encontró la imagen");
		}
		
		
		g.drawImage(imagen, 0, 100, 600, 300, null);
	}
	
	
}

class LaminaConPersona extends JPanel{
	private Image imagenBus;
	private Image imagenPersona;
	
	 
	public void paintComponent(Graphics g) {
		super.paintComponent(g);
		double cualPersona = Math.random();
		if(cualPersona < 0.334) {
		File persona = new File("persona.jpg");
		File autobus = new File("autobus.jpg");
		try {
		this.imagenBus = ImageIO.read(autobus);
		this.imagenPersona = ImageIO.read(persona);
		}catch(IOException e) {
			System.out.println("No se encontró la imagen");
		}
		}
		else if(cualPersona>0.333 && cualPersona<0.667 ) {
			File persona = new File("persona2.jpg");
			File autobus = new File("autobus.jpg");
			try {
			this.imagenBus = ImageIO.read(autobus);
			this.imagenPersona = ImageIO.read(persona);
			}catch(IOException e) {
				System.out.println("No se encontró la imagen");
			}
		}
		else{
			File persona = new File("persona3.jpg");
			File autobus = new File("autobus.jpg");
			try {
			this.imagenBus = ImageIO.read(autobus);
			this.imagenPersona = ImageIO.read(persona);
			}catch(IOException e) {
				System.out.println("No se encontró la imagen");
			}
		}
				
		g.drawImage(imagenPersona, 320, 430, 200, 150, null);
		g.drawImage(imagenBus, 300, 100, 600, 300, null);
		
	}
	
}
