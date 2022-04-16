from tkinter import *

from view.acceso.login import Login
from view.index import Index

from view.registroEmpresa.parametro_empresa import Parametros_Empresas
from view.registroEmpresa.catalogo_trabajo import Catalogo_Centro
from view.menuArchivo.contadores_publicos import Contadores_Publicos
from view.menuArchivo.usuraios import Usuarios

'''
# Views #
Parametros_Empresas(window)
Catalogo_Centro(window)
'''

if __name__ == '__main__':
    window = Tk()
    #login = Login(window)
    index = Index(window)

    #s = Usuarios(window)

    window.mainloop()