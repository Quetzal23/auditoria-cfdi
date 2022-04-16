from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.ttk import Treeview
from tkinter import filedialog as fd
import os.path
import pandas as pd
import xlrd

from view.upperentry import UpperEntry

class Catalogo_Centro:
    def __init__(self, window):
        wind_width  = 884
        wind_height = 417
        wind_geometry = str(wind_width) + 'x' + str(wind_height)
        self.wind = window
        self.wind.title('CATALOGO DE CENTROS')
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

    def widget_frame_treeview(self, parametros):
        frame_left = LabelFrame(parametros, relief='flat')
        frame_left.grid(row=1, column=0, padx=0, pady=0, sticky=NSEW)
        self.treeview = Treeview(frame_left, columns=2, height=16)
        self.treeview.heading("#0", text='', anchor=CENTER)
        self.treeview.heading("#1", text='Registro Patronal', anchor=CENTER)
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

        notebook = ttk.Notebook(frame_right)
        notebook.grid(row=2, column=0, sticky=NSEW)

        p1 = ttk.Frame(notebook)
        p2 = ttk.Frame(notebook)
        p3 = ttk.Frame(notebook)
        p4 = ttk.Frame(notebook)

        self.w_datos_generales(p1)
        self.w_direccion(p2)
        self.w_representante_legal(p3)
        self.w_configuracion_general(p4)

        notebook.add(p1, text='Datos Generales')
        notebook.add(p2, text='Dirección')
        notebook.add(p3, text='Representante Legal')
        notebook.add(p4, text='Configuración General')

    def w_datos_generales(self, frame):
        frame_datos = LabelFrame(frame, relief='flat')
        frame_datos.grid(row=0, column=0, columnspan=2, sticky=NSEW)

        patronal = Label(frame_datos, text='# Registro Patronal')
        patronal.grid(row=1, column=0, sticky=W, padx=2)
        self.patronal_entry = UpperEntry(frame_datos, width=38)
        self.patronal_entry.grid(row=2, column=0, sticky=W, padx=2, columnspan=2)

        finiciact = Label(frame_datos, text='Fecha Inicio de Act.')
        finiciact.grid(row=1, column=2, sticky=W, padx=2)
        self.finiciact_entry = UpperEntry(frame_datos, width=28)
        self.finiciact_entry.grid(row=2, column=2, sticky=W, padx=2)

        contador = Label(frame_datos, text='Contador Público')
        contador.grid(row=3, column=0, sticky=W, padx=2)
        self.contador_entry = ttk.Combobox(frame_datos,)
        self.contador_entry.grid(row=4, column=0, sticky=EW, padx=2, columnspan=2)

        finicioaud = Label(frame_datos, text='Fecha Inicio de Aud.')
        finicioaud.grid(row=5, column=0, sticky=W, padx=2)
        self.finicioaud_entry = UpperEntry(frame_datos, width=28)
        self.finicioaud_entry.grid(row=6, column=0, sticky=W, padx=2)

        ffincioaud = Label(frame_datos, text='Fecha Fin de Aud.')
        ffincioaud.grid(row=5, column=1, sticky=W, padx=2)
        self.ffincioaud_entry = UpperEntry(frame_datos, width=28)
        self.ffincioaud_entry.grid(row=6, column=1, sticky=W, padx=2)

        felabdic = Label(frame_datos, text='Fecha de Elab. de Dictámen')
        felabdic.grid(row=5, column=2, sticky=W, padx=2)
        self.felabdic_entry = UpperEntry(frame_datos, width=28)
        self.felabdic_entry.grid(row=6, column=2, sticky=W, padx=2)

        actprincipal = Label(frame_datos, text='Actividades Principales')
        actprincipal.grid(row=7, column=0, sticky=W, padx=2)
        self.actprincipal_entry = UpperEntry(frame_datos)
        self.actprincipal_entry.grid(row=8, column=0, sticky=EW, padx=2, columnspan=3)

    def w_direccion(self, frame):
        pass

    def w_representante_legal(self, frame):
        frame_datos = LabelFrame(frame, relief='flat')
        frame_datos.grid(row=0, column=0, columnspan=2, sticky=NSEW)

        representante = Label(frame_datos, text='Representante Legal')
        representante.grid(row=1, column=0, sticky=W, padx=2)
        self.representante_entry = UpperEntry(frame_datos, )
        self.representante_entry.grid(row=2, column=0, sticky=EW, padx=2, columnspan=3)

        puesto = Label(frame_datos, text='Puesto')
        puesto.grid(row=3, column=0, sticky=W, padx=2)
        self.puesto_entry = UpperEntry(frame_datos, width=48)
        self.puesto_entry.grid(row=4, column=0, sticky=W, padx=2, )

        puesto = Label(frame_datos, text='Puesto')
        puesto.grid(row=3, column=1, sticky=W, padx=2)
        self.puesto_entry = UpperEntry(frame_datos, width=30)
        self.puesto_entry.grid(row=4, column=1, sticky=W, padx=2, )
        
        fnotarial = Label(frame_datos, text='Fecha Cert P. Notarial')
        fnotarial.grid(row=5, column=0, sticky=W, padx=2)
        self.fnotarial_entry = UpperEntry(frame_datos, width=28)
        self.fnotarial_entry.grid(row=6, column=0, sticky=W, padx=2, )

        nonotaria = Label(frame_datos, text='Numero de Notaria')
        nonotaria.grid(row=5, column=1, sticky=W, padx=2)
        self.nonotaria_entry = UpperEntry(frame_datos, width=28)
        self.nonotaria_entry.grid(row=6, column=1, sticky=W, padx=2, )

    def w_configuracion_general(self, frame):
        opcion = IntVar()

        frame_datos = LabelFrame(frame, text='Indique el formato que desee aplicar al No. de Trabajador del Centro', relief='flat')
        frame_datos.grid(row=0, column=0, columnspan=2, sticky=NSEW, pady=10)

        frame_radio = LabelFrame(frame_datos, width=80)
        frame_radio.grid(row=1, column=0, rowspan=2, padx=4, pady=2, sticky=NSEW) 
        self.numerico = Radiobutton(frame_radio, text='Numérico', variable=opcion, value=1, )
        self.numerico.grid(row=0, column=0, sticky=W)
        self.alfanumerico = Radiobutton(frame_radio, text='Alfanumérico', variable=opcion, value=2, )
        self.alfanumerico.grid(row=1, column=0, sticky=W)

        longitud = Label(frame_datos, text='Longitud')
        longitud.grid(row=1, column=1, sticky=W, padx=2)
        self.longitud_entry = UpperEntry(frame_datos, width=28)
        self.longitud_entry.grid(row=2, column=1, sticky=W, padx=2)

        ejemplo = Label(frame_datos, text='Ejemplo')
        ejemplo.grid(row=1, column=2, sticky=W, padx=2)
        ejemplo_entry = Label(frame_datos, text='99999999', width=18, justify=LEFT, anchor='w')
        ejemplo_entry.grid(row=2, column=2, sticky=W, padx=2)

        ntrabajo = Label(frame_datos, text='Nombre del Centro de Trabajo')
        ntrabajo.grid(row=3, column=0, sticky=W, padx=2)
        self.ntrabajo_entry = UpperEntry(frame_datos)
        self.ntrabajo_entry.grid(row=4, column=0, padx=2, sticky=EW, columnspan=2)

        dirdb = Label(frame_datos, text='Directorio de la Base de Datos')
        dirdb.grid(row=5, column=0, sticky=W, padx=2)
        self.dirdb_entry = UpperEntry(frame_datos)
        self.dirdb_entry.grid(row=6, column=0, sticky=EW, padx=2, columnspan=3)

        self.dirbutton = Button(frame_datos, text='Buscar', command=self.search)
        self.dirbutton.grid(row=6, column=4, padx=2, sticky=W)

    def search(self):
    
        file = self.dirdb_entry.get()
        self.searchExcel(file)


        '''
        filetypes = (
            ('Excel files', '*xlsx; *.xls'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
        #showinfo(title='Select File', message=filename)
        self.dirdb_entry.insert(0, filename)
        
        '''

    def searchExcel(self, filename):
        if not os.path.isfile(filename):
            showinfo(title='Select File', message=('Archivo: %s \nNo encontrado' % filename))
            return None
        
        with open(filename, 'r') as file:
            data = file.read().replace('\n', '')
        print(data)

        '''
        xls = pd.ExcelFile(file)
        sheets = xls.sheet_names
        results = {}
        for sheet in sheets:
            results[sheet] = xls.parse(sheet)
        xls.close()
        print(results)
        '''