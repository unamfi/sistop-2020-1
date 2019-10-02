# Proyecto 2 | Restaurante Eléctrico

## Alumnos

- García Ruiz Andrea
- Flores Martínez Emanuel

## Plantamiento del problema

En uno de los mejores restaurantes de la Ciudad de México llega mucha gente de todo el mundo para proba la deliciosa comida mexicana, sin embargo como es un restaurante tan concurrido la empresa maneja 3 tipos de mesas:
- Mesa por pareja (2 personas)
- Mesa familiar (4 personas)
- Mesa para reuniones (4 a 8 personas)
De esta manera procurá estar atendiendo a la mayor clientela posible y tener espacio para los grupos grandes que puedan llegar.

Pero como siempre, el sistema no es perfecto, por lo que se cuenta con *l* mesas por pareja, *m* mesas familiares y *n* mesas para reuniones entonces si un cliente encuentra que ya no hay disponibles mesas de su tipo este tendrá que esperar en un ifila hasta que se libere una y un mesero se la ofrezca.

Se cuentan con *z* meseros, los cuales son siempre menores al número de mesas y su trabajo consiste en que si alguno esta desocupado lleva a los clientes a su respectiva mesa y les da la carta. Posteriormente se va a dormir a la estación hasta que sea requerido por alguna de las mesas que atendió.

Los clientes de cada mesa se ponen de acuerdo para tener todas las peticiones listas antes de llamar al mesero, así el mesero solo tendrá que tomar una sola orden, de igual solo llamarán al mesero cuando todos hayan acabado de comer y deseen pedir la cuenta. Cabe resaltar que la mesa solo será atendida por el mesero que les asigno la mesa.

Una vez que el mesero tiene la orden se la pasa a alguno de los chefs, que se tardará un tiempo indefinido para cada orden. El mesero debe estar al pendiente de cuando los alimentos esten listos, pero se le considerará desocupado por cualquier otra cosa que pueda atender dentro del restaurante.

## Mécanismo para resolver el problema

## Entorno de Desarrollo
Este programa se desarrolló en una sistema operativo tipo *UNIX* por lo que se recomienda ampliamente utilizarlo en un sistema similar. Está escrito en el lenguaje de programación *Python 3*, en específico la versión *3.7* sin embargo si se cuenta con la versión *3.6* no causa ningun conflicto.

Se necesita del módulo *tqdm* para la correcta ejecución del programa, para instalarlo se utiliza el siguiente comando:
~~~
pip install tqdm
~~~

o bien

~~~
pip3 install tqdm
~~~

En el caso de no tener instalada la herramienta *pip* se tendrá que consultar el gestor de paquetes del sistema operativo, a continuación un ejemplo de como instalarlo en distribuciones basas en Arch Linux:

~~~
sudo pacman -S python-pip
~~~

## Ejecución
Para ejecutar el programa se utiliza el siguiente comando:

~~~
python proyecto.py <clientes> <meseros> <mesas_pareja> <mesas_familiar> <mesas_reuniones>
~~~

o bien

~~~
python3 proyecto.py <clientes> <meseros> <mesas_pareja> <mesas_familiar> <mesas_reuniones>
~~~

en donde:

- *clientes* hace referencia a la cantidad de clientes que visitarán el restaurante
- *meseros* hace referencia a la cantidad de meseros que trabajan en el restaurante
- *mesas_pareja* es la cantidad de mesas por pareja con las que cuenta el restaurante
- *mesas_familiar* es la cantidad de mesas familiares con las que cuenta el restaurante
- *mesas_reuniones* es la cantidad de mesas para reuniones con las que cuenta el restaurante

### Ejemplo de Ejecución

~~~
python proyecto.py 20 8 7 5 6
~~~