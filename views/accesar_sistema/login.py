import tkinter as tk
from tkinter import EW, NSEW, W, Label, LabelFrame, PhotoImage, StringVar
from tkinter import ttk
from db.login_db import Login_DB

from views.options import Window_Center
from views.styles import Style

from views.index import Index

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        width=372
        height=220

        self.intentos = 0
        self.total_intento = 3
        
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

        self.var_user = StringVar()
        self.var_pass = StringVar()

        frame = LabelFrame(self, relief='flat')
        frame.grid(row=0, column=0, sticky=NSEW, padx=12, pady=12, ipadx=8, ipady=8)

        self.icon_label_1 = Label(frame, text='1', image=self.img1)
        self.icon_label_1.grid(row=0, column=0, sticky=NSEW, rowspan=2)
        self.icon_label_2 = Label(frame, text='2', image=self.img2)
        self.icon_label_2.grid(row=2, column=0, sticky=NSEW, rowspan=2)

        user_label = Label(frame, text='Usuario', font=("Arial Bold", 12, 'bold'))
        user_label.grid(row=0, column=1, sticky=W, padx=2)
        self.user_label = Label(frame, bg='black')
        self.user_label.grid(row=1, column=1, sticky=NSEW, columnspan=2)
        user_entry = ttk.Entry(self.user_label, font=("Arial Bold", 12), width=30, textvariable=self.var_user)
        user_entry.grid(row=0, column=0, sticky=W)
        user_entry.focus()

        pass_label = Label(frame, text='Contraseña', font=("Arial Bold", 12, 'bold'))
        pass_label.grid(row=2, column=1, sticky=W, padx=2)
        self.pass_label = Label(frame, bg='black')
        self.pass_label.grid(row=3, column=1, sticky=NSEW, columnspan=2)
        pass_entry = ttk.Entry(self.pass_label, show='*', font=("Arial Bold", 12), width=30, textvariable=self.var_pass)
        pass_entry.grid(row=0, column=0, sticky=W)

        btn_accept = ttk.Button(frame, text='Aceptar', style=self.button_success(), command=self.get_user)
        btn_accept.grid(row=4, column=1, padx=4, pady=10, ipady=2, sticky=EW)

        btn_cancel = ttk.Button(frame, text='Cancelar', style=self.button_danger(), command=self.exit)
        btn_cancel.grid(row=4, column=2, padx=4, pady=10, ipady=2, sticky=EW)

        self.intentos_label = Label(frame, text='Intentos: 3', font=("Arial Bold", 8, 'bold'))
        self.intentos_label.grid(row=5, column=1, sticky=W, columnspan=2)

        self.msg_label = Label(frame, font=("Arial Bold", 10, 'bold'))
        self.msg_label.grid(row=6, column=1, sticky=W, columnspan=2)

    def inputs_login(self):
        return len(self.var_user.get()) != 0 and len(self.var_pass.get()) != 0

    def get_user(self):
        self.intentos_label['text'] = 'Intentos: 3'
        self.msg_label['text'] = ''

        usern = self.var_user.get()
        passw = self.var_pass.get()

        if self.intentos == 2:
            self.intento_cero()
        
        if self.inputs_login():
            self.create_icon()
            db = Login_DB()

            self.icon_label_1['image']=self.img1
            self.icon_label_2['image']=self.img2
            
            # BD
            username = db.search_user(usern)
            password = db.search_pass(passw)

            if username == [] and password == []:
                self.intentos = self.intentos + 1
                self.total_intento = self.total_intento - 1
                
                self.msg_label['text'] = 'Los datos son incorrectos'
                self.msg_label['fg'] = '#D70F21'
                
                self.user_label.config(bg='red')
                self.pass_label.config(bg='red')
            else:
                if username == []:
                    self.intentos = self.intentos + 1
                    self.total_intento = self.total_intento - 1

                    self.msg_label['text'] = 'El usuario es incorrecto'
                    self.msg_label['fg'] = '#D70F21'
                    
                    self.user_label.config(bg='red')

                if password == []:
                    self.intentos = self.intentos + 1
                    self.total_intento = self.total_intento - 1

                    self.msg_label['text'] = 'La contraseña es incorrecta'
                    self.msg_label['fg'] = '#D70F21'

                    self.pass_label.config(bg='red')

                if username != [] and password != []:
                    try:
                        id_user = self.id_user(username)
                        id_rol = self.id_roles_user(username)

                        self.update()
                        self.withdraw()

                        app = Index(id_user, id_rol)
                        db.close()
                    except:
                        print('El id no existe')

                    self.msg_label['text'] = 'Iniciando sesión...'
                    self.msg_label['fg'] = '#009A22'

                    self.icon_label_2['image']=self.img3

                    self.user_label.config(bg='#009A22')
                    self.pass_label.config(bg='#009A22')    

        else:
            self.msg_label['text'] = 'Completa los campos'
            self.msg_label['fg'] = '#D70F21'

            self.user_label.config(bg='red')
            self.pass_label.config(bg='red')

            if len(usern):
                self.user_label.config(bg='black')
                self.pass_label.config(bg='red')
            
            if len(passw):
                self.user_label.config(bg='red')
                self.pass_label.config(bg='black')

            self.intentos = self.intentos + 1
            self.intentos_label['text'] = 'Intentos: 3'
        
        self.intentos_label['text'] = 'Intentos: %s' % self.total_intento
        self.var_pass.set('')

    def intento_cero(self):
        print('Intentos: 0')
        self.intentos = 0
        self.total_intento = 4

    def id_user(self, db_row):
        for row in db_row:
            id = row[0]
            return id

    def id_roles_user(self, db_row):
        for row in db_row:
            idrol = row[3]
            return idrol
            
    def button_success(self):
        style = Style()
        b = style.TButton__success()
        return b

    def button_danger(self):
        style = Style()
        b = style.TButton__danger()
        return b
