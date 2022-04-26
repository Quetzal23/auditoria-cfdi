from tkinter import Tk

from views.accesar_sistema.login import Login
from views.index import Index

if __name__ == '__main__':
    window = Tk()
    #wind = Index(window)
    ini = Login(window)
    window.mainloop()
