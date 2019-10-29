# Proyecto 3

Proyecto 3 de sistemas de archivos de Erik Sanabria Betancourt (415021636).

- El lenguaje utilizado es `C++`.

## Sistema de Archivos

**Planteamiento:**

- El sistema de archivos se lee con `std::ifstream`:

```C
std::ifstream archiv;

archiv.open(fname, std::ios::binary | std::ios::in);
```

- Primero verificamos que el número mágico sea el correcto:

```C
const std::string mag_def{ "FiUnamFS" };
```


- Si el número mágico no es el correcto terminamos la ejecución:

```C
if(mag_def != mag)
{
	std::cout << std::endl << "\tEl archivo no es valido...\t" << mag << std::endl;

	archiv.close();

	return 1;
}
```

- Ahora medimos el tamaño completo del sistema de archivos:

```C
archiv.seekg(0, std::ios::end);

tam = archiv.tellg();
```

- Leemos el encabezado de `64 bytes` desde la funcion `readHead(..)`:

```C
void readHead(std::ifstream *m_archiv, char *head, const unsigned short n_dir = 64, const unsigned short n_pos = 1024)
{
	if(m_archiv->is_open())
	{
		m_archiv->seekg(n_pos, std::ios::beg);
		m_archiv->read(head, n_dir);
		m_archiv->seekg(0, std::ios::beg);
	}
}
```
## Inconsistencias en el sistema de archivos

- Yo encontre que el valor de cluster del primer archivo, `5`, en el sistema de archivos no representa nada coherente.
- El archivo empieza en `5120 (0x1400)` y el valor que tiene de cluster `5*4*512=10240 (0x2800)`, el cluster número `5` por `4` sectores por cluster por `512` bytes por sector.
- Por lo tanto no calcule los valores a partir del encabezado.

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

- Ó si se prefiere desde la terminal, hay que pasarle el path completo como argumento:

```bash
$ ./proyecto_3 /home/<user>/Documents/UNAM/sistop-2020-1/proyectos/3/fiunamfs.img
```

## Licencia
[GPL v3](https://www.gnu.org/licenses/gpl-3.0.html)
