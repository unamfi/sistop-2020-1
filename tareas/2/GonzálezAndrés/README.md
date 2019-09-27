# Tarea 2. Comparación de planificadores

## Requisitos

- Python 3.7
- Módulo numpy. Intstrucciones de instalación [aquí](https://docs.scipy.org/doc/numpy/user/install.html)

## Instrucciones de ejecución

Para ejecutar el programa podemos usar el comando:

    $ python tarea2.py -p <num_de_procesos> -l <t_de_llegada_máx.> -t <t_requerido_máx.> -s <semilla>

- El número mínimo de procesos es 1 y el máximo es 26. 
- El tiempo máximo de llegada debe ser un número positivo.
- El tiempo requerido máximo debe ser un número mayor a 0
- La semilla debe ser un número entero

Por defecto, el programa inicia con 5 procesos y sin semilla. La semilla es un número entero que puede ser de utilidad para replicar alguna ejecución en específico.

## Ejemplo de ejecución

    $ python tarea2.py

    A: t_llegada=2, t_requerido=5.
    B: t_llegada=2, t_requerido=4.
    C: t_llegada=2, t_requerido=7.
    D: t_llegada=4, t_requerido=8.
    E: t_llegada=6, t_requerido=9.

    FCFS: T=16.20, E=9.60, P=2.30
    AAAAABBBBCCCCCCCDDDDDDDDEEEEEEEEE

    RR1: T=23.60, E=17.00, P=3.61
    ABCABDCAEBDCAEBDCAEDCEDCEDCEDEDEE

    RR2: T=22.80, E=16.20, P=3.42
    AABBCCAADDBBEECCADDEECCDDEECDDEEE

    RR4: T=20.80, E=14.20, P=3.06
    AAAABBBBCCCCDDDDAEEEECCCDDDDEEEEE

    SPN: T=16.00, E=9.40, P=2.21
    BBBBAAAAACCCCCCCDDDDDDDDEEEEEEEEE

    FB: T=24.80, E=18.20, P=3.86, (n_colas_prioridad = 4, ejec_para_degradado = 1, quantum = 1)
    ABCDAEBCDEABCDEABCDEACDECDECDEDEE

    FB: T=23.60, E=17.00, P=3.58, (n_colas_prioridad = 4, ejec_para_degradado = 2, quantum = 2)
    AABBCCAADDBBEECCDDEEACCDDEECDDEEE

    FB: T=24.40, E=17.80, P=3.76, (n_colas_prioridad = 4, ejec_para_degradado = 4, quantum = 1)
    ABCABDCAEBDCAEBDCEDEACDECDECDEDEE

    FB: T=21.60, E=15.00, P=3.22, (n_colas_prioridad = 4, ejec_para_degradado = 1, quantum = 4)
    AAAABBBBCCCCDDDDEEEEACCCDDDDEEEEE

## P.D.

Dejé hardcodeada una función que genera una carga de procesos con una distribución diferente. Los tiempos de ejecución de procesos solo toman dos valores, esto me sirvió para ver el comportamiento de los algoritmos cuando había muchos procesos largos con pocos cortos y viceversa.

Para usarla, hay que usar la función `crear_procesos_ch_g` en lugar de `crear_procesos_aleatorios`. Se encuentra por ahí de la línea 143 del archivo [tarea2.py](./tarea2.py).

````python
# lista_procesos = crear_procesos_aleatorios(num_procesos, llegada_max, requerido_max, seed)
lista_procesos = crear_procesos_ch_g(num_procesos, 
                                    llegada_max, 
                                    requerido_ch=1, 
                                    requerido_g=requerido_max, 
                                    prob_ch=0.2,
                                    seed = seed)
````
Con ello, vemos este comportamiento con más procesos grandes que chicos:

    $ python tarea2.py -p 10
    A: t_llegada=0, t_requerido=10.
    B: t_llegada=0, t_requerido=10.
    C: t_llegada=0, t_requerido=1.
    D: t_llegada=3, t_requerido=1.
    E: t_llegada=4, t_requerido=10.
    F: t_llegada=5, t_requerido=10.
    G: t_llegada=6, t_requerido=10.
    H: t_llegada=6, t_requerido=10.
    I: t_llegada=7, t_requerido=10.
    J: t_llegada=9, t_requerido=1.

    FCFS: T=36.60, E=29.30, P=13.02
    AAAAAAAAAABBBBBBBBBBCDEEEEEEEEEEFFFFFFFFFFGGGGGGGGGGHHHHHHHHHHIIIIIIIIIIJ

    RR1: T=45.60, E=38.30, P=5.82
    ABCABDAEBFGHAIEBJFGHAIEBFGHAIEBFGHAIEBFGHAIEBFGHAIEBFGHAIEBFGHIEFGHIEFGHI

    RR2: T=44.30, E=37.00, P=6.59
    AABBCAADBBEEFFGGHHAAIIJBBEEFFGGHHAAIIBBEEFFGGHHAAIIBBEEFFGGHHIIEEFFGGHHII

    RR4: T=46.70, E=39.40, P=8.81
    AAAABBBBCDAAAAEEEEFFFFGGGGHHHHIIIIBBBBJAAEEEEFFFFGGGGHHHHIIIIBBEEFFGGHHII

    SPN: T=28.50, E=21.20, P=4.11
    CAAAAAAAAAADJBBBBBBBBBBEEEEEEEEEEFFFFFFFFFFGGGGGGGGGGHHHHHHHHHHIIIIIIIIII

    FB: T=46.90, E=39.60, P=5.32, (n_colas_prioridad = 4, ejec_para_degradado = 1, quantum = 1)
    ABCADEFGHIJBEFGHIABEFGHIABEFGHIABEFGHIABEFGHIABEFGHIABEFGHIABEFGHIABEFGHI

    FB: T=46.30, E=39.00, P=6.61, (n_colas_prioridad = 4, ejec_para_degradado = 2, quantum = 2)
    AABBCAADBBEEFFGGHHIIJEEFFGGHHIIAABBEEFFGGHHIIAABBEEFFGGHHIIAABBEEFFGGHHII

    FB: T=47.60, E=40.30, P=6.02, (n_colas_prioridad = 4, ejec_para_degradado = 4, quantum = 1)
    ABCABDAEBFGHAIEBJFGHIEFGHIEFGHIABEFGHIABEFGHIABEFGHIABEFGHIABEFGHIABEFGHI

    FB: T=47.90, E=40.60, P=8.21, (n_colas_prioridad = 4, ejec_para_degradado = 1, quantum = 4)
    AAAABBBBCDEEEEFFFFGGGGHHHHIIIIJAAAABBBBEEEEFFFFGGGGHHHHIIIIAABBEEFFGGHHII

Y este otro cuando los procesos cortos superan en cantidad a los largos:

    python tarea2.py -p 20
    A: t_llegada=0, t_requerido=1.
    B: t_llegada=1, t_requerido=10.
    C: t_llegada=1, t_requerido=10.
    D: t_llegada=1, t_requerido=10.
    E: t_llegada=1, t_requerido=1.
    F: t_llegada=2, t_requerido=10.
    G: t_llegada=3, t_requerido=10.
    H: t_llegada=3, t_requerido=1.
    I: t_llegada=3, t_requerido=1.
    J: t_llegada=5, t_requerido=1.
    K: t_llegada=5, t_requerido=1.
    L: t_llegada=6, t_requerido=1.
    M: t_llegada=6, t_requerido=1.
    N: t_llegada=6, t_requerido=1.
    O: t_llegada=6, t_requerido=1.
    P: t_llegada=8, t_requerido=10.
    Q: t_llegada=9, t_requerido=1.
    R: t_llegada=9, t_requerido=1.
    S: t_llegada=9, t_requerido=1.
    T: t_llegada=9, t_requerido=1.

    FCFS: T=45.45, E=41.75, P=35.95
    ABBBBBBBBBBCCCCCCCCCCDDDDDDDDDDEFFFFFFFFFFGGGGGGGGGGHIJKLMNOPPPPPPPPPPQRST

    RR1: T=27.65, E=23.95, P=9.47
    ABCDEBFCGHIDJKBLMNOFCPGQRSTDBFCPGDBFCPGDBFCPGDBFCPGDBFCPGDBFCPGDBFCPGDFPGP

    RR2: T=30.20, E=26.50, P=12.65
    ABBCCDDEFFBBGGHICCJKLMNODDPPQRSTFFBBGGCCDDPPFFBBGGCCDDPPFFBBGGCCDDPPFFGGPP

    RR4: T=37.30, E=33.60, P=19.57
    ABBBBCCCCDDDDEFFFFGGGGHIBBBBJKLMNOPPPPCCCCQRSTDDDDFFFFGGGGBBPPPPCCDDFFGGPP

    SPN: T=20.70, E=17.00, P=8.73
    AEBBBBBBBBBBHIJKLMNOQRSTCCCCCCCCCCDDDDDDDDDDFFFFFFFFFFGGGGGGGGGGPPPPPPPPPP

    FB: T=25.40, E=21.70, P=6.81, (n_colas_prioridad = 4, ejec_para_degradado = 1, quantum = 1)
    ABCDEFGHIJKLMNOPQRSTBCDFGPBCDFGPBCDFGPBCDFGPBCDFGPBCDFGPBCDFGPBCDFGPBCDFGP

    FB: T=30.60, E=26.90, P=12.69, (n_colas_prioridad = 4, ejec_para_degradado = 2, quantum = 2)
    ABBCCDDEFFBBGGHICCJKLMNODDPPQRSTFFGGPPBBCCDDFFGGPPBBCCDDFFGGPPBBCCDDFFGGPP

    FB: T=28.10, E=24.40, P=9.51, (n_colas_prioridad = 4, ejec_para_degradado = 4, quantum = 1)
    ABCDEBFCGHIDJKBLMNOFCPGQRSTDBFCPGDFPGPBCDFGPBCDFGPBCDFGPBCDFGPBCDFGPBCDFGP

    FB: T=34.70, E=31.00, P=16.79, (n_colas_prioridad = 4, ejec_para_degradado = 1, quantum = 4)
    ABBBBCCCCDDDDEFFFFGGGGHIJKLMNOPPPPQRSTBBBBCCCCDDDDFFFFGGGGPPPPBBCCDDFFGGPP