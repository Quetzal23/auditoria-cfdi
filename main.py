import tkinter as tk

from views.accesar_sistema.login import Login
from views.index import Index

def main():
    #app = Login()
    app = Index(1, 1)
    app.mainloop()

if __name__ == '__main__':
    main()
