import time
from tkinter import LEFT, RIGHT, Label, LabelFrame, Menu
from tkinter.messagebox import showinfo

from assets.options import Window_Center

import route

class IndexView:
    def exit(self):
        self.root.destroy()
        self.root.quit()

    def __init__(self, root, id_user, id_rol):
        super().__init__()
        self.root = root
        self.id_user = id_user   #id usuario
        self.id_rol = id_rol

        width=1000
        height=600
        
        wind = Window_Center(self.root)

        self.root.title('AUDITORIA-CFDI *DEMO*')
        self.root.geometry(wind.center(width, height))
        self.root.state('zoomed')
        self.root.protocol("WM_DELETE_WINDOW", self.exit)

        self.create_widgets()

    def about(self):
        showinfo('Acerca de...', 
            'Sistema de auditoria para determinar las cuotas obrero patronales')

    def create_widgets(self):
        self.menu_bar()
        self.header()
        self.content()
        self.footer()

    def menu_bar(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        
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

    def header(self):
        header_frame = LabelFrame(self.root, bg='green', height=30)
        header_frame.pack(fill='both')

    def content(self):
        content_frame = LabelFrame(self.root)
        content_frame.pack(fill='both', expand=True)

    def footer(self):
        footer_frame = LabelFrame(self.root, height=30)
        footer_frame.pack(fill='both', side='bottom')

        self.user_label = Label(footer_frame, text='Usuario Actual: ', width=30, anchor='w')
        self.user_label.pack(side=LEFT, padx=5, pady=5)

        self.nivel_label = Label(footer_frame, text='Usuario Actual: ', width=24, anchor='w')
        self.nivel_label.pack(side=LEFT, padx=5, pady=5)

        self.hour_label = Label(footer_frame, width=6, anchor='w')
        self.hour_label.pack(side=RIGHT, padx=5, pady=5)

        self.times()

    def times(self):
        current_time = time.strftime("%H:%M:%S") 
        self.hour_label.config(text=current_time)
        self.hour_label.after(200, self.times)

    def menu_conf__config(self):
        route.parametro_empresas()