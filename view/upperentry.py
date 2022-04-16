from tkinter import *

class UpperEntry(Entry):
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



'''
https://es.stackoverflow.com/questions/356082/como-lograr-poner-may%C3%BAscula-en-los-campos-de-tipo-entry-y-formatear-n%C3%BAmeros-en-p
'''