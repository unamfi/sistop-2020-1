# Plan de solución

- [ ] Setup inicial
  - [ ] Crear un archivo con el nombre del sistema de archivos. Este archivo será el punto de partida de todo el sistema de archivos porque desde aquí se controlará lo que el usuario quiera hacer -> ```OstoaFS.py``` 
  - [ ] Crear directorio vacío donde estarán las definiciones de las clases que el sistema de archivos necesitará -> ```Library ``` 
- [ ] Detectar comandos del usuario 
  - [ ] Crear clase ```UserManager``` encargada de detectar las acciones que el usuario quiere realizar. Esta clase tendrá su participación principal dentro de ```OstoaFS.py```   
  - [ ] Esta clase recibe como parámetros principales los argumentos desde la consola, los procesa y manda a llamar a las funciones correspondientes dependiendo de los argumentos. Esta clase delega su funcionalidad a la clase ```ActionManager```. 
  - [ ] Esta clase también se encarga de manejar los errores del usuario al introducir los argumentos. 
- [ ] Abrir ```fiunamds.img``` 
  - [ ] Crear clase ```FileManager``` encargada de abrir el archivo ```FiUnamFS.img``` y vaciar el contenido del superbloque (cluster 0) en la clase ```SuperBlock```. 
    - [ ] Esta clase debe hacer la verificación de que la cadena del sistema de archivos sea ```FiUnamFS```. 
- [ ] Crear clase ```ActionManager``` encargada de definir las 5 funciones que pueda realizar el usuario sobre el sistema de archivos : 
  - [ ] Listar contenidos 
  - [ ] Copiar hacía adentro
  - [ ] Copiar hacía afuera
  - [ ] Eliminar archivo 
  - [ ] Desfragmentar 