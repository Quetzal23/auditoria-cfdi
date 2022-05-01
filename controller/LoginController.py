from tkinter import *

class LoginController:
    intentos = 0
    total_intento = 3

    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.btn_accept['command'] = self.get_entry
    
    def entry_validation(self):
        return len(self.view.var_user.get()) != 0 and len(self.view.var_pass.get()) != 0

    def get_entry(self):
        username = self.view.var_user.get()
        userpass = self.view.var_pass.get()

        db_username = self.model.search_user(username)
        db_userpass = self.model.search_pass(userpass)

        if self.intentos >= 3:
            self.total_intento_cero()

        if self.entry_validation():
            self.view.create_icon()
            self.view.icon_label_1['image'] = self.view.img1
            self.view.icon_label_2['image'] = self.view.img2

            if db_username == [] and db_userpass == []:
                self.intentos = self.intentos + 1
                self.total_intento = self.total_intento - 1
                
                self.view.msg_label['text'] = 'Los datos son incorrectos'
                self.view.msg_label['fg'] = '#D70F21'
                
                self.view.user_label.config(bg='red')
                self.view.pass_label.config(bg='red')
            else:
                if db_username == []:
                    self.intentos = self.intentos + 1
                    self.total_intento = self.total_intento - 1

                    self.view.msg_label['text'] = 'El usuario es incorrecto'
                    self.view.msg_label['fg'] = '#D70F21'
                    
                    self.view.user_label.config(bg='red')

                if db_userpass == []:
                    self.intentos = self.intentos + 1
                    self.total_intento = self.total_intento - 1

                    self.view.msg_label['text'] = 'La contraseña es incorrecta'
                    self.view.msg_label['fg'] = '#D70F21'

                    self.view.pass_label.config(bg='red')

                if db_username != [] and db_userpass != []:
                    self.view.msg_label['text'] = 'Iniciando sesión...'
                    self.view.msg_label['fg'] = '#009A22'

                    self.view.icon_label_2['image'] = self.view.img3

                    self.view.user_label.config(bg='#009A22')
                    self.view.pass_label.config(bg='#009A22')

                    self.successful(db_username)

        else:
            self.view.msg_label['text'] = 'Completa los campos'
            self.view.msg_label['fg'] = '#D70F21'
            self.view.user_label.config(bg='red')
            self.view.pass_label.config(bg='red')

            if len(username):
                self.view.user_label.config(bg='#849797')
                self.view.pass_label.config(bg='red')

            if len(userpass):
                self.view.user_label.config(bg='red')
                self.view.pass_label.config(bg='#849797')

            self.intentos = self.intentos + 1
            self.view.intentos_label['text'] = 'Intentos: 3'
        
        self.view.intentos_label['text'] = 'Intentos: %s' % self.total_intento
        self.view.var_pass.set('')
    
    def total_intento_cero(self):
        self.view.var_pass.set('')
        self.view.btn_accept['state'] = DISABLED
        
        self.remaining = 0
        self.countdown(5)

    def countdown(self, remaining=None):
        if remaining is not None:
            self.remaining = remaining
 
        elif self.remaining == 100:
            return
        if self.remaining <= 0:
            self.fin_temporizador()
        else:
            self.view.intentos_label['text'] = "Espere por %d seg" % self.remaining
            self.remaining = self.remaining - 1
            self.view.root.after(1000, self.countdown)

    def fin_temporizador(self):
            self.view.intentos_label['text'] = ''
            self.intentos = 0
            self.total_intento = 3
            
            self.view.btn_accept['state'] = NORMAL
            self.view.intentos_label['text'] = 'Intentos: %s' % self.total_intento

    def id_user(self, db_row):
        for row in db_row:
            id = row[0]
            return id

    def id_roles_user(self, db_row):
        for row in db_row:
            idrol = row[3]
            return idrol

    def successful(self, username):
        id_user = self.id_user(username)
        id_rol = self.id_roles_user(username)

        print(id_user)
        print(id_rol)
        
        self.model.close()