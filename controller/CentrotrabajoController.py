from datetime import date

from assets.options import CustomDateEntry


class CentroTrabajoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        style = self.view.style
        self.color_danger = style.color__danger
        self.color_success = style.color__success

        self.fIniAct_entry = CustomDateEntry(self.view.lbl2, selectmode='day')
        self.fIniAud_entry = CustomDateEntry(self.view.lbl5, selectmode='day')
        self.fFinAud_entry = CustomDateEntry(self.view.lbl6, selectmode='day')
        self.fElabDi_entry = CustomDateEntry(self.view.lbl7, selectmode='day')

        self.fIniAct_entry._set_text(self.fIniAct_entry._date.strftime('%d/%m/%Y'))
        self.fIniAud_entry._set_text(self.fIniAud_entry._date.strftime('%d/%m/%Y'))
        self.fFinAud_entry._set_text(self.fFinAud_entry._date.strftime('%d/%m/%Y'))
        self.fElabDi_entry._set_text(self.fElabDi_entry._date.strftime('%d/%m/%Y'))
        #self.form_disable()

        self.tipo_guardado = 0

        self.id_mother_company = self.view.id_empresa

        self.view.btn_new['command'] = self.new_button
        self.view.btn_save['command'] = self.save_button
        self.view.btn_edit['command'] = self.edit_button
        self.view.btn_delete['command'] = self.delete_button
        self.view.btn_print['command'] = self.print_button

        self.view.treeview.bind ('<<TreeviewSelect>>', self._on_tree_select)
        self.get_empresas()
    
    def new_button(self):
        self.view.msg_label['text'] = ''
        self.tipo_guardado = 1

        self.dateentry_forget()
        self.view.limpiar_formulario()
        self.view.normal_entry()
        self.view.form_pack()

        self.view._button_save()

    def save_button(self):
        # Datos Generales
        self.regPtrl = self.view.var1.get()
        #self.fIniAct = self.view.var2.get()
        self.contPub = self.view.var3.get()
        #self.view.var4.get()
        #self.fIniAud = self.view.var5.get()
        #self.fFinAud = self.view.var6.get()
        #self.fElabDi = self.view.var7.get()
        self.actPrin = self.view.var8.get()
        
        # Direccion
        self.calle = self.view.var9.get()
        self.num = self.view.var10.get()
        self.col = self.view.var11.get()
        self.mpio = self.view.var12.get()
        self.cp = self.view.var13.get()
        self.entFed = self.view.var14.get()
        self.poblac = self.view.var15.get()
        self.telefo = self.view.var16.get()

        # Representante Legal
        self.nomRepL = self.view.var17.get()
        self.puesto = self.view.var18.get()
        self.noEscPodNot = self.view.var19.get()
        self.fCertPNot = self.view.var20.get()
        self.noNota = self.view.var21.get()

        if self.entry_validation_general_data() and self.entry_validation_address():
            self.view.formulario_completo()
            #self.validar_datos_generales()

            '''if self.tipo_guardado == 1:
                self.add_empresa_matriz() # Llenar Datos Generales y Direccion en la bd'''
            if self.tipo_guardado == 2:
                self.edit_empresa() # Editar Datos Generales y Direccion en la bd
            
            self.tipo_guardado = 0
        else:
            #self.view.formulario_incompleto()
            #self.view.alert()
            print('Error')

    
    def entry_validation_general_data(self):
        return (len(self.view.regPtrl_entry.get()) != 0 and len(self.view.fIniAct_entry.get()) != 0 and
            len(self.view.contPub_entry.get()) != 0 and len(self.view.fIniAud_entry.get()) != 0 and
            len(self.view.fFinAud_entry.get()) != 0 and len(self.view.fElabDi_entry.get()) != 0 and
            len(self.view.actPrin_entry.get()) != 0)
    
    def entry_validation_address(self):
        return (len(self.view.calle_entry.get()) != 0 and len(self.view.num_entry.get()) != 0 and
            len(self.view.col_entry.get()) != 0 and len(self.view.mpio_entry.get()) != 0 and
            len(self.view.cp_entry.get()) != 0 and len(self.view.entFed_entry.get()) != 0 and
            len(self.view.pob_entry.get()) != 0 and len(self.view.tel_entry.get()) != 0)


    def edit_button(self):
        self.tipo_guardado = 2
        self.view._button_edit()
        self.view.normal_entry()

        self.form_normal()
    
    def delete_button(self):
        pass

    def print_button(self):
        pass


    def _on_tree_select(self, a):
        self.view.bloquear_formulario()
        
        curItem = self.view.treeview.focus()
        self.selected = self.view.treeview.item(curItem, 'text') # Obtener id de la empresa
        
        self.view._select_company()

        # Imprimir formulario
        self.imprimir_formulario(self.selected)

    # Llenar treeview de las empresas matriz
    def get_empresas(self):
        records = self.view.treeview.get_children()
        for element in records: # Limpiar tabla
            self.view.treeview.delete(element)
        
        empresa_matriz = self.model.get_company_by_id(self.id_mother_company)
        for row in empresa_matriz:
            id_empresa = row[0]
            id_datos = row[1]
            #id_direc = row[2]
            datos = self.model.get_company_general_data_by_id(id_datos)

            for emp_matriz in datos:
                name = emp_matriz[1] # Obtener nombre de la empreza matriz
                self.view.treeview.insert('', 0, text=id_empresa, values=(name, ))  # Llenar el treeview

    # Llenar el formulario
    def imprimir_formulario(self, selected):
        self.view.dateentry_forget()    # Desactivar los DateEntry de la vista
        self.form_pack()    # Acticvar el DateEntry del Controlador

        db_row = self.model.get_company_by_id(selected)
        for row in db_row:
            self.form_datosgenerales(row[1])
            self.form_direccion(row[2])
            self.form_representante_legal(row[3])
        self.form_disable()
    
    def form_datosgenerales(self, id_datos):
        db_row = self.model.get_company_general_data_by_id(id_datos)
        for row in db_row:
            self.view.var1.set(row[4])
            self.fIniAct_entry.set_date(row[6])
            self.view.var3.set(row[8])
            self.fIniAud_entry.set_date(row[10])
            self.fFinAud_entry.set_date(row[11])
            self.fElabDi_entry.set_date(row[7])
            #self.view.var7.set(row[7])
            self.view.var8.set(row[5])
        self.form_disable()

    

    def form_direccion(self, id_direccion):
        db_row = self.model.get_company_address_by_id(id_direccion)
        for row in db_row:
            self.view.var9.set(row[1])
            self.view.var10.set(row[2])
            self.view.var11.set(row[3])
            self.view.var12.set(row[4])
            self.view.var13.set(row[5])
            self.view.var14.set(row[6])
            self.view.var15.set(row[7])
            self.view.var16.set(row[8])

    def form_representante_legal(self, id_representante):
        db_row = self.model.get_legal_representative_by_id(id_representante)
        for row in db_row:
            self.view.var17.set(row[1])
            self.view.var18.set(row[2])
            self.view.var19.set(row[3])
            self.view.var20.set(row[4])
            self.view.var21.set(row[5])


    # Editar empresa
    def edit_empresa(self):
        # Datos Generales
        regPtrl = self.view.regPtrl_entry.get()
        fIniAct = self.fIniAct_entry.get()
        contPub = self.view.contPub_entry.get()
        #self.view.var4.get()
        fIniAud = self.fIniAud_entry.get()
        fFinAud = self.fFinAud_entry.get()
        fElabDi = self.fElabDi_entry.get()
        actPrin = self.view.actPrin_entry.get()
        
        # Direccion
        calle = self.view.calle_entry.get()
        num = self.view.num_entry.get()
        col = self.view.col_entry.get()
        mpio = self.view.mpio_entry.get()
        cp = self.view.cp_entry.get()
        entFed = self.view.entFed_entry.get()
        poblac = self.view.pob_entry.get()
        telefo = self.view.tel_entry.get()

        # Representante Legal
        nomRepL = self.view.nomRepL_entry.get()
        puesto = self.view.puesto_entry.get()
        noEscPodNot = self.view.noEscPodNot_entry.get()
        fCertPNot = self.view.fCertPNot_entry.get()
        noNota = self.view.noNot_entry.get()

        db_row = self.model.get_company_by_id(self.selected)
        for row in db_row:
            id_datos = row[1]
            id_direc = row[2]
            id_repre = row[3]

        try:
            self.model.edit_company_general_data(regPtrl, fIniAct, contPub, fIniAud, fFinAud, fElabDi, actPrin, id_datos)
            
            try:
                self.model.edit_company_address(calle, num, col, mpio, cp, entFed, poblac, telefo, id_direc)
                
                try:
                    self.model.edit_company_legal_representative(nomRepL, puesto, noEscPodNot, fCertPNot, noNota, regPtrl, id_repre)
                    #
                    self.view.dateentry_forget()
                    self.form_pack()
                    self.form_disable()
                    self.view.disabled_entry()

                    self.get_empresas()
                    self.view.bloquear_formulario()
                    #
                    self.view.msg_label['text'] = 'Empresa actualizada correctamente'
                    self.view.msg_label['fg'] = self.color_success
                except:
                    self.view.msg_label['text'] = 'No se logro actualizar el representante legal'
                    self.view.msg_label['fg'] = self.color_danger
            except:
                self.view.msg_label['text'] = 'No se logro actualizar la dirección'
                self.view.msg_label['fg'] = self.color_danger
        except:
            self.view.msg_label['text'] = 'No se logro actualizar los datos generales'
            self.view.msg_label['fg'] = self.color_danger


    def form_pack(self):
        self.fIniAct_entry.pack(fill='both')
        self.fIniAud_entry.pack(fill='both')
        self.fFinAud_entry.pack(fill='both')
        self.fElabDi_entry.pack(fill='both')

    def dateentry_forget(self):
        self.fIniAct_entry.forget()
        self.fIniAud_entry.forget()
        self.fFinAud_entry.forget()
        self.fElabDi_entry.forget()

    def form_disable(self):
        self.fIniAct_entry.config(state='disabled')
        self.fIniAud_entry.config(state='disabled')
        self.fFinAud_entry.config(state='disabled')
        self.fElabDi_entry.config(state='disabled')

    def form_normal(self):
        self.fIniAct_entry.config(state='normal')
        self.fIniAud_entry.config(state='normal')
        self.fFinAud_entry.config(state='normal')
        self.fElabDi_entry.config(state='normal')