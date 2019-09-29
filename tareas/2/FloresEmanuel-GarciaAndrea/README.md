# Tarea 2 Comparación de Planificadores

## Alumnos

- Flores Martínez Emanuel
- García Ruiz Andrea

## Introducción

En este proyecto se ha desarrollado un algoritmo de colas múltiples para la planificación de procesos que implementa el mecanismo *__retroalimentación multinivel__ (FB, multilevel feedback)* , se han utilizado 3 colas que simbolizan la prioridad de los procesos, siendo la *cola 0* la de mayor prioridad y la *cola 3* la de menor prioridad.
El número de procesos que se utilizan esta dado por el usuario. Para hacerlo más emocionante los procesos estarán en colas aleatorias, por lo que los procesos tendrán diferentes prioridades y será mas visible la implementación del algoritmo.

## Entorno de Desarrollo

Se recomienda para el correcto funcionamiento del programa utilizar un sistema *tipo Unix*, ya que se utilizan características específicas para este.
Para utilizarlo se debe tener instalado *Python 3*, ya que se necesitará instalar un módulo adicional que permitirá ver barras de progreso, para instalarlo se debe ejecutar el siguiente comando:

~~~
pip install tqdm
~~~

o bien

~~~
pip3 install tqdm
~~~

dependiendo de como se este manejando python en el sistema operativo.

## Ejecución

Para ejecutar el el programa se debe usar el siguiente comando desde línea de comandos:

~~~
python bf.py <num_procesos>
~~~

o bien

~~~
python3 bf.py <num_procesos>
~~~

en donde *num_procesos* es la cantidad de procesos que tendrá el programa.

### Ejemplo de ejecición
~~~
python bf.py 5
~~~