import tkinter as tk
from tkinter import ttk

import os
from fiunamfs import FIUNAMFS

class FIUNAMFSExplorer:
    def __init__(self, window=None):
        self.window = window
        self.window.title('FIUNAM Explorer')
        self.create_widgets()
        # fsimg_path = os.path.join('.', 'fiunamf v0.7.img')
        # fs = FIUNAMFS(fsimg_path)
        # fs.montar()
        # fs.montar()

        # l_archivos = fs.listdir()
        # print(l_archivos)

        # lEntDir = fs.scandir()

    def create_widgets(self):
        # Frame Container
        frame = tk.LabelFrame(self.window, text = 'Agregar archivos')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Name Input
        tk.Label(frame, text = 'Name: ').grid(row = 1, column = 0)
        self.name = tk.Entry(frame)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        # Price Input
        tk.Label(frame, text = 'Price: ').grid(row = 2, column = 0)
        self.price = tk.Entry(frame)
        self.price.grid(row = 2, column = 1)

        # Table
        self.tree = ttk.Treeview(height = 10, columns = ('#0', '#1', '#2', '#3', '#4'))
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Cluster', anchor = tk.CENTER)
        self.tree.heading('#1', text = 'Nombre', anchor = tk.CENTER)
        self.tree.heading('#2', text = 'Tamaño (bytes)', anchor = tk.CENTER)
        self.tree.heading('#3', text = 'Fecha Creación', anchor = tk.CENTER)
        self.tree.heading('#4', text = 'Fecha Modificación', anchor = tk.CENTER)

        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.pack(side="top")

        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=self.master.destroy)
        # self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
    
    def leer_dir(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = FIUNAMFSExplorer(window=root)
    app.window.mainloop()

# class FIUNAMFSExplorer(object):
#     def __init__(self, window : tk.Tk):
#         self.window = window
#         self.window.title('FIUNAM Explorer')
#         self.window.geometry((500,600))
#         frame = tk.LabelFrame(self.window, text='Agregar un archivo')
#         frame.grid(row=0, column=0, columnspan=3, pady=20)

# if __name__ == "__main__":
#     window = tk.Tk()
#     app = FIUNAMFSExplorer(window)
#     window.mainloop()