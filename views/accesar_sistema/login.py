import tkinter as tk
from tkinter import E, EW, NSEW, W, Label, LabelFrame, PhotoImage, StringVar
from tkinter import ttk

from views.options import Window_Center
from views.styles import Style

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        width=372
        height=234
        
        wind = Window_Center(self)

        self.title('INICIO DE SESIÓN DE USUARIO')
        self.geometry(wind.center(width, height))
        self.resizable(0,0)
        self.protocol("WM_DELETE_WINDOW", self.exit)

        self.create_widgets()

    def exit(self):
        self.destroy()
        self.quit()

    def create_icon(self):
        self.img1 = PhotoImage(file='images/icons/label/person_FILL0_wght400_GRAD0_opsz48.png')
        self.img2 = PhotoImage(file='images/icons/label/lock_FILL0_wght400_GRAD0_opsz48.png')
        self.img3 = PhotoImage(file='images/icons/label/lock_open_FILL0_wght400_GRAD0_opsz48.png')

    def create_widgets(self):
        self.create_icon()

        intentos = 3

        self.var_user = StringVar()
        self.var_pass = StringVar()

        frame = LabelFrame(self, relief='flat')
        frame.grid(row=0, column=0, sticky=NSEW, padx=12, pady=12, ipadx=8, ipady=8)

        icon_label_1 = Label(frame, text='1', image=self.img1)
        icon_label_1.grid(row=0, column=0, sticky=NSEW, rowspan=2)
        icon_label_2 = Label(frame, text='2', image=self.img2)
        icon_label_2.grid(row=2, column=0, sticky=NSEW, rowspan=2)

        user_label = Label(frame, text='Usuario', font=("Arial Bold", 12, 'bold'))
        user_label.grid(row=0, column=1, sticky=W, padx=2)
        user_entry = ttk.Entry(frame, font=("Arial Bold", 12), width=30, textvariable=self.var_user)
        user_entry.grid(row=1, column=1, sticky=W, columnspan=2)
        user_entry.focus()

        pass_label = Label(frame, text='Contraseña', font=("Arial Bold", 12, 'bold'))
        pass_label.grid(row=2, column=1, sticky=W, padx=2)
        pass_entry = ttk.Entry(frame, show='*', font=("Arial Bold", 12), width=30, textvariable=self.var_pass)
        pass_entry.grid(row=3, column=1, sticky=W, columnspan=2)

        btn_accept = ttk.Button(frame, text='Aceptar', style=self.button_success(), command=self.get_user)
        btn_accept.grid(row=4, column=1, padx=4, pady=10, ipady=2, sticky=EW)

        btn_cancel = ttk.Button(frame, text='Cancelar', style=self.button_danger(), command=self.exit)
        btn_cancel.grid(row=4, column=2, padx=4, pady=10, ipady=2, sticky=EW)

        self.intentos_label = Label(frame, text='Intentos: %s' % intentos, font=("Arial Bold", 8, 'bold'))
        self.intentos_label.grid(row=5, column=1, sticky=W, columnspan=2)

        self.msg_label = Label(frame, text='')
        self.msg_label.grid(row=6, column=1, sticky=W, columnspan=2)

    def inputs_login(self):
        return len(self.var_user.get()) != 0 and len(self.var_pass.get()) != 0

    def get_user(self):
        self.msg_label['text'] = ''

        usern = self.var_user.get()
        passw = self.var_pass.get()

        #print(usern)
        if self.inputs_login():
            print('Hola')
        else:
            self.msg_label['text'] = 'LLENE TODAS LAS CASILLAS'
            self.msg_label['fg'] = '#D70F21'


    def button_success(self):
        style = Style()
        b = style.TButton__success()
        return b

    def button_danger(self):
        style = Style()
        b = style.TButton__danger()
        return b
