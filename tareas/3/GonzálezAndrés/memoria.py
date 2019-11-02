import argparse
from string import ascii_uppercase

LETRAS = list(ascii_uppercase)

class Memoria(list):

    CHAR_ULIBRE = '-' # Identificador de unidad libre

    def __init__(self, *args, **kwargs):
        super(Memoria, self).__init__(args[0])
        self.__u_libres = 0
        for unidad in self:
            if(unidad == self.CHAR_ULIBRE):
                self.__u_libres +=1

    def liberar(self, proceso):
        pass

    def compactar(self):
        pass

    def asignar(self, proceso, unidades_req=2, tipo_ajuste=0):
        """Asigna una cantidad de unidades de memoria a un proceso
        Parámetros:
            proceso - nombre del proceso
            unidades_req - el número de unidades que pide el proceso
            tipo_ajuste - 0: Primer ajuste. 1: Mejor ajuste, 2: Peor ajuste
        """
        if unidades_req > self.__u_libres:
            print('No se pueden asignar %i unidades, memoria sin espacio disponible' % unidades_req)
            return
        espacio_libre = 0 # Para contar cuánto espacio hay entre procesos
        unidad_inicio = 0
        for i, unidad in enumerate(self):
            if(unidad == self.CHAR_ULIBRE):
                espacio_libre +=1
                if espacio_libre == unidades_req:
                    unidad_inicio = i - espacio_libre + 1
                    self[unidad_inicio:espacio_libre] = [proceso for _ in range(unidades_req)]
                    self.__u_libres -= unidades_req
                    return True
        print('No es posible asignar, necesita compactar')
            

def main(args):
    tam_mem = args.unidades
    u_libres = tam_mem
    memoria = Memoria(['-' for i in range(tam_mem)])
    for u in memoria:
        print(u, end='')
    print('')
    memoria.asignar('A')
    for u in memoria:
        print(u, end='')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("unidades", help="Unidades de memoria que tiene el sistema", 
                                    type=int, 
                                    nargs='*',
                                    default=30)
    args = parser.parse_args()
    main(args)