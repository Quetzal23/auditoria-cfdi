from sys import maxsize
from telnetlib import STATUS
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import Treeview

from db import Database

class Parametros_Empresas:
    db = Database('auditoria.db')

    def __init__(self, window):
        wind_width  = 808
        wind_height = 417

        wind_geometry = str(wind_width) + 'x' + str(wind_height)

        self.wind = window
        self.wind.title('PARAMETROS DE EMPRESAS')
        self.wind.geometry(wind_geometry)   #'750x412'
        self.wind.resizable(0,0)
        self.wind.protocol('WM_DELETE_WINDOW', )

        self.create_widgets(self.wind)

    def on_closing(self):
        self.wind.destroy()

    def create_widgets(self, wind):
        parametros = LabelFrame(wind, relief='flat')
        parametros.grid(row=0, column=0, padx=10, pady=8, sticky=NSEW)

        frame_top = LabelFrame(parametros, relief='flat')
        frame_top.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        self.button_new = Button(frame_top, text='New', command=self.entry_new)
        self.button_new.grid(column=0, row=0, padx=5, pady=5, sticky=W)
        self.button_save = Button(frame_top, text='Save', state='disabled', command=self.entry_save)
        self.button_save.grid(column=1, row=0, padx=5, pady=5, sticky=W)
        self.button_edit = Button(frame_top, text='Edit', command=self.edit_empresa)    # state='disabled',
        self.button_edit.grid(column=2, row=0, padx=5, pady=5, sticky=W)
        self.button_delete = Button(frame_top, text='Delete', state='disabled')
        self.button_delete.grid(column=3, row=0, padx=5, pady=5, sticky=W)
        self.button_print = Button(frame_top, text='Print', state='disabled')
        self.button_print.grid(column=4, row=0, padx=5, pady=5, sticky=W)
        label = Label(frame_top, text='', width=60)    #bg='yellow', width=70
        label.grid(column=5, row=0, padx=5, pady=5, sticky=E)
        self.button_exit = Button(frame_top, text='Exit', command=self.on_closing)
        self.button_exit.grid(column=6, row=0, padx=5, pady=5, sticky=EW)

        frame_left = LabelFrame(parametros, relief='flat')
        frame_left.grid(row=1, column=0, padx=0, pady=0, sticky=NSEW)
        # Tabla de empresas         [row=1, column=0]
        self.treeview = Treeview(frame_left, columns=2, height=16)
        self.treeview.heading("#0", text='', anchor=CENTER)
        self.treeview.heading("#1", text='Empresas', anchor=CENTER)
        self.treeview.column('#0', stretch=False, width=0, minwidth=0)
        self.treeview.column('#1', stretch=False, width=300, minwidth=300)    #220
        self.treeview.grid(row=0, column=0, columnspan=2, sticky="nsew")
        ##
        scrollbar = Scrollbar(frame_left, orient=VERTICAL, command=self.treeview.yview)
        scrollbar.grid(row=0, column=3, sticky="nse")
        self.treeview.configure(yscrollcommand=scrollbar.set)
        ##
        sc = Scrollbar(frame_left, orient=HORIZONTAL, command=self.treeview.xview)
        sc.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.treeview.configure(xscrollcommand=sc.set)

        frame_right = LabelFrame(parametros, relief='flat')
        frame_right.grid(row=1, column=1, padx=0, pady=0, sticky=NSEW)
        
        self.frame_right_disabled = LabelFrame(parametros, relief='flat', bg='#F0F0F0')
        self.frame_right_disabled.grid(row=1, column=1, padx=0, pady=0, sticky=NSEW)

        frame_datos = LabelFrame(frame_right, text='Datos Generales', relief='flat')
        frame_datos.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        # Datos genarales         [row=1, column=1]
        space = Label(frame_datos, text='')
        space.grid(column=0, row=0, pady=1, columnspan=3, sticky=EW)
        nombreE_label = Label(frame_datos, text='Nombre de Empresa')
        nombreE_label.grid(row=1, column=0, sticky=W, padx=2)
        #self.nombreE_entry = Entry(frame_datos, state='disabled')
        self.nombreE_entry = UpperEntry(frame_datos)
        self.nombreE_entry.grid(row=2, column=0, columnspan=3, sticky=EW, padx=2)
        nombreC_label = Label(frame_datos, text='Nombre corto')
        nombreC_label.grid(row=3, column=0, sticky=W, padx=2)
        #self.nombreC_entry = Entry(frame_datos, width=24, state='disabled')
        self.nombreC_entry = UpperEntry(frame_datos, width=24)
        self.nombreC_entry.grid(row=4, column=0, sticky=W, padx=2)
        rfc_label = Label(frame_datos, text='RFC')
        rfc_label.grid(row=3, column=1, sticky=W, padx=2)
        #self.rfc_entry = Entry(frame_datos, width=24, state='disabled')
        self.rfc_entry = UpperEntry(frame_datos, width=24)
        self.rfc_entry.grid(row=4, column=1, sticky=W, padx=2)
        patronal_label = Label(frame_datos, text='# Registro Patronal')
        patronal_label.grid(row=3, column=2, sticky=W, padx=2)
        #self.patronal_entry = Entry(frame_datos, width=24, state='disabled')
        self.patronal_entry = UpperEntry(frame_datos, width=24)
        self.patronal_entry.grid(row=4, column=2, sticky=W, padx=2)
        actividad_label = Label(frame_datos, text='Datos Generales')
        actividad_label.grid(row=5, column=0,  sticky=W, padx=2)
        #self.actividad_entry = Entry(frame_datos, state='disabled')
        self.actividad_entry = UpperEntry(frame_datos)
        self.actividad_entry.grid(row=6, column=0, columnspan=3, sticky=EW, padx=2)

        space = Label(frame_right, text='')
        space.grid(row=1, column=0, pady=1, columnspan=3, sticky=EW)

        frame_direccion = LabelFrame(frame_right, text='Dirección', relief='flat')
        frame_direccion.grid(row=2, column=0, columnspan=2, sticky=NSEW)
        space = Label(frame_direccion, text='')
        space.grid(row=0, column=0, pady=1, columnspan=3, sticky=EW)
        calle_label = Label(frame_direccion, text='Calle')
        calle_label.grid(row=1, column=0,  sticky=W, padx=2)
        #self.calle_entry = Entry(frame_direccion, width=24, state='disabled')
        self.calle_entry = UpperEntry(frame_direccion, width=24)
        self.calle_entry.grid(row=2, column=0, sticky=EW, padx=2)
        numero_label = Label(frame_direccion, text='Número')
        numero_label.grid(row=1, column=1,  sticky=W, padx=2)
        #self.numero_entry = Entry(frame_direccion, width=24, state='disabled')
        self.numero_entry = UpperEntry(frame_direccion, width=24)
        self.numero_entry.grid(row=2, column=1, sticky=W, padx=2)
        colonia_label = Label(frame_direccion, text='Colonia')
        colonia_label.grid(row=1, column=2,  sticky=W, padx=2)
        #self.colonia_entry = Entry(frame_direccion, width=24, state='disabled')
        self.colonia_entry = UpperEntry(frame_direccion, width=24)
        self.colonia_entry.grid(row=2, column=2, sticky=W, padx=2)
        municipio_label = Label(frame_direccion, text='Delegación o Municipio')
        municipio_label.grid(row=3, column=0,  sticky=W, padx=2)
        #self.municipio_entry = Entry(frame_direccion, width=24, state='disabled')
        self.municipio_entry = UpperEntry(frame_direccion, width=24)
        self.municipio_entry.grid(row=4, column=0, sticky=EW, padx=2)
        postal_label = Label(frame_direccion, text='Código Postal')
        postal_label.grid(row=3, column=1,  sticky=W, padx=2)
        #self.postal_entry = Entry(frame_direccion, width=24, state='disabled')
        self.postal_entry = UpperEntry(frame_direccion, width=24)
        self.postal_entry.grid(row=4, column=1, sticky=EW, padx=2)
        federativa_label = Label(frame_direccion, text='Entidad Federativa')
        federativa_label.grid(row=3, column=2,  sticky=W, padx=2)
        #self.federativa_entry = Entry(frame_direccion, width=24, state='disabled')
        self.federativa_entry = UpperEntry(frame_direccion, width=24)
        self.federativa_entry.grid(row=4, column=2, sticky=EW, padx=2)
        poblacion_label = Label(frame_direccion, text='Población')
        poblacion_label.grid(row=5, column=0,  sticky=W, padx=2)
        #self.poblacion_entry = Entry(frame_direccion, width=24, state='disabled')
        self.poblacion_entry = UpperEntry(frame_direccion, width=24)
        self.poblacion_entry.grid(row=6, column=0, sticky=EW, padx=2)
        telefono_label = Label(frame_direccion, text='Teléfono(s)')
        telefono_label.grid(row=5, column=1,  sticky=W, padx=2)
        #self.telefono_entry = Entry(frame_direccion, width=24, state='disabled')
        self.telefono_entry = UpperEntry(frame_direccion, width=24)
        self.telefono_entry.grid(row=6, column=1, sticky=EW, padx=2)

        self.get_empresas()
    
    def get_empresas(self):
        records = self.treeview.get_children()
        for element in records:
            self.treeview.delete(element)
        
        try:
            db_rows = self.db.get_empresa()
            for row in db_rows:
                self.treeview.insert('', END, text='', values=(row[1], ))
        except:
            print('TreeView vacio')


    def entry_new(self):
        self.button_save['state'] = 'normal'
        self.nombreE_entry.focus()
        self.frame_right_disabled.grid_forget()
        self.button_new['state'] = 'disabled'


    def validation(self):
        return ( len(self.nombreE_entry.get()) != 0 and len(self.nombreC_entry.get()) and 
            len(self.rfc_entry.get()) and len(self.patronal_entry.get()) and len(self.actividad_entry.get()) and
            len(self.calle_entry.get()) and len(self.numero_entry.get()) and len(self.colonia_entry.get()) and
            len(self.municipio_entry.get()) and len(self.postal_entry.get()) and len(self.federativa_entry.get()) and
            len(self.poblacion_entry.get()) and len(self.telefono_entry.get()) )

    def form_warning(self):
        showwarning('Guardar', 
            'Llene el formulario antes de guardar')


    def entry_save(self):
        if self.validation():
            self.frame_right_disabled.grid(row=1, column=1, padx=0, pady=0, sticky=NSEW)

            nemp = self.nombreE_entry.get()
            ncort =  self.nombreC_entry.get()
            rfc = self.rfc_entry.get()
            ptr = self.patronal_entry.get()
            activ = self.actividad_entry.get()
            calle = self.calle_entry.get()
            num = self.numero_entry.get()
            col = self.colonia_entry.get()
            mpio = self.municipio_entry.get()
            postal = self.postal_entry.get()
            fed = self.federativa_entry.get()
            pob = self.poblacion_entry.get()
            tel = self.telefono_entry.get()

            print('OK')
            self.db.add_empresa(nemp, ncort, rfc, ptr, activ, calle, num, col, mpio, postal, fed, pob, tel)
            
            self.button_save['state'] = 'disabled'
            self.button_new['state'] = 'normal'
        else:
            self.form_warning()
        #

    def edit_empresa(self):
        try:
            h = self.treeview.item(self.treeview.selection())['values'][0]
            #print(h)
        except:
            print('9')






'''
https://es.stackoverflow.com/questions/356082/como-lograr-poner-may%C3%BAscula-en-los-campos-de-tipo-entry-y-formatear-n%C3%BAmeros-en-p
'''
class UpperEntry(Entry):
    def __init__(self, parent, *args, **kwargs):
        self._var = kwargs.get("textvariable") or StringVar(parent)
        super().__init__(parent, *args, **kwargs)
        self.configure(textvariable=self._var)
        self._to_upper()

    def config(self, cnf=None, **kwargs):
        self.configure(cnf, **kwargs)

    def configure(self, cnf=None, **kwargs):
        var = kwargs.get("textvariable")
        if var is not None:
            var.trace_add('write', self._to_upper)
            self._var = var
        super().config(cnf, **kwargs)

    def __setitem__(self, key, item):
        if key == "textvariable":
            item.trace_add('write', self._to_upper)
            self._var = item
        super.__setitem__(key, item)

    def _to_upper(self, *args):
        self._var.set(self._var.get().upper())