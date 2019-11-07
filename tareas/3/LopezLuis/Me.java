package mem;

import java.util.LinkedList;
import java.util.concurrent.TimeUnit;

public class Me {
	public static void main(String [] args) throws InterruptedException {
		char [] memoria= new char [30];
		LinkedList<Character> procesos = new LinkedList<Character>();
		boolean [] procesosUti= new boolean[8];
		char elElegido = 0;
		procesos.add('A');
		procesos.add('B');
		procesos.add('C');
		procesos.add('D');
		procesos.add('E');
		procesos.add('F');
		procesos.add('G');
		procesos.add('H');
		  int opc=(int) Math.floor(Math.random()*2+1); 
		  int lug = memoria.length;
		  opc=1;
		  int res;
		while(true){
			if(opc==1){
				int letra=(int) Math.floor(Math.random()*8);
				if(procesosUti[letra]==false) {
				elElegido=procesos.get(letra);
				int veces=(int) Math.floor(Math.random()*(15-2+1)+2);
				if(lug>=veces) {
					res=meterproceso(memoria,veces,elElegido);
					System.out.println("Se mete proceso: "+elElegido+" utiliza:"+veces);
					while(res==1) {
						compactar(memoria,lug);
						res=meterproceso(memoria,veces,elElegido);
						System.out.println("Se mete proceso: "+elElegido+" utiliza:"+veces);
					}			
					
						lug=imprimir(memoria);

					procesosUti[letra]=true;
				}else {
					while(lug<veces) {
						sacarproceso(memoria, procesos,procesosUti);
						
					}
					
					int ok=0;
					
					ok=meterproceso(memoria,veces,elElegido);
					lug=imprimir(memoria);
					System.out.println("Se mete proceso: "+elElegido+" utiliza:"+veces);
					
					while(ok==1) {
						compactar(memoria,lug);
						ok=meterproceso(memoria,veces,elElegido);
						
					}
					lug=imprimir(memoria);
					System.out.println("Se mete proceso: "+elElegido+" utiliza:"+veces);
						
						
					}
				}
				
				}
			if(opc==2) {
				sacarproceso(memoria, procesos, procesosUti);
			}
			TimeUnit.SECONDS.sleep(4);
			}


		
		}



	
	
	
	static int meterproceso(char [] mem,int numero, char proceso) {
		int lugar = 0;
		int espacios = 0;
			for(int i=0;i<30;i++){
				if(mem[i]=='\0'){
					if(espacios==0){
					lugar=i;
					}
				espacios++;
				}else{
				espacios=0;
				lugar=-1;
				}

				if(espacios>=numero){
					for(int j=lugar;j<(lugar+numero);j++){
					mem[j]=proceso;
					
					}
					return 0;
				}

			}
	 if(espacios<numero){
		System.out.println("No hay espacio continuo para el proceso");
		
		}
	 return 1;	
	}
	
	static void sacarproceso(char[]men,LinkedList<Character> h,boolean []c) {
		char eLiluminado='\0';
		while(eLiluminado=='\0') {
			int letra=(int) Math.floor(Math.random()*30);
			 eLiluminado = men[letra];
		}
		
		for(int i = 0;i<men.length;i++) {
			if(men[i]==eLiluminado) {
				men[i]='\0';
			}
			
		}
		System.out.println("Se saco el proceso:"+eLiluminado);
		System.out.println();
		c[h.indexOf(eLiluminado)]=false;
	}
	static void compactar(char []mem,int lug) {	
		int dispo=0;
		Object x = null;
		int lugar=lugar(mem,dispo);
		dispo=lugar2(mem, dispo);
		int hasta=0;
		
		
		
		
		
		for(int i=dispo;i<mem.length;i++) {
			if(mem[i]==mem[dispo]) {
				hasta++;
			}else {
				break;
			}
		}
		 int hastcpy=hasta;
		for(int i =lugar;i<hastcpy+dispo;i++) {	
			if(hasta>0) {
				mem[i]=mem[dispo];
				hasta--;
			}else {
				mem[i]='\0';
				}
		}
		
		
		
		
		
		
		
		
		
	}
	static int lugar(char[]mem, int lugares) {
		int lugar=-1;
		int blanco = 0;
		
		boolean band=false;
		
		for(int i =0;i<mem.length;i++) {
			if(mem[i]=='\0'&& band==false) {
				blanco++;
				lugar=i;
				band=true;
			}else if(mem[i]=='\0'){
				blanco++;
			}
			else if(mem[i]!='\0' && band==true) {


				lugares=i; 
				break;
			}
		}
		
		return lugar;
		
	}
	
	static int lugar2(char[]mem, int lugares) {
		int lugar=-1;
		int blanco = 0;
		
		boolean band=false;
		for(int i =0;i<mem.length;i++) {
			if(mem[i]=='\0'&& band==false) {
				blanco++;
				lugar=i;
				band=true;
			}else if(mem[i]=='\0'){
				blanco++;
			}
			else if(mem[i]!='\0' && band==true) {
				
				lugares=i; 
				break;
			}
		}
		
		return lugares;
		
	}
	
	
	
	
	
	
	
	static int imprimir(char[]men) {
		int lugares = 0;
		for(int i=0;i<men.length;i++) {
		if(men[i]=='\0') {
			System.out.print("-");
			lugares++;
		}
			System.out.print(men[i]);
		
		}
		System.out.println();
		System.out.println("lugares disponibles "+lugares);
		
		return lugares;
	}
	
}
