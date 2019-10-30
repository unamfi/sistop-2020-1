# (Micro) sistema de archivos

## Autor

* Romero Andrade Cristian

## v7.0

# Lenguaje

Python 3

## Uso

Solo ejecutar

```bash
python3 main.py
```

## Funciones

* Lista el contenido
* Del sistema de archivos al sistema externo
* Del sistema externo al sistema de archivos
* Elimina Archivo
* Desfragmentar

## Lo que contenía fiunamfs.img

* README.org

![con1](img/con1.png)

* logo.png

![con2](img/con2.png)

* mensajes.jpg

![con3](img/con3.png)

## Notas:

Para el archivo de prueba que se [nos otorgo](./fiunamfs.img), este estaba para
un sistema acoplado a 1024 en vez del que se nos pidió 512. se nota ya que se empieza
por el 400 hexadecimal en vez del 200 hexadecimal (Claro si es que no estoy ignorando algo).
![prueba](img/error_de_prueba_espanto.png)

Aunque aquí si en vez de Xx.xXx.xXx.xXx. de lo pedido es encuentra AQUI_NO_VA_NADA
![aqui](img/aqui_esxx.xx.png)

Pero bueno aplicando unos pequeños cambios para probar la operaciones, aqui va el
ejemplo de la desfragmentación.

Antes
![antes](img/antes.png)

Después
![despues](img/despues.png)


Se anexa [una imagen de prueba generada con los requerimientos](algo.img)
