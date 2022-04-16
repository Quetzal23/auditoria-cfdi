from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from turtle import width

from view.upperentry import UpperEntry

class Usuarios:
    def __init__(self, window):
        wind_width  = 720
        wind_height = 200   #417
        wind_geometry = str(wind_width) + 'x' + str(wind_height)
        self.wind = window
        self.wind.title('USUARIOS')
        self.wind.geometry(wind_geometry)
        self.wind.resizable(0,0)
        self.wind.protocol('WM_DELETE_WINDOW', )
        self.create_widgets(self.wind)

    def on_closing(self):
        self.wind.destroy()
    
    def create_widgets(self, wind):
        parametros = LabelFrame(wind, relief='flat')
        parametros.grid(row=0, column=0, padx=10, pady=8, sticky=NSEW)

        self.widget_frame_buttons(parametros)
        self.widget_frame_treeview(parametros)
        self.widget_datos(parametros)
    
    def widget_frame_buttons(self, parametros):
        frame_top = LabelFrame(parametros, relief='flat')
        frame_top.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        self.button_new = Button(frame_top, text='New')
        self.button_new.grid(column=0, row=0, padx=5, pady=5, sticky=W)
        self.button_save = Button(frame_top, text='Save')
        self.button_save.grid(column=1, row=0, padx=5, pady=5, sticky=W)
        self.button_edit = Button(frame_top, text='Edit')
        self.button_edit.grid(column=2, row=0, padx=5, pady=5, sticky=W)
        self.button_delete = Button(frame_top, text='Delete')
        self.button_delete.grid(column=3, row=0, padx=5, pady=5, sticky=W)
        self.button_print = Button(frame_top, text='Print')
        self.button_print.grid(column=4, row=0, padx=5, pady=5, sticky=W)
        
        self.button_exit = Button(frame_top, text='Exit', command=self.on_closing)
        self.button_exit.grid(column=6, row=0, padx=5, pady=5, sticky=EW)

    def widget_frame_treeview(self, parametros):
        frame_left = LabelFrame(parametros, relief='flat')
        frame_left.grid(row=1, column=0, padx=0, pady=0, sticky=NSEW)

        self.treeview = Treeview(frame_left, columns=[f"#{n}" for n in range(0, 2)], height=5)
        self.treeview.heading("#0", text='', anchor=CENTER)
        self.treeview.heading("#1", text='Usuario', anchor=CENTER)
        self.treeview.heading("#2", text='Nivel', anchor=CENTER)

        self.treeview.column('#0', stretch=False, width=0, minwidth=0)
        self.treeview.column('#1', stretch=False, width=180, minwidth=64)    #220
        self.treeview.column('#2', stretch=False, width=120, minwidth=208)
        #self.treeview.config(show='headings')
        self.treeview.grid(row=0, column=0, columnspan=2, sticky="nsew")

        scrollbar = Scrollbar(frame_left, orient=VERTICAL, command=self.treeview.yview)
        scrollbar.grid(row=0, column=3, sticky="nse")
        self.treeview.configure(yscrollcommand=scrollbar.set)
        sc = Scrollbar(frame_left, orient=HORIZONTAL, command=self.treeview.xview)
        sc.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.treeview.configure(xscrollcommand=sc.set)

    def widget_datos(self, frame):
        frame_right = LabelFrame(frame, relief='flat')
        frame_right.grid(row=1, column=1, padx=0, pady=0, sticky=NSEW)
        
        nombre_label = Label(frame_right, text='Nombre Completo')
        nombre_label.grid(row=1, column=0,  sticky=W, padx=2)
        self.nombre_entry = UpperEntry(frame_right, width=28)
        self.nombre_entry.grid(row=2, column=0, columnspan=2, sticky=EW, padx=2)
        
        usuario_label = Label(frame_right, text='Usuario')
        usuario_label.grid(row=3, column=0, sticky=W, padx=2)
        self.usuario_entry = UpperEntry(frame_right, width=28)
        self.usuario_entry.grid(row=4, column=0, sticky=EW, padx=2)
        
        contras_label = Label(frame_right, text='Contraseña')
        contras_label.grid(row=3, column=1, sticky=W, padx=2)
        self.contras_entry = UpperEntry(frame_right, width=28)
        self.contras_entry.grid(row=4, column=1, sticky=EW, padx=2)

        contras_label = Label(frame_right, text='Nivel')
        contras_label.grid(row=5, column=0, sticky=W, padx=2)
        self.contras_entry = ttk.Combobox(frame_right, width=28)
        self.contras_entry.grid(row=6, column=0, sticky=EW, padx=2)