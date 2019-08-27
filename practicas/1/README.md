# Práctica 1: Uso de Git y de Github

    Práctica creada: 2019.08.06
	Entrega: 2019.08.15

Esta práctica busca que tengas las herramientas básicas mínimas para
utilizar tanto Git como GitHub, y sirve como base para todas las
prácticas futuras.

Te recuerdo que, para comprender el funcionamiento de Git y la forma
de colaboración de GitHub, les dí una serie de ligas en la
[página principal del repositorio](https://github.com/unamfi/sistop-2020-1).

## 1. Tu cuenta de usuario

Entra a https://github.com y crea una cuenta de usuario. Si ya tienes
una, puedes (y te recomiendo) utilizar la ya existente.

## 2. Un *fork* del repositorio principal

El repositorio principal desde el que estaremos trabajando es
<https://github.com/unamfi/sistop-2020-1>; lo primero que debes hacer
es copiar el repositorio a tu espacio personal (hacer un "fork" — Una
bifurcación, o una copia). Para esto, oprime el botón "Fork" en la
parte superior derecha.

Notarás que, en la parte superior izquierda, en vez de mostrar
`unamfi/sistop-2020-1`, ahora lo mostrará con tu nombre de usuario.

## 3. *Clona* el repositorio

El siguiente paso es llevar una copia del repositorio a tu
computadora, para que puedas trabajar en él localmente. Hazlo con la
dirección que ofrece el botón verde, *clone or download*, en la parte
derecha de la pantalla.

Ojo, esto deberás hacerlo con el programa que elijas para manejar
*Git* en tu computadora. Hay muchos programas que manejan Git, y cada
uno de ustedes puede elegir el que prefiera. La
[página de descargas de Git](https://git-scm.com/downloads) ofrece
clientes para Windows, MacOS, Linux y Solaris; en Linux, te recomiendo
fuertemente utilizar el que ya viene *empaquetado* para tu
distribución.

Las instrucciones que doy en esta práctica asumen que estás usando una
interfaz Git de línea de comando; si prefieres usar una basada en
interfaz gráfica, queda para tí el convertir las instrucciones en
*ratonazos* ;-)

Si tu nombre de usuario es `fulano`, tendrás que hacer algo como:

    $ git clone https://github.com/fulano/sistop-2020-1.git

Eso traerá una copia del repositorio a tu computadora, desde donde
podrás trabajar.

Te recomiendo que ubiques a esta copia en un lugar donde puedas
mantenerlo a largo plazo, dado que seguiremos utilizando este
repositorio a lo largo del cursado de la materia.

Ahora, vamos a estar trabajando desde *dentro* de tu directorio
*clonado*:

    $ cd sistop-2020-1

## 4. ¿Dónde vas a hacer las entregas?

¡Nadie quiere que su trabajo se pierda! Para facilitar la organización
del repositorio (¡y la generación de calificaciones!), vamos a
estandarizar en cómo van a hacerse las entregas.  Todas las entregas
se harán dentro de un directorio, siguiendo la lógica que a
continuación detallo.

En el transcurso del cursado de la materia harán cuatro tipos de
entrega: `exposiciones`, `prácticas`, `proyectos` y
`tareas`. Compruébalo, existe un directorio en la raiz del repositorio
con cada uno de esos nombres.

A excepción de las `exposiciones` (habrá una sóla por persona), para
todos los demás tendremos varias entregas de cada una; las numeraremos
de forma progresiva (`1`, `2`, `3`, etc.)

Por último, está tu nombre. Para hacer las cosas más simples y
estándar, vamos a usar `ApellidoNombre` (primera letra en mayúscula,
las demás en minúscula, y sin espacios). Esto es, si yo (Gunnar Wolf)
estoy trabajando en la presente práctica (la primera), mi resolución
debe ir dentro de:

    practicas/1/WolfGunnar/

Si van a hacer una entrega de proyecto o tarea en equipo, compongan el
directorio con el nombre de ambos, en órden alfabético y separado por
un guión: Si Alonso Quijano trabaja junto con Martín Fierro en el
proyecto número 3, todo el material relacionado con esta entrega debe
ir dentro del directorio

    proyectos/3/FierroMartín-QuijanoAlonso/

## 5. Indica tu nombre y usuario en GitHub

Lo único que te pido en esta práctica es que crees un archivo de texto
con tu nombre de usuario y nombre real. Para esto, desde tu
computadora (*ya no* mediante la interfaz Web de GitHub) crea un
archivo de texto con tu nombre de usuario dentro del directorio que
corresponde. Volviendo al ejemplo del usuario `fulano`, asumiendo que
tu nombre es "*Fulano de Tal*", crea el archivo
`practicas/1/DeTalFulano/fulano.txt`, e indícame en él tu nombre. En
una máquina Linux, desde la línea de comando:

    $ cd practicas/1
	$ mkdir DeTalFulano
	$ cd DeTalFulano
    $ echo "Soy Fulano de Tal, y mi nombre de usuario es «fulano»" > fulano.txt

Puedes observar que Git todavía no sabe qué hacer con el archivo que
acabas de crear:

    $ git status
	On branch master
	Your branch is up-to-date with 'origin/master'.
	Untracked files:
	  (use "git add <file>..." to include in what will be committed)

        	practicas/1/DeTalFulano/fulano.txt

    nothing added to commit but untracked files present (use "git add" to track)

Es probable que tengas que indicarle a Git tu nombre y correo, para
dar *atribución* (recuerda que Git es en primerísimo lugar un sistema
de *desarrollo colaborativo*):

    $ git config --global user.name "Fulano de Tal"
	$ git config --global usre.email fulano@tal.org

## 6. Agrega tu archivo a Git y envíalo al servidor

Primero indica a Git que vas a agregar el archivo que creaste:

    $ git add fulano.txt

Y ahora crea un *commit*. Recuerda darle una descripción acorde:

    $ git commit -m 'Agrego el nombre de Fulano de Tal'

Git es un sistema *distribuido* de control de cambios. Esto significa
que tus cambios están ya registrados en la historia de Git, pero
únicamente en tu computadora. Para enviarlos a GitHub, basta con que
los *empujes* o *publiques* en el servidor:

    $ git push

## 7. Notifica de tus cambios con un *pull request*

¡Bien! Si vamos hasta aquí, lograste publicar tus cambios en
GitHub. La práctica, sin embargo, no ha sido *entregada*: Yo aún no se
nada al respecto. Si ves la página de tu repositorio en GitHub
(https://github.com/fulano/sistop-2020-1/ substituyendo, claro,
`fulano` por tu nombre de usuario), verás que GitHub te notifica en el
área central que estás *adelantado* al repositorio central: *This
branch is 1 commit ahead of unamfi/sistop-2020-1*.

Como comentamos en clase, el uso que quiero que den a GitHub es
similar al que le darían si estuvieran corrigiendo un defecto en un
proyecto de software libre: Encontraste que el proyecto tiene un
defecto (tu práctica #1 no ha sido entregada), elaboraste la
corrección, y le envías al desarrollador del proyecto el *parche* para
que lo corrija. Esto, en el uso de GitHub, se llama un *pull request*.

En esa misma línea, del lado derecho, haz click en *Pull
request*. GitHub te mostrará un resumen de las diferencias entre mi
versión y la tuya, y si te parece correcta, te permite seleccionar el
botón verde, *Create pull request*.

Describe los cambios que hiciste, confirma tu mensaje, y GitHub te
mostrará que la solicitud ha sido creada.

¡Felicidades! Entregaste la práctica. La pelota ahora está ya en mi
cancha, me toca a mi revisar los cambios.

## 8. Configura tu copia local para seguir al repositorio raiz

A lo largo del cursado de la materia, vamos a seguir usando este
repositorio. Para poder actualizar el repositorio con las
instrucciones relevantes cuando haya nuevas prácticas, tareas o
proyectos, te recomiendo indicarle que estarás siguiendo una *rama
remota*. Por ejemplo, podrías llamarla de forma que me describa, `prof`:

    $ git remote add --track master prof git://github.com/unamfi/sistop-2020-1

Esto significa, *agrega una fuente remota en la dirección mencionada,
siguiendo la rama maestra, y dale localmente el nombre `prof`*. Puedes
elegir cualquier otro nombre para esta rama — Es únicamente un
identificador que quedará en tu computadora.

Haz la prueba: un par de días después de haber entregado esta
práctica, entra al directorio de tu repositorio e indícale:

    $ git pull prof master

Esta instrucción significa, *trae la rama principal del repositorio
remoto `prof`*. Cuando vuelvas a comenzar a trabajar con tu
repositorio, recuerda hacer esto para sincronizar con los últimos
cambios que yo haya enviado.
