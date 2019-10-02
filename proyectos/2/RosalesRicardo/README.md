# Proyecto 2 Monitor de Vuelo

_En este proyecto se desarrollo una interfaz la cual probé de un login , de un sign in y ademas de la pantalla de monitoreo de vuelos_

## Entorno de desarrollo
1. Lenguaje de programación: **python 3.7.2**
2. Bibliotecas utilizadas: **random, PIL , pickle , time, datetime, math, tkinter ,threading **
3. Desarrollado y probado en: **macOS 10.14.6** 
**NOTA:** Debería funcionar en entornos UNIX con python 3.7.2 instalado

## Introducción
Sistop Airlines es un sisteam desarrollado para la visualización en tiempo real de los aviones que se encuentran en la pista de despegue y los que se encuentran listos para despegar, utilizando el concepto de semaforos para la correcta sincroniación de los eventos y asi no porvocar accidentes entre aviones. 

## Desarrollo

Se utilizo la librería de tkinder para desarrollar una interfaz más amigable con el usuario , además de un registro con ususario y contraseña , hasta el momento solo es permitido un usuario porque el método de almacenamiento de usuarios al ser modificado se sobre escribe.

Lo que de verdad interesa es la forma en la cual trabaja con los semaforos para impedir que dos o más aviones se encuentren en la pista final de despegue, permitiendo el acceso a pista secundaria a tres aviones y finalmente limitando la final apra única y exclisivamente un avión. 



### Pruebas de ejecución 

