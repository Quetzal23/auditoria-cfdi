from tkinter import *

class IndexController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.get_user()
        self.command_menu()

    def get_user(self):
        id_user = self.view.id_user
        id_rol = self.view.id_rol
        
        db_row = self.model.exists_user(id_user, id_rol)
        if db_row == []:
            print('Vacio')
        else:
            for row in db_row:
                self.view.user_label['text'] = 'Usuario Actual: %s' % row[1]
                idrol = row[3]

            if idrol == 1:
                self.view.nivel_label['text'] = 'Administrador'
            if idrol == 2:
                self.view.nivel_label['text'] = 'Supervisor'
            if idrol == 3:
                self.view.nivel_label['text'] = 'Operador'

    def command_menu(self):
        pass