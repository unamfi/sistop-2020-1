# Proyecto 3: (Micro) sistema de archivos

González Flores Andrés

## Requerimientos

- Python 3

## Descripción de la interfaz

Este proyecto está hecho con python 3, con una interfaz gráfica usando la librería tkinter.

Para correrlo es necesario tener en la misma carpeta un archivo de imagen de sistema llamado fiunamfs.img y ejecutar el comando `$ python FIUNAMFSExplorer.py` o `$ python3 FIUNAMFSExplorer.py`, dependiendo de cuál sea el nombre del ejecutable de python 3. Hacer esto nos mostrará una interfaz como la que sigue:

![Pantalla de Inicio](./screenshots/pantallainicio.png)

En ella se muestra una lista con los archivos del directorio con la información del cluster donde inician, su nombre, su tamaño en bytes, su fecha de creación y su fecha de modificación. También se  muestran botones para añadir, eliminar y descargar un archivo; así como un boton para desfragmentar la unidad. 

### Funciones

#### Copiar un archivo de nuestro sistema de archivos a FIUNAMFS

Para agregar un archivo es necesario ingresar el nombre y ruta completa o relativa del archivo de origen, el cuál se escribirá con el nombre puesto en el campo *Ruta de archivo de destino*.

![Agregando un archivo](./screenshots/agregar1.png)

En caso de existir un error, se mostrará el mensaje correspondiente a este (este programa no está hecho para aceptar duplicados, así que el ingresar otro archivo con el mismo nombre resultará en un error).

![Error de archivo duplicado](./screenshots/archduperr.png)

![Error de archivo no encontrado](./screenshots/notfounderr.png)

![Error de espacio de almacenamiento](./screenshots/errespacio.png)

#### Eliminar un archivo.

Para eliminar un archivo basta con seleccionarlo haciendo clic en él y oprimir el botón correspondiente. Hacer esto nos mostrará un cuadro de diálogo pidiendo confirmación.

![Eliminar paso 1](./screenshots/eliminar1.png)

Al confirmar, muestra mensaje de éxito y elimina el archivo.

![Eliminar paso 2](./screenshots/eliminar1.png)

#### Copiar un archivo de FIUNAMFS a nuestro sistema de archivos