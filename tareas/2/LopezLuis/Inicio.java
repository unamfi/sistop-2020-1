
public class Inicio {
	public static int[][] generaProcesos() {
		int [][]num=new int [5][2];
		int M = 20;
		
		int sumtot=0,dif=0,mayo=0,cual = 0;
		int valorEntero=0;
		for(int i=0;i<5;i++) {			
		   valorEntero = (int)(Math.random()*M)+1;
		   
		   M=M-valorEntero;
		   sumtot=sumtot+valorEntero;
		   if(i==5) {
			   num[i][0]=valorEntero+M;
		   }else {
		   num[i][0]=valorEntero;
		   //System.out.println(valorEntero);
		   }
		}
		if(sumtot>20) {
			dif=sumtot-20;		
			for(int i=0;i<5;i++) {
				if(num[i][0]>mayo) {
					mayo=num[i][0];
					cual=i;
				}
			}
			num[cual][0]=num[cual][0]-dif;
		}
		//for(int i=0;i<5;i++) {
		//	if(num[i][0]==0);
			//band=true;
		//	break;
			//}	
		//if(band==true) {
			//Inicio.generaProcesos();
		//}
		//num=Inicio.verificar(num);
		for(int i=0;i<5;i++) {
			if(num[i][0]==0) {
			
			num[i][0]=1;
			num[cual][0]=num[cual][0]-1;
			
			}	
		}
		System.out.println("Tiempo de espera de cada proceso");
		for(int i=0;i<5;i++) {
			System.out.println(num[i][0]);
		}
		//System.out.println(num);
		 return num;
		 }
	
	public static int[][] generaLLegada() {
		int num[][]=new int [5][1];
		
		 return num;
		 }
	public static int[][] verificar(int arr[][]) {
		boolean band=false;
		for(int i=0;i<5;i++) {
			if(arr[i][0]==0);
			band=true;
			break;
			}	
		if(band==true) {
			Inicio.generaProcesos();
		}
		return arr;
	}
	
	public static void main(String []args) {
		int [][] num=new int [5][2];
		boolean band=false;
		//for(int i=0;i<5;i++) {
			num=Inicio.generaProcesos();
	//	}			
		//	num[0][0]=1;
	    //num[1][0]=13;
		//	num[2][0]=3;	
			//num[3][0]=1;
			//num[4][0]=2;	
			
			
			
			
		num[0][1]=0;
		num[1][1]=3;
		num[2][1]=4;	
		num[3][1]=7;
		num[4][1]=9;
		Algoritmos prueba = new Algoritmos();
		//prueba.SPN(num);
		prueba.FCFS(num);
		System.out.println();
		System.out.println("R1");
		prueba.R1(num);
		System.out.println();
		System.out.println("R2");
		prueba.R4(num);
		
		
		
	}
}
