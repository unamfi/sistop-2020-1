# Asignación de memoria -- Primer Ajuste

## Autor

* Romero Andrade Cristian

## Dependencias

Tener instalado _elixir_ y _mix_

* Arch Linux

  * `pacman -S elixir`
  
* Ubuntu 14.04/16.04/17.04/18.04/19.04 ó Debian 7/8/9 

  * Agregue el repositorio de Erlang Solutions: `wget https://packages.erlang-solutions.com/erlang-solutions_2.0_all.deb && sudo dpkg -i erlang-solutions_2.0_all.deb`
  * Ejecuta: `sudo apt-get update`
  * Instale la plataforma Erlang / OTP y todas sus aplicaciones: `sudo apt-get install esl-erlang`
  * Instalar Elixir: `sudo apt-get install elixir`

## Compilación

Ya se encuentra el archivo ejecutable con el nombre de `asigmem`, sin
embargo la compilación se hace de la siguiente manera.

Ubicarse en la raíz del proyecto y ejecutar

```bash
	mix escript.build
```

Al compilar se genera el binario en la raíz del proyecto

### Ejemplo de ejecución sin argumentos

```bash
./aigmen

Asignación:
uuuugg-----------nnnn-ggggg------y
Asignar o Liberar [a/l]: l
Proceso a liberar: u

Asignación:
----gg-----------nnnn-ggggg------y
Asignar o Liberar [a/l]: a
Nuevo Proceso [a] 20
*Compactación Requerida*
Nueva situación:
ggnnnngggggy----------------------
Asignando a aaaaaaaaaaaaaaaaaaaa

Asignación:
ggnnnngggggyaaaaaaaaaaaaaaaaaaaa--
Asignar o Liberar [a/l]: l
Proceso a liberar: x

Asignación:
ggnnnngggggyaaaaaaaaaaaaaaaaaaaa--
Asignar o Liberar [a/l]: l
Proceso a liberar: a

Asignación:
ggnnnngggggy----------------------
Asignar o Liberar [a/l]: q
```

### Ejemplo de ejecución con argumentos

```bash
./asigmem -p aabbcc---d--ee

Asignación:
aabbcc---d--ee
Asignar o Liberar [a/l]: a
Nuevo Proceso [f] 5
*Compactación Requerida*
Nueva situación:
aabbccdee-----
Asignando a fffff

Asignación:
aabbccdeefffff
Asignar o Liberar [a/l]: a
Nuevo Proceso [g] 1
*Compactación Requerida*
Nueva situación:
aabbccdeefffff

No hay espacio para el proceso

Asignando a g

Asignación:
aabbccdeefffff
Asignar o Liberar [a/l]: l
Proceso a liberar: e

Asignación:
aabbccd--fffff
Asignar o Liberar [a/l]: q
```
