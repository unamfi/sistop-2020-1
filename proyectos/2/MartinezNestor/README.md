# Aeropuerto Internacional Benito Juárez 

## Integrantes

* Martínez Ostoa Néstor Iván 

## Identificación y descripción del problema

Sobre el aeropuerto Internacional Benito Juárez circulan miles de personas cada día, sin embargo, para asegurar un tránsito exitoso de personas hay mecanismos complejos de sincronización. El gobierno federal nos ha pedido que realicemos un sistema de computación que modele el tránsito de aviones coordinados por una torre de control. Aunado a esto, también hay que modelar la circulación de los viajeros desde que bajan del avión hasta llegar a la terminal correspondiente (ya sea Terminal 1 o Terminal 2). Para realizar este sistema de manera exitosa hay que considerar las siguientes reglas: 

0. En este aeropuerto, los operadores de la torre de control no saben cuando llegará un **avión** pues el sistema de comunicaciones con los otros aeropuertos del mundo no funciona. Aunado a esto, para cada terminal (1 o 2) solo hay una puerta de entrada. 

1. El trabajo de los **operadores** dentro de la torre de control será asegurarse que cada avión que llegue tenga asegurada una pista de aterrizaje. En caso de que no haya pistas de aterrizaje disponibles:
   1. *El operador tendrá que mandar al avión a dar otra vuelta*, en caso de que el avión tenga un nivel de combustible menor al 25%. 
   2. *El operador tendrá que mandar al avión al aeropuerto de Toluca*, en caso de que el avión tenga un nivel de combustible mayor al 25%. 
2. El aeropuerto Internacional Benito Juárez cuenta con 4 pistas de aterrizaje. 
3. Los aviones una vez que aterricen, tendrán tiempo para descargar a los **viajeros** y posteriormente despegar para salir y liberar la pista. Cada avión tendrá entre **1 y 10** viajeros.
   * Una pista de aterrizaje será liberada solo si todos los viajeros han bajado del avión. 
4. Una vez que los viajeros bajen del avión, habrá un **camión** que los llevará a la terminal deseada. El camión solo arrancará si tiene 30 personas dentro de él. Para cada pista de aterrizaje habrá un camión. 
5. Los viajeros, en caso de desesperarse, podrán tomar un **scooter** para llegar a su terminal deseada. 

## Mecanismos de sincronización

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sagittis ut nibh eu dictum. Cras auctor ante dolor, eu accumsan est imperdiet at. Nunc pulvinar, dolor ac lobortis accumsan, erat eros dictum nibh, at pulvinar enim metus id est. Aliquam erat volutpat. Integer rutrum at mauris ac hendrerit. Duis bibendum tristique neque, et pellentesque purus gravida in. Duis suscipit eros eget felis pretium posuere. Nam in rutrum dolor. Sed vehicula mauris at ipsum accumsan tristique. Nullam lobortis vulputate blandit.

## Lógica de operación

* **Estado compartido**:
  * Aliquam erat volutpat. Integer rutrum at mauris ac hendrerit. Duis bibendum tristique neque, et pellentesque purus gravida in. Duis 
* **Avance de cada hilo**: 
  * Aliquam erat volutpat. Integer rutrum at mauris ac hendrerit. Duis bibendum tristique neque, et pellentesque purus gravida in. Duis 
* **Interacción entre hilos**:
  * Aliquam erat volutpat. Integer rutrum at mauris ac hendrerit. Duis bibendum tristique neque, et pellentesque purus gravida in. Duis 

## Entorno de Desarrollo

* **Lenguaje**:
  * Aliquam erat volutpat. Integer rutrum at mauris ac hendrerit. 
* **Bibliotecas externas**:
  * Aliquam erat volutpat. Integer rutrum at mauris ac hendrerit. 
* **Sistema operativo**:
  * Aliquam erat volutpat. Integer rutrum at mauris ac hendrerit. 

## Screenshots

