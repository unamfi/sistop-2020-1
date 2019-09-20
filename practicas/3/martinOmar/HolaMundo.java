

public class HolaMundo extends Thread{
	public static void main(String [] args){
	
		HolaMundo miMundo1 = new HolaMundo(1);
		HolaMundo miMundo2 = new HolaMundo(2);
		HolaMundo miMundo3 = new HolaMundo(3);

		miMundo1.start();
		miMundo2.start();
		miMundo3.start();
	}

	public HolaMundo(int idThread){
		this.idThread = idThread;
		
	}

	public void run(){
		try{
			this.sleep((int)Math.random()*10000);
		}catch(Exception e){
			System.out.println("No pudo dormir el thread");
		}
		System.out.println("Hola Mundo, por omarmartin. Desde el thread "+ idThread);
	
	}

	private int idThread;

}
