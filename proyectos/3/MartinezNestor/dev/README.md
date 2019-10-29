# OstoaFS - Ostoa File System 

## Integrantes 

```
Martínez Ostoa Néstor Iván 
```

## Preámbulo

Para este proyecto cree un programa en ```Python 3.7.4``` que fuera capaz de realizar las siguientes operaciones sobre un micro sistema de archivos llamado ```FiUnamFS```: 

1. Listar el contenido de ```FiUnamFS```. 
2. Copiar uno de los archivos de dentro del `FiUnamFS` hacia ```OstoaFS```. 
3. Copiar un archivo de tu computadora hacia `FiUnamFS`. 
4. Eliminar un archivo del `FiUnamFS`. 
5. Desfragmentar ```FiUnamFS```. 

## Entorno y dependencias 

Entorno: 

* Programa escrito en ```Python 3.7.4``` 

Dependencias externas: 

* Internas de ```Python```: 
  * ```datetime```,  ```mmap``` , ```optparse```, ```os``` , ```random```.

## Desarrollo 

### 0. Ayuda sobre como manjear ```FiUnamFS```:

![icon](../images/help.png)

Aquí se pueden observar los comandos disponibles que el usuario puede emplear para manejar el micro sistema de archivos ```FiUnamFS```. 



### 1. Listar 

![icon](../images/list.png)

Este comando lista el contenido del directorio raíz de ```FiUnamFS```. 



### 2. Copiar uno de los archivos de ```FiUnamFS``` hacía tu computadora

![icon](../images/cpo.png)

Todos los archivos que el usuario quiera copiar desde ```FiUnamFS``` hacía su computadora se guardarán en un directorio llamado ```cpo_files```. 



### 3. Copiar un archivo de tu computadora hacía ```FiUnamFS``` 

![icon](../images/cpi.png)

Aquí no hay mayor ciencia, solo copia un archivo de tu directorio al directorio raíz de ```FiUnamFS```.



### 4. Eliminar un archivo de ```FiUnamFS``` 

![icon](../images/rem.png)



### 5. Desfragmentar ```FiUnamFS``` 

![icon](../images/defrag.png)