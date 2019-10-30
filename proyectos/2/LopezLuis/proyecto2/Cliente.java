/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package proyecto2;

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
