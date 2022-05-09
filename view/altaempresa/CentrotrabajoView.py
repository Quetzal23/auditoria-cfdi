import tkinter as tk

from assets.options import Window_Center, UpperEntry
from assets.styles import Style

class CentroTrabajoView:
    def on_closing(self):
        self.root.destroy()

    def __init__(self, root, id_empresa):
        super().__init__()
        self.root = root

        nempresa = 'S'

        wind_width  = 898#900
        wind_height = 410#390

        wind = Window_Center(self.root)
        self.style = Style()

        self.root.grab_set()
        self.root.focus_force()

        self.root.geometry(wind.center(wind_width, wind_height))
        self.root.title('CATALOGOS DE CENTROS - %s ' % nempresa)
        self.root.resizable(0, 0)
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)