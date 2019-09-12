# Los Alumnos y el Asesor

---
Alumno: Romero Andrade Cristian
---

Un profesor de la facultad asesora a varios estudiantes, y estamos en su horario de atención.

Modelar la interacción durante este horario de modo que la espera(para todos) sea tan corta como sea posible.

## Reglas

 * Un profesor tiene *x* sillas en su cubículo (7 en este caso)
 
   * Cuando no hay alumnos que atender, las sillas sirven como
   sofá, y el profesor se acuesta a dormir la siesta.
	 
	 ```python
	 # En la clase Profesor
	 @classmethod
	 def dormir(cls, puede: bool):
		
		if puede:
		print('Zzzzzzzzzzzzzzzzzzzz...')
		sleep(1)
		print('desperté')
	 ```
	 
   * Los alumnos pueden tocar a su puerta en cualquier momento,pero no pueden entrar más de
   _x_ alumnos
   
   ```python
   # en main
   def entran_a_salon():
	  
	  while True:
          sleep(0.15)
          if randint(0, 1) == 1:
			  with TORNIQUETE:
				  CUB.entra_salon(ALUMNOS[randint(0, len(ALUMNOS)-1)])
   ```
   
   * Para evitar confundir al profesor, sólo un alumno puede presentar su duda
   (y esperar a su respuesta) al mismo tiempo
   
     * Los demás alumnos sentados deben esperar pacientemente su turno.
	 
	 * Cada alumno puede preguntar desde 1 y hasta _x_ (en este caso es hasta 7 o
	 hasta que el alumno quiera irse) preguntas(permitiendo que los demás alumnos pregunten entre una yotra)
   ```python
   # en main
   def inicia_clase():
	 while True:
		 with PREGUNTA:
             print(CUB.responder())
             sleep(0.1)
   ```
   
## Ejecución
 
Ubicarse donde se encuentra el archivo `main.py` y ejecutar:

```zsh
> python main.py
```

Para deterner usar la combinación de `C-c` en la terminal
