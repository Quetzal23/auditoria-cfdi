from tkinter import *
import tkinter as tk

from controller.LoginController import LoginController
from model.LoginModel import LoginModel
from view.acceso.LoginView import LoginView

def login():
    view = LoginView(root)
    model = LoginModel()
    controller = LoginController(model, view)
    root.mainloop()

if __name__ == '__main__':
    root = Tk()
    login()