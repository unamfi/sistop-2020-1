import java.util.*;
public class Algoritmos {
	
	public void FCFS(int [][] array){ 
	int orden[]= new int [5];
	LinkedList<Integer> val = new LinkedList<Integer>();
	int ini[]= new int [5];
	int ter[]= new int [5];
	int reflex[]= new int [5];
	int timeactu=0;	
	
		
		for(int i=0;i<5;i++) {
			orden[i]=array[i][1];	
			val.add(array[i][1]);
		}		
		bubbleSort(orden);
		for(int i=0;i<5;i++) {
			reflex[i]=val.indexOf(orden[i]);				
			}
		
		for(int i=0;i<5;i++) {
			
			if(orden[i]<timeactu) {
				ini[i]=timeactu;
				}
			
			if(orden[i]==timeactu) {
				ini[i]=orden[i];
			}
		ter[i]=timeactu+array[i][0];
		timeactu=ter[i];
		}	
		
		
		System.out.println("FCFS");
		System.out.println("Proceso   Inicio   Final");
		for(int i=0;i<5;i++) {
			System.out.println(reflex[i]+"            "+ini[i]+"        "+ter[i]);				
			}	
	}
	public void R1(int [][] array) {
		int orden[]= new int [5];
		LinkedList<Integer> val = new LinkedList<Integer>();
		LinkedList<Integer> tempo = new LinkedList<Integer>();
		int ini[]= new int [5];
		int ter[]= new int [5];
		int res[]= new int[5];
		int reflex[]= new int [5];
		int timeactu=0;	
		int ultima=0;
		for(int i=0;i<5;i++) {
			orden[i]=array[i][1];	
			val.add(array[i][1]);
			tempo.add(array[i][0]);
		}		
		bubbleSort(orden);
		for(int i=0;i<5;i++) {
			reflex[i]=val.indexOf(orden[i]);	
			res[i]=tempo.get(reflex[i]);	
		}
		
	/*	for(int i=0;i<5;i++) {
			ultima=ultima+array[i][0];
			ultima=ultima+array[i][1];
		}*/
			//System.out.println(ultima);
		for(int i=0;i<5;i++) {
					
		}
		boolean sw=false;
		while(!vacio(res)) {
			
		for(int i=0;i<5;i++) {
			if(sw) {
				timeactu--;
				sw=false;
			}
			if(orden[i]<=timeactu && res[i]>0){
				res[i]=res[i]-1;
				System.out.print(reflex[i]);
				timeactu++;
				
			}else {
				timeactu++;
				sw=true;
			}
			
			
		}
		
		
		}
				
		
	}
	
	public void R4(int [][] array) {
		int orden[]= new int [5];
		LinkedList<Integer> val = new LinkedList<Integer>();
		LinkedList<Integer> tempo = new LinkedList<Integer>();
		int ini[]= new int [5];
		int ter[]= new int [5];
		int res[]= new int[5];
		int reflex[]= new int [5];
		int timeactu=0;	
		int ultima=0;
		for(int i=0;i<5;i++) {
			orden[i]=array[i][1];	
			val.add(array[i][1]);
			tempo.add(array[i][0]);
		}		
		bubbleSort(orden);
		for(int i=0;i<5;i++) {
			reflex[i]=val.indexOf(orden[i]);	
			res[i]=tempo.get(reflex[i]);	
		}
		
		
		boolean sw=false;
		while(!vacio(res)) {
		for(int i=0;i<5;i++) {
			if(sw) {
				timeactu--;
				sw=false;
			}
			if(orden[i]<=timeactu && res[i]>0){
				if(res[i]<3) {
					res[i]=0;
				}else {
				res[i]=res[i]-4;
				}
				
				System.out.print(reflex[i]);
				timeactu++;
				
			}else {
				timeactu++;
				sw=true;
			}
			
			
		}
		
		
		}
				
		
	}
	public void SPN(int [][] array) {
		int orden[]= new int [5];
		LinkedList<Integer> val = new LinkedList<Integer>();
		LinkedList<Integer> tempo = new LinkedList<Integer>();
		LinkedList<Integer> cort = new LinkedList<Integer>();
		LinkedList<Integer> aux = new LinkedList<Integer>();
		LinkedList<Integer> pasadas = new LinkedList<Integer>();
		int del=0;
		int global1=0;
		int global2=0;
		int global3=0;
		int global4=0;
		int global5=0;
		int ini[]= new int [5];
		int ter[]= new int [5];
		int res[]= new int[5];
		int reflex[]= new int [5];
		int timeactu=0;	
		int ultima=0;
		int cont=0;
		for(int i=0;i<5;i++) {
			orden[i]=array[i][1];	
			val.add(array[i][1]);
			tempo.add(array[i][0]);
		}		
		bubbleSort(orden);
		for(int i=0;i<5;i++) {
			reflex[i]=val.indexOf(orden[i]);	
			res[i]=tempo.get(reflex[i]);	
		}
		int val_min=0;
	
		while(true) {
			cort.removeAll(cort);
		 for(int i=0;i<orden.length;i++) {
			 if(orden[i]<=timeactu) {
				 cort.add(res[i]);
			 }
		 }
		 aux.add(res[0]);
		 aux.add(res[1]);
		 aux.add(res[2]);
		 aux.add(res[3]);
		 aux.add(res[4]);
		 if(!pasadas.isEmpty()) {
		 for(int i=0;i<pasadas.size();i++) {		
			 int va=pasadas.get(i);
			 if(va==0) {
			//	 	aux.add(cort.get(0))		 
			 }else if(va==1) {
				 aux.add(res[1]);
			 }else if(va==2) {
				 aux.add(res[2]);
			 }else if(va==3) {
				 aux.add(res[3]);
			 }else if(va==4) {
				 aux.add(res[4]);
			 }
				
				
				
			}
		 }
		if(!cort.isEmpty()) {
			val_min=cort.get(0);
		for(int i=0;i<cort.size();i++) {
			if(cort.get(i)<=val_min) {
				val_min=cort.get(i);			
			}
		}
		
		del=cort.indexOf(val_min);
		cort.remove(del);
		
		if(array[0][0]==val_min && global1!=1) {
			ultima=0;
			global1=1;
		}else
		if(array[1][0]==val_min && global2!=2) {
			ultima=1;
			global2=2;
		}else
		if(array[2][0]==val_min && global3!=3) {
			ultima=2;
			global3=3;
		}else
		if(array[3][0]==val_min && global4!=4) {
			ultima=3;
			global4=4;
		}else
		if(array[4][0]==val_min && global5!=5) {
			ultima=4;
			global5=5;
		}
		if(pasadas.contains(ultima)) {
			timeactu++;
		}else {
		pasadas.add(ultima);
		
		System.out.print(ultima);
	  cont++;
	  timeactu=timeactu+val_min;
		if(cont==5) {
			break;
		}
		}
		}else {
			timeactu++;
		}
		}
	} 
	

	
	boolean vacio(int a[]) {
		boolean vacio = false;
		for(int i=0;i<a.length;i++) {
			if(a[i]>0) {
				vacio=false;
				break;
			}
			else {
				vacio=true;
			}
		}
		
		
		return vacio;
	}

	
	
	void bubbleSort(int arr[]) 
    { 
        int n = arr.length; 
        for (int i = 0; i < n-1; i++) 
            for (int j = 0; j < n-i-1; j++) 
                if (arr[j] > arr[j+1]) 
                { 
                    int temp = arr[j]; 
                    arr[j] = arr[j+1]; 
                    arr[j+1] = temp; 
                } 
    } 
}
