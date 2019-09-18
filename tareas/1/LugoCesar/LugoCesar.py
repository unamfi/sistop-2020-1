1
#Tarea1 de sistemas operativos
#Solución del problema de sincronización
elfos_max = 3
reindeer = 9

#Declaramos los semaforos que vamos a usar dentro del programa

dummy_elf = 3 #Solo 3 elfos pueden ir despertar a santa si tienen un problema
rein_wait = 0 # Lugar donde esperan los renos

elf_mutex = 1 #Mutex para el contador de elfos
rein_mutex = 1 #mutex para el contador de renos

signal_santa = 0
santa = 0 #Santa esta dormido
problems = 0

done = 0 #Santa nos ha ayudado ñ.ñ

#Declaramos los contadores de renos y elfos
rein_count = 0 #contador de renos que han vuelto ñ.ñ
elf_count = 0 #Contador de elfos con problemas TTwTT

#proceso de los elfos
def elf():
    wait(dummy_elf)
    wait(elf_mutex)
    elf_count++

    if (elf_count == elfos_max):
        signal (elf_mutex)
        signal(santa) #Despierta a santa
    else:
        signal(elf_mutex)
        wait(signal_santa) #Los elfos esperan en la puerta


#Proceso Santa
def santaClaus():
    wait(santa)
    wait(rein_mutex)


    if (rein_count == reindeer):
        rein_count = 0
        signal(rein_mutex)
        for i in range(reindeer):
            i++
            signal(signal_santa)
        wait(elf_mutex)
        elf_count = 0
        signal(elf_mutex)
        for j in range(elfos_max):
            signal(problems)
            signal(done)
#Proceso renos
 def renitos():
     wait(rein_mutex)
     rein_count++
     if (rein_count == reindeer):
         signal(rein_mutex)
         signal(Santa)
     else:
         signal(rein_mutex)
         wait(rein_wait)
