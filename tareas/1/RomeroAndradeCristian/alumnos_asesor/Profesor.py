# !/usr/bin/python
# -*- coding: UTF-8 -*-

from time import sleep

class Profesor:
    """Clase que define un profesor"""

    __resp_3 = '\tSi, es el sentido de la vida, el universo y todo lo demás'
    __resp_4 = '\tEs reconfortante saber que\n\t'
    __resp_4 += 'tienes una toalla, porque si tienes una\n\t'
    __resp_4 += 'toalla, es fácil que otros asuman que también\n\t'
    __resp_4 += 'tienes cepillo de dientes, jabón, galletas, una\n\t'
    __resp_4 += 'brújula, un traje espacial, etcétera, por lo que\n\t'
    __resp_4 += 'estarán dispuestos a ayudarte en tu viaje.'
    __respuestas = {'¿El hombre es realmente libre?': '\tSi',
                    '¿Nuestro universo es real?': '\tFilosofia es alado',
                    '¿Dios existe?': "\tEl mio si, el tuyo no",
                    '¿El número 42 es perfecto?': __resp_3,
                    'Para ir al espacio necesito una toalla': __resp_4,
                    '¿Qué es todo?': '\tSalsa, Cilantro y cebolla'}



    def __init__(self, nombre: str):
        """Contructor

        :param nombre: El nombre del profesor
        :type nombre: str
        """

        self.nombre = nombre
        
    @classmethod
    def dormir(cls, puede: bool):
        """El profesor vé si puede dormir,
        si es asi duerme
        """

        if puede:
            print('Zzzzzzzzzzzzzzzzzzzz...')
            sleep(1)
            print('desperté')

    def responder(self, pregunta):
        """Responde la pregunta dada"""

        return self.__respuestas[pregunta]

    

    def __str__(self):
        return self.nombre
