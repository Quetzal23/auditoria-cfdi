from tkinter import * 
from tkinter import ttk 

class Style:
    def __init__(self):
        self.style = ttk.Style()
        #print(self.style.theme_names())
        #print(self.style.theme_use())
        
        self.font = 'Arial Bold'
        self.fontsize_title = 12
        self.fontsize_cont = 8
        self.fontsize_msg = 10

        self.color__normal = '#849797'
        self.color__success = '#009A22'    #26A042'
        self.color__danger = '#ff0000'  #'#D70F21'
        self.color__title = 'blue'

    
    def Treeview(self):
        a = "style.Treeview"
        self.style.configure(a, highlightthickness=0, bd=0, font=(self.font, 11))
        self.style.configure("style.Treeview.Heading", font=(self.font, 13, 'bold'))
        self.style.layout(a, [('style.Treeview.treearea', {'sticky': 'nswe'})])
        return a

    def TButton__danger(self):
        a = "danger.TButton"
        self.style.configure(a, foreground=self.color__danger)
        return a
        
    def TButton__success(self):
        a = "success.TButton"
        self.style.configure(a, foreground=self.color__success)
        return a

    def TNotebook_Tab(self):
        a = "TNotebook.Tab"
        self.style.configure(a, padding=[2, 2], font=(self.font, 10))
        self.style.map(a, foreground= [("selected", self.color__title)])