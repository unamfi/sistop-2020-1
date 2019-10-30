# Microsistema de archivos

## Alumnos

* Flores Martínez Emanuel
* García Ruiz Andrea

## Planteamiento del problema

Desarrollar un programa que pueda obtener, crear y modificar información en el micro-sistema-de-archivos de la   Facultad de Ingeniería, `FiUnamFS`.

Siguiendo la especificación que aparece en la siguiente sección,tienen que desarrollar un programa que pueda:

1. Listar los contenidos del directorio
2. Copiar uno de los archivos de dentro del `FiUnamFS` hacia tu sistema
3. Copiar un archivo de tu computadora hacia tu `FiUnamFS`
4. Eliminar un archivo del `FiUnamFS`
5. Desafortunadamente, este sistema de archivos *simplote* es muy dado     a la fragmentación externa. Generen también un programa que     *desfragmente* al `FiUnamFS`. Ojo, la defragmentación debe hacerse     *dentro del sistema de archivos* (no creando un sistema de archivos     nuevo y copiando hacia éste).

## Descripción de la solución

Para este proyecto se tomaron en cuenta los requísitos de implementación, dados en el planteamiento 
por el profesor. Se crearon 3 clases las cuales se describen a continuación:

#### Clase Superbloque
Contiene toda la información general del sistema de archivos, de qué tamaño serán los clústers, cuántos clústers tenemos, etc.

#### Clase ENT_DIR
Define cómo están construidas todas las entradas de directorio; es decir qué datos debe tener y en qué posición.

#### Clase FSUnamFI
Utiliza los datos brindados por las 2 clases anteriores para realizar el funcionamiento requerido en el planteamiento. Contiene las funciones para listar, borrar, copiar un archivo de FIUnamFs a nuestra máquina, copiar un archivo de nuestra máquina al sistema de archivos y defragmentar.

## Entorno y dependencias

Este programa se desarrolló en una sistema operativo tipo *UNIX*  por lo que se recomienda ampliamente utilizarlo en un sistema similar. Está escrito en el lenguaje de programación *Python 3*, en específico la versión *3.5.3*.

Este programa se probó en sistema basado en Debian (Deepin 15.10.1 GNU/Linux).

## EjecuciÃ³n

Para ejecutar el `FiUnamFS ` se cuenta con tres tipos de comandos distintos

* Los comandos que no necesitan parámetros `ls` y  `dfg`
* Los comandos que cuenta con un parámetro `cp_in` y `rm`
* Y `cp_out` que cuenta con dos parámetros.

#### ls

```bash
python3 fiunamfs.py ls
```

![ls](img/ls.png)

#### dfg

``` bash
python3 fiunamfs.py dfg
```

![dfg](img/dfg.png)

#### rm

```bash
python3 fiunamfs.py rm
```

![dfg](img/rm.png)

#### cp_in

``` bash
python3 fiunamfs.py cp_in <nombre_archivo>
```

![dfg](img/cp_in.png)

#### cp_out

```bash
python3 fiunamfs.py cp_out <nombre_archivo> <ruta>
```

![dfg](img/cp_out.png)

