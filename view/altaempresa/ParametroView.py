from tkinter import messagebox as mb
from tkinter import CENTER, END, EW, HORIZONTAL, LEFT, NSEW, RIGHT, VERTICAL, W, Label, LabelFrame, PhotoImage, StringVar
from tkinter import ttk
import tkinter as tk

from assets.options import Window_Center, UpperEntry
from assets.styles import Style

class ParametroView():
    def on_closing(self):
        self.root.destroy()

    def alert(self):
        mb.showwarning('Alerta',
            'Llene todos los campos para continuar')

    def __init__(self, root):
        super().__init__()
        self.root = root

        wind_width  = 898#900
        wind_height = 410#390

        wind = Window_Center(self.root)
        self.style = Style()

        self.root.grab_set()
        self.root.focus_force()

        self.root.geometry(wind.center(wind_width, wind_height))
        self.root.title('PARAMETROS DE EMPRESAS')
        self.root.resizable(0, 0)
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        
        self.create_widgets()
        

    def create_icon(self):
        self.img1 = self.image_button(PhotoImage(file='assets/images/button/draft_FILL0_wght400_GRAD0_opsz48.png'))
        self.img2 = self.image_button(PhotoImage(file='assets/images/button/save_FILL0_wght400_GRAD0_opsz48.png'))
        self.img3 = self.image_button(PhotoImage(file='assets/images/button/edit_FILL0_wght400_GRAD0_opsz48.png'))
        self.img4 = self.image_button(PhotoImage(file='assets/images/button/delete_FILL0_wght400_GRAD0_opsz48.png'))
        self.img5 = self.image_button(PhotoImage(file='assets/images/button/domain_FILL0_wght400_GRAD0_opsz48.png'))
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
        frame_top.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=6)

        self.btn_new = ttk.Button(frame_top, text='New', image=self.img1,)
        self.btn_save = ttk.Button(frame_top, text='Save', image=self.img2,)
        self.btn_edit = ttk.Button(frame_top, text='Edit', image=self.img3)
        self.btn_delete = ttk.Button(frame_top, text='Delete', image=self.img4)
        self.btn_center = ttk.Button(frame_top, text='Centro de Trabajo', image=self.img5)
        self.btn_exit = ttk.Button(frame_top, text='Exit', image=self.img6, command=self.on_closing)

        self.btn_new.pack(side=LEFT, padx=4, pady=4,)
        self.btn_save.pack(side=LEFT, padx=4, pady=4,)
        self.btn_edit.pack(side=LEFT, padx=4, pady=4,)
        self.btn_delete.pack(side=LEFT, padx=4, pady=4,)
        self.btn_center.pack(side=LEFT, padx=4, pady=4,)
        self.btn_exit.pack(side=RIGHT, padx=4, pady=4,)

    def frame_left(self):
        frame_left = LabelFrame(self.root, bg='#849797', relief='flat')
        frame_left.grid(row=1, column=0, sticky=NSEW, padx=6)

        self.treeview = ttk.Treeview(frame_left, height=15, style=self.style.Treeview())
        self.treeview['columns'] = ('Emp', )
        self.treeview.heading('#0', text='', anchor=CENTER)
        self.treeview.heading('Emp', text='Empresa', anchor=CENTER)
        self.treeview.column('#0', stretch=False, width=0, minwidth=0)
        self.treeview.column('Emp', stretch=False, width=300, minwidth=300)

        vscrollbar = ttk.Scrollbar(frame_left, orient=VERTICAL, command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=vscrollbar.set)

        hscrollbar = ttk.Scrollbar(frame_left, orient=HORIZONTAL, command=self.treeview.xview)
        self.treeview.configure(xscrollcommand=hscrollbar.set)

        self.treeview.grid(row=0, column=0, sticky="nsew")
        
        vscrollbar.grid(row=0, column=3, sticky="nse")
        hscrollbar.grid(row=1, column=0, sticky="ew")

    def frame_right(self):
        frame_right = LabelFrame(self.root, relief='flat')
        frame_right.grid(row=1, column=1, sticky=NSEW, padx=6)

        self.datos_generales(frame_right)
        Label(frame_right).grid(row=1)
        self.direccion(frame_right)
        
        self.disabled_entry()

    def datos_generales(self, labelframe):
        frame = LabelFrame(labelframe, text='Datos Generales', fg='blue', relief='flat')
        frame.grid(row=0, column=0, sticky=NSEW, padx=6)
        
        _label_1 = Label(frame, text='Nombre de Empresa', anchor='w')
        _label_2 = Label(frame, text='Nombre corto', width=24, anchor='w')
        _label_3 = Label(frame, text='RFC', width=24, anchor='w')
        _label_4 = Label(frame, text='# Registro Patronal', width=24, anchor='w')
        _label_5 = Label(frame, text='Datos Generales', anchor='w')

        self.lbl1 = Label(frame, bg='#849797')
        self.lbl2 = Label(frame, bg='#849797')
        self.lbl3 = Label(frame, bg='#849797')
        self.lbl4 = Label(frame, bg='#849797')
        self.lbl5 = Label(frame, bg='#849797')

        self.var1 = StringVar()
        self.var2 = StringVar()
        self.var3 = StringVar()
        self.var4 = StringVar()
        self.var5 = StringVar()

        self.nomEmp_entry = UpperEntry(self.lbl1, textvariable=self.var1)
        self.nomCorto_entry = UpperEntry(self.lbl2, textvariable=self.var2)
        self.rfc_entry = UpperEntry(self.lbl3, textvariable=self.var3)
        self.noPatrl_entry = UpperEntry(self.lbl4, textvariable=self.var4)
        self.actPpal_entry = UpperEntry(self.lbl5, textvariable=self.var5)

        _label_1.grid(row=0, column=0, columnspan=3, sticky=EW, padx=2)
        _label_2.grid(row=2, column=0, sticky=EW, padx=2)
        _label_3.grid(row=2, column=1, sticky=EW, padx=2)
        _label_4.grid(row=2, column=2, sticky=EW, padx=2)
        _label_5.grid(row=4, column=0, columnspan=3, sticky=EW, padx=2)

        self.lbl1.grid(row=1, column=0, columnspan=3, sticky=NSEW, padx=2)
        self.lbl2.grid(row=3, column=0, sticky=NSEW, padx=2)
        self.lbl3.grid(row=3, column=1, sticky=NSEW, padx=2)
        self.lbl4.grid(row=3, column=2, sticky=NSEW, padx=2)
        self.lbl5.grid(row=5, column=0, columnspan=3, sticky=NSEW, padx=2)

        self.nomEmp_entry.pack(fill='both')
        self.nomCorto_entry.pack(fill='both')
        self.rfc_entry.pack(fill='both')
        self.noPatrl_entry.pack(fill='both')
        self.actPpal_entry.pack(fill='both')
    
    def direccion(self, labelframe):
        frame = LabelFrame(labelframe, text='Dirección', fg='blue', relief='flat')
        frame.grid(row=2, column=0, sticky=NSEW, padx=6)

        _label_6 = Label(frame, text='Calle', width=24, anchor='w')
        _label_7 = Label(frame, text='Número', width=24, anchor='w')
        _label_8 = Label(frame, text='Colonia', width=24, anchor='w')
        _label_9 = Label(frame, text='Delegación o Municipio', width=24, anchor='w')
        _label_10 = Label(frame, text='Código Postal', width=24, anchor='w')
        _label_11 = Label(frame, text='Entidad Federativa', width=24, anchor='w')
        _label_12 = Label(frame, text='Población', width=24, anchor='w')
        _label_13 = Label(frame, text='Teléfono(s)', width=24, anchor='w')

        self.lbl6 = Label(frame, bg='#849797')
        self.lbl7 = Label(frame, bg='#849797')
        self.lbl8 = Label(frame, bg='#849797')
        self.lbl9 = Label(frame, bg='#849797')
        self.lbl10 = Label(frame, bg='#849797')
        self.lbl11 = Label(frame, bg='#849797')
        self.lbl12 = Label(frame, bg='#849797')
        self.lbl13 = Label(frame, bg='#849797')
        
        self.var6 = StringVar()
        self.var7 = StringVar()
        self.var8 = StringVar()
        self.var9 = StringVar()
        self.var10 = StringVar()
        self.var11 = StringVar()
        self.var12 = StringVar()
        self.var13 = StringVar()

        self.calle_entry = UpperEntry(self.lbl6, textvariable=self.var6)
        self.num_entry = UpperEntry(self.lbl7, textvariable=self.var7)
        self.col_entry = UpperEntry(self.lbl8, textvariable=self.var8)
        self.mpio_entry = UpperEntry(self.lbl9, textvariable=self.var9)
        self.cp_entry = ttk.Entry(self.lbl10, textvariable=self.var10, validate="key")
        self.entFed_entry = UpperEntry(self.lbl11, textvariable=self.var11)
        self.pob_entry = UpperEntry(self.lbl12, textvariable=self.var12)
        self.tel_entry = UpperEntry(self.lbl13, textvariable=self.var13)

        _label_6.grid(row=1, column=0, sticky=W, padx=2)
        _label_7.grid(row=1, column=1, sticky=W, padx=2)
        _label_8.grid(row=1, column=2, sticky=W, padx=2)
        _label_9.grid(row=3, column=0, sticky=W, padx=2)
        _label_10.grid(row=3, column=1, sticky=W, padx=2)
        _label_11.grid(row=3, column=2,  sticky=W, padx=2)
        _label_12.grid(row=5, column=0,  sticky=W, padx=2)
        _label_13.grid(row=5, column=1,  sticky=W, padx=2)

        self.lbl6.grid(row=2, column=0, sticky=EW, padx=2)
        self.lbl7.grid(row=2, column=1, sticky=EW, padx=2)
        self.lbl8.grid(row=2, column=2, sticky=EW, padx=2)
        self.lbl9.grid(row=4, column=0, sticky=EW, padx=2)
        self.lbl10.grid(row=4, column=1, sticky=EW, padx=2)
        self.lbl11.grid(row=4, column=2, sticky=EW, padx=2)
        self.lbl12.grid(row=6, column=0, sticky=EW, padx=2)
        self.lbl13.grid(row=6, column=1, sticky=EW, padx=2)
        
        self.calle_entry.pack(fill='both')
        self.num_entry.pack(fill='both')
        self.col_entry.pack(fill='both')
        self.mpio_entry.pack(fill='both')
        self.cp_entry.pack(fill='both')
        self.entFed_entry.pack(fill='both')
        self.pob_entry.pack(fill='both')
        self.tel_entry.pack(fill='both')
    
    def disabled_entry(self):
        self.btn_save['state'] = tk.DISABLED
        self.btn_edit['state'] = tk.DISABLED
        self.btn_delete['state'] = tk.DISABLED
        self.btn_center['state'] = tk.DISABLED

        self.nomEmp_entry.config(state='disabled')
        self.nomCorto_entry.config(state='disabled')
        self.rfc_entry.config(state='disabled')
        self.noPatrl_entry.config(state='disabled')
        self.actPpal_entry.config(state='disabled')
        self.calle_entry.config(state='disabled')
        self.num_entry.config(state='disabled')
        self.col_entry.config(state='disabled')
        self.mpio_entry.config(state='disabled')
        self.cp_entry.config(state='disabled')
        self.entFed_entry.config(state='disabled')
        self.pob_entry.config(state='disabled')
        self.tel_entry.config(state='disabled')

    def normal_entry(self):
        self.nomEmp_entry.config(state='normal')
        self.nomEmp_entry.focus()
        self.nomCorto_entry.config(state='normal')
        self.rfc_entry.config(state='normal')
        self.noPatrl_entry.config(state='normal')
        self.actPpal_entry.config(state='normal')
        self.calle_entry.config(state='normal')
        self.num_entry.config(state='normal')
        self.col_entry.config(state='normal')
        self.mpio_entry.config(state='normal')
        self.cp_entry.config(state='normal')
        self.entFed_entry.config(state='normal')
        self.pob_entry.config(state='normal')
        self.tel_entry.config(state='normal')

    def formulario_completo(self):
        self.lbl1.config(bg='#849797')
        self.lbl2.config(bg='#849797')
        self.lbl3.config(bg='#849797')
        self.lbl4.config(bg='#849797')
        self.lbl5.config(bg='#849797')
        self.lbl6.config(bg='#849797')
        self.lbl7.config(bg='#849797')
        self.lbl8.config(bg='#849797')
        self.lbl9.config(bg='#849797')
        self.lbl10.config(bg='#849797')
        self.lbl11.config(bg='#849797')
        self.lbl12.config(bg='#849797')
        self.lbl13.config(bg='#849797')

    def formulario_incompleto(self):
        if len(self.var1.get()) == 0:
            self.lbl1.config(bg='red')
        else:
            self.lbl1.config(bg='#849797')
        if len(self.var2.get()) == 0:
            self.lbl2.config(bg='red')
        else:
            self.lbl2.config(bg='#849797')
        if len(self.var3.get()) == 0:
            self.lbl3.config(bg='red')
        else:
            self.lbl3.config(bg='#849797')
        if len(self.var4.get()) == 0:
            self.lbl4.config(bg='red')
        else:
            self.lbl4.config(bg='#849797')
        if len(self.var5.get()) == 0:
            self.lbl5.config(bg='red')
        else:
            self.lbl5.config(bg='#849797')


        if len(self.var6.get()) == 0:
            self.lbl6.config(bg='red')
        else:
            self.lbl6.config(bg='#849797')
        if len(self.var7.get()) == 0:
            self.lbl7.config(bg='red')
        else:
            self.lbl7.config(bg='#849797')
        if len(self.var8.get()) == 0:
            self.lbl8.config(bg='red')
        else:
            self.lbl8.config(bg='#849797')
        if len(self.var9.get()) == 0:
            self.lbl9.config(bg='red')
        else:
            self.lbl9.config(bg='#849797')
        if len(self.var10.get()) == 0:
            self.lbl10.config(bg='red')
        else:
            self.lbl10.config(bg='#849797')
        if len(self.var11.get()) == 0:
            self.lbl11.config(bg='red')
        else:
            self.lbl11.config(bg='#849797')
        if len(self.var12.get()) == 0:
            self.lbl12.config(bg='red')
        else:
            self.lbl12.config(bg='#849797')
        if len(self.var13.get()) == 0:
            self.lbl13.config(bg='red')
        else:
            self.lbl13.config(bg='#849797')

    def _button_save(self):
        self.btn_new['state'] = tk.DISABLED
        self.btn_save['state'] = tk.NORMAL
        self.btn_edit['state'] = tk.DISABLED
        self.btn_delete['state'] = tk.DISABLED
        self.btn_center['state'] = tk.DISABLED

    def _button_new(self):
        self.btn_new['state'] = tk.NORMAL
        self.btn_save['state'] = tk.DISABLED
        self.btn_edit['state'] = tk.DISABLED
        self.btn_delete['state'] = tk.DISABLED
        self.btn_center['state'] = tk.DISABLED

    def bloquear_formulario(self):
        self.nomEmp_entry.delete(0, END)
        self.nomCorto_entry.delete(0, END)
        self.rfc_entry.delete(0, END)
        self.noPatrl_entry.delete(0, END)
        self.actPpal_entry.delete(0, END)
        self.calle_entry.delete(0, END)
        self.num_entry.delete(0, END)
        self.col_entry.delete(0, END)
        self.mpio_entry.delete(0, END)
        self.cp_entry.delete(0, END)
        self.entFed_entry.delete(0, END)
        self.pob_entry.delete(0, END)
        self.tel_entry.delete(0, END)

        self.disabled_entry()

        self._button_new()

    def _select_company(self):
        self.btn_new['state'] = tk.NORMAL
        self.btn_save['state'] = tk.DISABLED
        self.btn_edit['state'] = tk.NORMAL
        self.btn_delete['state'] = tk.NORMAL
        self.btn_center['state'] = tk.NORMAL