from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb

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

        self.get_empresa_matriz()

    def _button_save(self):
        self.view.btn_new['state'] = tk.DISABLED
        self.view.btn_save['state'] = tk.NORMAL
        self.view.btn_edit['state'] = tk.DISABLED
        self.view.btn_delete['state'] = tk.DISABLED
        self.view.btn_center['state'] = tk.DISABLED

    def _button_new(self):
        self.view.btn_new['state'] = tk.NORMAL
        self.view.btn_save['state'] = tk.DISABLED
        self.view.btn_edit['state'] = tk.DISABLED
        self.view.btn_delete['state'] = tk.DISABLED
        self.view.btn_center['state'] = tk.DISABLED

    def new_button(self):
        self. _button_save()

        self.normal_entry()

        # Codigo Postal
        self.view.var10.trace("w", lambda *args: text_limiter(self.view.var10, 5))
        self.view.cp_entry['validatecommand'] = (self.view.cp_entry.register(number_validation),'%P','%d')


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
            self.formulario_completo()
            
            #self.validar_datos_generales()

            # Llenar bd
            self.add_dempresa()
        else:
            self.formulario_incompleto()
            
            mb.showwarning('Alerta',
                'Llene todos los campos para continuar')
            
    def edit_button(self):
        pass

    def delete_button(self):
        pass

    def center_button(self):
        pass

    def formulario_completo(self):
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

    def formulario_incompleto(self):
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

    '''def validar_datos_generales(self):
        if self.validar.nombre_empresa(str(self.nomEmp)):
            self.view.lbl1.config(bg='#849797')
        else:
            self.view.lbl1.config(bg='red')'''


    def add_dempresa(self):
        try:
            self.model.capture_company_general_data(self.nomEmp, self.nomCorto, self.rfc, self.noPatrl, self.actPpal)
            self.model.capture_company_address(self.calle, self.num, self.col, self.mpio, self.cp, self.entFed, self.pob, self.tel)

            try:
                # Obtener id de los datos y direccion de la empresa
                id_datos_empresa = self.get_id_datos_empresa()
                id_direc_empresa = self.get_id_direccion_empresa()
                
                # Llenar la tabla de empresas
                self.model.capture_company(id_datos_empresa, id_direc_empresa)

                try:
                    # Obtener id empresa
                    id_empresa = self.get_id_empresa(id_datos_empresa, id_direc_empresa)

                    # Llenar impresa matriz
                    self.model.capture_mother_company(id_empresa)

                    self.bloquear_formulario()
                    self.get_empresa_matriz()
                except:
                    print('No se logro capturar la Empresa Matriz')
            except:
                print('No se logro capturar la Empresa')
        except:
            print('No se logro capturar Los Parametros de Empresas')
        
        
    def get_id_datos_empresa(self):
        db_row = self.model.get_company_general_data(self.rfc)
        for row in db_row:
            id = row[0]
            return id

    def get_id_direccion_empresa(self):
        db_row = self.model.get_company_address(self.cp)
        for row in db_row:
            id = row[0]
            return id

    
    def get_id_empresa(self, id_dato, id_dir):
        db_row = self.model.get_company(id_dato, id_dir)
        for row in db_row:
            id = row[0]
            return id

    

    def get_empresa_matriz(self):
        # Limpiar tabla
        records = self.view.treeview.get_children()
        for element in records:
            self.view.treeview.delete(element)

        # Obtener todas las id de empresas
        db_row = self.model.get_mother_companies()
        for row in db_row:
            self.get_id_datos_empresa_matriz(row[1])  # Obtener id de la empresa matriz
        
    def get_id_datos_empresa_matriz(self, id_emp):
        # Obtener todas id de datos generales
        db_row = self.model.get_company_by_id(id_emp)
        for row in db_row:
            #print(self.get_nombre_empresa_matriz(row[1]))   # Obtener id datos generales de la empreza matriz
            self.get_nombre_empresa_matriz(row[1])

    def get_nombre_empresa_matriz(self, id_dato):
        # Obtener todos los nombres de la empresa
        db_row = self.model.get_data_company_by_id(id_dato)
        for row in db_row:
            name = row[1] # Obtener nombre de la empreza matriz
            self.view.treeview.insert('', 0, text='', values=(name, ))


    def bloquear_formulario(self):
        self.view.nomEmp_entry.delete(0, END)
        self.view.nomCorto_entry.delete(0, END)
        self.view.rfc_entry.delete(0, END)
        self.view.noPatrl_entry.delete(0, END)
        self.view.actPpal_entry.delete(0, END)
        self.view.calle_entry.delete(0, END)
        self.view.num_entry.delete(0, END)
        self.view.col_entry.delete(0, END)
        self.view.mpio_entry.delete(0, END)
        self.view.cp_entry.delete(0, END)
        self.view.entFed_entry.delete(0, END)
        self.view.pob_entry.delete(0, END)
        self.view.tel_entry.delete(0, END)

        self.view.disabled_entry()

        self._button_new()
