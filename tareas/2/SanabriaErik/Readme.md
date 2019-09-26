# Tarea 1

Tarea 2 de planificación de procesos de Erik Sanabria Betancourt (415021636).

- El lenguaje utilizado es `C++`.

## First Come First Serve

**Planteamiento:**

- Todo es lineal, llegan cierto número aleatorio de procesos y se forman a una lista `std::queue<Proc> m_proc`, donde Proc es un objeto:

```C
class Proc
{
	//(..)
};
```


- Ahora los ejecutamos uno por uno mediante una función miembro de `Proc`:

```C
void Proc::exec()
{
	//Ejecutar y medir las metricas
}

//(...)

//obtenemos el proceso que esta en frente de la fila
Proc B = m_proc.front();

//lo ejecutamos
B.exec();

//como ya termino se va de la fila
m_proc.pop();

```

- En `void Proc::exec()` imprimimos los resultados de ese proceso. 

## Round Robin

**Planteamiento:**

- Todo es lineal, llegan cierto número aleatorio de procesos y se forman a una lista `std::queue<Proc> m_procs`

- A diferencia de First Come First Serve, cada proceso tiene un tiempo maximo de ejecucion:

```C
const size_t m_tiem_a{ 3 };
```

- Si no termino guardamos la diferencia del tiempo requerido `m_t` y el quantum `m_tiem_a` y lo guardamos en `m_falta` y se vuelve a formar el proceso hasta atrás:

```C
if(f > 0)
{
	//reordenalo al principio
	m_procs.push(A);
}
else if(f == 0)
{
	//si ya no le falta nada quitalo.
	m_procs.pop();
}
```

## Requerimientos

```bash
Linux Kernel >= 3.10
gcc >= 8.3
Eclipse CDT
Procesador 64 bits
```
## Compilación

- Se necesita [Eclipse CDT](https://www.eclipse.org/downloads/packages/release/2019-09/r/eclipse-ide-cc-developers) para compilar

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
