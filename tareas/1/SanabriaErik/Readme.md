# Tarea 1

Tarea 1 de sincronización de Erik Sanabria Betancourt (415021636).

## Problema del Gato y los Ratones

**Planteamiento:**

- Los gatos pueden comer juntos solo si hay platos disponibles, si llega un raton algun gato se lo come.

- Los ratones comen si no hay gatos, y si un raton esta comiendo y llega un gato, el gato no puede comer. 

**Mi propuesta:**

**Ya no logre terminar por mi falta de fluidez con `pthreads`**

- Generar una cantidad aleatoria de `gatos`, `raton` y `platos`.

- Los gatos y ratones son estructuras que van a ser guardadas en un arreglo dinámico `a_gatos` y `a_ratones` repsectivamente:

```C
typedef struct
{
	Argv args;
	pthread_t id;
	bool comiendo;
}Animal;
```

- Los platos también se guardan en un arreglo de estructuras `a_platos` pero no los considero como hilos:

```C
typedef struct
{
	size_t n;
	size_t total;
	bool en_uso;
}Plato;
 ```
 
- Las funciones de comer de cada animal las considero como los hilos y una funcion esta asociada a un animal a la véz:

```C
void *gato_come(void *argv)
{
	//(...)
}

void *raton_come(void *argv)
{
	//(...)
}
 ```

- El parametro de ambas funciones `void *argv` es una estructura de argumentos que contiene el identificador del hilo `pthread_t m_id` y el número de animal `size_t m_num`:

```C
typedef struct
{
	pthread_t m_id;
	size_t m_num;
}Argv; 
```

- Usar un semáforo tipo mutex inicializado en la cantidad de platos disponibles, los gatos tienen prioridad y cada vez que uno empieza a comer se lo queda hasta que termine o sea interrumpido por un raton.
- Darle la capacidad al hilo de `gato_come` para que termine la ejecución de un `raton_come` que representaria el gato comiendose al raton.

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

- **Bonus:** Compilar a ensamblador:

```bash
make ass
```

## Ejecución

```bash
./exec
```

## Licencia
[GPL v3](https://www.gnu.org/licenses/gpl-3.0.html)

Ejemplos de pthreads que me han ayudado:

- [Ej1](https://www.geeksforgeeks.org/multithreading-c-2/)

- [Ej2](https://timmurphy.org/2010/05/04/pthreads-in-c-a-minimal-working-example/)

- [Ej3](https://www.cs.cmu.edu/afs/cs/academic/class/15492-f07/www/pthreads.html)
