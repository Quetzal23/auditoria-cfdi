from tkinter import CENTER, E, EW, HORIZONTAL, LEFT, NSEW, RIGHT, VERTICAL, W, Label, LabelFrame, PhotoImage
from tkinter import ttk
import tkinter as tk

from views.styles import Style

from views.options import Window_Center, UpperEntry

class Parametro_Empresa(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        wind_width  = 900
        wind_height = 414

        wind = Window_Center(self)
        self.style = Style()

        self.geometry(wind.center(wind_width, wind_height))
        self.title('PARAMETROS DE EMPRESAS')
        self.resizable(0,0)
        self.protocol('WM_DELETE_WINDOW', self.on_closing)

        self.create_widgets()

    def on_closing(self):
        self.destroy()

    def create_widgets(self):
        self.frame_top()
        self.frame_left()
        self.frame_right()

    def frame_top(self):
        frame_top = LabelFrame(self, relief='flat')
        frame_top.grid(row=0, column=0, columnspan=2, sticky=NSEW)

        '''
        imgnew = self.image_button('images/buttons_icons/draft_FILL0_wght400_GRAD0_opsz48.png')
        imgsave = self.image_button('images/buttons_icons/save_FILL0_wght400_GRAD0_opsz48.png')
        imgedit = self.image_button('images/buttons_icons/edit_FILL0_wght400_GRAD0_opsz48.png')
        imgdele = self.image_button('images/buttons_icons/delete_FILL0_wght400_GRAD0_opsz48.png')
        imgsave = self.image_button('images/buttons_icons/save_FILL0_wght400_GRAD0_opsz48.png')
        imgwork = self.image_button('images/buttons_icons/domain_FILL0_wght400_GRAD0_opsz48.png')
        imgexit = self.image_button('images/buttons_icons/close_FILL0_wght400_GRAD0_opsz48.png')
        '''

        button_new = ttk.Button(frame_top, text='New', )  #, image=imgnew
        #button_new.grid(column=0, row=0, padx=5, pady=5, sticky=W)
        button_save = ttk.Button(frame_top, text='Save')    #, image=imgsave
        #button_save.grid(column=1, row=0, padx=5, pady=5, sticky=W)
        button_edit = ttk.Button(frame_top, text='Edit')    #, image=imgedit
        #button_edit.grid(column=2, row=0, padx=5, pady=5, sticky=W)
        button_delete = ttk.Button(frame_top, text='Delete')    #, image=imgdele
        #button_delete.grid(column=3, row=0, padx=5, pady=5, sticky=W)
        button_center = ttk.Button(frame_top, text='Centro de Trabajo') #, image=imgwork
        #button_center.grid(column=5, row=0, padx=5, pady=5, sticky=W)
        button_exit = ttk.Button(frame_top, text='Exit', command=self.on_closing)   #, image=imgexit
        #button_exit.grid(column=6, row=0, padx=5, pady=5, sticky=E)

        button_new.pack(side=LEFT, padx=5, pady=5,)
        button_save.pack(side=LEFT, padx=5, pady=5,)
        button_edit.pack(side=LEFT, padx=5, pady=5,)
        button_delete.pack(side=LEFT, padx=5, pady=5,)
        button_center.pack(side=LEFT, padx=5, pady=5,)
        button_exit.pack(side=RIGHT, padx=10, pady=5,)

    def frame_left(self):
        frame_left = LabelFrame(self, relief='flat')
        frame_left.grid(row=1, column=0, sticky=NSEW, padx=6)

        self.treeview = ttk.Treeview(frame_left, columns=2, height=14, style=self.style.Treeview())
        self.treeview.heading("#0", text='', anchor=CENTER)
        self.treeview.heading("#1", text='Empresa', anchor=CENTER)
        self.treeview.column('#0', stretch=False, width=0, minwidth=0)
        self.treeview.column('#1', stretch=False, width=300, minwidth=300)    #220
        self.treeview.grid(row=0, column=0, sticky="nsew")

        vscrollbar = ttk.Scrollbar(frame_left, orient=VERTICAL, command=self.treeview.yview)
        vscrollbar.grid(row=0, column=3, sticky="nse")
        self.treeview.configure(yscrollcommand=vscrollbar.set)

        hscrollbar = ttk.Scrollbar(frame_left, orient=HORIZONTAL, command=self.treeview.xview)
        hscrollbar.grid(row=1, column=0, sticky="ew")
        self.treeview.configure(xscrollcommand=hscrollbar.set)

        #self.treeview.insert('', '0', values=('Hola',))

    
    def frame_right(self):
        frame_right = LabelFrame(self, relief='flat')
        frame_right.grid(row=1, column=1, sticky=NSEW, padx=6)

        self.datos_generales(frame_right)
        Label(frame_right).grid(row=1)
        self.direccion(frame_right)

    def datos_generales(self, labelframe):
        frame = LabelFrame(labelframe, text='Datos Generales', relief='flat')
        frame.grid(row=0, column=0, sticky=NSEW, padx=6)

        nomEmpresa_label = Label(frame, text='Nombre de Empresa')
        nomEmpresa_label.grid(row=1, column=0, sticky=W, padx=2)
        self.nomEmpresa_entry = UpperEntry(frame)
        self.nomEmpresa_entry.grid(row=2, column=0, columnspan=3, sticky=EW, padx=2)
        #self.nomEmpresa_entry.config(state='disabled')

        nomCorto_label = Label(frame, text='Nombre corto')
        nomCorto_label.grid(row=3, column=0, sticky=W, padx=2)
        self.nomCorto_entry = UpperEntry(frame, width=28)
        self.nomCorto_entry.grid(row=4, column=0, sticky=W, padx=2)
        #self.nomCorto_entry.config(state='disabled')

        rfc_label = Label(frame, text='RFC')
        rfc_label.grid(row=3, column=1, sticky=W, padx=2)
        self.rfc_entry = UpperEntry(frame, width=28)
        self.rfc_entry.grid(row=4, column=1, sticky=W, padx=2)
        #self.rfc_entry.config(state='disabled')

        noPatronal_label = Label(frame, text='# Registro Patronal')
        noPatronal_label.grid(row=3, column=2, sticky=W, padx=2)
        self.noPatronal_entry = UpperEntry(frame, width=28)
        self.noPatronal_entry.grid(row=4, column=2, sticky=W, padx=2)
        #self.noPatronal_entry.config(state='disabled')

        actividadP_label = Label(frame, text='Datos Generales')
        actividadP_label.grid(row=5, column=0, sticky=W, padx=2)
        self.actividadP_entry = UpperEntry(frame)
        self.actividadP_entry.grid(row=6, column=0, columnspan=3, sticky=EW, padx=2)
        #self.actividadP_entry.config(state='disabled')

    def direccion(self, labelframe):
        frame = LabelFrame(labelframe, text='Dirección', relief='flat')
        frame.grid(row=2, column=0, sticky=NSEW, padx=6)

        calle_label = Label(frame, text='Calle')
        calle_label.grid(row=1, column=0, sticky=W, padx=2)
        self.calle_entry = UpperEntry(frame, width=28)
        self.calle_entry.grid(row=2, column=0, sticky=EW, padx=2)
        #self.calle_entry.config(state='disabled')

        numero_label = Label(frame, text='Número')
        numero_label.grid(row=1, column=1, sticky=W, padx=2)
        self.numero_entry = UpperEntry(frame, width=28)
        self.numero_entry.grid(row=2, column=1, sticky=W, padx=2)
        #self.numero_entry.config(state='disabled')

        colonia_label = Label(frame, text='Colonia')
        colonia_label.grid(row=1, column=2, sticky=W, padx=2)
        self.colonia_entry = UpperEntry(frame, width=28)
        self.colonia_entry.grid(row=2, column=2, sticky=W, padx=2)
        #self.colonia_entry.config(state='disabled')

        municipio_label = Label(frame, text='Delegación o Municipio')
        municipio_label.grid(row=3, column=0, sticky=W, padx=2)
        self.municipio_entry = UpperEntry(frame, width=28)
        self.municipio_entry.grid(row=4, column=0, sticky=EW, padx=2)
        #self.municipio_entry.config(state='disabled')

        postal_label = Label(frame, text='Código Postal')
        postal_label.grid(row=3, column=1, sticky=W, padx=2)
        self.postal_entry = UpperEntry(frame, width=28)
        self.postal_entry.grid(row=4, column=1, sticky=EW, padx=2)
        #self.postal_entry.config(state='disabled')

        federativa_label = Label(frame, text='Entidad Federativa')
        federativa_label.grid(row=3, column=2,  sticky=W, padx=2)
        self.federativa_entry = UpperEntry(frame, width=24)
        self.federativa_entry.grid(row=4, column=2, sticky=EW, padx=2)
        #self.federativa_entry.config(state='disabled')

        poblacion_label = Label(frame, text='Población')
        poblacion_label.grid(row=5, column=0,  sticky=W, padx=2)
        self.poblacion_entry = UpperEntry(frame, width=24)
        self.poblacion_entry.grid(row=6, column=0, sticky=EW, padx=2)
        #self.poblacion_entry.config(state='disabled')

        telefono_label = Label(frame, text='Teléfono(s)')
        telefono_label.grid(row=5, column=1,  sticky=W, padx=2)
        self.telefono_entry = UpperEntry(frame, width=24)
        self.telefono_entry.grid(row=6, column=1, sticky=EW, padx=2)
        #self.telefono_entry.config(state='disabled')

    '''
    def image_button(self, imgpath):
        self.img = PhotoImage(file=imgpath)
        self.img = self.img.zoom(2)
        self.img = self.img.subsample(3)
        return self.img
    '''

