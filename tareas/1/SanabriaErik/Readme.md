# Tarea 1

Tarea 1 de sincronización de Erik Sanabria Betancourt (415021636).

## Problema del Gato y los Ratones

Planteamiento:
- Los gatos pueden comer juntos solo si hay platos disponibles, si llega un raton algun gato se lo come.

- Los ratones comen si no hay gatos, y si un raton esta comiendo y llega un gato, el gato no puede comer. 

## Requerimientos

```bash
Linux Kernel >= 3.10
gcc >= 5.4
pthreads
Procesador 64 bits
```
## Compilación

- Con símbolos para depuración:

```bash
make
```
- Sin símbolos para depuración:

```bash
make release
```

## Ejecución

```bash
./exec
```

## Licencia
[GPL v3](https://www.gnu.org/licenses/gpl-3.0.html)

Ejemplos de pthreads:

- [Ej1](https://www.geeksforgeeks.org/multithreading-c-2/)

- [Ej2](https://timmurphy.org/2010/05/04/pthreads-in-c-a-minimal-working-example/)

- [Ej3](//https://www.cs.cmu.edu/afs/cs/academic/class/15492-f07/www/pthreads.html)