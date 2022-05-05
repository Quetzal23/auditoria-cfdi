from tkinter import *

from controller.LoginController import LoginController
from model.LoginModel import LoginModel
from view.acceso.LoginView import LoginView

from controller.IndexController import IndexController
from model.IndexModel import IndexModel
from view.IndexView import IndexView

from controller.ParametroController import ParametroController
from model.ParametroModel import ParametroModel
from view.altaempresa.ParametroView import ParametroView

def login():
    root = Tk()
    view = LoginView(root)
    model = LoginModel()
    controller = LoginController(model, view)
    root.mainloop()

def index(id_user, id_rol=()):
    root = Tk()
    view = IndexView(root, id_user, id_rol)
    model = IndexModel()
    controller = IndexController(model, view)
    #root.mainloop() # Eliminar despues de acabar con las pruebas, Desactivar al iniciar con el login

def parametro_empresas():
    root = Toplevel()
    view = ParametroView(root)
    model = ParametroModel()
    controller = ParametroController(model, view)
    #root.mainloop() # Eliminar despues de acabar con las pruebas, Desactivar al iniciar con el login