
public class Cliente {
	public static int Clientes=0;
	String nombre;
	int[]orden1= new int[2];
	
	public Cliente(String nombre, int[] orden) {
		this.nombre=nombre;
		this.orden1=orden;
		Clientes++;
	}

	public Cliente() {
		// TODO Auto-generated constructor stub
	}
	
}
