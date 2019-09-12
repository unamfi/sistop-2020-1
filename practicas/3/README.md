# Práctica 3: Ignorando archivos *innecesarios*

    Práctica creada el 2019.__.__
	Entrega: 2019.__.__

Los sistemas de control de cambios están hechos para poder dar
seguimiento a la historia de los archivos que forman parte de nuestro
proyecto. Ahora bien, cuando desarrollamos software, trabajamos con
conjuntos de datos, e incluso cuando escribimos prosa, es frecuente
que se generen archivos *derivados* de nuestro trabajo.

## Presentando el problema

¿A qué me refiero? Imagina que estás programando en C. Algo tan
sencillo como un *hola mundo*. Tu programa se llama `hola.c`:

	#include <stdio.h>
	int main() {
	    printf("Hola mundo!\n");
		return 0;
	}

Probaste el código, y funcionó correctamente:

    $ gcc hola.c
	$ ./a.out
	Hola mundo!
	$

Emocionado, quieres hacer tu commit como ya aprendiste: Primero
revisas el estado actual:

	$ git status
	On branch master
	Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
	  (use "git checkout -- <file>..." to discard changes in working directory)

		modified:   hola.c

    Untracked files:
      (use "git add <file>..." to include in what will be committed)

    	a.out

	no changes added to commit (use "git add" and/or "git commit -a")

Pero... ¿Por qué está ahí `a.out`? Porque es el nombre *por omisión*
de la salida del compilador de C (por lo menos, en sistemas Unix; en
tu entorno podría usar un nombre distinto): Es tu programa ya
compilado. Y dado que probablemente no sirva tal cual a otras personas
(ya sea porque sus versiones de las bibliotecas estándar sean otras, o
incluso usen un compilador distinto), hay que indicar a Git que ignore
ese archivo.

## La solución Git: El archivo .gitignore

Cada sistema de control de cambios tiene una manera distinta de evitar
este problema. En Git, basta con crear un archivo llamado `.gitignore`
en el directorio en que estés trabajando. Este directorio incluirá los
*patrones* de nombres de archivo a ignorar. En el caso en particular
aquí descrito, basta con que contenga la siguiente línea:

    a.out

Pero en un proyecto más grande, podrías requerir ignorar todos los
archivos objeto de C (`*.o`), todos los archivos compilados de Java
(`*.class`), o incluso las bitácoras (`*.log`) o bases de datos
(`*.sqlite`) generadas como parte de la operación de tu sistema.

Volviendo al caso descrito, creas el archivo .gitignore, y vuelves a
pedir el estado:

    $ git status
	On branch master
	Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
	  (use "git checkout -- <file>..." to discard changes in working directory)

		modified:   hola.c

    Untracked files:
      (use "git add <file>..." to include in what will be committed)

    	.gitignore

	no changes added to commit (use "git add" and/or "git commit -a")

Ahora sí, nos está mostrando únicamente los cambios que hicimos
personalmente. Vamos a hacer dos *commits* separados, detallando la
naturaleza de cada uno de estos cambios:

	$ git commit .gitignore -m 'Ignoramos los archivos autogenerados'
	$ git commit hola.c -m 'Terminamos la ejecución con un "return 0"'
	$ git push

Ahora sí, envías un *pull request* a tu maestro, y tienes tu punto
asegurado por un trabajo bien hecho.

# Ahora sí, la práctica

Quiero que repliquen lo que les presenté como situación
hipotética. Dentro del directorio de esta práctica, crea un directorio
con tu nombre, siguiendo la nomenclatura ya acordada. Dentro de este
directorio, crea un archivo que genere un archivo como consecuencia de
su compilación o uso — De preferencia, un programa relacionado con lo
que abordamos en estos días en clase.

Como siempre, sugiero manejar cada entrega en una rama separada — Ya
sabes cómo se hace.

Haz un primer commit que incluya a tu programa, *pero no al archivo
autogenerado*.

Haz un segundo commit con el archivo `.gitignore` únicamente.

Como siempre, envíame un *pull request* cuando hayas terminado la
práctica.

# Notas al pie

Un par de notas relacionadas con el manejo de `.gitignore`:

- *El nombre*. Por convención, en Unix se ignoran todos los archivos
  cuyo nombre comienza por `.` — Puede verse raro ante las prácticas
  actuales, pero vas a encontrar muchos archivos que siguen esta
  lógica. Busca algunos e intenta comprender lo que son.

- *De aquí pa'bajo*. Cuando creas un archivo `.gitignore`, su efecto
  se extiende a todos los subdirectorios debajo del directorio donde
  fue creado. Esto es, podríamos haber creado un `.gitignore` en el
  directorio principal; no lo hice para que cada uno de ustedes lo
  haga por su cuenta (o, como dicen, *¡pa' que aprendan!*).

- *Lo que ya existe no se ignora*. Si habías ya ignorado tu archivo
  `*.class`, `a.out`, `*.pyc` o similar, Git no lo ignorará a pesar de
  estar su nombre listado en el `.gitignore`; tienes que eliminarlo
  explícitamente del repositorio (con `git rm a.out`). Después de
  esto, Git ya lo ignorará.
