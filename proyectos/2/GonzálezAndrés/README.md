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
