
# coding: utf-8

# In[ ]:


import threading
import time
import logging
import random

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-7s) %(message)s',)
#formato de impresion con nombre de hilo incluido
                    
class Contador(object):
    def __init__(self, start = 0):
        self.lock = threading.Lock()
        self.value = start
        self.act = []
    def actualizar(self):
        #logging.debug('Esperando para generar actualización')
        self.lock.acquire()
        try:
            self.value = self.value + 1
            self.act.append(1)
            
            if (self.value == len(self.act)): #cuando la cuenta es igual al tamaño de la lista entonces se puede actualizar
                logging.debug('')
                logging.debug('Adquirió un turno para generar actualización ')
    
            #logging.debug('Contador: %d', cuenta.value)
            logging.debug('Procesando actualización de usuario')
            
        finally:
            logging.debug('Generando actualización, se han realizado %d actualizaciones', self.value )
            logging.debug('Liberando turno')
            self.lock.release()
        

def usuario(c):
    
    for j in range(3):     #numero de veces que un usuario (hilo) actualiza los datos (cuenta.value)
        r = random.random()
        logging.debug('Actualizando Datos Espera %3.2f[s] para poder actualizar', r)
        time.sleep(r)
        c.actualizar()
       
    logging.debug('')
    logging.debug('Haz realizado las actualizaciones permitidas')
    logging.debug('')
    
if __name__ == '__main__':
    cuenta = Contador()
    logging.debug('Esperando usuarios para actualizar trafico')
    logging.debug('')
    
    for i in range(5):    #numero de usuarios (hilos)
        t = threading.Thread(target=usuario, args=(cuenta,))
        t.start()

    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()
    
        
    

