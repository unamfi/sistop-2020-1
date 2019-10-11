# Comparación de planificadores

	Tarea creada: 2019.09.19
    Entrega: 2019.09.26

Revisamos en clase los mecanismos de planificación de procesos,
comenzando con los más sencillos (FCFS/FIFO, RR, SPN), y avanzando
hacia algunos más entretenidos (FB, SRR).

Vimos también las [pruebas que hizo Raphael
Finkel](http://gwolf.sistop.org/laminas/09_extras_planif_proc.pdf#page=5)
para comparar de forma más completa el rendimiento de cada uno de
ellos, ante una saturación estable. Comentamos que resulta iluso
comparar a estos distintos mecanismos únicamente a partir de un único
conjunto de procesos.

Para esta tarea, les pido que escriban un programa que genere *varias
cargas aleatorias*, y compare el resultado sobre varias
ejecuciones. Les pido que presenten unas cinco ejecuciones, para poder
comparar las tendencias — ¡Y revisen manualmente por lo menos algunos
de los resultados, para confirmar que son correctos!

Pueden entregar la tarea de forma individual, o en equipos de dos personas.

## Ejemplo de ejecución

Para considerar la tarea como entregada, basta con que presenten una
ejecución como la siguiente:

    $ ./compara_planif
	- Primera ronda:
      A: 0, t=3; B: 1, t=5; C: 3, t=2; D: 9, t=5; E: 12, t=5
		  (tot:20)
	  FCFS: T=6.2, E=2.2, P=1.74
	  RR1: T=7.6, E=3.6, P=1.98
	  RR4: T=7.2, E=3.2, P=1.88
	  SPN: T=5.6, E=1.6, P=1.32
	- Segunda ronda
	  A: 0, t=5; B: 3, t=3; C: 3, t=7; D: 7, t=4; E:8, t=4 (tot:23)
	  (...)

Claro está, estaré más contento (y ustedes más satisfechos, y les
facilitará verificar la ejecución) si presentan un esquema visual de
cómo sería la ejecución. Del ejemplo anterior:

	  FCFS: T=6.2, E=2.2, P=1.74
      AAABBBBBCCDDDDDEEEEE
	  RR1: T=7.6, E=3.6, P=1.98
	  ABABCABCBDBDEDEDEDEE
	  RR4: T=7.2, E=3.2, P=1.88
	  AAABBBBCCBDDDDEEEEDE
	  SPN: T=5.6, E=1.6, P=1.32
	  AAACCBBBBBDDDDDEEEEE

## ¡Vamos por el 10!

¿Cómo se calificará esta tarea?

- Toda entrega que muestre trabajo y se acerque al planteamiento,
  aunque no funcione, tiene asegurada una calificación mínima de 6
- Si replica exitosamente el primer ejemplo (sólo tabla de
  resultados), 7.5
- Si presenta el esquema visual, 9
- Si desarrollan un algoritmo de colas múltiples (retroalimentación
  multinivel/FB, ronda egoísta/SRR), 9
- Si presenta el esquema visual y además desarrollan un algoritmo de
  colas múltiples, 10

¿Les parece buena motivación? ☺

## Decisiones e interpretaciones

Al implementar los algoritmos, verán que hay puntos donde hay más de
un curso válido de acción. Por ejemplo, en el ejemplo que les dí, con
RR1: ¿Es correcto ABABCABC... o ABACBACB...? Ustedes, como
implementadores, pueden decidir — Ambos cumplen con el planteamiento
formal.

## Entrega

Hagan sus entregas siguiendo los lineamientos que hemos ido revisando
a lo largo de las prácticas 1, 2 y 3.

## Calificaciones

Pueden ver [las calificaciones a sus entregas aquí](./revision.org).
