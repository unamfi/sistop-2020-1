# Proyecto 3 Sistop 2019-2

_El proposito de este proyecto es btener, crear y modificar información en el micro-sistema-de-archivos de la Facultad de Ingeniería, ```FiUnamFS.```_

## Introducción 📖

_El proyecto presenta un programa que permite dado un archivo .img un sistema de archivos muy sencillo bajo las características que se solicitaron y que permite realizar las siguientes operaciones:_

* **_Montaje_**
* **_Listado de Archivos_**
* **_Copiar archivos hacia el FS_**
* **_Eliminar archivos_**
* **_Desfragmentar_**


## Desarrollo 🛠 ️

_El programa solo contiene un archivo: ```filesi.py``` , el cual contiene la lógica que hace funcionar al sistema de archivos. A Continuación se describe dicha lógica:_ 

* **_getFiles_** : Abre y recorre el archivo obtenido de las listas de los nombres, tamaños y clusters e inicializan cada archivo.

* **_getInfo_** : Obtiene y guarda la información del sistema para luego mostrarla.

* **_copyTo_** : Copia a una dirección dada.

* **_deleteFile_** : Se encarga de borrar archivos.

* **_copyFrom_** :Copia archivos a la ruta de mi _programa.py_

* **_main_** : función principal donde se llaman todos los metodos anteriores._




## Pre-requisitos 📋

_Para poder compilar este programa, solo necesitamos tener Python2 instalados en nuestro sistema_

```
$ sudo apt-get install python3
```
_Compruebe que ya esta instalado_
```
$ python2 --version
```

## Compilación 🔧

_¿Cómo compilarlo? Fácil.._

_Una vez asegurandonos de tener instalado Python2, solo basta con poner desde la linea de comando:_


```
python2 filesi.py
```

_Aparecera un menú de opciones, donde podrás escoger una opción._

## Ejecutando las pruebas ⚙️

_Explica como ejecutar las pruebas automatizadas para este sistema_



## Y las pruebas de estilo de codificación ⌨️

_Aqui van impresiones del programa_

```
ejemplo
```

## Construido con 🛠️

Sistemas operativos utilizados:

* [_Kali Linux_ 64-Bit versión 2019.3](https://www.kali.org/downloads/) 
* [_Debian_ versión 10 _'Buster'_](https://www.debian.org/distrib/) 


## Repositorio Github 📖

Se puede obtener mas informacion a cerca del proyecto en el repositoro de [Github.](https://github.com/unamfi/sistop-2020-1/tree/master/proyectos/3)



## Autores ✒️

Este proyecto fué realizado por:

* **Ramos Barraza Jorge Luis** - [Github](https://github.com/jorgeluis098)- [Instagram](https://www.instagram.com/jorge.luis.rb/)-  [Facebook](https://www.instagram.com/jorge.luis.rb/)
* **Espinoza Cerón Brian Arian**  - [Github](https://github.com/brianarian)  -  [Instagram](https://www.instagram.com/brianarian)-  [Facebook](https://www.facebook.com/arianespin0za)




