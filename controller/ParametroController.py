from tkinter import *
import tkinter as tk

from assets.validation import Validation_Entry, number_validation, text_limiter

class ParametroController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.validar = Validation_Entry(self.view.root)

        self.view.btn_new['command'] = self.new_button
        self.view.btn_save['command'] = self.save_button
        self.view.btn_edit['command'] = self.edit_button
        self.view.btn_delete['command'] = self.delete_button
        self.view.btn_center['command'] = self.center_button

        #self.view.root.mainloop()

    def new_button(self):
        self.view.btn_new['state'] = tk.DISABLED
        self.view.btn_save['state'] = tk.NORMAL
        self.view.btn_edit['state'] = tk.DISABLED
        self.view.btn_delete['state'] = tk.DISABLED
        self.view.btn_center['state'] = tk.DISABLED

        self.normal_entry()

        # Codigo Postal
        self.view.var10.trace("w", lambda *args: text_limiter(self.view.var10, 5))
        self.view.cp_entry['validatecommand'] = (self.view.cp_entry.register(number_validation),'%P','%d')
        
        #self.view.root.mainloop()


    def save_button(self):
        self.nomEmp   = self.view.var1.get()
        self.nomCorto = self.view.var2.get()
        self.rfc      = self.view.var3.get()
        self.noPatrl  = self.view.var4.get()
        self.actPpal  = self.view.var5.get()

        self.calle = self.view.var6.get()
        self.num   = self.view.var7.get()
        self.col   = self.view.var8.get()
        self.mpio  = self.view.var9.get()
        self.cp    = self.view.var10.get()
        self.entFed= self.view.var11.get()
        self.pob   = self.view.var12.get()
        self.tel   = self.view.var13.get()

        if self.entry_validation_general_data() and self.entry_validation_address():
            self.view.lbl1.config(bg='#849797')
            self.view.lbl2.config(bg='#849797')
            self.view.lbl3.config(bg='#849797')
            self.view.lbl4.config(bg='#849797')
            self.view.lbl5.config(bg='#849797')
            self.view.lbl6.config(bg='#849797')
            self.view.lbl7.config(bg='#849797')
            self.view.lbl8.config(bg='#849797')
            self.view.lbl9.config(bg='#849797')
            self.view.lbl10.config(bg='#849797')
            self.view.lbl11.config(bg='#849797')
            self.view.lbl12.config(bg='#849797')
            self.view.lbl13.config(bg='#849797')
            
            self.validar_datos_generales()
        else:
            if len(self.nomEmp) == 0:
                self.view.lbl1.config(bg='red')
            else:
                self.view.lbl1.config(bg='#849797')
            if len(self.nomCorto) == 0:
                self.view.lbl2.config(bg='red')
            else:
                self.view.lbl2.config(bg='#849797')
            if len(self.rfc) == 0:
                self.view.lbl3.config(bg='red')
            else:
                self.view.lbl3.config(bg='#849797')
            if len(self.noPatrl) == 0:
                self.view.lbl4.config(bg='red')
            else:
                self.view.lbl4.config(bg='#849797')
            if len(self.actPpal) == 0:
                self.view.lbl5.config(bg='red')
            else:
                self.view.lbl5.config(bg='#849797')


            if len(self.calle) == 0:
                self.view.lbl6.config(bg='red')
            else:
                self.view.lbl6.config(bg='#849797')
            if len(self.num) == 0:
                self.view.lbl7.config(bg='red')
            else:
                self.view.lbl7.config(bg='#849797')
            if len(self.col) == 0:
                self.view.lbl8.config(bg='red')
            else:
                self.view.lbl8.config(bg='#849797')
            if len(self.mpio) == 0:
                self.view.lbl9.config(bg='red')
            else:
                self.view.lbl9.config(bg='#849797')
            if len(self.cp) == 0:
                self.view.lbl10.config(bg='red')
            else:
                self.view.lbl10.config(bg='#849797')
            if len(self.entFed) == 0:
                self.view.lbl11.config(bg='red')
            else:
                self.view.lbl11.config(bg='#849797')
            if len(self.pob) == 0:
                self.view.lbl12.config(bg='red')
            else:
                self.view.lbl12.config(bg='#849797')
            if len(self.tel) == 0:
                self.view.lbl13.config(bg='red')
            else:
                self.view.lbl13.config(bg='#849797')

            
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

    def entry_validation_general_data(self):
        return (len(self.view.nomEmp_entry.get()) != 0 and len(self.view.nomCorto_entry.get()) != 0 and
            len(self.view.rfc_entry.get()) != 0 and len(self.view.noPatrl_entry.get()) != 0 and
            len(self.view.actPpal_entry.get()) != 0)

    def entry_validation_address(self):
        return (len(self.view.calle_entry.get()) != 0 and len(self.view.num_entry.get()) != 0 and
            len(self.view.col_entry.get()) != 0 and len(self.view.mpio_entry.get()) != 0 and
            len(self.view.cp_entry.get()) != 0 and len(self.view.entFed_entry.get()) != 0 and
            len(self.view.pob_entry.get()) != 0 and len(self.view.tel_entry.get()) != 0)

    def validar_datos_generales(self):
        if self.validar.nombre_empresa(str(self.nomEmp)):
            self.view.lbl1.config(bg='#849797')
        else:
            self.view.lbl1.config(bg='red')
