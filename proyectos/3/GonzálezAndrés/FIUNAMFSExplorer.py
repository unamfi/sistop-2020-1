import tkinter as tk
from tkinter import ttk

import os
from fiunamfs import FIUNAMFS, format_date

HEADINGS = ['Cluster', 'Nombre', 'Tamaño (bytes)', 'Fecha Creación', 'Fecha Modificación']

class FIUNAMFSExplorer:
    def __init__(self, window=None):
        # Montar sistema de archivos
        fsimg_path = os.path.join('.', 'fiunamfs.img')
        self.fs = FIUNAMFS(fsimg_path)
        self.fs.montar()
        # self.lEntDir = self.fs.scandir()

        self.window = window
        self.window.title('FIUNAM Explorer')
        self.create_widgets()

    def create_widgets(self):
        # Frame Container
        frame = tk.LabelFrame(self.window, text = 'Agregar archivos')
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Nombre de origen
        tk.Label(frame, text = 'Ruta del archivo de origen: ').grid(row = 1, column = 0)
        self.entry_origen = tk.Entry(frame)
        self.entry_origen.focus()
        self.entry_origen.grid(row = 1, column = 1)

        # Nombre de destino
        tk.Label(frame, text = 'Ruta del archivo de destino: ').grid(row = 2, column = 0)
        self.entry_destino = tk.Entry(frame)
        self.entry_destino.focus()
        self.entry_destino.grid(row = 2, column = 1)

        # Botón subir archivo
        ttk.Button(frame, text = 'Añadir archivo', command = self.subir_archivo).grid(row = 3, columnspan = 2, sticky = tk.W + tk.E)

        # Mensajes de salida 
        self.message = tk.Label(text = '', fg = 'red')
        self.message.grid(row = 4, column = 0, columnspan = 2, sticky = tk.W + tk.E)

        # Tabla
        self.tree = ttk.Treeview(height = 10, columns = ('#1', '#2', '#3', '#4', '#5'))

        self.tree.column("#0", width=0, minwidth=0)
        self.tree.column("#1", width=60, minwidth=50)
        self.tree.column("#2", width=150, minwidth=50)
        self.tree.column("#3", width=100, minwidth=50)
        self.tree.column("#4", width=150, minwidth=50)
        self.tree.column("#5", width=150, minwidth=50)

        self.tree.heading('#0', text = 'id', anchor = tk.CENTER)
        self.tree.heading('#1', text = 'Cluster', anchor = tk.CENTER)
        self.tree.heading('#2', text = 'Nombre', anchor = tk.CENTER)
        self.tree.heading('#3', text = 'Tamaño (bytes)', anchor = tk.CENTER)
        self.tree.heading('#4', text = 'Fecha Creación', anchor = tk.CENTER)
        self.tree.heading('#5', text = 'Fecha Modificación', anchor = tk.CENTER)

        self.tree.grid(row = 5, column = 0, columnspan = 2) # Poniendo la tabla

        # Botones descargar y eliminar
        ttk.Button(text = 'Eliminar', command = self.eliminar_archivo).grid(row = 6, column = 0, sticky = tk.W + tk.E)
        ttk.Button(text = 'Descargar', command = self.descargar_archivo).grid(row = 6, column = 1, sticky = tk.W + tk.E)

        # Boton para desfragmentar
        ttk.Button(text = 'Desfragmentar Unidad', command = self.desfragmentar_unidad).grid(row = 7, column = 0, columnspan = 2, sticky = tk.W + tk.E + tk.N + tk.S)

        self.imprime_dir()

    def desfragmentar_unidad(self):
        self.message['fg'] = 'blue'
        self.message['text'] = 'Desfragmentando unidad...'
        self.fs.desfragmentar()
        self.message['fg'] = 'green'
        self.message['text'] = 'Unidad desgragmentada'
        self.imprime_dir()
    
    def subir_archivo(self):
        origen = self.entry_origen.get()
        if not origen:
            self.message['fg'] = 'red'
            self.message['text'] = 'Escribe la ruta de origen'
            return
        destino = self.entry_destino.get()
        if not destino:
            self.message['fg'] = 'red'
            self.message['text'] = 'Escribe la ruta de destino'
            return
        try:
            if self.fs.subir(origen, destino):
                self.imprime_dir()
                self.message['fg'] = 'green'
                self.message['text'] = 'Archivo %s escrito satisfactoriamente' % destino
        except Exception as e:
            self.message['fg'] = 'red'
            self.message['text'] = str(e)

    def eliminar_archivo(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['fg'] = 'red'
            self.message['text'] = 'Por favor, selecciona un archivo'
            return
        nombre = self.tree.item(self.tree.selection())['values'][1]
        # print('Seleccionaste %s' % nombre)

        self.conf_del_win = tk.Toplevel() # Ventana de confirmación de eliminación
        self.conf_del_win.title = 'Eliminar archivo'
        
        # Mensaje de verificación
        tk.Label(self.conf_del_win, text = ('¿Realmente desea eliminar \n%s?:' % nombre)).grid(row = 0, column = 0, columnspan=2)

        # Botones
        tk.Button(self.conf_del_win, text = 'Eliminar', command = lambda : self.eliminar_definitivo(nombre)).grid(row = 1, column = 0, sticky = tk.W + tk.E)
        tk.Button(self.conf_del_win, text = 'Cancelar', command = self.conf_del_win.destroy).grid(row = 1, column = 1, sticky = tk.W + tk.E)

        # Posicion de la ventana de verificación        
        x = self.window.winfo_x()
        y = self.window.winfo_y()
        #w = self.conf_del_win.winfo_width()
        #h = self.conf_del_win.winfo_height()  
        self.conf_del_win.geometry("%dx%d+%d+%d" % (180, 60, x + 200, y + 100))
        self.conf_del_win.mainloop()
    
    def eliminar_definitivo(self, nombre_archivo):
        self.fs.eliminar(nombre_archivo)
        self.conf_del_win.destroy()
        self.imprime_dir()
        self.message['fg'] = 'green'
        self.message['text'] = '%s eliminado satisfactoriamente' % nombre_archivo

    def descargar_archivo(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['fg'] = 'red'
            self.message['text'] = 'Por favor, selecciona un archivo'
            return
        
        nombre = self.tree.item(self.tree.selection())['values'][1]

        self.conf_descarga_win = tk.Toplevel() # Ventana de confirmación de eliminación
        self.conf_descarga_win.title = 'Descargar archivo'
        # Posicion de la ventana de verificación        
        x = self.window.winfo_x()
        y = self.window.winfo_y()
        self.conf_descarga_win.geometry("%dx%d+%d+%d" % (300, 100, x + 100, y + 100))
        
        # Mensaje de verificación
        tk.Label(self.conf_descarga_win, text = 'Ruta del archivo a escribir:').grid(row = 0, column = 0, columnspan=1)
        self.entry_destino_descarga = tk.Entry(self.conf_descarga_win)
        self.entry_destino_descarga.focus()
        self.entry_destino_descarga.grid(row = 0, column = 1, columnspan=1)

        # Mensajes de salida 
        self.label_msj_pop = tk.Label(self.conf_descarga_win, text = '', fg = 'red')
        self.label_msj_pop.grid(row = 1, column = 0, columnspan = 2, sticky = tk.W + tk.E)

        # Boton
        tk.Button(self.conf_descarga_win, text = 'Descargar', command = lambda : self.descargar_definitivo(nombre)).grid(row = 2, column = 0, columnspan=2)

        self.conf_descarga_win.mainloop()

    def descargar_definitivo(self, origen):
        destino = self.entry_destino_descarga.get()
        if not destino:
            self.label_msj_pop['fg'] = 'red'
            self.label_msj_pop['text'] = 'Escribe un nombre de archivo'
        else:
            try:
                self.fs.descargar(origen, destino)
                self.conf_descarga_win.destroy()
                self.imprime_dir()
                self.message['fg'] = 'green'
                self.message['text'] = 'Se descargó el archivo %s satisfactoriamente' % destino
            except Exception as e:
                self.message['fg'] = 'red'
                self.message['text'] = str(e)

    # Imprimir directorio
    def imprime_dir(self):
        # Limpiar tabla 
        lista_ed = self.fs.scandir() # Lista de entradas del directorio
        registros = self.tree.get_children()
        for e in registros:
            self.tree.delete(e)
        
        for ed in lista_ed:
            valores = [ed.cluster_inicial, ed.nombre, ed.tam_archivo, format_date(ed.f_creacion), format_date(ed.f_modif)]
            self.tree.insert('', 0, values = valores)

if __name__ == "__main__":
    root = tk.Tk()
    app = FIUNAMFSExplorer(window=root)
    app.window.mainloop()