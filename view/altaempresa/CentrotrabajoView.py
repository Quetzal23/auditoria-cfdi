from tkinter import CENTER, EW, HORIZONTAL, LEFT, NSEW, RIGHT, VERTICAL, W, IntVar, Label, LabelFrame, PhotoImage, Radiobutton, StringVar
from tkinter import ttk
from tkcalendar import *

from assets.options import Window_Center, UpperEntry
from assets.styles import Style

class CentroTrabajoView:
    def on_closing(self):
        self.root.destroy()

    def __init__(self, root, id_empresa):
        super().__init__()
        self.root = root
        self.id_e = id_empresa

        wind_width  = 898#900
        wind_height = 410#390

        wind = Window_Center(self.root)

        self.style = Style()
        self.color_normal = self.style.color__normal
        self.color_danger = self.style.color__danger
        self.color_success = self.style.color__success
        self.color_title = self.style.color__title

        self.font = self.style.font

        self.Treeview = self.style.Treeview()

        self.root.grab_set()
        self.root.focus_force()

        self.root.geometry(wind.center(wind_width, wind_height))
        self.root.title('CATALOGOS DE CENTROS - ')
        self.root.resizable(0, 0)
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)

        self.create_widgets()


    def create_icon(self):
        self.img1 = self.image_button(PhotoImage(file='assets/images/button/draft_FILL0_wght400_GRAD0_opsz48.png'))
        self.img2 = self.image_button(PhotoImage(file='assets/images/button/save_FILL0_wght400_GRAD0_opsz48.png'))
        self.img3 = self.image_button(PhotoImage(file='assets/images/button/edit_FILL0_wght400_GRAD0_opsz48.png'))
        self.img4 = self.image_button(PhotoImage(file='assets/images/button/delete_FILL0_wght400_GRAD0_opsz48.png'))
        self.img5 = self.image_button(PhotoImage(file='assets/images/button/print_FILL0_wght400_GRAD0_opsz48.png'))
        self.img6 = self.image_button(PhotoImage(file='assets/images/button/close_FILL0_wght400_GRAD0_opsz48.png'))
    
    def image_button(self, imgpath):
        img = imgpath
        img = img.zoom(2)
        img = img.subsample(3)
        return img

    def create_widgets(self):
        self.frame_top()
        self.frame_left()
        self.frame_right()

    def frame_top(self):
        self.create_icon()

        frame_top = LabelFrame(self.root, relief='flat')
        frame_top.pack(fill='both')

        self.btn_new = ttk.Button(frame_top, text='New', image=self.img1,)
        self.btn_save = ttk.Button(frame_top, text='Save', image=self.img2,)
        self.btn_edit = ttk.Button(frame_top, text='Edit', image=self.img3)
        self.btn_delete = ttk.Button(frame_top, text='Delete', image=self.img4)
        self.btn_center = ttk.Button(frame_top, text='Print', image=self.img5)
        self.btn_exit = ttk.Button(frame_top, text='Exit', image=self.img6, command=self.on_closing)
        self.msg_label = Label(frame_top, text='', width=50, anchor='e')

        self.btn_new.pack(side=LEFT, padx=4, pady=4,)
        self.btn_save.pack(side=LEFT, padx=4, pady=4,)
        self.btn_edit.pack(side=LEFT, padx=4, pady=4,)
        self.btn_delete.pack(side=LEFT, padx=4, pady=4,)
        self.btn_center.pack(side=LEFT, padx=4, pady=4,)
        self.btn_exit.pack(side=RIGHT, padx=4, pady=4,)
        self.msg_label.pack(side=RIGHT, padx=4, pady=4,)

    def frame_left(self):
        frame_left = LabelFrame(self.root, relief='flat')
        frame_left.pack(side='left', fill='y')

        frame = Label(frame_left, bg=self.color_normal)
        frame.grid(row=0, column=0, sticky="nsew", padx=6)

        self.treeview = ttk.Treeview(frame, height=15, style=self.Treeview)
        self.treeview['columns'] = ('Emp', )
        self.treeview.heading('#0', text='', anchor=CENTER)
        self.treeview.heading('Emp', text='Reg. Patronal', anchor=CENTER)
        self.treeview.column('#0', stretch=False, width=0, minwidth=0)
        self.treeview.column('Emp', stretch=False, width=300, minwidth=300)

        vscrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=vscrollbar.set)

        hscrollbar = ttk.Scrollbar(frame, orient=HORIZONTAL, command=self.treeview.xview)
        self.treeview.configure(xscrollcommand=hscrollbar.set)

        self.treeview.grid(row=0, column=0, sticky="nsew")
        
        vscrollbar.grid(row=0, column=3, sticky="nse")
        hscrollbar.grid(row=1, column=0, sticky="ew")

    def frame_right(self):
        frame_right = LabelFrame(self.root, relief='flat')
        frame_right.pack(fill='y',)

        frame = Label(frame_right,) # bg=self.color_normal
        frame.grid(row=0, column=0, sticky="nsew", padx=6, ipady=32)

        notebook = ttk.Notebook(frame)

        self.l1 = LabelFrame(notebook, relief='flat')
        self.l2 = LabelFrame(notebook, relief='flat')
        self.l3 = LabelFrame(notebook, relief='flat')
        self.l4 = LabelFrame(notebook, relief='flat') #, background='#FFFFFF'

        notebook.add(self.l1, text="Datos Generales", compound='center')
        notebook.add(self.l2, text="Dirección")
        notebook.add(self.l3, text="Representante Legal")
        notebook.add(self.l4, text="Configuración General") #, padding=4

        self.style.TNotebook_Tab()
        notebook.pack(fill='both', expand=True, ipadx=0, ipady=0)

        self.datos_generales()
        self.direccion()
        self.representante_legal()
        self.configuracion_general()

    def datos_generales(self):
        _label_1 = ttk.Label(self.l1, text='# Registro Patronal', anchor='w', width=22)
        _label_2 = Label(self.l1, text='Fecha Inicio de Act', anchor='w', width=22)
        _label_3 = Label(self.l1, text='Contador Público', anchor='w', width=22)
        #_label_4 = Label(self.l1, text='Nombre Representante legal', anchor='w', width=22)
        _label_5 = Label(self.l1, text='Fecha Inicio de Aud.', anchor='w', width=22)
        _label_6 = Label(self.l1, text='Fecha Fin de Aud.', anchor='w', width=22)
        _label_7 = Label(self.l1, text='Fecha de Elab. de Dictámen', anchor='w', width=22)
        _label_8 = Label(self.l1, text='Actividades Principales', anchor='w')


        self.lbl1 = Label(self.l1, bg=self.color_normal)
        self.lbl2 = Label(self.l1, bg=self.color_normal)
        self.lbl3 = Label(self.l1, bg=self.color_normal)
        #self.lbl4 = Label(self.l1, bg=self.color_normal)
        self.lbl5 = Label(self.l1, bg=self.color_normal)
        self.lbl6 = Label(self.l1, bg=self.color_normal)
        self.lbl7 = Label(self.l1, bg=self.color_normal)
        self.lbl8 = Label(self.l1, bg=self.color_normal)

        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()
        self.var5 = StringVar()
        self.var6 = StringVar()
        self.var7 = StringVar()
        self.var8 = StringVar()

        self.regPtrl_entry = UpperEntry(self.lbl1)
        self.fIniAct_entry = DateEntry(self.lbl2, selectmode='day')
        self.contPub_entry = UpperEntry(self.lbl3)

        self.fIniAud_entry = DateEntry(self.lbl5, selectmode='day')
        self.fFinAud_entry = DateEntry(self.lbl6, selectmode='day')
        self.fElabDi_entry = DateEntry(self.lbl7, selectmode='day')
        self.actPrin_entry = UpperEntry(self.lbl8)

        a1 = Label(self.l1, text='*', fg=self.color_danger, font=(self.font, 13, 'bold'))
        a2 = Label(self.l1, text='*', fg=self.color_danger, font=(self.font, 13, 'bold'))
        #a3 = Label(self.l1, text='*', fg=self.color_danger, font=(self.font, 13, 'bold'))
        a4 = Label(self.l1, text='*', fg=self.color_danger, font=(self.font, 13, 'bold'))
        a5 = Label(self.l1, text='*', fg=self.color_danger, font=(self.font, 13, 'bold'))
        a6 = Label(self.l1, text=' ', fg=self.color_danger, font=(self.font, 13, 'bold'))
        #a7 = Label(self.l1, text='*', fg=self.color_danger, font=(self.font, 13, 'bold'))
        #a8 = Label(self.l1, text='*', fg=self.color_danger, font=(self.font, 13, 'bold'))
        
        _label_1.grid(row=0, column=0, padx=2, sticky=EW)
        _label_2.grid(row=0, column=2, padx=2, sticky=EW)
        _label_3.grid(row=2, column=0, padx=2, sticky=EW)
        #_label_4.grid(row=2, column=1, padx=2, sticky=EW)
        _label_5.grid(row=4, column=0, padx=2, sticky=EW)
        _label_6.grid(row=4, column=2, padx=2, sticky=EW)
        _label_7.grid(row=4, column=4, padx=2, sticky=EW)
        _label_8.grid(row=6, column=0, padx=2, sticky=EW)

        self.lbl1.grid(row=1, column=0, padx=2, sticky=NSEW)
        self.lbl2.grid(row=1, column=2, padx=2, sticky=NSEW)
        self.lbl3.grid(row=3, column=0, padx=2, sticky=NSEW)
        #self.lbl4.grid(row=3, column=1, padx=2, sticky=NSEW)
        self.lbl5.grid(row=5, column=0, padx=2, sticky=NSEW)
        self.lbl6.grid(row=5, column=2, padx=2, sticky=NSEW)
        self.lbl7.grid(row=5, column=4, padx=2, sticky=NSEW)
        self.lbl8.grid(row=7, column=0, padx=2, sticky=NSEW, columnspan=5)

        a1.grid(row=1, column=1)
        a2.grid(row=1, column=3)
        a4.grid(row=5, column=1)
        a5.grid(row=5, column=3)
        a6.grid(row=5, column=5)

        self.regPtrl_entry.pack(fill='both')
        self.fIniAct_entry.pack(fill='both')
        self.contPub_entry.pack(fill='both')

        self.fIniAud_entry.pack(fill='both')
        self.fFinAud_entry.pack(fill='both')
        self.fElabDi_entry.pack(fill='both')
        self.actPrin_entry.pack(fill='both')


    def direccion(self):
        _label_9 = Label(self.l2, text='Calle', width=34, anchor='w')
        _label_10 = Label(self.l2, text='Número', width=34, anchor='w')
        _label_11 = Label(self.l2, text='Colonia', width=24, anchor='w')
        _label_12 = Label(self.l2, text='Delegación o Municipio', width=24, anchor='w')
        _label_13 = Label(self.l2, text='Código Postal', width=24, anchor='w')
        _label_14 = Label(self.l2, text='Entidad Federativa', width=24, anchor='w')
        _label_15 = Label(self.l2, text='Población', width=24, anchor='w')
        _label_16 = Label(self.l2, text='Teléfono(s)', width=24, anchor='w')

        self.lbl9 = Label(self.l2, bg=self.color_normal)
        self.lbl10 = Label(self.l2, bg=self.color_normal)
        self.lbl11 = Label(self.l2, bg=self.color_normal)
        self.lbl12 = Label(self.l2, bg=self.color_normal)
        self.lbl13 = Label(self.l2, bg=self.color_normal)
        self.lbl14 = Label(self.l2, bg=self.color_normal)
        self.lbl15 = Label(self.l2, bg=self.color_normal)
        self.lbl16 = Label(self.l2, bg=self.color_normal)
        
        self.var9 = StringVar()
        self.var10 = StringVar()
        self.var11 = StringVar()
        self.var12 = StringVar()
        self.var13 = StringVar()
        self.var14 = StringVar()
        self.var15 = StringVar()
        self.var16 = StringVar()

        self.calle_entry = UpperEntry(self.lbl9, textvariable=self.var9)
        self.num_entry = UpperEntry(self.lbl10, textvariable=self.var10)
        self.col_entry = UpperEntry(self.lbl11, textvariable=self.var11)
        self.mpio_entry = UpperEntry(self.lbl12, textvariable=self.var12)
        self.cp_entry = ttk.Entry(self.lbl13, textvariable=self.var13, validate="key")
        self.entFed_entry = UpperEntry(self.lbl14, textvariable=self.var14)
        self.pob_entry = UpperEntry(self.lbl15, textvariable=self.var15)
        self.tel_entry = UpperEntry(self.lbl16, textvariable=self.var16)

        a9 = Label(self.l2, text='*', fg=self.color_danger, font=(self.font, 13, 'bold'))
        a10 = Label(self.l2, text='*', fg=self.color_danger, font=(self.font, 13, 'bold'))
        a11 = Label(self.l2, text='*', fg=self.color_danger, font=(self.font, 13, 'bold'))
        a12 = Label(self.l2, text='*', fg=self.color_danger, font=(self.font, 13, 'bold'))
        a13 = Label(self.l2, text='*', fg=self.color_danger, font=(self.font, 13, 'bold'))
        a14 = Label(self.l2, text='*', fg=self.color_danger, font=(self.font, 13, 'bold'))
        a15 = Label(self.l2, text='*', fg=self.color_danger, font=(self.font, 13, 'bold'))
        a16 = Label(self.l2, text='*', fg=self.color_danger, font=(self.font, 13, 'bold'))

        _label_9.grid(row=1, column=0, sticky=W, padx=2)
        _label_10.grid(row=1, column=2, sticky=W, padx=2)
        _label_11.grid(row=3, column=0, sticky=W, padx=2)
        _label_12.grid(row=3, column=2, sticky=W, padx=2)
        _label_13.grid(row=5, column=0, sticky=W, padx=2)
        _label_14.grid(row=5, column=2,  sticky=W, padx=2)
        _label_15.grid(row=7, column=0,  sticky=W, padx=2)
        _label_16.grid(row=7, column=2,  sticky=W, padx=2)

        self.lbl9.grid(row=2, column=0, sticky=EW, padx=2)
        self.lbl10.grid(row=2, column=2, sticky=EW, padx=2)
        self.lbl11.grid(row=4, column=0, sticky=EW, padx=2)
        self.lbl12.grid(row=4, column=2, sticky=EW, padx=2)
        self.lbl13.grid(row=6, column=0, sticky=EW, padx=2)
        self.lbl14.grid(row=6, column=2, sticky=EW, padx=2)
        self.lbl15.grid(row=8, column=0, sticky=EW, padx=2)
        self.lbl16.grid(row=8, column=2, sticky=EW, padx=2)
        
        a9.grid(row=2, column=1)
        a10.grid(row=2, column=3)
        a11.grid(row=4, column=1)
        a12.grid(row=4, column=3)
        a13.grid(row=6, column=1)
        a14.grid(row=6, column=3)
        a15.grid(row=8, column=1)
        a16.grid(row=8, column=3)

        self.calle_entry.pack(fill='both')
        self.num_entry.pack(fill='both')
        self.col_entry.pack(fill='both')
        self.mpio_entry.pack(fill='both')
        self.cp_entry.pack(fill='both')
        self.entFed_entry.pack(fill='both')
        self.pob_entry.pack(fill='both')
        self.tel_entry.pack(fill='both')


    def representante_legal(self):
        _label_17 = Label(self.l3, text='Nombre Representante Legal', width=34, anchor='w')
        _label_18 = Label(self.l3, text='Puesto', width=34, anchor='w')
        _label_19 = Label(self.l3, text='No. Esc Poder Notarial', width=34, anchor='w')
        _label_20 = Label(self.l3, text='Fecha Cert P. Notarial', width=34, anchor='w')
        _label_21 = Label(self.l3, text='Numero de Notaria', width=34, anchor='w')

        self.lbl17 = Label(self.l3, bg=self.color_normal)
        self.lbl18 = Label(self.l3, bg=self.color_normal)
        self.lbl19 = Label(self.l3, bg=self.color_normal)
        self.lbl20 = Label(self.l3, bg=self.color_normal)
        self.lbl21 = Label(self.l3, bg=self.color_normal)

        self.nomRepL_entry = UpperEntry(self.lbl17, textvariable=self.var9)
        self.puesto_entry = UpperEntry(self.lbl18, textvariable=self.var10)
        self.noEscPodNot_entry = UpperEntry(self.lbl19, textvariable=self.var11)
        self.fCertPNot_entry = UpperEntry(self.lbl20, textvariable=self.var12)
        self.noNot_entry = ttk.Entry(self.lbl21, textvariable=self.var13)

        _label_17.grid(row=0, column=0, sticky=W, padx=2)
        _label_18.grid(row=2, column=0, sticky=W, padx=2)
        _label_19.grid(row=2, column=1, sticky=W, padx=2)
        _label_20.grid(row=4, column=0, sticky=W, padx=2)
        _label_21.grid(row=4, column=1, sticky=W, padx=2)

        self.lbl17.grid(row=1, column=0, sticky=EW, padx=2, columnspan=2)
        self.lbl18.grid(row=3, column=0, sticky=EW, padx=2)
        self.lbl19.grid(row=3, column=1, sticky=EW, padx=2)
        self.lbl20.grid(row=5, column=0, sticky=EW, padx=2)
        self.lbl21.grid(row=5, column=1, sticky=EW, padx=2)

        self.nomRepL_entry.pack(fill='both')
        self.puesto_entry.pack(fill='both')
        self.noEscPodNot_entry.pack(fill='both')
        self.fCertPNot_entry.pack(fill='both')
        self.noNot_entry.pack(fill='both')


    def configuracion_general(self):
        opcion = IntVar()
        
        _label_22 = Label(self.l4, text='Indique el formato que desee aplicar al No. de Trabajador del Centro', anchor='w')
        _label_23 = Label(self.l4, text='Longitud', anchor='w')
        _label_24 = Label(self.l4, text='Ejemplo', anchor='w')
        _label_25 = Label(self.l4, text='Nombre del Centro de Trabajo', anchor='w')

        a22 = Label(self.l4, text='*', fg=self.color_danger, font=(self.font, 13, 'bold'))
        a23 = Label(self.l4, text=' ', fg=self.color_danger, font=(self.font, 13, 'bold'))
        a24 = Label(self.l4, text='*', fg=self.color_danger, font=(self.font, 13, 'bold'))
        '''a25 = Label(self.l4, text='*', fg=self.color_danger, font=(self.font, 13, 'bold'))
        a26 = Label(self.l4, text='*', fg=self.color_danger, font=(self.font, 13, 'bold'))'''

        label = LabelFrame(self.l4,)
        self.lbl22 = Label(self.l4, bg=self.color_normal, width=18)
        self.lbl23 = Label(self.l4, bg=self.color_normal, width=24)
        self.lbl24 = Label(self.l4, bg=self.color_normal)   #, width=24
        
        Radiobutton(label, text="Numérico", variable=opcion, value=1, ).pack(anchor=W)  #command=
        Radiobutton(label, text="Alfanumérico", variable=opcion, value=2, ).pack(anchor=W)
        self.long_entry = ttk.Entry(self.lbl22)
        self.nCenTrab_entry = UpperEntry(self.lbl24)

        _label_22.grid(row=0, column=0, sticky=NSEW, columnspan=6, padx=2)
        _label_23.grid(row=1, column=2, padx=2)
        _label_24.grid(row=1, column=4, padx=2)
        _label_25.grid(row=3, column=0, padx=2)

        self.lbl22.grid(row=2, column=2, padx=2)
        self.lbl23.grid(row=2, column=4, padx=2)
        self.lbl24.grid(row=4, column=0, sticky=NSEW, columnspan=3, padx=2,)
        
        label.grid(row=1, column=0, sticky=NSEW, padx=2, rowspan=2)
        
        a22.grid(row=2, column=3)
        a23.grid(row=2, column=5)
        a24.grid(row=4, column=3)

        self.long_entry.pack(fill='both')
        self.nCenTrab_entry.pack(fill='both')


    def configuracion_nomina(self):
        pass