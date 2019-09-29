import java.util.ArrayList;

public class ParaderoRuta {

	private int ruta;
	private ArrayList<Autobus> filaAutobuses = new ArrayList<>();
	private ArrayList<Persona> filaPasajeros = new ArrayList<>();
	
	
	public ParaderoRuta(int ruta){
		this.ruta = ruta;
	}

	public int getRuta(){
		return this.ruta;
	}

	public void formarAutobus(Autobus autobus){
		filaAutobuses.add(autobus);
        System.out.println("Hay "+ filaAutobuses.size() + " autobuses en la fila");
	}
	
	public void formarPasajeros(Persona pasajero) {
		this.filaPasajeros.add(pasajero);
        System.out.println("Hay "+ filaPasajeros.size() + " personas en la fila");
	}
}
