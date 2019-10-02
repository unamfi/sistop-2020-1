# Proyecto 2. Una situación cotidiana paralelizable

## El problema: Un restaurante
En un restaurante tenemos *n* clientes pidiendo órdenes, *m* meseros atendiendo dichos clientes y *p* cocineros preparando platillos. El problema lo describo a continuación:

- El cliente tiene la tarea de pedir platillos y comerlos
- Sólo puede pedir un platillo a la vez a algún mesero desocupado.
- Mientras el cliente espera su órden, el cliente duerme.
- Cuando termina de comer, el cliente se retira del restaurante.

- El mesero tiene 4 tareas: 
  - Recibir órdenes de clientes.
  - Anotar órdenes en una lista para que los cocineros preparen los platillos en ella.
  - Verificar las órdenes listas.
  - Entregar órdenes al cliente.
- Estas tareas se pueden hacer sin un órden en específico.
- Un mesero sólo puede atender a un cliente a la vez.
- Los meseros solo duermen cuando no hay clientes en el restaurante.

- Los cocineros tienen la tarea de preparar los platillos que el mesero puso en la lista.
- El cocinero debe preparar un platillo a la vez y no puede haber más de un cocinero preparando el mismo platillo.
- Cuando terminen de prepararlos, deben ponerlos en lista de órdenes listas y avisarle al mesero.
- Un cocinero duerme cada que no tiene platillos que cocinar.

### Problemas que ocasiona la concurrencia en mi problema:

- Muchos cocineros podrían estar preparando el mismo platillo si no se comunican entre ellos.
- Muchos meseros podrían estar tomando la misma órden del mismo cliente.
- Muchos meseros podrían intentar recoger el platillo cocinado de la barra de platillos listos.

## Mi implementación

El programa iba a consistir en una serie de listas y variables de condición, algo así como una fila de bandas transportadoras de consumidores y productores, donde los consumidores de una a su vez serían productores de la otra.
Al final me confundí de fechas pensando que se entregaba el jueves, hasta que vi su correo del martes. Ya no pude implementar todo lo que quería. 

Lo que funciona es: 

- Los clientes llegndo al restaurante y pidiendo que los atiendan
- Los meseros durmiendo cuando no les dan una señal cada que llega un cliente
- Los meseros tomando órdenes de los clientes y "registrarlas" con su nombre

### Requisitos

- python 3
- módulo faker
- módulo [colorama](https://pypi.org/project/colorama/)