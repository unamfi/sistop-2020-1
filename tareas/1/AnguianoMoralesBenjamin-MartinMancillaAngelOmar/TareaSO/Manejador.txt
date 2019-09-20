import java.util.ArrayList;
import java.util.Random;
import java.util.concurrent.Semaphore;

/**
 *---Tarea #1---
*Programa que resuelve o trata de resolver el problema "De gatos y ratones"
*@author Anguiano Morales Benjamin y Martín Mancilla Angel Omar
*@version 12/09/19 5.0
 */

public class Manejador{
	/**
	 * Metodo main.
	 * @param args Este parametro es el utilizado para el "main" usualmente
	 */
	public static void main(String[] args){
		//Semáforo que me dará acceso a los platos.
		Plato platos = new Plato(3); 
		//Sirve para crear la lista donde pasarán los animales a comer.
		GeneradorAnimales generadorPlatos = new GeneradorAnimales(platos, null); 
		//Utiliza el generador de platos para crear la lista donde estarán los animales.
		ArrayList<Animal> estanciaPlatos = generadorPlatos.estanciaPlatos(platos.availablePermits()); 
		//Va generando aleatoriamente gatos y ratones. Además hace que pasen a comer.
		GeneradorAnimales generador = new GeneradorAnimales(platos, estanciaPlatos); 
		//Indica los permisos de inicio para el uso de los platos.
		System.out.println("Hay "+ platos.availablePermits()+ " platos para poder utilizar"); 
		//Inicia el generador.
		generador.start(); 	
	}
	
}

/**
 * Esta clase sirve para crear los platos y hereda de semaforos.
 * @see Semaphore 
 *
 */

class Plato extends Semaphore { 
	
	public Plato(int permisos) {
		super(permisos);
		
	}
}

/**
 * Esta clase generaliza a cualquier animal y asimila como un hilo.
 * @see Thread 
 *
 */

class Animal extends Thread{
	//Indica el animal que se encuentra delante en la fila.
	Animal animalAdelante; 
	//Indicará si es un gato "g" o un ratón "r"
	char tipo;				
	/**
	 * Método que se inicia con un start(); Es un hilo.
	 */
	public void run() {		
		
	}
}

/**
 * Es la clase que va generando animales, los forma en varias filas y les indica cuando deben pasar a comer.
 *@see Thread  
 *
 */

class GeneradorAnimales extends Thread{ 
	
	//Filas en donde se formarán los animales.
	ArrayList<Animal> numeroFilas[]; 
	//Indica el total de platos que hay.
	private int numeroPlatos;			
	//Se usa para comprobar una condición. Para pasar a los gatos si no hay ratones comiendo
	private boolean bandera = true;		
	//Servirá como 1 y 0 al generar gatos o ratones.
	private int gatoORaton;				
	//Sería la lista total de animales
	private ArrayList<Animal> animales = new ArrayList<>(); 
	//Es el semáforo.
	Plato platos;						
	//La lista donde pasan a comer.
	ArrayList<Animal> estanciaPlatos;	

	/**
	 * Este metodo es el que genera a los animales.
	 * @param platos Este parametro es para la utilizacion del plato.
	 * @param estanciaPlatos Aqui es donde se estan estanciando los platos.
	 */
	public GeneradorAnimales(Plato platos, ArrayList<Animal> estanciaPlatos){
		this.numeroPlatos = platos.availablePermits(); 
		numeroFilas = new ArrayList[numeroPlatos];
		this.platos = platos;
		System.out.println("Se creó el generador");	
		this.estanciaPlatos = estanciaPlatos;
	}
	
	/**
	 * Método que genera la fila. Arreglo de arreglos.
	 * @param numeroPlatos Se generan 'n' cantidad de platos.
	 */
	
	public void generarFilas(int numeroPlatos) {
		for(int i=1; i<numeroPlatos; i++) {
			System.out.println("Se generó la fila "+i);
			numeroFilas[i] = animales;
			}
	}
	/**
	 * Genera la estancia donde están los platos.
	 * @param numeroPlatos Numero de platos que se generaron.
	 * @return Regresa los platos estanciados y generados.
	 */
	public ArrayList<Animal> estanciaPlatos(int numeroPlatos) {  
		this.estanciaPlatos = new ArrayList<>();
		
		return estanciaPlatos;
	}
	
