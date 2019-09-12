# Tarea 1. Los Alumnos y el Asesor

## Planteamiento
Un profesor de la facultad asesora a varios estudiantes, y estamos
en su horario de atención.
Modelar la interacción durante este horario de modo que la espera
(para todos) sea tan corta como sea posible.

## Reglas
* Un profesor tiene x sillas en su cubículo
  * Cuando no hay alumnos que atender, las sillas sirven como sofá, y el profesor se acuesta a dormir la siesta.
* Los alumnos pueden tocar a su puerta en cualquier momento, pero no pueden entrar más de x alumnos
* Para evitar confundir al profesor, sólo un alumno puede presentar su duda (y esperar a su respuesta) al mismo tiempo.
  * Los demás alumnos sentados deben esperar pacientemente su turno.
  * Cada alumno puede preguntar desde 1 y hasta y preguntas (permitiendo que los demás alumnos pregunten entre una y otra)

## Mi implementación
Decidí atacar el problema haciendo que el profesor, los alumnos y sus preguntas fueran hilos; el profesor esperando preguntas y los alumnos a su vez creando un hilo por cada pregunta, esto garantizaría que no hubiera un orden definido al responder preguntas.

El profesor tiene *x* sillas en su cubículo y los alumnos intentan entrar este usando un semáforo inicializado en *x*. Cuando el semáforo llega a 0, el cubículo no deja pasar más alumnos. 

Una vez dentro, los alumnos lanzan tantos hilos como preguntas tengan (la cantidad de preguntas se crea con un número entero al azar entre 1 y 6). Cada pregunta intenta adquirir un mutex, esto evita que dos alumnos pregunten al mismo tiempo. Al terminar la pregunta, se libera el mutex y despierta a algún hilo de pregunta lanzado por cuaquier alumno dentro del cubículo. 

Luego de agotarse todas las preguntas en la lista de un alumno, este libera el semáforo de acceso al cubículo y termina su ejecución, permitiendo que otro alumno pueda entrar.

## Requisitos
* python 3
* modulo faker instalado (instrucciones de instalación [aquí](https://pypi.org/project/Faker/))

## Pasos para la ejecución
Se debe ejecutar el script de python [main.py](./main.py) usando el comando

    $ python .\main.py

Por defecto, el cubículo inicia con 3 sillas y se crean 10 alumnos, uno por segundo. Para cambiar esta configuración, podemos darle argumentos por medio de línea de comandos con la siguiente sintaxis.

    $ python .\main.py -s <numero de sillas> -a <numero de alumnos>