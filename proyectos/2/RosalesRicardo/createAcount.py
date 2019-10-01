def signIn(window):
    print("Hello")
    window.withdraw()
    win = Toplevel()
    win.title("Crea cuenta")

    name = StringVar()
    lastname = StringVar()
    email = StringVar()
    password = StringVar()
    password1 = StringVar()
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

    boton1 = Button(win, text = "Sign in" , width = 6 , command = paginaInicio)
    boton1.place(x=10, y=200)

from main import paginaInicio