	/**
	 * Es el método que genera filas, animales que agrega a las filas y escoge cuándo comerán.
	 */
	public void run() {		
		
		for(int i=0; i<this.numeroPlatos; i++) {
			System.out.println("Se generó la fila "+i);
			numeroFilas[i] = animales;
			}
		//o es una variables random que se usará más abajo.
		Random o = new Random(); 
		while(bandera==true) {
			for(int i=0;i<10; i++) {
				for(int j=0;j<numeroFilas.length;j++) {
					gatoORaton = (int)o.nextInt(2);
					
					//Con cero, crea gatos con sus respectivas condiciones, según el problema enunciado.
					if(gatoORaton== 0) { 
						if(i == 0) {
							Gato gato = new Gato(platos, this.estanciaPlatos, null);
							numeroFilas[j].add(i, gato);
							System.out.println("nuevo gato en posición "+ i + " y fila "+ j);
							estanciaPlatos.add(gato);
							gato.start();
							}else { 			
							//Aquí son los gatos que no fueron el primero de cada fila y conocen al animal que tienen delante.
							Gato gato = new Gato(platos, estanciaPlatos, numeroFilas[j].get(i-1));
							numeroFilas[j].add(i, gato);
							System.out.println("nuevo gato en posición "+ i + " y fila "+ j);
							
							boolean hayRatones = true;
							int cantidadRatones = 0;
							
							//Comprueba si hay ratones en la estancia antes de que pase un gato.
							while(hayRatones == true) { 
								for(int w = 0; w<estanciaPlatos.size(); w++) {
									if(estanciaPlatos.get(w).tipo == 'r') {
										cantidadRatones = cantidadRatones+1;
										System.out.println("Hay un ratón comiendo en el plato "+ w);
									}
									else {
									}
								}
								if(cantidadRatones == 0) {
									System.out.println("No hay ratones comiendo");
									hayRatones = false;
								}else {
									System.out.println("!!!!!!! El gato no pudo pasar, hay ratones comiendo");
									try {
										gato.sleep(3000);
									} catch (InterruptedException e) {
										// TODO Auto-generated catch block
										e.printStackTrace();
									}
								}
								
							}
							//Añade al gato a la estancia si el animal de enfrente ya terminó de comer o si ya murió.
							try { 		
								if(numeroFilas[j].get(i-1).isAlive()) {
								numeroFilas[j].get(i-1).join();
								estanciaPlatos.add(gato);
								gato.start();
								}
								else {
									estanciaPlatos.add(gato);
									gato.start();
								}
							} catch (InterruptedException e) {
								
							}
							
						}
				}
				else { //Genera al ratón que pudiese estar al inicio de una fila y lo manda directo a comer.
					if(i == 0) {
						Raton raton = new Raton(platos, this.estanciaPlatos, null );
					
						numeroFilas[j].add(i, raton);
						System.out.println("nuevo raton en posición "+ i + " y fila "+ j);
						estanciaPlatos.add(raton);
						raton.start();
					}
					else{ 
						//Genera los ratones que no están al inicio de la fila, que conocen al animal que tienen delante y esperan a que desocupe el plato para pasar.
						Raton raton = new Raton(platos, this.estanciaPlatos, numeroFilas[j].get(i-1));
						numeroFilas[j].add(i, raton);
						System.out.println("nuevo raton en posición "+ i + " y fila "+ j);
						try {
							if(numeroFilas[j].get(i-1).isAlive()) {
							numeroFilas[j].get(i-1).join();
							estanciaPlatos.add(raton);
							raton.start();
							}
							else {
								raton.start();
							}
						} catch (InterruptedException e) {
							
						}
					}
				}
					
					try {
						this.sleep(1000);
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
					
					
				}
			}
			bandera = false;
		}
	}
	
}
 /**
  * Clase gato que hereda atributos y métodos de la clase Animal. Básicamente es un hilo.
  * @see Animal
  *
  */

class Gato extends Animal{ 	
	Animal animalAdelante;
	Plato plato;
	ArrayList<Animal> estanciaPlatos;
	char tipo;
	boolean hayRatones;
	
