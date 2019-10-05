Tarea 2 - Comparación de planificadores
---

* Romero Andrade Cristian
* López López Ulysses 

---

Se comparan los siguientes algoritmos:

* FCFS
* Round robin(RRB)
* Round robin 4 (RRB4)
* SPN

---

Se ejecuta de la siguiente manera:

```zsh
python3 main.py
```

Salida
---

```zsh
        |T|: 2, t = 4.09
        |I|: 4, t = 4.79
        |S|: 7, t = 5.24
        |D|: 8, t = 4.19
        |Y|: 15, t = 5.49
                (total: 23.79)

----------------------------------------------------------------------------------------------------

FCFS: T = 10.60 , E = 5.84 , P = 2.23
| || ||T||T||T||T||T||I||I||I||I||I||S||S||S||S||S||S||D||D||D||D||D||Y||Y||Y||Y||Y||Y|

SPN: T = 10.40 , E = 5.00 , P = 1.88
| || ||T||T||T||T||T||I||I||I||I||I||D||D||D||D||D||S||S||S||S||S||S||Y||Y||Y||Y||Y||Y|| |

Round Robin: T = 17.20 , E = 11.80 , P = 3.21
|T||T||I||T||I||S||D||T||I||S||D||T||I||S||D||Y||I||S||D||Y||S||D||Y||S||Y||Y||Y|| |

Round Robin: T = 2.80 , E = 0.80 , P = 1.40
|T||T||I||I|| ||S||D||S||D|| || || || ||Y||Y|| |
```

En esta ejecución vemos que el round Robin con los quantums cuadruplicados
es el mejor caso promedio, pero entando en el esquema de los quantums
unitarios, el SPN es el mejor que ejecuta los procesos ya que se va con el
proceso más corto para finalizar más rápido los procesos.
