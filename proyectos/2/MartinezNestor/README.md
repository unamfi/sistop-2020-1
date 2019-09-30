# Aeropuerto Internacional Benito Juárez 

## Integrantes

* Martínez Ostoa Néstor Iván 

## Identificación y descripción del problema

Sobre el aeropuerto Internacional Benito Juárez circulan miles de personas cada día, sin embargo, para asegurar un tránsito exitoso de personas hay mecanismos complejos de sincronización. El gobierno federal  se quiere preparar para una falla de sistemas de comunicación a nivel mundial y saber cuánto le va a costar por día. El objetivo es realizar un sistema de computación que modele la actividad aeroportuaria cada día y calcular el costo por el manejo efectivo de los aviones y pasajeros. Este sistema tiene que modelar dos fenómenos principales: 

	1. El tránsito de aviones coordinados por operadores dentro de la torre de control. 
 	2. El tránsito de pasajeros desde que bajan del avión hasta que llegan a la terminal de salida. 

** **Nota importante**: el aeropuerto solo cuenta con una puerta por cada terminal. 



Para realizar este sistema de manera exitosa hay que considerar las siguientes reglas: 

* En este aeropuerto, los operadores de la torre de control no saben cuando llegará un avión pues el sistema de comunicaciones con los otros aeropuertos del mundo no funciona. 

* El trabajo de los operadores dentro de la torre de control será asegurarse que cada avión que llegue tenga asegurada una pista de aterrizaje. En caso de que no haya pistas de aterrizaje disponibles:
  * El operador tendrá que mandar al avión a dar otra vuelta, en caso de que el avión tenga un nivel de combustible menor al 25%. 
  * El operador tendrá que mandar al avión al aeropuerto de Toluca, en caso de que el avión tenga un nivel de combustible mayor al 25%. Sin embargo, esta opción penaliza al aeropuerto puesto que tiene que pagar el transporte de los viajeros de Toluca a la Ciudad de México. 

* El aeropuerto cuenta con solo 4 pistas de aterrizaje. 

* Los aviones una vez que aterricen, tendrán tiempo para descargar a los viajeros y posteriormente despegar para liberar la pista. Cada avión tendrá entre 1 y 10 viajeros.

* Una pista de aterrizaje será liberada solo si todos los viajeros han bajado del avión. 

* Una vez que los viajeros bajen del avión, habrá un camión que los llevará a la terminal deseada. El camión solo arrancará si tiene 30 personas dentro de él. Para cada pista de aterrizaje habrá un camión. 

* Los viajeros, en caso de desesperarse, podrán tomar un scooter para llegar a su terminal deseada. 



## Actores dentro del problema 



## Mecanismos de sincronización

Al iniciar el programa, se genera una cantidad inicial ```n``` de aviones. Estos aviones son detectados por la torre de control y agregados a una lista global de aviones detectados. La torre de control asigna un avión a un operador cuando el operador esté disponible. Cuando el operador decide qué hacer con el avión, éste quita al avión de la lista. Para este punto necesitamos dos mecanismos: 

* Una **señalización** para avisarle a cada operador que hay un avión en la lista. 
* Un **mutex** para proteger el acceso a la lista de aviones detectados pues es compartida entre los diferentes operadores. 

Una vez que un avión es asignado a un operador, el operador se encarga de trabajar con él. Para esto, tiene que consultar una lista global de pistas de aterrizaje disponibles. Si se encuentra una pista disponible, el avión es asignado a ésta y quitado de la lista global de aviones detectados. Para esto necesitamos lo siguiente: 

* Un **mutex** para proteger las operaciones a la lista de pistas de aterrizaje disponibles. 

En caso de que no haya disponibilidad en las pistas, el operador tiene que tomar la decisión de mandar al avión a dar una vuelta o mandarlo al aeropuerto de Toluca. 

* Si elige mandarlo a dar una vuelta, el operador cambia la prioridad del avión a urgente y lo agrega de nuevo a la lista de aviones detectados. Para estas operaciones, necesitamos un **mutex**. 
* Si elige mandarlo a Toluca, el operador tiene que avisarle a un camión en Toluca para que reciba a los pasajeros de ese vuelo y los traiga a la Ciudad de México. Para esto necesitamos una **señalización**. 

Una vez que un avión haya aterrizado en una pista, la pista de aterrizaje detecta esto y avisa al camión que tiene que venir a recoger a los viajeros de ese vuelo. 

* Para esto necesitamos implementar **rendezvous** puesto que el hilo de un camión estará a la espera de que el hilo de la pista tenga un avión y por ende, viajeros que transportar. 

Posteriormente, los pasajeros tienen que bajarse del avión y conforme van bajando, se van agregando a una lista global de pasajeros en tierra. El tiempo de desembarque dependerá de factores como el número de pasajeros y la edad de ellos. La edad pues suponemos que personas de edad mayor o niñ@s tardarán en promedio más tiempo que un adulto. Una vez finalizado el desembarque de pasajeros, el avión despegará y liberará la pista de aterrizaje. 

* Para lo anterior, necesitamos un **mutex** para agregar a los pasajeros a la lista global de pasajeros en tierra y para agregar la pista de aterrizaje a la lista global de pistas de aterrizaje disponibles. 

Una vez que los pasajeros se encuentren en tierra, estos tendrán dos opciones: tomar un camión para llegar a la terminal o tomar un scooter. El camión solo puede arrancar si tiene 30 pasajeros dentro de él, de lo contrario, tendrá que esperar a que lleguen más vuelos. 

* Para lograr lo anterior, necesitamos emplear una **barrera** puesto que el camión tiene que esperar a que lleguen 30 pasajeros para arrancar. 
* También necesitamos un **mutex** para proteger los accesos a una lista de pasajeros en el camión.
* Sin embargo, como el aeropuerto puede manejar 4 camiones (pues es un camión por pista de aterrizaje) necesitamos emplear una lista de semáforos para ir indicando a qué pista se dirigirá un camión.

En caso de que algún pasajero se desespere, puede solicitar un scooter para irse directo a la terminal. 

* Para lograr lo anterior, empleamos una **cola** pues tenemos dos clases de hilos (Viajero y Scooter) y ambos deben proceder en pares. 

* Sin embargo, como el aeropuerto puede manejar 20 scooters, necesitamos emplear una lista de de 20 semáforos inicializados en 0 que se irán liberando conforme los pasajeros los vayan usando. 

Cuando un pasajero llega a la terminal, es necesario actualizar las siguientes listas utilizando un **mutex**:

* Lista de pasajeros en tierra 
* Lista de scooters disponibles 
* Lista de camiones disponibles

## Lógica de operación

* **Estado compartido**:
  * Pistas de aterrizaje disponibles. 
* **Avance de cada hilo**: 
  * Aliquam erat volutpat. Integer rutrum at mauris ac hendrerit. Duis bibendum tristique neque, et pellentesque purus gravida in. Duis 
* **Interacción entre hilos**:
  * Aliquam erat volutpat. Integer rutrum at mauris ac hendrerit. Duis bibendum tristique neque, et pellentesque purus gravida in. Duis 

## Entorno de Desarrollo

* **Lenguaje**:
  * Python 3.7.4
* **Bibliotecas externas**:
  + -- 
* **Sistema operativo**:
  * MacOs 10.14.6

## Para ejecutar el programa





## Screenshots

