# Revisión de MiComputer

	Planteamiento: 20.08.2019
    Entrega: 29.08.2019

Corría la década de 1980, y niños y jóvenes nos entusiasmábamos con
aprender computación. Las computadoras eran simples, y con un poco de
empeño, podíamos comprender sus diversos aspectos.

Además... Bueno, en México no teníamos acceso a buena parte del
panorama — Conocíamos a unos pocos sistemas dominantes (Apple 2,
Commodore 16 y 64, algunas versiones de la Timex Sinclair...), y tener
acceso a información técnica adicional nos resultaba invaluable.

¡Bienvenidos a mi mundo!

## MiComputer

La revista española MiComputer se vendía en casi todas las esquinas en
México. Es la traducción al español del *Home Computer Course*,
publicado en el Reino Unido. ¿Pueden imaginar este tipo de contenido
en una revista _para cualquiera_ el día de hoy?

Encontré scanneados
[los primeros 24 ejemplares de MiComputer](http://web8bits.com/Coleccion/Libros/Espanhol/MiComputer/MiComputer.html)
en la página _Web8Bits_. El _Internet Archive_ tiene los mismos
[24 ejemplares en inglés](https://archive.org/details/The_Home_Computer_Course),
si prefieren conocer la versión original.

## Eligiendo nuestro fascículo

Este proyecto es para realizarse, tanto como sea posible, *en equipos
de dos personas*.

Podría pedirles que elijan un fascículo al azar, pero estoy seguro que
la distribución distaría mucho de ser homogénea ☺ Por tanto:

*m = m<sub>1</sub> + m<sub>2</sub>*

*f = &lfloor; (m % 100) / 4 &rfloor;*

*f == 0 ⇒ f = rand(24)*

Esto es:

- Sumen el número de *matrícula* de alumno (o número de *cuenta*) de
  ambos participantes del equipo. En caso de que hayas quedado sin
  pareja, asume que *m<sub>2</sub> = 00000000*.

- Tomen sus dos últimos números (*m módulo 100*).

- Divídanlos sobre 4 (con aritmética entera, descartando partes
  fraccionales)

- Si los últimos dos números de la suma son 00, 01, 02 o 03 elige un
  fascículo al azar.

Por favor, indica en la entrega el número de matrícula de ambos.

## ¿Qué leer?

Revisa la tabla de contenido del fascículo que te toca.

Todos los números tenían como artículo central la reseña de un equipo
de cómputo. Lee la reseña que corresponda a tu fascículo.

Además, elige otro tema de los que presenta dicho fascículo que llame
tu atención, enfocándote en los temas que vimos hasta ahora en clase.

## ¿Qué hacer?

Les pido que desarrollen una reseña de lo que leyeron, prestando
especial atención a los temas que abordamos en clase, y apuntando qué
aspectos de ambos artículos les resultaron más interesantes o
notorios.

Te pido que la reseña sea *corta* (unas 2-3 páginas en total; no
repitas lo que leíste, resume lo que llamó tu atención.

## ¿Cómo cuenta este ejercicio?

Este cuenta como el *primer proyecto* de la materia. Esto es, como si
fuera un examen parcial.

## Calificaciones y comentarios

Conforme vaya calificando, [los iré publicando aquí](./calificaciones.org).
