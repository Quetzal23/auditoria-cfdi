from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview

from view.upperentry import UpperEntry

class Catalogo_Trabajadores:
    def __init__(self, window):
        wind_width  = 884
        wind_height = 538
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
        self.widget_search(parametros)
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

    def widget_search(self, parametros):
        self.opcion = IntVar()
        self.buscar = IntVar()

        frame_top = LabelFrame(parametros, relief='flat')
        frame_top.grid(row=1, column=0, columnspan=2, sticky=NSEW)

        self.activos = Radiobutton(frame_top, text='Activos', variable=self.opcion, value=1, )
        self.activos.grid(row=0, column=0, sticky=W)
        self.todos = Radiobutton(frame_top, text='Todos', variable=self.opcion, value=2, )
        self.todos.grid(row=0, column=1, sticky=W)

        label = Label(frame_top, width=3)
        label.grid(row=0, column=3, sticky=W)

        label = Label(frame_top, text='Buscar Trabajador por: ' )
        label.grid(row=0, column=4, sticky=W, padx=2)
        self.numero = Radiobutton(frame_top, text='Numero', variable=self.buscar, value=1, )
        self.numero.grid(row=0, column=5, sticky=W)
        self.apellido = Radiobutton(frame_top, text='Apellido Paterno', variable=self.buscar, value=2, )
        self.apellido.grid(row=0, column=6, sticky=W)
        self.nss = Radiobutton(frame_top, text='NSS', variable=self.buscar, value=3, )
        self.nss.grid(row=0, column=7, sticky=W)
        self.buscar_entry = UpperEntry(frame_top, width=54)
        self.buscar_entry.grid(row=0, column=8, sticky=W, padx=2)

    def widget_frame_treeview(self, parametros):
        frame_left = LabelFrame(parametros, relief='flat')
        frame_left.grid(row=2, column=0, padx=0, pady=0, sticky=NSEW)

        self.treeview = Treeview(frame_left, columns=[f"#{n}" for n in range(0, 2)], height=20) #columns=[f"#{n}" for n in range(0, 2)],
        self.treeview.heading("#0", text='', anchor=CENTER)
        self.treeview.heading("#1", text='Clave', anchor=CENTER)
        self.treeview.heading("#2", text='Trabajador', anchor=CENTER)

        self.treeview.column('#0', stretch=False, width=0, minwidth=0)
        self.treeview.column('#1', stretch=False, width=90, minwidth=90)    #220
        self.treeview.column('#2', stretch=False, width=280, minwidth=280)
        #self.treeview.config(show='headings')
        self.treeview.grid(row=0, column=0, columnspan=2, sticky="nsew")

        scrollbar = Scrollbar(frame_left, orient=VERTICAL, command=self.treeview.yview)
        scrollbar.grid(row=0, column=3, sticky="nse")
        self.treeview.configure(yscrollcommand=scrollbar.set)
        sc = Scrollbar(frame_left, orient=HORIZONTAL, command=self.treeview.xview)
        sc.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.treeview.configure(xscrollcommand=sc.set)

    def widget_frame_datos(self, parametros):
        frame_right = LabelFrame(parametros, relief='flat')
        frame_right.grid(row=2, column=1, padx=0, pady=0, sticky=NSEW)

        self.w_datos_generales(frame_right)
        nombreE_label = Label(frame_right,)
        nombreE_label.grid(row=1, column=0, sticky=W, padx=2, pady=1)
        self.w_datos(frame_right)

    def w_datos_generales(self, frame):
        frame_datos = LabelFrame(frame, relief='flat')
        frame_datos.grid(row=0, column=0, sticky=NSEW)

        numTrabajador_label = Label(frame_datos, text='Num. Trabajador')
        numTrabajador_label.grid(row=0, column=0, sticky=W, padx=2)
        self.numTrabajador_entry = UpperEntry(frame_datos, width=24)
        self.numTrabajador_entry.grid(row=1, column=0, sticky=EW, padx=2)

        apellidoP_label = Label(frame_datos, text='Apellido Paterno')
        apellidoP_label.grid(row=0, column=1, sticky=W, padx=2)
        self.apellidoP_entry = UpperEntry(frame_datos, width=24)
        self.apellidoP_entry.grid(row=1, column=1, sticky=EW, padx=2)
        
        apellidoM_label = Label(frame_datos, text='Apellido Materno')
        apellidoM_label.grid(row=0, column=2, sticky=W, padx=2)
        self.apellidoM_entry = UpperEntry(frame_datos, width=24)
        self.apellidoM_entry.grid(row=1, column=2, sticky=EW, padx=2)

        nombreT_label = Label(frame_datos, text='Nombre Trabajador')
        nombreT_label.grid(row=2, column=0, sticky=W, padx=2)
        self.nombreT_entry = UpperEntry(frame_datos, width=24)
        self.nombreT_entry.grid(row=3, column=0, sticky=EW, padx=2)

        faltaNom_label = Label(frame_datos, text='Fecha Alta Nómina')
        faltaNom_label.grid(row=2, column=1, sticky=W, padx=2)
        self.faltaNom_entry = UpperEntry(frame_datos, width=24)
        self.faltaNom_entry.grid(row=3, column=1, sticky=EW, padx=2)

        faltaLiq_label = Label(frame_datos, text='Fecha Alta Liq.')
        faltaLiq_label.grid(row=2, column=2, sticky=W, padx=2)
        self.faltaLiq_entry = UpperEntry(frame_datos, width=24)
        self.faltaLiq_entry.grid(row=3, column=2, sticky=EW, padx=2)

        cuotad_label = Label(frame_datos, text='Cuota Diaria')
        cuotad_label.grid(row=4, column=0, sticky=W, padx=2)
        self.cuotad_entry = UpperEntry(frame_datos, width=24)
        self.cuotad_entry.grid(row=5, column=0, sticky=EW, padx=2)

        sexo_label = Label(frame_datos, text='Sexo')
        sexo_label.grid(row=4, column=1, sticky=W, padx=2)
        self.sexo_entry = ttk.Combobox(frame_datos,)
        self.sexo_entry.grid(row=5, column=1, sticky=EW, padx=2, )

        tNomina_label = Label(frame_datos, text='Tipo Nómina')
        tNomina_label.grid(row=4, column=2, sticky=W, padx=2)
        self.tNomina_entry = ttk.Combobox(frame_datos,)
        self.tNomina_entry.grid(row=5, column=2, sticky=EW, padx=2, )

        turno_label = Label(frame_datos, text='Turno')
        turno_label.grid(row=6, column=0, sticky=W, padx=2)
        self.turno_entry = ttk.Combobox(frame_datos,)
        self.turno_entry.grid(row=7, column=0, sticky=EW, padx=2, )

        categoria_label = Label(frame_datos, text='Categoría')
        categoria_label.grid(row=6, column=1, sticky=W, padx=2)
        self.categoria_entry = ttk.Combobox(frame_datos,)
        self.categoria_entry.grid(row=7, column=1, sticky=EW, columnspan=2, padx=2, )

        pensionadoN_label = Label(frame_datos, text='Pensionado Nómina')
        pensionadoN_label.grid(row=8, column=0, sticky=W, padx=2)
        self.pensionadoN_entry = ttk.Combobox(frame_datos,)
        self.pensionadoN_entry.grid(row=9, column=0,sticky=EW, padx=2, )

        pensionadoL_label = Label(frame_datos, text='Pensionado Liquidación')
        pensionadoL_label.grid(row=8, column=1, sticky=W, padx=2)
        self.pensionadoL_entry = ttk.Combobox(frame_datos,)
        self.pensionadoL_entry.grid(row=9, column=1, sticky=EW, padx=2, )

    def w_datos(self, frame):
        frame_datos = LabelFrame(frame, relief='flat')
        frame_datos.grid(row=2, column=0, columnspan=2, sticky=NSEW)

        calle_label = Label(frame_datos, text='Calle')
        calle_label.grid(row=1, column=0,  sticky=W, padx=2)

        notebook = ttk.Notebook(frame_datos)
        notebook.grid(row=2, column=0, sticky=NSEW)

        p1 = ttk.Frame(notebook)
        p2 = ttk.Frame(notebook)
        p3 = ttk.Frame(notebook)
        p4 = ttk.Frame(notebook)

        self.datos_imss(p1)

        notebook.add(p1, text='I.M.S.S')
        notebook.add(p2, text='Amortización Nomina')
        notebook.add(p3, text='Amortización Liquidación')
        notebook.add(p4, text='Afiliación')

    def datos_imss(self, frame):
        frame_imss = LabelFrame(frame, relief='flat')
        frame_imss.grid(row=0, column=0, columnspan=2, sticky=NSEW)

        nss = Label(frame_imss, text='N.S.S')
        nss.grid(row=1, column=0, sticky=W, padx=2)
        self.nss_entry = UpperEntry(frame_imss, width=24)
        self.nss_entry.grid(row=2, column=0, sticky=W, padx=2,)

        rfc = Label(frame_imss, text='R.F.C')
        rfc.grid(row=1, column=1, sticky=W, padx=2)
        self.rfc_entry = UpperEntry(frame_imss, width=24)
        self.rfc_entry.grid(row=2, column=1, sticky=W, padx=2,)
        
        curp = Label(frame_imss, text='C.U.R.P')
        curp.grid(row=1, column=2, sticky=W, padx=2)
        self.curp_entry = UpperEntry(frame_imss, width=24)
        self.curp_entry.grid(row=2, column=2, sticky=W, padx=2,)

        trabajador = Label(frame_imss, text='Tipo de Trabajo')
        trabajador.grid(row=3, column=0, sticky=W, padx=2)
        self.trabajador_entry = ttk.Combobox(frame_imss, )
        self.trabajador_entry.grid(row=4, column=0, sticky=EW, padx=2, )

        reducir = Label(frame_imss, text='Jor o Sem Reducida')
        reducir.grid(row=3, column=1, sticky=W, padx=2)
        self.reducir_entry = ttk.Combobox(frame_imss, )
        self.reducir_entry.grid(row=4, column=1, sticky=EW, padx=2, )
        
        semanaRed = Label(frame_imss, text='Ocupación')
        semanaRed.grid(row=3, column=2, sticky=W, padx=2)
        self.semanaRed_entry = ttk.Combobox(frame_imss, )
        self.semanaRed_entry.grid(row=4, column=2, sticky=EW, padx=2, )

        tipoSalario = Label(frame_imss, text='Tipo de Salario')
        tipoSalario.grid(row=5, column=0, sticky=W, padx=2)
        self.tipoSalario_entry = ttk.Combobox(frame_imss, )
        self.tipoSalario_entry.grid(row=6, column=0, sticky=EW, padx=2, )

        departamento = Label(frame_imss, text='Departamento')
        departamento.grid(row=5, column=1, sticky=W, padx=2)
        self.departamento_entry = ttk.Combobox(frame_imss, )
        self.departamento_entry.grid(row=6, column=1, sticky=EW, padx=2, )