import tkinter as tk
from tkinter import EW, NSEW, W, Label, LabelFrame, PhotoImage, StringVar
from tkinter import ttk

from assets.options import Window_Center
from assets.styles import Style

class LoginView:
    def exit(self):
        self.root.destroy()
        self.root.quit()

    def __init__(self, root):
        super().__init__()
        self.root = root
        width=372
        height=220
        
        wind = Window_Center(self.root)

        self.root.title('INICIO DE SESIÓN DE USUARIO')
        self.root.geometry(wind.center(width, height))
        self.root.resizable(0,0)
        self.root.protocol("WM_DELETE_WINDOW", self.exit)

        self.create_widgets()
    
    def create_widgets(self):
        self.create_icon()
        
        self.var_user = StringVar()
        self.var_pass = StringVar()

        frame = LabelFrame(self.root, relief='flat')
        frame.grid(row=0, column=0, sticky=NSEW, padx=12, pady=12, ipadx=8, ipady=8)

        self.icon_label_1 = Label(frame, text='1', image=self.img1)
        self.icon_label_2 = Label(frame, text='2', image=self.img2)

        user_label = Label(frame, text='Usuario', font=("Arial Bold", 12, 'bold'))
        self.user_label = Label(frame, bg='#849797')
        user_entry = ttk.Entry(self.user_label, font=("Arial Bold", 12), width=30, textvariable=self.var_user)
        user_entry.focus()

        pass_label = Label(frame, text='Contraseña', font=("Arial Bold", 12, 'bold'))
        self.pass_label = Label(frame, bg='#849797')
        pass_entry = ttk.Entry(self.pass_label, show='*', font=("Arial Bold", 12), width=30, textvariable=self.var_pass)
        
        self.btn_accept = ttk.Button(frame, text='Aceptar', style=self.button_success())
        self.btn_cancel = ttk.Button(frame, text='Cancelar', style=self.button_danger(), command=self.exit)

        self.intentos_label = Label(frame, text='Intentos: 3', font=("Arial Bold", 8, 'bold'))
        self.msg_label = Label(frame, font=("Arial Bold", 10, 'bold'))
        
        self.icon_label_1.grid(row=0, column=0, sticky=NSEW, rowspan=2)
        self.icon_label_2.grid(row=2, column=0, sticky=NSEW, rowspan=2)
        
        user_label.grid(row=0, column=1, sticky=W, padx=2)
        self.user_label.grid(row=1, column=1, sticky=NSEW, columnspan=2)
        user_entry.grid(row=0, column=0, sticky=W)

        pass_label.grid(row=2, column=1, sticky=W, padx=2)
        self.pass_label.grid(row=3, column=1, sticky=NSEW, columnspan=2)
        pass_entry.grid(row=0, column=0, sticky=W)
        
        self.btn_accept.grid(row=4, column=1, padx=4, pady=10, ipady=2, sticky=EW)
        self.btn_cancel.grid(row=4, column=2, padx=4, pady=10, ipady=2, sticky=EW)

        self.intentos_label.grid(row=5, column=1, sticky=W, columnspan=2)
        self.msg_label.grid(row=6, column=1, sticky=W, columnspan=2)
        
    def create_icon(self):
        self.img1 = PhotoImage(file='assets/images/label/person_FILL0_wght400_GRAD0_opsz48.png')
        self.img2 = PhotoImage(file='assets/images/label/lock_FILL0_wght400_GRAD0_opsz48.png')
        self.img3 = PhotoImage(file='assets/images/label/lock_open_FILL0_wght400_GRAD0_opsz48.png')

    def button_success(self):
        style = Style()
        b = style.TButton__success()
        return b

    def button_danger(self):
        style = Style()
        b = style.TButton__danger()
        return b
