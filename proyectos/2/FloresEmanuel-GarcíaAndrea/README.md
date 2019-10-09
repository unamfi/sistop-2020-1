# Proyecto 2 | Restaurante Eléctrico

## Alumnos

- García Ruiz Andrea
- Flores Martínez Emanuel

## Plantamiento del problema

En uno de los mejores restaurantes de la Ciudad de México llega mucha gente de todo el mundo para probar la deliciosa comida mexicana, sin embargo como es un restaurante tan concurrido la empresa procurá estar atendiendo a la mayor clientela posible y tener espacio para los grupos grandes que puedan llegar.

Pero como siempre, el sistema no es perfecto, si un cliente encuentra que ya no hay disponibles mesas este tendrá que esperar en una fila hasta que se libere una y un mesero se la ofrezca.

Se cuentan con *m* meseros, los cuales son siempre menores al número de mesas *n* y su trabajo consiste en que si alguno esta desocupado lleva a los clientes a su respectiva mesa y les da la carta. Posteriormente se va a dormir a la estación hasta que sea requerido por cualquier actividad que se presente.

Los clientes de cada mesa se ponen de acuerdo para tener todas las peticiones listas antes de llamar al mesero, así el mesero solo tendrá que tomar una sola orden, de igual solo llamarán al mesero cuando todos hayan acabado de comer y deseen pedir la cuenta. 

Una vez que el mesero tiene la orden se la pasa a alguno de los chefs, que se tardará un tiempo indefinido para cada orden. El mesero debe estar al pendiente de cuando los alimentos esten listos, pero se le considerará desocupado por cualquier otra cosa que pueda atender dentro del restaurante.

## Mécanismo para resolver el problema

Se utilizaron varios mecanismos para la resolución del problema ya que al momento de hacer fila los clientes se podría comparar a un torniquete, ya que solo permite ir pasando de uno en uno cuando las mesas se van desocupando por los otros clientes. 

Por otro lado se utilizó el mecanismo de barrera cuando los clientes van a pedir una orden, ya que al momento de cada cliente y sus acompañantes saben que ordenar es cuando deben pedir la cuenta, por lo que los procesos se esperan entre sí.

Se lograró implementar de manera correcta, auque al principio había un deadlock, se solucionó, y el programa se ejecuta correctamente, los clientes que estan definidos por el usuario no son en realidad los que van a atender los meseros, ya que los invitados se generan de manera aleatorio, pero los clientes definidos por el usuario son los que pedirán una mesa y se formarán para obtener una.

Los colores se generan de manera aleatoria, lo que hace que más dinámico el programa en ejecución.

## Entorno de Desarrollo
Este programa se desarrolló en una sistema operativo tipo *UNIX* por lo que se recomienda ampliamente utilizarlo en un sistema similar. Está escrito en el lenguaje de programación *Python 3*, en específico la versión *3.7* sin embargo si se cuenta con la versión *3.6* no causa ningun conflicto.

## Ejecución
Para ejecutar el programa se utiliza el siguiente comando:

~~~
python proyecto2.py <mesas> <meseros> <clientes>
~~~

o bien

~~~
python3 proyecto2.py <mesas> <meseros> <clientes> 
~~~

en donde:

- *mesas* hace referencia a la cantidad de mesas que trabajan en el restaurante.
- *meseros* hace referencia a la cantidad de meseros que trabajan en el restaurante.
- *clientes* hace referencia a la cantidad de clientes que visitarán el restaurante.

### Ejemplo de Ejecución

~~~
python proyecto.py 20 8 7 
~~~