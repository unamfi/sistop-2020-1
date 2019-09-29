from Tkinter import *
import tkMessageBox
from PIL import ImageTk,Image  
from functools import partial  
import threading
import time
import datetime
import pickle
#from  createAcount import signIn


window = Tk()
mutex = threading.Semaphore(1)

def click(): 
    entered_text = textentry.get()  #Colecta el texto del input 
    output.delete(0.0 , END)
    try :
        definition = my_dictionary[entered_text] 
    except: 
        definition = "Sorry , whe don't find this word"
    output.insert(END , definition)

def validar(user , password):
    dic = cargarDatos()
    print(dic)
    if password.get() == "contrasena":
        tkMessageBox.showinfo("Password Correct","Password Correct" )
    else:
        tkMessageBox.showinfo("Password incorrect", "Password incorrect")

def inicia(window):
    print("Hello")
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

    textentry = Entry(frame, width = 20, bg = "white")
    textentry.grid(row = 2 , column =0 , sticky= W)

    textentry1 = Entry(frame, textvariable = password,width = 20, bg = "white")
    textentry1.grid(row = 2 , column =1, sticky= W)
    
    validate = partial( validar ,user ,  password)
    sign = partial(signIn, window)

    boton1 = Button(frame , text = "Sign in" , width = 6 , command = sign)
    boton1.place(x=10, y=200)

    boton2 = Button(frame , text = "Log in" , width = 6 , command = validate)
    boton2.place(x=100, y=200)
    
    #Label(frame , text = "\nDefinition ", bg = "black", fg = "white", font = "nonde 12 bold") .grid(row = 4, column = 0 , sticky= W)

    #output = Text(frame ,width = 75, height = 6 , wrap = WORD , background = "white")
    #output.grid(row = 5 , column = 0, columnspan = 2, sticky = W)

    my_dictionary = {
        'algorithm' : 'Step by step instructions to complete a task',
        'bug' : 'pice of code taht causes a program to fail'
    }

def muestraHora(window):
    #while True:
    x = datetime.datetime.now()
    hour = Label(window , text = "%s:%s:%s" % (x.hour, x.minute, x.second),borderwidth=2 ,relief = "groove", fg = "blue" , font = "none 19 bold")
    hour.place(x = 600 , y = 10)

def signIn(window):
    print("Hello")
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

    boton1 = Button(win, text = "Sign in" , width = 6 , command = inicio)
    boton1.place(x=5, y=250)


def muestraInicio(win, name, lastname , email , password , password1):
    print(password.get())
    print(password1.get())
    if password.get() == password1.get:
        usuario = { 'name' : name.get() , 'lastname': lastname.get() , 'email' : email.get() , 'password' : password.get()}
        guardarDatos(user)
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

def main():
    paginaInicio()
    

def paginaInicio():
   
    window.title("Proyecto" )
    inicia(window)
    window.mainloop()

def paginasSec():
    print("Hello")
    window.withdraw()
    win = Toplevel()

main()