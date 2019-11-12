# Asignación de memoria

	Tarea creada el 2019.10.29
	Entrega: 2019.11.05

## ¿Qué hay que hacer?

Los modelos de _partición variable_ y _segmentación_ requieren que
el sistema operativo asigne y libere porciones de la memoria conforme
lo requiere el conjunto de procesos.

Asumamos que los procesos no pueden pedir el _ajuste_ (esto es, que
el espacio de memoria que solicitan en un inicio se mantiene durante
toda la vida del proceso).

Escriban un programa que vaya realizando esta asignación. Asuman un
sistema que tiene 30 _unidades_ de memoria (o, mejor aún, que sea
_parametrizable_); un proceso puede especificar que requiere entre 2 y
15 unidades.

Su programa puede recibir entrada aleatoria o del operador (ustedes
deciden cómo implementarlo, ambas estrategias valen).

1. Después de cada solicitud (de asignación o liberación de espacio),
   imprimir cómo queda el mapa de memoria. Por ejemplo,

	    Asignación actual:

		AABBBBCCCCDDDDDDEEEE---HHHII--
		Asignar (0) o liberar (1): 1
		Proceso a liberar (ABCDEHI): C
		Asignación actual:

		AABBBB----DDDDDDEEEE---HHHII--
		Asignar (0) o liberar (1): 0
		Nuevo proceso (J): 3
		Nueva asignación:
		AABBBBJJJ-DDDDDDEEEE---HHHII--

2. Resolver la solicitud de los procesos; si es necesario hacer una
   compactación, indíquenlo:

		AABBBBJJJ-DDDDDDEEEE---HHHII--
		Asignar (0) o liberar (1):
		Nuevo proceso (K): 5
		*Compactación requerida*
		Nueva situación:
		AABBBBJJJDDDDDDEEEEHHHII------
		Asignando a K:
		AABBBBJJJDDDDDDEEEEHHHIIKKKKK-

3. Indicar si están resolviendo las solicitudes por _peor ajuste_,
   _mejor ajuste_ o _primer ajuste_ — o, nuevamente, intenten
   resolverlo de forma que sea parametrizable.

## Precisiones de la entrega

Esta tarea puede ser entregada _de forma individual_ o _en equipos de
dos personas_.

## Calificaciones y comentarios

[Disponibles en el archivo calificaciones.org](./calificacion.org)
