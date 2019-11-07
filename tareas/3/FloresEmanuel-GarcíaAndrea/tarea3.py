import argparse

def get_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--first-adjust', action='store_true', help='Resolver solcitudes por primer ajuste.')
    parser.add_argument('--best', action='store_true', help='Resolver solcitudes por mejor ajuste.')
    parser.add_argument('--worst', action='store_true', help='Resolver solcitudes por peor ajuste.')
    parser.add_argument('-m', '--memory', dest='memory', type=int, help='Define el tamaño de la memoria.')

    options = parser.parse_args()

    if options.first_adjust:
        return 'first', options.memory
    elif options.best:
        return 'best', options.memory
    elif options.worst:
        return 'worst', options.memory
    else:
        print('[-] Ingresa un modo para resolver las solicitudes.')
        exit(-1)

memoria = []
procesos = []
espacio_disp = 0
modo, num_bloques = get_arguments()
if num_bloques is None:
    num_bloques = 30
liberados = 0

def iniciar():
    global memoria, espacio_disp, num_bloques
    #Definir el número de bloques
    espacio_disp = num_bloques
    #Inicialmente no tenemos ningún bloque asignado, así que inicializa la memoria con "-" 
    for i in range(num_bloques):
        memoria.append("-")    
    
def mostrar():
    cadena = ""
    for bloque in memoria:
        cadena += bloque
    print(cadena)


def liberar(proceso):
    global memoria,espacio_disp,procesos, liberados, num_bloques 
    #Ya que los bloques asignados son contiguos, encontramos la primera coincidencia
    inicio = memoria.index(proceso)
    #Y a partir de ahí liberamos todo el proceso
    while memoria[inicio] == proceso and inicio <= num_bloques-1:
        memoria[inicio] = "-"
        espacio_disp += 1 
        if inicio == num_bloques - 1:
            break
        inicio += 1
    procesos.remove(proceso)
    liberados += 1    
    

def asignar(tam):
    global memoria, espacio_disp, procesos, liberados    
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #Es posible asignar espacio si aún hay disponible    
    if espacio_disp >= tam:
        #Se debe verificar si se necesita compactación y realizarla 
        block_emp = encuentra_bloques()
        if requiere_comp(tam, block_emp):
            print("Se requiere una compactación D:")
            mostrar()
            compactar()
            print("Nueva situación...")
            mostrar()
            #Ya que se realizo la compactación, se deben actualizar los bloques disponibles
            block_emp = encuentra_bloques()
        #----------------------------------------------------------
        num_proc = len(procesos) + liberados
        #Asigna el nombre del proceso
        nom_proc = letras[num_proc]
        #Se agrega a la lista de procesos actuales
        procesos.append(nom_proc)
        #Elección de estrategia
        if modo == 'first':
            primer_ajuste(nom_proc, tam)
        elif modo == 'worst':
            peor_ajuste(block_emp, tam, nom_proc) 
        elif modo == 'best':
            mejor_ajuste(block_emp, tam, nom_proc)      
    else:
        print("[-]Ya no hay espacio disponible :(")
    
def requiere_comp(tam, bloques):
    #Los tamaños de los bloques se le pasan como un diccionario
    llaves = bloques.keys()
    bloque_max = max(llaves)
     
    if bloque_max < tam and bloque_max != tam:
        return True
    else:
        return False
   
def encuentra_bloques():
    global memoria, num_bloques
    #Diccionario que almacenará los bloques de diversos tamaños, así como su inicio y fin
    bloques_tot = {}
    #---------------------------------------
    cont = 0
    block = False
    datos = []
    #---------------------------------------
    for bloque in memoria:
        if block == False:
            #Si es la primera vez que se encuentra con "-" (que indica vacío)
            if bloque == "-":
                #Se inicia un bloque...
                datos.append(cont)
                block = True
        else:
            #Se termina un bloque...
            if bloque != "-" or cont == num_bloques-1:
                block = False
                if cont == num_bloques - 1:
                    tam = cont - datos[0] + 1
                else: 
                    tam = cont - datos[0]
                datos.append(cont)                
                bloques_tot[tam] = datos
                datos = []
        cont += 1
    #Último bloque, que no alcanza a entrar en el for
    if len(datos) > 0: 
        tam = cont - datos[0]
        datos.append(cont)
        bloques_tot[tam] = datos
        
    #Al retornar un diccionario si hay más de un bloque que mida lo mismo, sólo se incluye la 
    #última coincidencia   
    return bloques_tot 

