from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import Treeview

class Parametros_Empresas:
    def __init__(self, window):
        self.wind = window
        self.wind.title('PARAMETROS DE EMPRESAS')
        self.wind.geometry('750x412')
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
        self.button_edit = Button(frame_top, text='Edit', state='disabled')
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
        treeview = Treeview(frame_left, columns=2, height=16)
        treeview.heading("#0", text='', anchor=CENTER)
        treeview.heading("#1", text='Empresas', anchor=CENTER)
        treeview.column('#0', stretch=False, width=20)
        treeview.column('#1', stretch=False, width=220)
        treeview.grid(row=0, column=0, columnspan=2, sticky="nsew")
        scrollbar = Scrollbar(frame_left, orient=VERTICAL, command=treeview.yview)
        scrollbar.grid(row=0, column=3, sticky="nse")
        treeview.configure(yscrollcommand=scrollbar.set)

        frame_right = LabelFrame(parametros, relief='flat')
        frame_right.grid(row=1, column=1, padx=0, pady=0, sticky=NSEW)

        frame_datos = LabelFrame(frame_right, text='Datos Generales', relief='flat')
        frame_datos.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        # Datos genarales         [row=1, column=1]
        space = Label(frame_datos, text='')
        space.grid(column=0, row=0, pady=1, columnspan=3, sticky=EW)
        nombreE_label = Label(frame_datos, text='Nombre de Empresa')
        nombreE_label.grid(row=1, column=0, sticky=W, padx=2)
        self.nombreE_entry = Entry(frame_datos, state='disabled')
        self.nombreE_entry.grid(row=2, column=0, columnspan=3, sticky=EW, padx=2)
        nombreC_label = Label(frame_datos, text='Nombre corto')
        nombreC_label.grid(row=3, column=0, sticky=W, padx=2)
        self.nombreC_entry = Entry(frame_datos, width=24, state='disabled')
        self.nombreC_entry.grid(row=4, column=0, sticky=W, padx=2)
        rfc_label = Label(frame_datos, text='RFC')
        rfc_label.grid(row=3, column=1, sticky=W, padx=2)
        self.rfc_entry = Entry(frame_datos, width=24, state='disabled')
        self.rfc_entry.grid(row=4, column=1, sticky=W, padx=2)
        patronal_label = Label(frame_datos, text='# Registro Patronal')
        patronal_label.grid(row=3, column=2, sticky=W, padx=2)
        self.patronal_entry = Entry(frame_datos, width=24, state='disabled')
        self.patronal_entry.grid(row=4, column=2, sticky=W, padx=2)
        actividad_label = Label(frame_datos, text='Datos Generales')
        actividad_label.grid(row=5, column=0,  sticky=W, padx=2)
        self.actividad_entry = Entry(frame_datos, state='disabled')
        self.actividad_entry.grid(row=6, column=0, columnspan=3, sticky=EW, padx=2)

        space = Label(frame_right, text='')
        space.grid(row=1, column=0, pady=1, columnspan=3, sticky=EW)

        frame_direccion = LabelFrame(frame_right, text='Dirección', relief='flat')
        frame_direccion.grid(row=2, column=0, columnspan=2, sticky=NSEW)
        space = Label(frame_direccion, text='')
        space.grid(row=0, column=0, pady=1, columnspan=3, sticky=EW)
        calle_label = Label(frame_direccion, text='Calle')
        calle_label.grid(row=1, column=0,  sticky=W, padx=2)
        self.calle_entry = Entry(frame_direccion, width=24, state='disabled')
        self.calle_entry.grid(row=2, column=0, sticky=EW, padx=2)
        numero_label = Label(frame_direccion, text='Número')
        numero_label.grid(row=1, column=1,  sticky=W, padx=2)
        self.numero_entry = Entry(frame_direccion, width=24, state='disabled')
        self.numero_entry.grid(row=2, column=1, sticky=W, padx=2)
        colonia_label = Label(frame_direccion, text='Colonia')
        colonia_label.grid(row=1, column=2,  sticky=W, padx=2)
        self.colonia_entry = Entry(frame_direccion, width=24, state='disabled')
        self.colonia_entry.grid(row=2, column=2, sticky=W, padx=2)
        municipio_label = Label(frame_direccion, text='Delegación o Municipio')
        municipio_label.grid(row=3, column=0,  sticky=W, padx=2)
        self.municipio_entry = Entry(frame_direccion, width=24, state='disabled')
        self.municipio_entry.grid(row=4, column=0, sticky=EW, padx=2)
        postal_label = Label(frame_direccion, text='Código Postal')
        postal_label.grid(row=3, column=1,  sticky=W, padx=2)
        self.postal_entry = Entry(frame_direccion, width=24, state='disabled')
        self.postal_entry.grid(row=4, column=1, sticky=EW, padx=2)
        federativa_label = Label(frame_direccion, text='Entidad Federativa')
        federativa_label.grid(row=3, column=2,  sticky=W, padx=2)
        self.federativa_entry = Entry(frame_direccion, width=24, state='disabled')
        self.federativa_entry.grid(row=4, column=2, sticky=EW, padx=2)
        poblacion_label = Label(frame_direccion, text='Población')
        poblacion_label.grid(row=5, column=0,  sticky=W, padx=2)
        self.poblacion_entry = Entry(frame_direccion, width=24, state='disabled')
        self.poblacion_entry.grid(row=6, column=0, sticky=EW, padx=2)
        telefono_label = Label(frame_direccion, text='Teléfono(s)')
        telefono_label.grid(row=5, column=1,  sticky=W, padx=2)
        self.telefono_entry = Entry(frame_direccion, width=24, state='disabled')
        self.telefono_entry.grid(row=6, column=1, sticky=EW, padx=2)
        '''
        fax_label = Label(frame_direccion, text='Fax')
        fax_label.grid(row=5, column=2,  sticky=W, padx=2)
        self.fax_entry = Entry(frame_direccion, width=24, state='disabled')
        self.fax_entry.grid(row=6, column=2, sticky=EW, padx=2)
        '''

    def entry_new(self):
        self.button_save['state'] = 'normal'
        #
        self.nombreE_entry['state'] = 'normal'
        self.nombreC_entry['state'] = 'normal'
        self.rfc_entry['state'] = 'normal'
        self.patronal_entry['state'] = 'normal'
        self.actividad_entry['state'] = 'normal'

        self.calle_entry['state'] = 'normal'
        self.numero_entry['state'] = 'normal'
        self.colonia_entry['state'] = 'normal'
        self.municipio_entry['state'] = 'normal'
        self.postal_entry['state'] = 'normal'
        self.federativa_entry['state'] = 'normal'
        self.poblacion_entry['state'] = 'normal'
        self.telefono_entry['state'] = 'normal'
        #self.fax_entry['state'] = 'normal'

    def validation(self):
        return len(self.nombreE_entry.get()) != 0

    def form_warning(self):
        showwarning('Guardar', 
            'Llene el formulario antes de guardar')

    def entry_save(self):
        self.button_save['state'] = 'disabled'
        #
        if self.validation():
            print('OK')
        
        else:
            self.form_warning()
            
        #
        self.nombreE_entry['state'] = 'disabled'
        self.nombreC_entry['state'] = 'disabled'
        self.rfc_entry['state'] = 'disabled'
        self.patronal_entry['state'] = 'disabled'
        self.actividad_entry['state'] = 'disabled'

        self.calle_entry['state'] = 'disabled'
        self.numero_entry['state'] = 'disabled'
        self.colonia_entry['state'] = 'disabled'
        self.municipio_entry['state'] = 'disabled'
        self.postal_entry['state'] = 'disabled'
        self.federativa_entry['state'] = 'disabled'
        self.poblacion_entry['state'] = 'disabled'
        self.telefono_entry['state'] = 'disabled'
        #self.fax_entry['state'] = 'disabled'