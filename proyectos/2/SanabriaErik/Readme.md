# Proyecto 2

Proyecto 2 de Erik Sanabria Betancourt (415021636).

- El lenguaje utilizado es `C++ 2017`.

## Documentación

- [Documentación](https://docs.google.com/document/d/1d_4FKo_zNpxnDSwCBcXSQYZYe-6ZIZT-JwtrXpVZeWE/edit?usp=sharing).
- UML con [Umbrello](https://umbrello.kde.org/) ubicado en `Docs/`.

**Planteamiento:**

- Este programa busca paralelizar un simple renderer. Por un lado se tiene la ventana principal en donde se mostrará todo y detrás de ésta se debe de estar actualizando la imagen y mandarla a la pantalla.

![Ejemplo](img.gif?raw=true "Ejemplo")

## Requerimientos

```bash
Linux Kernel >= 3.10
gcc >= 8.3
Eclipse CDT
Procesador 64 bits
lpthread
C++ 2017
libsdl2-dev
```
## Compilación

- Se necesita [Eclipse CDT](https://www.eclipse.org/downloads/packages/release/2019-09/r/eclipse-ide-cc-developers) para compilar.

- Asegurarse de tener `libsdl2-dev` instalado y se asume que los includes estan en `/usr/include/SDL2`.

- `C++ 2017` es indispensable, se compila con `-std=c++17` desde Eclipse y esto implica tener un `gcc` relativamente nuevo. 

- Por default se compila con simbolos de depuración.

- Desde eclipse:

```
ctrl + B
```

## Ejecución

- Desde Eclipse:

```bash
ctrl + F11
```

## Licencia
[GPL v3](https://www.gnu.org/licenses/gpl-3.0.html)