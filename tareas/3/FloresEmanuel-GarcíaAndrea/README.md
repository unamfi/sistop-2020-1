# Tarea 3 | Asignación de Memoria

## Alumnos

- García Ruiz Andrea
- Flores Martínez Emanuel

## Plantamiento del problema

Los modelos de partición variable y segmentación requieren que el sistema operativo asigne y libere porciones de la memoria conforme lo requiere el conjunto de procesos.

Asumamos que los procesos no pueden pedir el ajuste (esto es, que el espacio de memoria que solicitan en un inicio se mantiene durante toda la vida del proceso).

## Mécanismo para resolver el problema

En este caso tenemos una memoria de tamaño limitado, por defecto es 30, pero puede ser modificado por el usuario. La memoria que abarca cada proceso es variable y esta dada por el usuario, puede abarcar desde 1 hasta la longitud de la memoria, si se sobrepasa simplemente no habrá espacio para reservar y mandará un error. 

El proceso de asignación de memoria, será el mismo durante todo el programa, sin embargo se puede decidir el método que se usará, cada uno funciona de la siguiente manera:

### Primer Ajuste
En este caso a el proceso se le asignará la primera memoria que se encuentre disponible. Hay que tener en cuenta los posibles casos:

- Si hay memoria disponible, pero el tamaño es menor al tamaño del proceso se seguirá buscando en la siguiente área de memoria.
- En el caso de que haya memoria disponible, pero este repartida en segmentos diferentes se hará uso de la compactación, para así poder agregar la memoria.

### Mejor Ajuste
En este método, se buscará la memoria que quede mejor con el tamaño del proceso, esto quiere decir que, si un segmento es exactamente igual al tamaño de nuestro proceso se le asignará este espacio, sin importar la posición de este. Hay que tomar en cuenta que:
- Si no se encuentra un segmento del mismo tamaño que el proceso, se debe tomar el segmento que sea más cercano a el tamaño del proceso.
- Se debe tomar en cuenta que si hay memoria disponible pero no hay ningun segmento disponible del tamaño del proceso, se deberá hacer compactación para agregar el proceso.

### Peor Ajuste
El peor ajuste es lo contrario al mejor ajuste, en vez de buscar cuál segmento dsponible podría ser mejor para el proceso, siempre se asignará el más grande, este método es más rápido que los otros dos, pero es más probable que queden pequeños segmentos vacíos, por lo que será más frecuente el proceso de compactación.

Otra función importante es liberar la memoria, que básicamente consiste en quitar a un proceso de la memoria para que pueda ser utilizado por otro proceso.

## Entorno de Desarrollo
Este programa se desarrolló en una sistema operativo tipo *UNIX* por lo que se recomienda ampliamente utilizarlo en un sistema similar. Está escrito en el lenguaje de programación *Python 3*, en específico la versión *3.7* sin embargo si se cuenta con la versión *3.6* no causa ningun conflicto.

El programa hace uso del módulo `argparse`, es importante verificar que se encuentra instalado. Para instalarlo se puede usar el comando:

~~~
pip install argparse
~~~

## Ejecución
Hay varias maneras de ejecutar el programa, pero se especificarán los principales parámetros:
- `-m [INT], --memory [INT]`: Con esta bandera se especifica el tamaño de la memoria, si no se pone esta bandera por defecto el tamaño es 30.
- `--fist-adjust`: Esta bandera hace referencia a que se usará el método de primer ajuste para asignar memoria.
- `--best`: Esta bandera hace referencia a que se usará el método de mejor ajuste para asignar memoria.
- `--worst`: Esta bandera hace referencia a que se usará el método de peor ajuste para asignar memoria.

Si no se especifica un método mandará un error.

~~~
python tarea3.py [<-m [INT]>] <--first-adjust | --best | --worst>
~~~

### Ejemplo de Ejecución

- Ejecución con la memoria por defecto, usando el primer ajuste.
~~~
python tarea3.py --first-adjust
~~~

- Ejecución con tamaño de memoria de 60, usando el peor ajuste.
~~~
python tarea3.py -m 60 --worst
~~~