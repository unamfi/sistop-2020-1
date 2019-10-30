
import java.io.BufferedOutputStream;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;

import java.io.FileWriter;
import java.io.IOException;

import java.io.RandomAccessFile;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.BasicFileAttributes;

import java.sql.Date;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.LinkedList;
import java.util.Scanner;


public class sistema {
	public static void main(String args[]) throws IOException {
		long longitud=0;
		char lec;
		String str;//fiunamfs.img
		byte[] buff= new byte[64];
		
		LinkedList<String> archivos = new LinkedList<String>();
		 Scanner sc =new Scanner(System.in);
		try {
			System.out.println("Dame el nombre del sistema de archivos,tiene que estar en tu directorio con el archivo fuente o introduce una ruta absoluta");
			str=sc.nextLine(); 
			File f = new File (str);
			 RandomAccessFile fichero = new RandomAccessFile(f, "rw");
			 nombrefich(fichero,f);
			 int opc=0;
			 while(opc!=6) {
			 System.out.println("opciones\n1.Listar\n2.Agregar\n3.Pasar a tu sistema\n4.Borrar"+
			 "\n5.Desfragmentar");
			 System.out.println("6 Para Salir");
			 opc=sc.nextInt();
			 String arch;
			 switch(opc) {
			 case 1:
				 listar(fichero, archivos);
				 break;
			 case 2:
				 System.out.println("Que archivo agregaras?, Con extension");
				 sc.nextLine();
				 str=sc.nextLine(); 
				 
				 listar2(fichero, archivos);
				 pasarAsis(fichero, str);
				 break;
			 case 3:
				 System.out.println("Que archivo pasaras a tu sistema?, Con extension");
				 sc.nextLine();
				 arch=sc.nextLine();
				 listar2(fichero, archivos);
				 Seleccion(fichero, arch, archivos);
				 break;
			 case 4:
				 System.out.println("Que archivo borraras?, Con extension");
				 sc.nextLine();
				 arch=sc.nextLine();
				 
				 listar2(fichero, archivos);
				 eliminar(fichero, archivos, arch);
				 break;
			 case 5:
				 listar2(fichero, archivos);
				 desfragmentar(fichero, archivos);
				 break;
			 }
			}
			
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}	
	
	
	public static int eliminar(RandomAccessFile arch,LinkedList<String> a,String nombre) throws IOException {
		String seleccion;
		for(int i=0;i<a.size();i++) {
			seleccion=a.get(i);
			if(seleccion.contains(nombre)) {
				double tamaño = Integer.parseInt(seleccion.substring(16, 24));
				int cluster = Integer.parseInt(seleccion.substring(25, 30));
				double clusternece=Math.ceil((tamaño/2048));
				arch.seek((cluster*2048));
				byte [] blanco = new byte[(int) (clusternece*2048)];
				arch.write(blanco);
				
				byte[] buff= new byte[64];
				String conte;
				for(int k=2048;k<10240;k+=64) {
					arch.seek(k);
					arch.read(buff);		
					conte=new String(buff);
					if(conte.contains(nombre)) {
						arch.seek(k);
						//Cadena de bytes que representan la entrada 							//disponible
						
						byte[] name= {88, 120, 46, 120, 88, 120, 46, 120, 88, 120, 46, 120, 88, 120, 46, 0, 48, 48, 48, 48, 48, 48, 48, 48, 0, 48, 48, 48, 48, 48, 0, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 0, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 0, 0, 0, 0};
						
						arch.write(name);
						
							
						
					System.out.println("Se logro");
					break;
					}
					}
				return 0;
			}
		}
		System.out.println("No tengo registro de ese archivo");
		return 0;
		
	}
	
	public static void pasar ( String ficheroCopia,byte []a)
	{
		try
		{
                 	//con un arreglo de bytes los pasa a sistema 
			FileOutputStream fileOutput = new FileOutputStream (ficheroCopia);
			BufferedOutputStream bufferedOutput = new BufferedOutputStream(fileOutput);
			
			
		
				bufferedOutput.write(a);
				
			

			
		
			bufferedOutput.close();
		}
		catch (Exception e)
		{
			e.printStackTrace();
		}
	}

	public static int pasarAsis(RandomAccessFile a,String nombre) throws IOException {
		//este metodo estatico pasa a sistema de archivos un archivo		
		//la funcion trim quita los espacios de una cadena
		//BasicFileAttrubutes es para obtener la fecha de creacion
		
		java.io.File fichero = new java.io.File(nombre);
		FileInputStream ficheroStream = new FileInputStream(fichero);
		byte contenido[] = new byte[(int)fichero.length()];
		ficheroStream.read(contenido);
		long ultima=fichero.lastModified();
		Path file = Paths.get(nombre);
		BasicFileAttributes attr = Files.readAttributes(file, BasicFileAttributes.class);
		String last =ultimamodi(ultima);
		long time =attr.creationTime().toMillis();
		String crea =ultimamodi(time);
		double tamanio =fichero.length();
		double cluster =tamanio/2048;
		cluster= Math.ceil(cluster);
		int clu =(int)cluster;
		int cluini = 0;
		String tam=String.format("%08d",(int)tamanio);
		boolean band=false;
		for(int i=10240;i<1474560;i+=2048) {
			a.seek(i);
			byte []ori= new byte[clu*2048];
			
			a.read(ori);
			String leido = new String(ori);
			leido=leido.trim();
			
			if(leido.equals("")) {
				a.seek(i);
				a.write(contenido);
				cluini=i/2048;
				band=true;
				break;
			}
			
		}
		if(band=false) {
			System.out.println("No se pudo ");
			return 0;
		}
		
		String clust=String.format("%05d", cluini);
		
		
		byte[] buff= new byte[64];
		String conte;
		
		
		for(int i=2048;i<10240;i+=64) {
			a.seek(i);
			a.read(buff);		
			conte=new String(buff);
			if(conte.contains("Xx.xXx.xXx.xXx.")) {
				a.seek(i);
				//aqui se busca un entrada disponible y se sustituyen los datos 				//obtenidos
				byte[] name= new byte[64];
				a.write(name);
				a.seek(i);
				 name =nombre.getBytes();
				 a.write(name);
				 a.seek(i+16);
				 name=tam.getBytes();
				a.write(name);
				a.seek(i+25);
				name=clust.getBytes();
				a.write(name);
				a.seek(i+31);
				name=last.getBytes();
				a.write(name);
				a.seek(i+46);
				name=crea.getBytes();
				a.write(name);
								
			System.out.println("Se logro");
			break;
			}
		}
		return 0;
		//AAAAMMDDHHMMSS		
	}
	
	public static int desfragmentar(RandomAccessFile a,LinkedList<String> b) throws IOException {
	byte [] buff = new byte [2048]; 
	int cluster=0;
	
	for(int i =10240;i<(720*2048);i+=2048) {
		a.seek(i);
		a.read(buff);
		String conte = new String (buff);
		conte=conte.trim();
		if(conte.equals("")) {
			cluster++;
		}else if(cluster>0) {
			int clusteract=i/2048;
			for(int k=0;k<b.size();k++) {
			String aux =b.get(k) ;
			String hype = b.get(k);
			if(aux.substring(25, 30).contains(String.valueOf(clusteract))) {
				//obtenemos el tamaño del archivo para saber donde 					//podriamos copiar				
				aux = aux.substring(16, 24);
				int ta=Integer.parseInt(aux);				
				byte[] contenido= new byte[ta];
				byte[] blanco=new byte[ta];
				a.seek(i);
				a.read(contenido);
				a.seek(i);
				a.write(blanco);
				a.seek((i-(cluster*2048)));
				a.write(contenido);
				a.seek(i);
				a.read(contenido);
				
				
				//se actualiza el directorio
				byte[] directorios= new byte[64];
				String directo;
				byte[] name= new byte[64];
				for(int j=2048;j<10240;j+=64) {
					a.seek(j);
					a.read(directorios);		
					directo=new String(directorios);
					if(directo.contains(hype)) {
						int cluini=((i/2048)-cluster);
						a.seek(j+25);
						String clust=String.format("%05d", cluini);
						name=clust.getBytes();
						a.write(name);
						a.seek(j+16);
						clust=String.format("%08d", ta);
						name=clust.getBytes();
						a.write(name);
						
						System.out.println("Se realizo");
						listar(a, b);
						desfragmentar(a,b);
						return 0;
					}
				}
				
				
				
				
			}
			
			
				
				
			}		
			
		}
		
		
	}
	System.out.println("Se acabo de desfragmentar");
		return 0;
		
		
	}
	//funcion que lista sin imprimir todas las funciones dependen de listar por lo que 		//actualizamos la lista de manera "oculta al usuario"
	public static void listar2(RandomAccessFile a,LinkedList<String> b) throws IOException {
		byte[] buff= new byte[64];
		String contenido;
		
		for(int i=2048;i<10240;i+=64) {
			a.seek(i);
			a.read(buff);		
			contenido=new String(buff);
			if(!contenido.contains("Xx.xXx.xXx.xXx.")) {
				b.add(contenido);
				//imparch(buff);
			}
		}
		
	}
	//pasamos los datos obtenidos de la ultima modificacion, los datos estan en milisegundos
	//los pasamos a una fecha
	public static String ultimamodi(long datos) {
		Date d= new Date(datos);
		Calendar c = new GregorianCalendar();
		c.setTime(d);
		int mes=(c.get(Calendar.MONTH)+1);
		String me=(String.format("%02d",mes));
		int dia=(c.get(Calendar.DATE));
		String di=(String.format("%02d",dia));
		int hora=(c.get(Calendar.HOUR_OF_DAY));
		String ho=(String.format("%02d",hora));
		int min=c.get(Calendar.MINUTE);
		String mi=(String.format("%02d",min));
		int seg=c.get(Calendar.SECOND);
		String se=(String.format("%02d",seg));	
		String last = Integer.toString(c.get(Calendar.YEAR))+me+di+ho+mi+se;
		return last;
		
	}
	
	public static void recorrer(RandomAccessFile a, String inicio, String tam,String no) throws IOException{
		int ta =Integer.parseInt(tam);
		int ini =Integer.parseInt(inicio);
		ini=ini*2048;
		byte[] buff= new byte[ta];
		String contenido;
	
			a.seek(ini);
			a.read(buff);
			pasar(no, buff);
			//contenido=new String(buff);
			//pasarAsistema(contenido,no);
			//System.out.println(contenido);
			
		}

	//este metodo no se utiliza me parece, no lo quite para que me de buena suerte
	public static void pasarAsistema(String a,String nom) {
		FileWriter fichero = null;
		try
		{
		//Crear un objeto File se encarga de crear o abrir acceso a un archivo que se 			especifica en su constructor
		File archivo=new File(nom);

		//Crear objeto FileWriter que sera el que nos ayude a escribir sobre archivo
		FileWriter escribir=new FileWriter(archivo);

		//Escribimos en el archivo con el metodo write
		escribir.write(a);

		//Cerramos la conexion
		escribir.close();
		}

		//Si existe un problema al escribir cae aqui
		catch(Exception e)
		{
		System.out.println("Error al escribir");
		}
		
	}
	//metodo qye busca nuestro elemento que queremos pasar a sistema de archivos y obtiene sus 	datos para copiar, cluster, tamaño 
	public static void Seleccion(RandomAccessFile a,String name,LinkedList<String> arch) throws IOException {
		String seleccion="";
		String tam="";
		String inicio="";
		for(int i=0;i<arch.size();i++) {
			seleccion=arch.get(i);
			if(seleccion.contains(name)) {
				tam = seleccion.substring(16, 24);
				inicio = seleccion.substring(25,30);
				recorrer(a,inicio,tam,name);
			}
		}
		
	}
	
	public static void listar(RandomAccessFile a,LinkedList<String> b) throws IOException {
		byte[] buff= new byte[64];
		String contenido;
		
		for(int i=2048;i<10240;i+=64) {
			a.seek(i);
			a.read(buff);		
			contenido=new String(buff);
			if(!contenido.contains("Xx.xXx.xXx.xXx.")) {
				b.add(contenido);
				imparch(buff);
			}
		}
		
	}
	public static void nombrefich(RandomAccessFile a,File b) throws IOException {
		String str="";
		for(int i=0;i<9;i++) {
			a.seek(i);
			char lec = (char) a.read();
			str = str+String.valueOf(lec);
			//System.out.print(lec);		
		}
	
		str=str.trim();
		System.out.println("El nombre del Sistema de archivos: "+str);
		if(str.equals("FiUnamFS")) {
			System.out.println("Estas en el sistema de archivos correcto");
		}else {
			System.out.println("No es el sistema");
			b.delete();
			System.exit(0);
		}
	}
	public static void imparch(byte[] x) {
		//String verif= new String(x,46,14);
		//if(!verif.contains(" ")) {
		System.out.println("Nombre:"+(new String(x,0,15).trim())+" Tamaño de"
				+ "l archivo:"+(new String(x,16,8).trim()+" Cluster Inicial:"
						+ ""+(new String(x,25,5).trim()))+" Hora y Fecha de creacion:"
								+ ""+new String(x,31,14).trim()+" Hora y fecha de ultima modificacion:"+new String(x,46,14).trim());
		//}
		}
	
}
