from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import Treeview

#from db import *

from view.index_parametro_empresa import Parametros_Empresas

class Index:
    #db = Database('auditoria.db')

    def exit(self):
        self.wind.destroy()
        self.wind.quit()

    def acerca_de(self):
        showinfo('Acerca de...', 
            'Sistema de auditoria para determinar las cuotas obrero patronales')

    def __init__(self, window):
        self.wind = window
        self.wind.state('zoomed')
        self.wind.title('Auditoria-CFDI * DEMO *')
        self.wind.protocol("WM_DELETE_WINDOW", self.exit)

        self.create_widgets(self.wind)
    
    def create_widgets(self, wind):
        menubar = self.menu_bar(wind)

    def menu_bar(self, wind):
        menubar = Menu(wind)
        wind.config(menu=menubar)

        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Archivo', menu=filemenu)
        confmenu = Menu(menubar, tearoff=0)
        confmenu.add_command(label='Configuración ...', command=self.parametros_empresas)   #command=self.parametros_empresas
        filemenu.add_cascade(label='Empresas', menu=confmenu)
        filemenu.add_command(label='Cerrar Empresa')
        filemenu.add_separator()
        filemenu.add_command(label="Cerrar Sesión")
        filemenu.add_command(label="Salir", command=wind.quit)

        editmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Editar', menu=editmenu)

        helpmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Ayuda', menu=helpmenu)
        helpmenu.add_command(label="Ayuda")
        filemenu.add_separator()
        helpmenu.add_command(label="Acerca de...", command=self.acerca_de)
    
    def parametros_empresas(self):
        toplevel = Toplevel()
        toplevel.grab_set()
        #toplevel.focus_set()
        #toplevel.grab_set_global()
        parametro = Parametros_Empresas(toplevel)
        
        