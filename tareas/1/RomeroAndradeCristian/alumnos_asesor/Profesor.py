# !/usr/bin/python
# -*- coding: UTF-8 -*-

from time import sleep

class Profesor:
    """Clase que define un profesor"""

    __resp_3 = 'Si, es el sentido de la vida, el universo y todo lo demás'
    __resp_4 = 'Es reconfortante saber que'
    __resp_4 += 'tienes una toalla, porque si tienes una '
    __resp_4 += 'toalla, es fácil que otros asuman que también'
    __resp_4 += 'tienes cepillo de dientes, jabón, galletas, una'
    __resp_4 += 'brújula, un traje espacial, etcétera, por lo que'
    __resp_4 += 'estarán dispuestos a ayudarte en tu viaje.'
    __respuestas = {'¿El hombre es realmente libre?': 'Si',
                    '¿Nuestro universo es real?': 'Filosofia es alado',
                    '¿Dios existe?': "El mio si, el tuyo no",
                    '¿El número 42 es perfecto?': __resp_3,
                    'Para necesito una toalla en la': __resp_4,
                    '¿Qué es todo?': 'Salsa, Cilantro y cebolla'}



    def __init__(self, nombre: str):
        """Contructor

        :param nombre: El nombre del profesor
        :type nombre: str
        """

        self.nombre = nombre

    def dormir(self, puede: bool):
        """El profesor vé si puede dormir,
        si es asi duerme
        """

        if puede:
            print('Zzzzzzzzzzzzzzzzzzzz...')
            sleep(5)

    def responder(self, pregunta):
        """Responde la pregunta dada"""

        return pregunta[pregunta]

    

    def __str__(self):
        return self.nombre
