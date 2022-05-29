from tkinter import *
import tkinter as tk
from tkinter import ttk 

from tkcalendar import DateEntry
from datetime import datetime
import time

class Window_Center(Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.wind = master

    def center(self, wind_width, wind_height):
        x_wind = self.wind.winfo_screenwidth() // 2 - wind_width // 2
        y_wind = self.wind.winfo_screenheight() // 2 - wind_height // 2
        position = str(wind_width) + "x" + str(wind_height) + "+" + str(x_wind) + "+" + str(y_wind)
        return position

class CustomDateEntry(DateEntry):
    def _select(self, event=None):
        date = self._calendar.selection_get()
        if date is not None:
            self._set_text(date.strftime('%d/%m/%Y'))
            self.event_generate('<<DateEntrySelected>>')
        self._top_cal.withdraw()
        if 'readonly' not in self.state():
            self.focus_set()
        
class UpperEntry(ttk.Entry):
    def __init__(self, parent, *args, **kwargs):
        self._var = kwargs.get("textvariable") or StringVar(parent)
        super().__init__(parent, *args, **kwargs)
        self.configure(textvariable=self._var)
        self._to_upper()

    def config(self, cnf=None, **kwargs):
        self.configure(cnf, **kwargs)

    def configure(self, cnf=None, **kwargs):
        var = kwargs.get("textvariable")
        if var is not None:
            var.trace_add('write', self._to_upper)
            self._var = var
        super().config(cnf, **kwargs)

    def __setitem__(self, key, item):
        if key == "textvariable":
            item.trace_add('write', self._to_upper)
            self._var = item
        super.__setitem__(key, item)

    def _to_upper(self, *args):
        self._var.set(self._var.get().upper())

class Info_System():
    def __init__(self):
        self.time = datetime.now()

    def get_hour(self):
        hour = '%s:%s:%s' % (self.time.hour, self.time.month, self.time.second)
        return hour

    def times():
        current_time=time.strftime("%H:%M:%S")
        return current_time