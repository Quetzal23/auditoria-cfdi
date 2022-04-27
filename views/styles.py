from tkinter import * 
from tkinter import ttk 

class Style:
    def __init__(self):
        self.style = ttk.Style()
        #print(self.style.theme_names())
        #print(self.style.theme_use())

    
    def Treeview(self):
        a = "style.Treeview"
        self.style.configure(a, highlightthickness=0, bd=0, font=('Calibri', 11))
        self.style.configure("style.Treeview.Heading", font=('Calibri', 13,'bold'))
        self.style.layout(a, [('style.Treeview.treearea', {'sticky': 'nswe'})])
        return a

    def TButton__danger(self):
        a = "danger.TButton"
        self.style.configure(a, foreground="#ff0000")
        return a
        
    def TButton__success(self):
        a = "success.TButton"
        self.style.configure(a, foreground="#26A042")
        return a