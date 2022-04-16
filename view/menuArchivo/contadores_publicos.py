from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview

from view.upperentry import UpperEntry

class Contadores_Publicos:
    def __init__(self, window):
        wind_width  = 884
        wind_height = 417
        wind_geometry = str(wind_width) + 'x' + str(wind_height)
        self.wind = window
        self.wind.title('CATALOGO DE CONTADORES PÚBLICOS')
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
        self.widget_frame_datos(parametros)

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

    def widget_frame_datos(self, parametros):
        frame_right = LabelFrame(parametros, relief='flat')
        frame_right.grid(row=1, column=1, padx=0, pady=0, sticky=NSEW)
        
        self.frame_right_disabled = LabelFrame(parametros, relief='flat', bg='#F0F0F0')
        #self.frame_right_disabled.grid(row=1, column=1, padx=0, pady=0, sticky=NSEW)

        self.w_datos_generales(frame_right)
        space = Label(frame_right, text='')
        space.grid(row=1, column=0, pady=1, columnspan=3, sticky=EW)
        self.w_datos_direccion(frame_right)
        
    def widget_frame_treeview(self, parametros):
        frame_left = LabelFrame(parametros, relief='flat')
        frame_left.grid(row=1, column=0, padx=0, pady=0, sticky=NSEW)

        self.treeview = Treeview(frame_left, columns=[f"#{n}" for n in range(0, 2)], height=16) #columns=[f"#{n}" for n in range(0, 2)],
        self.treeview.heading("#0", text='', anchor=CENTER)
        self.treeview.heading("#1", text='Num', anchor=CENTER)
        self.treeview.heading("#2", text='Nombre', anchor=CENTER)

        self.treeview.column('#0', stretch=False, width=0, minwidth=0)
        self.treeview.column('#1', stretch=False, width=64, minwidth=64)    #220
        self.treeview.column('#2', stretch=False, width=208, minwidth=208)
        #self.treeview.config(show='headings')
        self.treeview.grid(row=0, column=0, columnspan=2, sticky="nsew")

        scrollbar = Scrollbar(frame_left, orient=VERTICAL, command=self.treeview.yview)
        scrollbar.grid(row=0, column=3, sticky="nse")
        self.treeview.configure(yscrollcommand=scrollbar.set)
        sc = Scrollbar(frame_left, orient=HORIZONTAL, command=self.treeview.xview)
        sc.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.treeview.configure(xscrollcommand=sc.set)
    
    def w_datos_generales(self, frame):
        frame_datos = LabelFrame(frame, text='Datos Generales', relief='flat')
        frame_datos.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        space = Label(frame_datos, text='')
        space.grid(column=0, row=0, pady=1, sticky=EW)

        nombreC_label = Label(frame_datos, text='Nombre del Contador Público')
        nombreC_label.grid(row=1, column=0, sticky=W, padx=2)
        self.nombreC_entry = UpperEntry(frame_datos)
        self.nombreC_entry.grid(row=2, column=0, columnspan=3, sticky=EW, padx=2)

        noimss_label = Label(frame_datos, text='No. Registro IMSS')
        noimss_label.grid(row=3, column=0, sticky=W, padx=2)
        self.noimss_entry = UpperEntry(frame_datos, )
        self.noimss_entry.grid(row=4, column=0, sticky=EW, padx=2)

        noinfonavit_label = Label(frame_datos, text='No. Registro INFONAVIT')
        noinfonavit_label.grid(row=3, column=1, sticky=W, padx=2)
        self.noinfonavit_entry = UpperEntry(frame_datos, width=28)
        self.noinfonavit_entry.grid(row=4, column=1, sticky=EW, padx=2)

        email_label = Label(frame_datos, text='E-Mail')
        email_label.grid(row=3, column=2, sticky=W, padx=2)
        self.email_entry = UpperEntry(frame_datos, width=32)
        self.email_entry.grid(row=4, column=2, sticky=W, padx=2)

        colegio_label = Label(frame_datos, text='Colegio o Asociación Profesional')
        colegio_label.grid(row=5, column=0,  sticky=W, padx=2)
        self.colegio_entry = UpperEntry(frame_datos)
        self.colegio_entry.grid(row=6, column=0, columnspan=2, sticky=EW, padx=2)

        despacho_label = Label(frame_datos, text='Nombre del Despacho')
        despacho_label.grid(row=5, column=2,  sticky=W, padx=2)
        self.despacho_entry = UpperEntry(frame_datos)
        self.despacho_entry.grid(row=6, column=2, sticky=EW, padx=2)

    def w_datos_direccion(self, frame):
        frame_direccion = LabelFrame(frame, text='Dirección', relief='flat')
        frame_direccion.grid(row=2, column=0, columnspan=2, sticky=NSEW)
        space = Label(frame_direccion, text='')
        space.grid(row=0, column=0, pady=1, columnspan=3, sticky=EW)

        calle_label = Label(frame_direccion, text='Calle')
        calle_label.grid(row=1, column=0,  sticky=W, padx=2)
        self.calle_entry = UpperEntry(frame_direccion, width=28)
        self.calle_entry.grid(row=2, column=0, sticky=EW, padx=2)

        numero_label = Label(frame_direccion, text='Número')
        numero_label.grid(row=1, column=1,  sticky=W, padx=2)
        self.numero_entry = UpperEntry(frame_direccion, width=28)
        self.numero_entry.grid(row=2, column=1, sticky=W, padx=2)

        colonia_label = Label(frame_direccion, text='Colonia')
        colonia_label.grid(row=1, column=2,  sticky=W, padx=2)
        self.colonia_entry = UpperEntry(frame_direccion, width=28)
        self.colonia_entry.grid(row=2, column=2, sticky=W, padx=2)

        municipio_label = Label(frame_direccion, text='Delegación o Municipio')
        municipio_label.grid(row=3, column=0,  sticky=W, padx=2)
        self.municipio_entry = UpperEntry(frame_direccion, width=28)
        self.municipio_entry.grid(row=4, column=0, sticky=EW, padx=2)

        postal_label = Label(frame_direccion, text='Código Postal')
        postal_label.grid(row=3, column=1,  sticky=W, padx=2)
        self.postal_entry = UpperEntry(frame_direccion, width=28)
        self.postal_entry.grid(row=4, column=1, sticky=EW, padx=2)

        federativa_label = Label(frame_direccion, text='Entidad Federativa')
        federativa_label.grid(row=3, column=2,  sticky=W, padx=2)
        self.federativa_entry = UpperEntry(frame_direccion, width=28)
        self.federativa_entry.grid(row=4, column=2, sticky=EW, padx=2)
        
        telefono_label = Label(frame_direccion, text='Teléfono(s)')
        telefono_label.grid(row=5, column=0,  sticky=W, padx=2)
        self.telefono_entry = UpperEntry(frame_direccion, width=28)
        self.telefono_entry.grid(row=6, column=0, sticky=EW, padx=2)