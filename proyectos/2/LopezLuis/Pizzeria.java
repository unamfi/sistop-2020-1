import java.util.LinkedList;
import java.util.concurrent.TimeUnit;

public class Pizzeria {
	public static void main(String [] args) throws InterruptedException {
	LinkedList<String> nombresCli = new LinkedList<String>();
	LinkedList<String> nombresEmple = new LinkedList<String>();
	System.out.println("Bienvenido");
	
	nombresCli.add("Joaquin");
	nombresCli.add("Rafael");
	nombresCli.add("Saul");
	nombresCli.add("Óscar");
	nombresCli.add("Alberto");
	nombresCli.add("David");
	
	nombresEmple.add("Ismael");
	nombresEmple.add("Alonso");
	nombresEmple.add("Oliver");
	nombresEmple.add("Nico");
	nombresEmple.add("Jorge");
	
	while(true) {// van llegando situaciones: se generan items,o se atienden personas
	int num=(int) (Math.random()*2);
	if(num==0) {
		Personal generador = new Personal();
		generador.start();
	}
	if(num==1) {
		int [] orden = {(int) (Math.random()*15),(int) (Math.random()*6)};
		Cliente cli = new Cliente(nombresCli.get((int) (Math.random()*6)),orden);
		Personal emple = new Personal(nombresEmple.get((int) (Math.random()*4)),cli);
		emple.start();
	}
		
			
		TimeUnit.SECONDS.sleep(1);
		
	}
	
	}

}
