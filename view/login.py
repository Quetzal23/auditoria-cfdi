from tkinter import *

from db import Database
from view.index import Index

from info import Info

import time

class Login:
    db = Database('auditoria.db')
    info = Info()

    def __init__(self, window):
        self.wind = window
        
        self.time = self.info.get_cancuntime()
        #
        #self.ip = self.info.get_publicIP()
        self.ip = self.info.get_ipv4()
        self.so = self.info.get_os()

        self.intentos = 3

        wind_width  = 390
        wind_height = 200

        wind_x =  self.wind.winfo_screenwidth() // 2 - wind_width // 2
        wind_y = self.wind.winfo_screenheight() // 2 - wind_height // 2

        wind_pos = str(wind_width) + "x" + str(wind_height) + "+" + str(wind_x) + "+" + str(wind_y)
        self.wind.geometry(wind_pos)

        self.wind.resizable(0, 0)
        self.wind.title('Inicio de sesión')
        
        main_frame = LabelFrame(self.wind, relief='flat')
        main_frame.grid(row=0, column=0, columnspan=3, pady=18, padx=18)

        self.create_widgets(main_frame)
    
    def create_widgets(self, wind):
        self.frame = wind
        # Username [row=0]
        username_label = Label(self.frame, text='USUARIO:', font=("Arial Bold", 12))
        username_label.grid(column=0, row=0, sticky=W, padx=5, pady=5)  #padx=5, pady=5

        self.username_entry = Entry(self.frame, font=("Arial Bold", 12))
        self.username_entry.grid(column=1, row=0, sticky=E, padx=5, pady=5)
        self.username_entry.focus()
        # Password [row=1]
        password_label = Label(self.frame, text="CONTRASEÑA:", font=("Arial Bold", 12))
        password_label.grid(column=0, row=1, sticky=W, padx=5, pady=5)  #padx=5, pady=5

        self.password_entry = Entry(self.frame,  show="*", font=("Arial Bold", 12))
        self.password_entry.grid(column=1, row=1, sticky=E, padx=5, pady=5)
        # Mensaje [row=2]
        self.message_label = Label(self.frame, text='')
        self.message_label.config(width=47, anchor=NW)
        self.message_label.grid(column=0, row=2, columnspan=2, padx=5, pady=5)
        # login button [row=3]
        self.login_button = Button(self.frame, text="ACCEDER", font=("Arial Bold", 12), command=self.user_verification)    #command=self.get_users
        self.login_button.grid(column=1, row=3, sticky=E, padx=5, pady=5)

    def input_login_validation(self):
        return len(self.username_entry.get()) != 0 and len(self.password_entry.get()) != 0

    def user_verification(self):
        self.message_label['text'] = ''

        nuser = self.username_entry.get()
        passw = self.password_entry.get()

        username = self.db.search_user(nuser)
        password = self.db.search_pass(passw)
        #self.logins(0)

        if self.input_login_validation():
            if username == [] and password == []:      # False
                self.message_label['text'] = 'USUARIO Y/O CONTRASEÑA INCORRECTOS'
                self.message_label['fg'] = '#D70F21'
                #Guardar Intento Fallido
                self.intentos -= 1
                self.logins(3)
                self.clear_text()
            else:
                #print(username[0][1])      # Nombre de usuario
                if username == []:
                    self.message_label['text'] = 'USUARIO INCORRECTO'
                    self.message_label['fg'] = '#D70F21'
                    #Guardar Intento Fallido
                    self.intentos -= 1
                    self.logins(1)
                    self.clear_text()

                if password == []:
                    self.message_label['text'] = 'CONTRASEÑA INCORRECTA'
                    self.message_label['fg'] = '#D70F21'
                    #Guardar Intento Fallido
                    self.intentos -= 1
                    self.logins(2)
                    self.clear_text()
                '''
                else:
                    self.user_i = username[0][0]   # get_id
                    self.user_n = username[0][1]
                '''

                if username != [] and password != []:
                    self.message_label['text'] = 'INICIANDO SESIÓN'
                    self.message_label['fg'] = '#009A22'
                    #Guardar Intento Exitoso
                    self.intentos = 3
                    self.logins(0)
                    
                    #self.wind.destroy()
                    self.new_window()

        else:
            self.message_label['text'] = 'LLENE TODAS LAS CASILLAS'
            self.message_label['fg'] = '#D70F21'

    def new_window(self):
        self.db.__del__()
        self.wind.update()
        time.sleep(0.02)

        self.wind.withdraw()

        window = Toplevel()
        index = Index(window)

    def clear_text(self):
        self.password_entry.delete(0, END)


    def logins(self, fail):
        username = self.username_entry.get()

        if fail == 0:
            action = 'loginOK'

        elif fail == 1:
            action = 'loginFailInvalidUsername'
        elif fail == 2:
            action = 'loginFailInvalidPassword'
            #self.db.add_login_failed(usid, user, time, ip)
        else:
            action = 'loginFailInvalidUsernameANDPassword'

        self.db.add_logins(self.time, fail, action, username, self.ip, self.so)
        
        #print(action)