def seleccionar(opcion):
    global procesos
    salir = True
    if opcion == 0:
        try:
            tam_proc = int(input("Ingrese el tamaño del nuevo proceso: "))
            asignar(tam_proc)
            return True
        except:
            print('[-] Tipo de dato no válido, intente con un número entero.')
            return True
    elif opcion == 1:
        cadena = ""
        salir = True
        for proceso in procesos:
            cadena+= proceso
        #Si no hay procesos no se puede liberar
        if cadena == "":
            print("No hay ningún proceso :(")
            return True
        while salir:
            proceso = str(input("Ingresa el nombre del proceso a liberar (" + cadena +  ") : "))
            if proceso in procesos:
                liberar(proceso)
                salir = False
            else:
                print("[-] El proceso seleccionado no es válido")
                salir = True
        return True
    elif opcion == 2:
        return False
    else:
        print("[-] Lo siento, opción no válida :( intenta de nuevo")
        return True

def compactar():
    global memoria, procesos
    inicio = []
    movimiento = []
    #Encontrar el inicio de cada proceso
    for proceso in procesos:
        index = memoria.index(proceso)
        inicio.append(index)
    inicio.sort()
    #Para cada proceso
    for indice in inicio:
        valor = indice - 1
        #Mientras haya espacios en blanco en el bloque anterior...      
        while memoria[valor] == "-" and valor > 0:
            #Mover todo el proceso una posición menos            
            mover_proc(valor, indice)
            #Se disminuyen valores
            valor -= 1
            indice -= 1
            
def mover_proc(nuevo_in,in_proc):
    global memoria, num_bloques
    proceso = memoria[in_proc]
    while memoria[in_proc] == proceso and in_proc < num_bloques:
        memoria[nuevo_in] = memoria[in_proc]
        memoria[in_proc] = "-"
        in_proc += 1
        nuevo_in += 1
        if in_proc == num_bloques:
            break
        
def primer_ajuste(nom_proc, tam):
    global memoria, espacio_disp
    bloques = 0
    fin = 0
    bloque_disp = True
    for bloque in memoria:
        #Cuando se encuentra el tamaño suficiente, procedemos a asignar la memoria
        if bloques != tam:
                if bloque == "-":
                    bloques += 1
                else:
                    bloques = 0
        else:
            break
        fin += 1       
    inicio = fin - tam
    while inicio < fin:
        memoria[inicio] = nom_proc
        inicio += 1
        espacio_disp -= 1

def mejor_ajuste(bloques,tam, nom_proc):
    global memoria, espacio_disp
    llaves = list(bloques.keys())
    llaves.sort()
    cont = 0
    while len(llaves) > 0:
        minimo = min(llaves)
        #Sí el bloque más pequeño es del tamaño suficiente... se puede asignar
        if minimo >= tam:
            index = minimo
            llaves = []
        else:
            llaves.pop(cont)
        cont += 1
    #Se saca la información del diccionario
    inicio_fin = bloques.get(index)
    inicio = inicio_fin[0]
    fin = inicio_fin[1]
    cont = 0
    while cont < tam:
        memoria[inicio] = nom_proc
        espacio_disp -= 1
        inicio += 1
        cont += 1
            
def peor_ajuste(bloques,tam, nom_proc):
    global memoria, espacio_disp
    #Se selecciona el bloque más grande
    max_block = max(bloques)
    #Se saca la información del diccionario
    inicio_fin = bloques.get(max_block)
    inicio = inicio_fin[0]
    fin = inicio_fin[1]
    cont = 0
    while cont < tam:
        memoria[inicio] = nom_proc
        espacio_disp -= 1
        inicio += 1
        cont += 1
             
def main():
    global num_bloques, espacio_disp
    salir = True
    iniciar()
    while salir:
        mostrar()
        opcion = int(input("Asignar (0) \nLiberar(1) \nSalir(2)\n"))
        salir = seleccionar(opcion)


if __name__ == '__main__':
    main()


