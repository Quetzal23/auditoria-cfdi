from tkinter import CENTER, END, EW, HORIZONTAL, LEFT, NSEW, RIGHT, VERTICAL, W, IntVar, Label, LabelFrame, PhotoImage, Radiobutton, StringVar
from tkinter import ttk
import tkinter as tk
from tkcalendar import *

from datetime import date

from assets.options import CustomDateEntry, Window_Center, UpperEntry
from assets.styles import Style

class CentroTrabajoView:
    def on_closing(self):
        self.root.destroy()

    def __init__(self, root, id_empresa):
        super().__init__()
        self.root = root
        self.id_empresa = id_empresa

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
        
        self.disabled_entry()

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
        self.btn_print = ttk.Button(frame_top, text='Print', image=self.img5)
        self.btn_exit = ttk.Button(frame_top, text='Exit', image=self.img6, command=self.on_closing)
        self.msg_label = Label(frame_top, text='', width=50, anchor='e')

        self.btn_new.pack(side=LEFT, padx=4, pady=4,)
        self.btn_save.pack(side=LEFT, padx=4, pady=4,)
        self.btn_edit.pack(side=LEFT, padx=4, pady=4,)
        self.btn_delete.pack(side=LEFT, padx=4, pady=4,)
        self.btn_print.pack(side=LEFT, padx=4, pady=4,)
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
        #self.var2 = StringVar()
        self.var3 = StringVar()
        #self.var4 = StringVar()
        #self.var5 = StringVar()
        #self.var6 = StringVar()
        #self.var7 = StringVar()
        self.var8 = StringVar()

        self.regPtrl_entry = UpperEntry(self.lbl1, textvariable=self.var1)
        self.fIniAct_entry = CustomDateEntry(self.lbl2, selectmode='day')
        self.contPub_entry = UpperEntry(self.lbl3, textvariable=self.var3)

        self.fIniAud_entry = CustomDateEntry(self.lbl5, selectmode='day')
        self.fFinAud_entry = CustomDateEntry(self.lbl6, selectmode='day')
        self.fElabDi_entry = CustomDateEntry(self.lbl7, selectmode='day')
        self.actPrin_entry = UpperEntry(self.lbl8, textvariable=self.var8)

        
        self.fIniAct_entry._set_text(self.fIniAct_entry._date.strftime('%d/%m/%Y'))

        self.fIniAud_entry._set_text(self.fIniAud_entry._date.strftime('%d/%m/%Y'))
        self.fFinAud_entry._set_text(self.fFinAud_entry._date.strftime('%d/%m/%Y'))
        self.fElabDi_entry._set_text(self.fElabDi_entry._date.strftime('%d/%m/%Y'))

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
        self.contPub_entry.pack(fill='both')
        self.actPrin_entry.pack(fill='both')
        self.form_pack()

    def form_pack(self):
        self.fIniAct_entry.pack(fill='both')
        self.fIniAud_entry.pack(fill='both')
        self.fFinAud_entry.pack(fill='both')
        self.fElabDi_entry.pack(fill='both')

    def dateentry_forget(self):
        self.fIniAct_entry.forget()
        self.fIniAud_entry.forget()
        self.fFinAud_entry.forget()
        self.fElabDi_entry.forget()


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
        
        self.var17 = StringVar()
        self.var18 = StringVar()
        self.var19 = StringVar()
        self.var20 = StringVar()
        self.var21 = StringVar()

        self.nomRepL_entry = UpperEntry(self.lbl17, textvariable=self.var17)
        self.puesto_entry = UpperEntry(self.lbl18, textvariable=self.var18)
        self.noEscPodNot_entry = UpperEntry(self.lbl19, textvariable=self.var19)
        self.fCertPNot_entry = UpperEntry(self.lbl20, textvariable=self.var20)
        self.noNot_entry = ttk.Entry(self.lbl21, textvariable=self.var21)

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
        self.opcion = IntVar()
        self.opcion.set(1)
        
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
        
        self.radio_1 = Radiobutton(label, text="Numérico", variable=self.opcion, value=1, )
        self.radio_2 = Radiobutton(label, text="Alfanumérico", variable=self.opcion, value=2, )
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

        self.radio_1.pack(anchor=W)  #command=
        self.radio_2.pack(anchor=W)
        self.long_entry.pack(fill='both')
        self.nCenTrab_entry.pack(fill='both')


    def configuracion_nomina(self):
        pass

    def bloquear_formulario(self):
        self.limpiar_formulario()
        self.disabled_entry()
        '''self._button_new()'''

    def limpiar_formulario(self):
        self.var1.set('')
        #self.var2.set('')
        self.var3.set('')
        #self.var4.set('')
        #self.var5.set('')
        #self.var6.set('')
        #self.var7.set('')
        self.var8.set('')
        self.var9.set('')
        self.var10.set('')
        self.var11.set('')
        self.var12.set('')
        self.var13.set('')
        self.var14.set('')
        self.var15.set('')
        self.var16.set('')
        self.var17.set('')
        self.var18.set('')
        self.var19.set('')
        self.var20.set('')
        self.var21.set('')
        #self.limpiar_form_string()

        self.regPtrl_entry.delete(0, END)
        self.fIniAct_entry.delete(0, END)
        self.contPub_entry.delete(0, END)
        self.fIniAud_entry.delete(0, END)
        self.fFinAud_entry.delete(0, END)
        self.fElabDi_entry.delete(0, END)
        self.actPrin_entry.delete(0, END)

        self.calle_entry.delete(0, END)
        self.num_entry.delete(0, END)
        self.col_entry.delete(0, END)
        self.mpio_entry.delete(0, END)
        self.cp_entry.delete(0, END)
        self.entFed_entry.delete(0, END)
        self.pob_entry.delete(0, END)
        self.tel_entry.delete(0, END)

        self.nomRepL_entry.delete(0, END)
        self.puesto_entry.delete(0, END)
        self.noEscPodNot_entry.delete(0, END)
        self.fCertPNot_entry.delete(0, END)
        self.noNot_entry.delete(0, END)

        '''self.radio_1.delete(0, END)
        self.radio_2.delete(0, END)'''
        self.long_entry.delete(0, END)
        self.nCenTrab_entry.delete(0, END)

    def normal_entry(self):
        self.regPtrl_entry.config(state='normal')
        self.fIniAct_entry.config(state='normal')
        self.contPub_entry.config(state='normal')
        self.fIniAud_entry.config(state='normal')
        self.fFinAud_entry.config(state='normal')
        self.fElabDi_entry.config(state='normal')
        self.actPrin_entry.config(state='normal')

        self.calle_entry.config(state='normal')
        self.num_entry.config(state='normal')
        self.col_entry.config(state='normal')
        self.mpio_entry.config(state='normal')
        self.cp_entry.config(state='normal')
        self.entFed_entry.config(state='normal')
        self.pob_entry.config(state='normal')
        self.tel_entry.config(state='normal')

        self.nomRepL_entry.config(state='normal')
        self.puesto_entry.config(state='normal')
        self.noEscPodNot_entry.config(state='normal')
        self.fCertPNot_entry.config(state='normal')
        self.noNot_entry.config(state='normal')

    def disabled_entry(self):
        self._button_new()
        
        self.regPtrl_entry.config(state='disabled')
        self.fIniAct_entry.config(state='disabled')
        self.contPub_entry.config(state='disabled')
        self.fIniAud_entry.config(state='disabled')
        self.fFinAud_entry.config(state='disabled')
        self.fElabDi_entry.config(state='disabled')
        self.actPrin_entry.config(state='disabled')

        self.calle_entry.config(state='disabled')
        self.num_entry.config(state='disabled')
        self.col_entry.config(state='disabled')
        self.mpio_entry.config(state='disabled')
        self.cp_entry.config(state='disabled')
        self.entFed_entry.config(state='disabled')
        self.pob_entry.config(state='disabled')
        self.tel_entry.config(state='disabled')

        self.nomRepL_entry.config(state='disabled')
        self.puesto_entry.config(state='disabled')
        self.noEscPodNot_entry.config(state='disabled')
        self.fCertPNot_entry.config(state='disabled')
        self.noNot_entry.config(state='disabled')

        self.radio_1.config(state='disabled')
        self.radio_2.config(state='disabled')
        self.long_entry.config(state='disabled')
        self.nCenTrab_entry.config(state='disabled')

    def formulario_completo(self):
        self.lbl1.config(bg=self.color_normal)
        self.lbl2.config(bg=self.color_normal)
        self.lbl3.config(bg=self.color_normal)
        #self.lbl4.config(bg=self.color_normal)
        self.lbl5.config(bg=self.color_normal)
        self.lbl6.config(bg=self.color_normal)
        self.lbl7.config(bg=self.color_normal)
        self.lbl8.config(bg=self.color_normal)

        self.lbl9.config(bg=self.color_normal)
        self.lbl10.config(bg=self.color_normal)
        self.lbl11.config(bg=self.color_normal)
        self.lbl12.config(bg=self.color_normal)
        self.lbl13.config(bg=self.color_normal)
        self.lbl14.config(bg=self.color_normal)
        self.lbl15.config(bg=self.color_normal)
        self.lbl16.config(bg=self.color_normal)

        self.lbl17.config(bg=self.color_normal)
        self.lbl18.config(bg=self.color_normal)
        self.lbl19.config(bg=self.color_normal)
        self.lbl20.config(bg=self.color_normal)
        self.lbl21.config(bg=self.color_normal)

    def formulario_incompleto(self):
        if len(self.var1.get()) == 0:
            self.lbl1.config(bg=self.color_danger)
        else:
            self.lbl1.config(bg=self.color_normal)
        if len(self.var2.get()) == 0:
            self.lbl2.config(bg=self.color_danger)
        else:
            self.lbl2.config(bg=self.color_normal)
        if len(self.var3.get()) == 0:
            self.lbl3.config(bg=self.color_danger)
        else:
            self.lbl3.config(bg=self.color_normal)
        '''if len(self.var4.get()) == 0:
            self.lbl4.config(bg=self.color_danger)
        else:
            self.lbl4.config(bg=self.color_normal)'''
        if len(self.var5.get()) == 0:
            self.lbl5.config(bg=self.color_danger)
        else:
            self.lbl5.config(bg=self.color_normal)
        if len(self.var6.get()) == 0:
            self.lbl6.config(bg=self.color_danger)
        else:
            self.lbl6.config(bg=self.color_normal)
        if len(self.var7.get()) == 0:
            self.lbl7.config(bg=self.color_danger)
        else:
            self.lbl7.config(bg=self.color_normal)
        if len(self.var8.get()) == 0:
            self.lbl8.config(bg=self.color_danger)
        else:
            self.lbl8.config(bg=self.color_normal)

        if len(self.var9.get()) == 0:
            self.lbl9.config(bg=self.color_danger)
        else:
            self.lbl9.config(bg=self.color_normal)
        if len(self.var10.get()) == 0:
            self.lbl10.config(bg=self.color_danger)
        else:
            self.lbl10.config(bg=self.color_normal)
        if len(self.var11.get()) == 0:
            self.lbl11.config(bg=self.color_danger)
        else:
            self.lbl11.config(bg=self.color_normal)
        if len(self.var12.get()) == 0:
            self.lbl12.config(bg=self.color_danger)
        else:
            self.lbl12.config(bg=self.color_normal)
        if len(self.var13.get()) == 0:
            self.lbl13.config(bg=self.color_danger)
        else:
            self.lbl13.config(bg=self.color_normal)
        if len(self.var14.get()) == 0:
            self.lbl14.config(bg=self.color_danger)
        else:
            self.lbl14.config(bg=self.color_normal)
        if len(self.var15.get()) == 0:
            self.lbl15.config(bg=self.color_danger)
        else:
            self.lbl15.config(bg=self.color_normal)
        if len(self.var16.get()) == 0:
            self.lbl16.config(bg=self.color_danger)
        else:
            self.lbl16.config(bg=self.color_normal)
            
        if len(self.var17.get()) == 0:
            self.lbl17.config(bg=self.color_danger)
        else:
            self.lbl17.config(bg=self.color_normal)
        if len(self.var18.get()) == 0:
            self.lbl18.config(bg=self.color_danger)
        else:
            self.lbl18.config(bg=self.color_normal)
        if len(self.var19.get()) == 0:
            self.lbl19.config(bg=self.color_danger)
        else:
            self.lbl19.config(bg=self.color_normal)
        if len(self.var20.get()) == 0:
            self.lbl20.config(bg=self.color_danger)
        else:
            self.lbl20.config(bg=self.color_normal)
        if len(self.var21.get()) == 0:
            self.lbl21.config(bg=self.color_danger)
        else:
            self.lbl21.config(bg=self.color_normal)

    def _select_company(self):
        self.btn_new['state'] = tk.NORMAL
        self.btn_save['state'] = tk.DISABLED
        self.btn_edit['state'] = tk.NORMAL
        self.btn_delete['state'] = tk.NORMAL
        self.btn_print['state'] = tk.NORMAL

    def _button_edit(self):
        self.btn_new['state'] = tk.DISABLED
        self.btn_save['state'] = tk.NORMAL
        self.btn_edit['state'] = tk.DISABLED
        self.btn_delete['state'] = tk.DISABLED
        self.btn_print['state'] = tk.DISABLED

    def _button_new(self):
        self.btn_new['state'] = tk.NORMAL
        self.btn_save['state'] = tk.DISABLED
        self.btn_edit['state'] = tk.DISABLED
        self.btn_delete['state'] = tk.DISABLED
        self.btn_print['state'] = tk.DISABLED

    def _button_save(self):
        self.btn_new['state'] = tk.DISABLED
        self.btn_save['state'] = tk.NORMAL
        self.btn_edit['state'] = tk.DISABLED
        self.btn_delete['state'] = tk.DISABLED
        self.btn_print['state'] = tk.DISABLED