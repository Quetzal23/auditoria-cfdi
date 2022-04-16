from tkinter import *
from tkinter.ttk import Treeview
from tkinter.messagebox import *

from view.upperentry import UpperEntry

class Parametros_Empresas:
    def __init__(self, window):
        wind_width  = 808
        wind_height = 417
        wind_geometry = str(wind_width) + 'x' + str(wind_height)
        self.wind = window
        self.wind.title('PARAMETROS DE EMPRESAS')
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
        self.button_save = Button(frame_top, text='Save',)
        self.button_save.grid(column=1, row=0, padx=5, pady=5, sticky=W)
        self.button_edit = Button(frame_top, text='Edit',)
        self.button_edit.grid(column=2, row=0, padx=5, pady=5, sticky=W)
        self.button_delete = Button(frame_top, text='Delete',)
        self.button_delete.grid(column=3, row=0, padx=5, pady=5, sticky=W)
        self.button_print = Button(frame_top, text='Print',)
        #self.button_print.grid(column=4, row=0, padx=5, pady=5, sticky=W)
        self.button_center = Button(frame_top, text='Centro de Trabajo')
        self.button_center.grid(column=5, row=0, padx=5, pady=5, sticky=W)
        label = Label(frame_top, text='', width=60)    #bg='yellow', width=70
        #label.grid(column=5, row=0, padx=5, pady=5, sticky=E)
        self.button_exit = Button(frame_top, text='Exit', command=self.on_closing)
        self.button_exit.grid(column=6, row=0, padx=5, pady=5, sticky=EW)

    def widget_frame_treeview(self, parametros):
        frame_left = LabelFrame(parametros, relief='flat')
        frame_left.grid(row=1, column=0, padx=0, pady=0, sticky=NSEW)
        self.treeview = Treeview(frame_left, columns=2, height=16)
        self.treeview.heading("#0", text='', anchor=CENTER)
        self.treeview.heading("#1", text='Empresas', anchor=CENTER)
        self.treeview.column('#0', stretch=False, width=0, minwidth=0)
        self.treeview.column('#1', stretch=False, width=300, minwidth=300)    #220
        self.treeview.grid(row=0, column=0, columnspan=2, sticky="nsew")
        scrollbar = Scrollbar(frame_left, orient=VERTICAL, command=self.treeview.yview)
        scrollbar.grid(row=0, column=3, sticky="nse")
        self.treeview.configure(yscrollcommand=scrollbar.set)
        sc = Scrollbar(frame_left, orient=HORIZONTAL, command=self.treeview.xview)
        sc.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.treeview.configure(xscrollcommand=sc.set)

    def widget_frame_datos(self, parametros):
        frame_right = LabelFrame(parametros, relief='flat')
        frame_right.grid(row=1, column=1, padx=0, pady=0, sticky=NSEW)
        
        self.frame_right_disabled = LabelFrame(parametros, relief='flat', bg='#F0F0F0')
        #self.frame_right_disabled.grid(row=1, column=1, padx=0, pady=0, sticky=NSEW)

        self.w_datos_generales(frame_right)
        space = Label(frame_right, text='')
        space.grid(row=1, column=0, pady=1, columnspan=3, sticky=EW)
        self.w_datos_direccion(frame_right)

        
        
    def w_datos_generales(self, frame):
        frame_datos = LabelFrame(frame, text='Datos Generales', relief='flat')
        frame_datos.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        space = Label(frame_datos, text='')
        space.grid(column=0, row=0, pady=1, columnspan=3, sticky=EW)

        nombreE_label = Label(frame_datos, text='Nombre de Empresa')
        nombreE_label.grid(row=1, column=0, sticky=W, padx=2)
        self.nombreE_entry = UpperEntry(frame_datos)
        self.nombreE_entry.grid(row=2, column=0, columnspan=3, sticky=EW, padx=2)

        nombreC_label = Label(frame_datos, text='Nombre corto')
        nombreC_label.grid(row=3, column=0, sticky=W, padx=2)
        self.nombreC_entry = UpperEntry(frame_datos, width=24)
        self.nombreC_entry.grid(row=4, column=0, sticky=W, padx=2)

        rfc_label = Label(frame_datos, text='RFC')
        rfc_label.grid(row=3, column=1, sticky=W, padx=2)
        self.rfc_entry = UpperEntry(frame_datos, width=24)
        self.rfc_entry.grid(row=4, column=1, sticky=W, padx=2)

        patronal_label = Label(frame_datos, text='# Registro Patronal')
        patronal_label.grid(row=3, column=2, sticky=W, padx=2)
        self.patronal_entry = UpperEntry(frame_datos, width=24)
        self.patronal_entry.grid(row=4, column=2, sticky=W, padx=2)

        actividad_label = Label(frame_datos, text='Datos Generales')
        actividad_label.grid(row=5, column=0,  sticky=W, padx=2)
        self.actividad_entry = UpperEntry(frame_datos)
        self.actividad_entry.grid(row=6, column=0, columnspan=3, sticky=EW, padx=2)

    def w_datos_direccion(self, frame):
        frame_direccion = LabelFrame(frame, text='Dirección', relief='flat')
        frame_direccion.grid(row=2, column=0, columnspan=2, sticky=NSEW)
        space = Label(frame_direccion, text='')
        space.grid(row=0, column=0, pady=1, columnspan=3, sticky=EW)

        calle_label = Label(frame_direccion, text='Calle')
        calle_label.grid(row=1, column=0,  sticky=W, padx=2)
        self.calle_entry = UpperEntry(frame_direccion, width=24)
        self.calle_entry.grid(row=2, column=0, sticky=EW, padx=2)

        numero_label = Label(frame_direccion, text='Número')
        numero_label.grid(row=1, column=1,  sticky=W, padx=2)
        self.numero_entry = UpperEntry(frame_direccion, width=24)
        self.numero_entry.grid(row=2, column=1, sticky=W, padx=2)

        colonia_label = Label(frame_direccion, text='Colonia')
        colonia_label.grid(row=1, column=2,  sticky=W, padx=2)
        self.colonia_entry = UpperEntry(frame_direccion, width=24)
        self.colonia_entry.grid(row=2, column=2, sticky=W, padx=2)

        municipio_label = Label(frame_direccion, text='Delegación o Municipio')
        municipio_label.grid(row=3, column=0,  sticky=W, padx=2)
        self.municipio_entry = UpperEntry(frame_direccion, width=24)
        self.municipio_entry.grid(row=4, column=0, sticky=EW, padx=2)

        postal_label = Label(frame_direccion, text='Código Postal')
        postal_label.grid(row=3, column=1,  sticky=W, padx=2)
        self.postal_entry = UpperEntry(frame_direccion, width=24)
        self.postal_entry.grid(row=4, column=1, sticky=EW, padx=2)

        federativa_label = Label(frame_direccion, text='Entidad Federativa')
        federativa_label.grid(row=3, column=2,  sticky=W, padx=2)
        self.federativa_entry = UpperEntry(frame_direccion, width=24)
        self.federativa_entry.grid(row=4, column=2, sticky=EW, padx=2)

        poblacion_label = Label(frame_direccion, text='Población')
        poblacion_label.grid(row=5, column=0,  sticky=W, padx=2)
        self.poblacion_entry = UpperEntry(frame_direccion, width=24)
        self.poblacion_entry.grid(row=6, column=0, sticky=EW, padx=2)
        
        telefono_label = Label(frame_direccion, text='Teléfono(s)')
        telefono_label.grid(row=5, column=1,  sticky=W, padx=2)
        self.telefono_entry = UpperEntry(frame_direccion, width=24)
        self.telefono_entry.grid(row=6, column=1, sticky=EW, padx=2)