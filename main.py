from tkinter import *

from view.login import Login
from view.index import Index

if __name__ == '__main__':
    window = Tk()
    #login = Login(window)
    index = Index(window)
    window.mainloop()