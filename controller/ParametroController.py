from tkinter import *
import tkinter as tk

class ParametroController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.btn_new['command'] = self.new_button
        self.view.btn_save['command'] = self.save_button
        self.view.btn_edit['command'] = self.edit_button
        self.view.btn_delete['command'] = self.delete_button
        self.view.btn_center['command'] = self.center_button

    def new_button(self):
        self.view.btn_new['state'] = tk.DISABLED
        self.view.btn_save['state'] = tk.NORMAL
        self.view.btn_edit['state'] = tk.DISABLED
        self.view.btn_delete['state'] = tk.DISABLED
        self.view.btn_center['state'] = tk.DISABLED

        self.normal_entry()

    def save_button(self):
        pass

    def edit_button(self):
        pass

    def delete_button(self):
        pass

    def center_button(self):
        pass

    def normal_entry(self):
        self.view.nomEmp_entry.config(state='normal')
        self.view.nomEmp_entry.focus()
        self.view.nomCorto_entry.config(state='normal')
        self.view.rfc_entry.config(state='normal')
        self.view.noPatrl_entry.config(state='normal')
        self.view.actPpal_entry.config(state='normal')
        self.view.calle_entry.config(state='normal')
        self.view.num_entry.config(state='normal')
        self.view.col_entry.config(state='normal')
        self.view.mpio_entry.config(state='normal')
        self.view.cp_entry.config(state='normal')
        self.view.entFed_entry.config(state='normal')
        self.view.pob_entry.config(state='normal')
        self.view.tel_entry.config(state='normal')