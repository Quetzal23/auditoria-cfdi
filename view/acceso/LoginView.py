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

        self.style = Style()

        self.color_normal = self.style.color__normal

        self.style_font = self.style.font
        self.font_size_title = self.style.fontsize_title
        self.font_size_cont = self.style.fontsize_cont
        self.font_size_msg = self.style.fontsize_msg

        self.button_success = self.style.TButton__success()
        self.button_danger = self.style.TButton__danger()

        self.root.title('INICIO DE SESIÓN DE USUARIO')
        self.root.geometry(wind.center(width, height))
        self.root.resizable(0, 0)
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

        user_label = Label(frame, text='Usuario', font=(self.style_font, self.font_size_title, 'bold'))
        pass_label = Label(frame, text='Contraseña', font=(self.style_font, self.font_size_title, 'bold'))

        self.user_label = Label(frame, bg=self.color_normal, width=30)
        self.pass_label = Label(frame, bg=self.color_normal, width=30)

        user_entry = ttk.Entry(self.user_label, font=(self.style_font, self.font_size_title), textvariable=self.var_user, width=30)
        user_entry.focus()

        pass_entry = ttk.Entry(self.pass_label, show='*', font=(self.style_font, self.font_size_title), textvariable=self.var_pass, width=30)
        
        self.btn_accept = ttk.Button(frame, text='Aceptar', style=self.button_success)
        self.btn_cancel = ttk.Button(frame, text='Cancelar', style=self.button_danger, command=self.exit)

        self.intentos_label = Label(frame, text='Intentos: 3', font=(self.style_font, self.font_size_cont, 'bold'))
        self.msg_label = Label(frame, font=(self.style_font, self.font_size_msg, 'bold'))

        self.icon_label_1.grid(row=0, column=0, sticky=NSEW, rowspan=2)
        self.icon_label_2.grid(row=2, column=0, sticky=NSEW, rowspan=2)

        user_label.grid(row=0, column=1, sticky=W, padx=2)
        pass_label.grid(row=2, column=1, sticky=W, padx=2)
        
        self.user_label.grid(row=1, column=1, sticky=NSEW, columnspan=2)
        self.pass_label.grid(row=3, column=1, sticky=NSEW, columnspan=2)

        user_entry.pack(fill='both')
        pass_entry.pack(fill='both')

        self.btn_accept.grid(row=4, column=1, padx=4, pady=10, ipady=2, sticky=EW)
        self.btn_cancel.grid(row=4, column=2, padx=4, pady=10, ipady=2, sticky=EW)

        self.intentos_label.grid(row=5, column=1, sticky=W, columnspan=2)
        self.msg_label.grid(row=6, column=1, sticky=W, columnspan=2)

    def create_icon(self):
        self.img1 = PhotoImage(file='assets/images/label/person_FILL0_wght400_GRAD0_opsz48.png')
        self.img2 = PhotoImage(file='assets/images/label/lock_FILL0_wght400_GRAD0_opsz48.png')
        self.img3 = PhotoImage(file='assets/images/label/lock_open_FILL0_wght400_GRAD0_opsz48.png')