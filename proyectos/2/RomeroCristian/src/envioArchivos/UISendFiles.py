#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
from threading import Thread, Semaphore, Lock
from envioArchivos.SplitFile import SplitFile
from envioArchivos.JoinParts import JoinParts
from os.path import dirname

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class UISendFiles(wx.Frame):
    def __init__(self, *args, **kwds):
        """
        Objetos utilizados en la GUI
        """

        # begin wxGlade: UISendFiles.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.mutex = Semaphore(1)

        self.SetSize((400, 300))
        self.archivo_in = wx.FilePickerCtrl(self, wx.ID_ANY, "Archivo Entrada")
        self.dir_out = wx.DirPickerCtrl(self, wx.ID_ANY, "button_1")
        #self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "")
        self.send = wx.Button(self, wx.ID_ANY, "Iniciar")
        self.send.Bind(wx.EVT_BUTTON, self.get_path)
        self.num_split = wx.SpinCtrlDouble(self, wx.ID_ANY, '4')

        self.status = wx.StaticText(self, wx.ID_ANY, "Status")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: UISendFiles.__set_properties
        self.SetTitle("frame")
        # end wxGlade

    def get_path(self, event):
        """
        Aqui se inica la ejecución de las clases
        """

        s = SplitFile(self.archivo_in.GetPath(),
                      dest_dir=self.dir_out.GetPath())
        t = Thread(target=s.start_split, args=(
            self.mutex, int(self.num_split.GetValue())))
        t.start()
        self.status.SetLabel(str(self.num_split.GetValue()))
        j = JoinParts(self.archivo_in.GetPath(), self.dir_out.GetPath(),
                      work_dir=dirname(self.archivo_in.GetPath()))

        t2 = Thread(target=j.join, args=(self.mutex,))
        t2.start()
        s.clean_part(self.mutex)

    def __do_layout(self):
        """
        El 'lienzo' de la GUI
        """
        # begin wxGlade: UISendFiles.__do_layout
        Menu = wx.BoxSizer(wx.VERTICAL)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        Menu.Add(wx.StaticText(self, wx.ID_ANY, 'Seleccione el archivo:'),
                 0, wx.EXPAND, 0)
        Menu.Add(self.archivo_in, 0, wx.EXPAND, 0)
        Menu.Add(wx.StaticText(self, wx.ID_ANY, 'Seleccione la ruta:'),
                 0, wx.EXPAND, 0)
        Menu.Add(self.dir_out, 0, wx.EXPAND, 0)

        Menu.Add(wx.StaticText(self, wx.ID_ANY, 'Seleccione el número a dividir:'),
                 0, wx.EXPAND, 0)
        Menu.Add(self.num_split, 0, 0, 0)
        #Menu.Add(self.text_ctrl_1, 0, 0, 0)
        sizer_1.Add(self.status, 0, 0, 0)
        sizer_1.Add(self.send, 0, 0, 0)
        Menu.Add(sizer_1, 1, wx.ALIGN_CENTER, 0)
        self.SetSizer(Menu)
        self.Layout()
        # end wxGlade

# end of class UISendFiles


class MyApp(wx.App):
    def OnInit(self):
        self.frame = UISendFiles(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp


if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
