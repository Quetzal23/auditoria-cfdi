import re
from tkinter import END, Tk
import tkinter

class Validation_Entry:
    def __init__(self, root):
        self.root = root

    def set_telefono(self, entryTelefono):
        self.entryTelefono = entryTelefono

    def tel_validation(self, event):
        if event.char.isdigit():
            texto = self.entryTelefono.get()
            letras = 0
            for i in texto:
                letras +=1                                  
            if len(texto) == 0:                             
                self.entryTelefono.insert(0,"(")
            if letras == 4:     
                self.entryTelefono.insert(4,")-")
            elif letras == 9:
                self.entryTelefono.insert(9,"-")
            elif letras == 12:
                self.entryTelefono.insert(12,"-")
        else:
            return "break"

        
    def nombre_empresa(self, cadena):
        pattern = '[a-zA-Z]+'
        if re.match(pattern, cadena):
            return True

    

def text_limiter(entry_text, leng):
    if len(entry_text.get()) > 0:
        entry_text.set(entry_text.get()[:leng])

def number_validation(inStr, acttyp):
    if acttyp == '1':
        if not inStr.isdigit():
            return False
    return True