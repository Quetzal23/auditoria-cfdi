from tkinter import NSEW, W, Frame, Label
from tkinter.ttk import LabelFrame

from views.options import Window_Center

class Login(Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.wind = parent

        width=480
        height=280

        wind = Window_Center(self.wind)

        self.wind.geometry(wind.center(width, height))
        self.wind.resizable(0,0)
        self.wind.title('INICIO DE SESIÓN DE USUARIO')
        self.wind.protocol("WM_DELETE_WINDOW", self.exit)

        self.create_widgets()


    def exit(self):
        self.wind.destroy()
        self.wind.quit()

    def create_widgets(self):
        frame = LabelFrame(self.wind)
        frame.grid(row=0, column=0, sticky=NSEW, padx=4, pady=4)

        '''
        icon_label_1 = Label(frame, text='1')
        icon_label_1.grid(row=0, column=0,)
        icon_label_2 = Label(frame, text='2')
        icon_label_2.grid(row=2, column=0,)
        '''

        user_label = Label(frame, text='Usuario')
        user_label.grid(row=0, column=0, sticky=W)
        pass_label = Label(frame, text='Contraseña')
        pass_label.grid(row=2, column=0, sticky=W)