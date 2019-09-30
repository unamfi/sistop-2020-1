from Tkinter import *
import tkMessageBox
from PIL import ImageTk,Image  
from functools import partial  
from threading import Semaphore, Thread
from time import sleep
from random import randint
import datetime
import pickle
#from  createAcount import signIn


window = Tk()
pista = Semaphore(3)
pista_Cola = []
salida_entrada = Semaphore(1)

def validar(user , password):
    global window
    dic = cargarDatos()
    print(dic)
    print(dic['password'])
    print(dic['email'])
    print(user.get())
    print(password.get())
    if password.get() == dic['password'] and user.get() == dic['email'] :
        tkMessageBox.showinfo("Password Correct","Password Correct" )
        monitor(window)
    else:
        tkMessageBox.showinfo("Password incorrect", "Password incorrect")

def inicia(window):
    password = StringVar()
    user = StringVar()
    w = 800
    h = 300
    x = 50
    y = 100
    # use width x height + x_offset + y_offset (no spaces!)
    window.geometry("%dx%d+%d+%d" % (w, h, x, y)) 

    frame = Frame(window)
    frame.pack(fill='both', expand='yes')

    
    img = ImageTk.PhotoImage(Image.open("logo.png"))
    photo = Label(frame , image = img )
    photo.image = img
    photo.grid(row = 0, column = 0)
    
    #hilo = threading.Thread(target=muestraHora, args=[window])
    #hilo.start()

    muestraHora(frame)

    Label (frame , text = "Usuario : " ,  fg = "black", font="none 12 ") .grid(row= 1, column = 0 , sticky = W)
    Label (frame , text = "Contrasena : " , fg = "black", font="none 12 ") .grid(row= 1, column = 1 , sticky = W)

    textentry = Entry(frame, textvariable = user ,width = 20, bg = "white")
    textentry.grid(row = 2 , column =0 , sticky= W)

    textentry1 = Entry(frame, textvariable = password,width = 20, bg = "white")
    textentry1.grid(row = 2 , column =1, sticky= W)
    
    validate = partial( validar ,user ,  password)
    sign = partial(signIn, window)

    boton1 = Button(frame , text = "Sign in" , fg = "black" ,bg ="green", width = 6 , command = sign)
    boton1.place(x=10, y=200)

    boton2 = Button(frame , text = "Log in" ,fg = "black" , width = 6 , command = validate)
    boton2.place(x=100, y=200)
    

def muestraHora(window):
    #while True:
    x = datetime.datetime.now()
    hour = Label(window , text = "%s:%s:%s" % (x.hour, x.minute, x.second),borderwidth=2 ,relief = "groove", fg = "blue" , font = "none 19 bold")
    hour.place(x = 600 , y = 10)

#FUNCION QUE ABRE UNA NUVEA VENTANA PARA INGRESAR UN NUEVO USUARIO
def signIn(window): 
    window.withdraw()
    win = Toplevel()
    win.title("Crea cuenta")

    w = 300
    h = 300
    x = 50
    y = 100
    # use width x height + x_offset + y_offset (no spaces!)
    win.geometry("%dx%d+%d+%d" % (w, h, x, y)) 

    name = StringVar()
    lastname = StringVar()
    email = StringVar()
    password = StringVar()
    password1 = StringVar()

    inicio = partial(muestraInicio, win , name , lastname , email, password , password1)

    #Nombre
    Label (win , text = "Nombre" ,  fg = "black", font="none 12 ") .grid(row= 1, column = 0 , sticky = W)
    textentry = Entry(win, textvariable = name, width = 20, bg = "white")
    textentry.grid(row = 2 , column =0 , sticky= W)
    
    #Apellido
    Label (win, text = "Apellido : " , fg = "black", font="none 12 ") .grid(row= 3, column = 0 , sticky = W)
    textentry1 = Entry(win, textvariable = lastname,width = 20, bg = "white")
    textentry1.grid(row = 4 , column =0, sticky= W)

    #correo
    Label (win , text = "Correo : " , fg = "black", font="none 12 ") .grid(row= 5, column = 0 , sticky = W)
    textentry2 = Entry(win, textvariable = email,width = 20, bg = "white")
    textentry2.grid(row = 6 , column =0, sticky= W)

    #contrasena 
    Label (win , text = "Contrasena : " , fg = "black", font="none 12 ") .grid(row= 7, column = 0 , sticky = W)
    textentry3 = Entry(win, textvariable = password,width = 20, bg = "white")
    textentry3.grid(row = 8 , column =0, sticky= W)

    #contrasena 
    Label (win , text = "Contrasena  : " , fg = "black", font="none 12 ") .grid(row= 9, column = 0 , sticky = W)
    textentry4 = Entry(win, textvariable = password1,width = 20, bg = "white")
    textentry4.grid(row = 10 , column =0, sticky= W)

    boton1 = Button(win, bg = "black",text = "Sign in" , width = 6 , command = inicio)
    boton1.place(x=5, y=250)


def muestraInicio(win, name, lastname , email , password , password1):
    print(password.get())
    print(password1.get())
    if password.get() == password1.get() :
        usuario = { 'name' : name.get() , 'lastname': lastname.get() , 'email' : email.get() , 'password' : password.get()}
        guardarDatos(usuario)
        win.destroy()
        window.state(newstate = 'normal')
    else : 
        tkMessageBox.showinfo("Error","Las contrasenas no coinciden" )

def guardarDatos(dic):
    with open("usuarios.dat", "wb") as f:
        pickle.dump(dic, f)

def cargarDatos():
    try:
        with open("usuarios.dat", "rb") as f:
            return pickle.load(f)
    except (OSError, IOError) as e:
        return dict()

