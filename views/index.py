import tkinter as tk
from tkinter import Menu
from tkinter.messagebox import showinfo

from views.options import Window_Center
from views.registro_empresa.parametro_empresa import Parametro_Empresa

class Index(tk.Tk):
    def __init__(self, id):
        super().__init__()
        self.id_user = id

        width=1000
        height=600

        wind = Window_Center(self)
        self.title('AUDITORIA-CFDI *DEMO*')
        self.geometry(wind.center(width, height))
        self.state('zoomed')
        self.protocol("WM_DELETE_WINDOW", self.exit)
        
        self.create_widgets()

    def exit(self):
        self.destroy()
        self.quit()

    def about(self):
        showinfo('Acerca de...', 
            'Sistema de auditoria para determinar las cuotas obrero patronales')

    def create_widgets(self):
        self.menu_bar()
        
    def menu_bar(self):
        menubar = Menu(self)
        self.config(menu=menubar)
        
        filemenu = Menu(menubar, tearoff=0)
        editionmenu = Menu(menubar, tearoff=0)
        viewmenu = Menu(menubar, tearoff=0)
        infomenu = Menu(menubar, tearoff=0)
        catalogmenu = Menu(menubar, tearoff=0)
        auditmenu = Menu(menubar, tearoff=0)
        reportmenu = Menu(menubar, tearoff=0)
        processmenu = Menu(menubar, tearoff=0)
        helpmenu = Menu(menubar, tearoff=0)

        file_conf = Menu(menubar, tearoff=0)
        file_props = Menu(menubar, tearoff=0)
        file_config = Menu(menubar, tearoff=0)

        menubar.add_cascade(label='Archivo', menu=filemenu)
        menubar.add_cascade(label='Editar' ,menu=editionmenu)
        menubar.add_cascade(label='Ver' ,menu=viewmenu)
        menubar.add_cascade(label='Información' ,menu=infomenu)
        menubar.add_cascade(label='Catálogo' ,menu=catalogmenu)
        menubar.add_cascade(label='Auditoría' ,menu=auditmenu)
        menubar.add_cascade(label='Reportes' ,menu=reportmenu)
        menubar.add_cascade(label='Procesos' ,menu=processmenu)
        menubar.add_cascade(label='Ayuda', menu=helpmenu)

        filemenu.add_cascade(label='Empresas', menu=file_conf)
        filemenu.add_command(label='Cerrar Empresa')
        filemenu.add_command(label='Cambio de Periodo')
        filemenu.add_separator()
        filemenu.add_command(label='Contadores Públicos')
        filemenu.add_command(label='Usuarios')
        filemenu.add_separator()
        filemenu.add_command(label='Configurar Impresión')
        filemenu.add_separator()
        filemenu.add_cascade(label='Utilerías', menu=file_props)
        filemenu.add_separator()
        filemenu.add_cascade(label='Configuración Sistema', menu=file_config)
        filemenu.add_separator()
        filemenu.add_command(label='Cerrar Sesión')
        filemenu.add_command(label='Salir', command=exit)

        file_conf.add_command(label='Configuración...', command=self.menu_conf__config)
        file_props.add_command(label='')
        file_config.add_command(label='')

        helpmenu.add_command(label='Acerca de', command=self.about)

    def menu_conf__config(self):
        parametro_empresa = Parametro_Empresa(self)
        parametro_empresa.grab_set()
        parametro_empresa.focus_force()
        parametro_empresa.mainloop()    