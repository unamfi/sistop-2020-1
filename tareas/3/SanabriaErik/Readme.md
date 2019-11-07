# Tarea 3

Tarea 3 de manejo de memoria de Erik Sanabria Betancourt (415021636).

- El lenguaje utilizado es `C++`.

## Manejo de memoria

**Planteamiento:**

- Primero creamos un arreglo dinamico de caracteres con base a valores leidos de la consola y lo inicializamos con `-`:

```C
	char *arr_mem{ new char[mem] };

	for(size_t k{ 0 }; k < mem; ++k)
	{
		arr_mem[k] = '-';
	}
```

- Con una funcion sencilla imprimimos la memoria:

```C
void printMem(char *data, size_t n = 30)
{
	std::cout << "\n\n\tContenidos de la memoria:\n\t" << std::flush;

	for(size_t i{ 0 }; i < n; ++i)
	{
		std::cout << data[i];
	}

	std::cout << std::endl;
}
```

- Para asignar la memoria definimos una funcion para ello.
- Busca los espacios vacios linealmente y si el proceso cabe lo ingresa ahi:

```C
size_t asigMem(char *data, char newData, size_t newDataSize, size_t n = 30)
{
	for(size_t k{ 0 }; k < n; ++k)
	{
		if((data[k] == '-') && ((n - k) >= newDataSize))
		{
			for(size_t h{ k }; h < (newDataSize + k); ++h)
			{
				data[h] = newData;
			}

			return 0;
		}
		else if(data[k] != '-')
		{
			continue;
		}
	}

	return 1;
}
```

- Para remover un proceso, buscamos su letra y lo borramos:

```C
size_t remLet(char *data, char let, size_t n = 30)
{
	bool blet{ false };			//se encuentra la letra?

	for(size_t i{ 0 }; i < n; ++i)
	{
		if(data[i] == let)
		{
			blet = true;

			data[i] = '-';
		}
	}

	if(!blet)
	{
		return 1;
	}

	return 0;
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
