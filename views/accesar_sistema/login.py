import tkinter as tk
from tkinter import NSEW, W, Label, LabelFrame, PhotoImage
from tkinter import ttk

from views.options import Window_Center

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        width=480
        height=280
        
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

        frame = LabelFrame(self)
        frame.grid(row=0, column=0, sticky=NSEW, padx=4, pady=4, ipadx=8, ipady=8)

        icon_label_1 = Label(frame, text='1', image=self.img1)
        icon_label_1.grid(row=0, column=0, rowspan=2)
        icon_label_2 = Label(frame, text='2', image=self.img2)
        icon_label_2.grid(row=2, column=0, rowspan=2)

        user_label = Label(frame, text='Usuario', font=("Arial Bold", 12, 'bold'))
        user_label.grid(row=0, column=1, sticky=W, padx=4)
        user_entry = ttk.Entry(frame, font=("Arial Bold", 12))
        user_entry.grid(row=1, column=1, sticky=W, padx=4)
        user_entry.focus()

        pass_label = Label(frame, text='Contraseña', font=("Arial Bold", 12, 'bold'))
        pass_label.grid(row=2, column=1, sticky=W, padx=4)
        pass_entry = ttk.Entry(frame, font=("Arial Bold", 12))
        pass_entry.grid(row=3, column=1, sticky=W, padx=4)

        