	/**
	 * Este metodo construye gatos.
	 * @param plato Este esl plato que se le sera asignado.
	 * @param estanciaPlatos Esta en la estancia que tendra el gato al plato.
	 * @param animalAdelante Aqui es donde el animal tendra el conocimiento de que animal es el que esta delante de el.
	 */
	
	public Gato(Plato plato, ArrayList<Animal> estanciaPlatos, Animal animalAdelante) { 
		this.tipo = 'g';
		this.plato = plato;
		this.estanciaPlatos = estanciaPlatos;
		this.animalAdelante = animalAdelante;
	}
	
	
	/**
	 * Método que indica el comportamiento del gato cuando va a comer.
	 */
	
	public void run() { 
		boolean hayRatones = true;
		
		//Adquiere un permiso el semáforo
		try {
			plato.acquire();		
			
		} catch (InterruptedException e) {
			System.out.println("El gato no pudo adquirir permiso para pasar a comer");	
		}
		
		estanciaPlatos.add(this);		//Pasa al gato a la estancia
		System.out.println("El gato está comiendo");
		try {
			this.sleep(3000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		//El gato observa los demás platos y, si ve a un ratón, se lo come.
		for(int h = 0; h<estanciaPlatos.size();h++) {  	
			if(estanciaPlatos.get(h).tipo == 'r') {
				System.out.println("GGGGGGGGGGGGGGGGGGGGG ha devorado al ratón del plato "+ h);
				//Interrumpe el proceso del ratón.
				estanciaPlatos.get(h).interrupt();			
				//Quita al ratón de la estancia
				estanciaPlatos.remove(estanciaPlatos.get(h));	
				//Libera el recurso que ocupaba el ratón
				plato.release();		
				
			}
		}
		//Saca al gato de la estancia
		this.estanciaPlatos.remove(this);	
		//Libera el recurso que ocupaba el gato
		this.plato.release(); 			
		System.out.println("Se ha liberado un plato por un gato "+ this.currentThread());
		System.out.println("Hay " +this.plato.availablePermits()+ " platos disponibles");
		
	}
	
}
/**
 * Clase que hereda atributos y métodos de la clase Animal. 
 * @see Animal
 *
 */

class Raton extends Animal{ 	
	//Animal que tiene delante en la fila.
	Animal animalAdelante;	
	//El semáforo que otorga los permisos.
	Plato plato;				
	//La estancia donde se encuentran los platos.
	ArrayList<Animal> estanciaPlatos;		
	//Tipo de animal.
	char tipo;						
	
	/**
	 * Este metodo construye ratones.
	 * @param plato Este esl plato que se le sera asignado.
	 * @param estanciaPlatos Esta en la estancia que tendra el gato al plato.
	 * @param animalAdelante Aqui es donde el animal tendra el conocimiento de que animal es el que esta delante de el.
	 */
	
	public Raton(Plato plato, ArrayList<Animal> estanciaPlatos, Animal animalAdelante) { 
		this.tipo= 'r';
		this.plato = plato;
		this.estanciaPlatos = estanciaPlatos;
		this.animalAdelante = animalAdelante;
		
	}
	
	/**
	 * Método que indica el comportamiento del ratón cuando va a comer.
	 */
	
	public void run() {
		
			//Adquiere permiso para pasar a comer
			try {
				plato.acquire();				
			} catch (InterruptedException e) {
					
				}
			//estanciaPlatos.add(this);
			System.out.println("El raton está comiendo");
			try {
				this.sleep(6000);
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			//Libera el recurso del ratón
			this.plato.release();		
			//Sale de la estancia el ratón
			this.estanciaPlatos.remove(this);	
			System.out.println("Se ha liberado un plato por un ratón "+ this.currentThread());
			System.out.println("Hay " +this.plato.availablePermits()+ " platos disponibles");
			
	}
		
}
