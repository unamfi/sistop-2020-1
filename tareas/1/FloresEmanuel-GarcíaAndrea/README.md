# Tarea 1 Ejercicios de Sincronización

## Problema Elegido | De gatos y ratones

### Alumnos
- Flores Martínez Emanuel
- García Ruíz Andrea

## Lenguaje y Entorno de Desarrollo
El programa fue desarrollado con lenguaje de programación *Python 3.7.4*, tambíen funciona con *Python 3.6*. 
Su desarrollo fue en un sistema operativo tipo *Unix* por lo que se recomienda ejecutarlo en un sistema operativo similar.

El programa se ejecuta de la siguiente manera:

- Si se tiene instalado, *Python 3* por defecto:
~~~ 
python gato_raton.py [numero_gatos] [numero_ratones] [numero_platos] 
~~~

- Si se tiene instalado, *Python 2* por defecto, se debe verificar que se tenga instalado *Python 3*:

~~~ 
python3 gato_raton.py [numero_gatos] [numero_ratones] [numero_platos] 
~~~

Las palabras encerradas entre corchetes  corresponden a los parámetros que recibe el programa, estos deben ser números enteros mayores a cero.

### Ejemplo de ejecucion:

~~~
python gato_raton.py 8 5 6 
~~~

## Estrategia de Sincronización

Para resolver este problema se utilizó el patrón *__Apagador__*, ya que se tiene una situación de *exclusión categórica*, esto se da entre los gatos y los ratones, ya que si los gatos estan comiendo los ratones no pueden entrar y viceversa. Además este patrón nos permite evitar la inanición, lo cuál es otro de los requerimientos del problema.

Para resolverlo se utilizarón dos casos en los cuáles podía ocurrir la concurrencia:

- Un gato está comiendo, si llega un ratón a comer, el gato se come al ratón.

- Si un ratón está comiendo, un gato no puede ir a comer ya que es un caballero.