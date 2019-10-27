# Plan de solución

- [x] Setup inicial
  - [x] Crear un archivo con el nombre del sistema de archivos. Este archivo será el punto de partida de todo el sistema de archivos porque desde aquí se controlará lo que el usuario quiera hacer -> ```OstoaFS.py``` 
  - [x] Crear directorio vacío donde estarán las definiciones de las clases que el sistema de archivos necesitará -> ```fslib``` 
- [x] Detectar comandos del usuario 
- [x] Abrir ```fiunams.img``` 
  - [x] Crear clase ```FileManager``` encargada de abrir el archivo ```FiUnamFS.img``` y vaciar el contenido del superbloque (cluster 0) en la clase ```SuperBlock```. 
    - [x] Esta clase debe hacer la verificación de que la cadena del sistema de archivos sea ```FiUnamFS```. 
- [ ] Crear clase ```CommandManager``` encargada de definir las 5 funciones que pueda realizar el usuario sobre el sistema de archivos : 
  - [ ] Listar contenidos 
  - [ ] Copiar hacía adentro
  - [ ] Copiar hacía afuera
  - [ ] Eliminar archivo 
  - [ ] Desfragmentar 
- [ ] Agregar comentarios 