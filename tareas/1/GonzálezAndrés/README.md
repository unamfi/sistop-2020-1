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