#FUNCION QUE REGRESA UNA VENTANA DE MONITOREO DE VUELOS
def monitor(window): 
    window.withdraw()
    win = Toplevel()
    win.title("Monitor de Vuelos")
    
    w = 1200
    h = 400
    x = 50
    y = 100
    # use width x height + x_offset + y_offset (no spaces!)
    win.geometry("%dx%d+%d+%d" % (w, h, x, y)) 
   

    frame = Frame(win)
    frame.pack(fill='both', expand='yes')

   
    Label (frame , text = "Modelo" ,  fg = "black", width = 20, font="none 12 ") .grid(row= 1, column = 1 , sticky = W)
    
    Label (frame, text = "Aerolinea" , fg = "black", width = 20,font="none 12 ") .grid(row= 1, column = 2 , sticky = W)

    Label (frame , text = "Origen" , fg = "black",  width = 20, font="none 12 ") .grid(row= 1, column = 3 , sticky = W)
  
    Label (frame , text = "Destino" , fg = "black", width = 20, font="none 12 ") .grid(row= 1, column = 4 , sticky = W)
  
    Label (frame, text = "Hora de Salida " , width = 20, fg = "black", font="none 12 ") .grid(row= 1, column = 5 , sticky = W)

    Label (frame, text = "Hora de Llegada " , width = 20, fg = "black", font="none 12 ") .grid(row= 1, column = 6 , sticky = W)
   
    Label (frame , text = "Estado " , width = 20,  fg = "black", font="none 12 ") .grid(row= 1, column = 7 , sticky = W)
    
    monitorGeneral(frame)
    
def cambiaEstadoVuelos(win , vuelos):
    for n in range(len(vuelos)):
        
        Label (win , text = vuelos[n].modelo ,  fg = "black", width = 12, font="none 10 ") .grid(row= n+2, column = 1 , sticky = W)
    
        Label (win, text = vuelos[n].aerolinea , fg = "black", width = 12,font="none 10 ") .grid(row= n+2, column = 2 , sticky = W)

        Label (win , text = vuelos[n].origen , fg = "black",  width = 12, font="none 10 ") .grid(row= n+2, column = 3 , sticky = W)
  
        Label (win , text = vuelos[n].destino , fg = "black", width = 12, font="none 10") .grid(row= n+2, column = 4 , sticky = W)
  
        Label (win, text = vuelos[n].horaSalida, width = 12, fg = "black", font="none 10 ") .grid(row= n+2, column = 5 , sticky = W)

        Label (win, text = vuelos[n].horaLlegada , width = 12, fg = "black", font="none 10 ") .grid(row= n+2, column = 6 , sticky = W)
   
        Label (win , text = vuelos[n].estado, width = 12,  fg = "black", font="none 10 ") .grid(row= n+2, column = 7 , sticky = W)

def monitorGeneral(win):
    vuelos = generaVuelos()
    cambiaEstadoVuelos(win , vuelos)
    for i in range(len(vuelos)):
        Thread(target=control, args=[vuelos[i], vuelos , win]).start()


def control(vuelo, vuelos , win):
    global salida_entrada, pista, window, pista_Cola
    
    print("Vuelo %s con direccion %s , listo!" % (vuelo.modelo, vuelo.destino ))
    with pista:
        with salida_entrada:
            pista_Cola.append(vuelo)
            print("Soy %s. Estamos dentro: %s" % (vuelo, pista_Cola))
            print(len(pista_Cola))

        sleep(randint(3,10))
        
        if(vuelo.estado == "vuelo"):
            vuelo.modificandoEstado("aterrizando")
            cambiaEstadoVuelos(win , vuelos)
            sleep(1)
            print("%s fuera!" % vuelo)
        else:
            vuelo.modificandoEstado("despegando")
            cambiaEstadoVuelos(win , vuelos)
            sleep(1)
            print("%s fuera!" % vuelo)

        with salida_entrada:
            pista_Cola.remove(vuelo)


class Avion: 

    def __init__(self , modelo , aerolinea , origen , destino , estado):
        self.modelo = modelo
        self.aerolinea = aerolinea
        self.origen = origen
        self.destino = destino
        self.estado = estado
        self.horaLlegada = "********"
        self.horaSalida = "*********"

    def modificandoEstado(self, accion):
        self.estado = accion
        sleep(randint(3,10))
        self.estado = "terminado"
        x = datetime.datetime.now()
        if(accion == "aterrizando"):
            self.horaLlegada = "%s:%s:%s" % (x.hour, x.minute, x.second)
        else:
            self.horaSalida = "%s:%s:%s" % (x.hour, x.minute, x.second)



def generaVuelos():
    vuelos = []
    localidad = ["Mexico" , "China" , "EUA", "Cuba", "Argentina" , "Colombia ", "Espana"]
    modelo = ["Airbus340" , "Boeing747","Boeing777","Boeing757" , "Boeing737", "McDonnell Douglas MD-80"]
    aerolinea = ["Interjet" , "Volaris", "Viva Aerobus", "Aero Mexico", "Air France" , "Emirates Airlines"]
    estado = ["tierra", "vuelo"]
    cont = 0 
    while cont < 20:
        origen = randint(0,5)
        destino = randint(0,5)
        if(origen != destino):
            cont += 1
            vuelos.append(Avion(modelo[randint(0,5)], aerolinea[randint(0,5)] , localidad[origen] , localidad[destino] , estado[randint(0,1)]))
    return vuelos

        
def main():
    paginaInicio()
    

def paginaInicio():
    global window
    window.title("Proyecto" )
    inicia(window)
    window.mainloop()


main()