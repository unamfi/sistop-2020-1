import threading
from random import randrange

l = 3
k = 5
m = 4
ratonenCocina = 0
platos = [threading.Semaphore(1) for i in range(m)]
cocina = threading.Semaphore(1)
mutRatones = threading.Semaphore(1)
mutGatos = threading.Semaphore(1)
ratonenCocina = 0
gatoenCocina = 0
inanicionRaton = 0
inanicionGato = 0


def gato(id):
    global gatoenCocina
    global inanicionGato
    while True:
        durmiendo(id)
        if inanicionGato >= 10:
            mutGatos.acquire()
            cocina.release()
            inanicionGato = 0
            mutGatos.release()
        else:
            mutGatos.acquire()
            inanicionGato = inanicionGato + 1
            gatoenCocina = gatoenCocina + 1
            if gatoenCocina == 1:
                cocina.acquire()
            mutGatos.release()
            comer("gato", id)
            mutGatos.acquire()
            gatoenCocina = gatoenCocina - 1
            if gatoenCocina == 0:
                cocina.release()
            mutGatos.release()

def durmiendo(id):
    print(id,": zzz")

def comer(tipo, id):
    temp = randrange(m)
    platos[temp].acquire()
    print("Soy ",tipo," numero ",id," como de plato ",temp)
    platos[temp].release()

def raton(id):
    global ratonenCocina
    global inanicionRaton
    while True:
        if inanicionRaton >= 10 :
            mutRatones.acquire()
            cocina.release()
            print("cocina liberada")
            print(ratonenCocina)
            inanicionRaton = 0
            mutRatones.release()
        else:
            mutRatones.acquire()
            inanicionRaton = inanicionRaton + 1
            ratonenCocina = ratonenCocina + 1
            if ratonenCocina == 1:
                cocina.acquire()
            mutRatones.release()
            comer("raton", id)
            mutRatones.acquire()
            ratonenCocina = ratonenCocina - 1
            if ratonenCocina == 0:
                cocina.release()
                print("cocina vacia")
                print(ratonenCocina)
            mutRatones.release()

gatos = []
ratones = []
for i in range(k):
    g = threading.Thread(target=gato, args=[i])
    gatos.append(g)
    g.start()

for i in range(l):
    r = threading.Thread(target=raton, args=[i])
    ratones.append(r)
    r.start()