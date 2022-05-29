from assets.validation import Validation_Entry, number_validation, text_limiter

import route 

class ParametroController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        style = self.view.style
        self.color_danger = style.color__danger
        self.color_success = style.color__success

        self.tipo_guardado = 0

        self.validar = Validation_Entry(self.view.root)

        self.view.btn_new['command'] = self.new_button
        self.view.btn_save['command'] = self.save_button
        self.view.btn_edit['command'] = self.edit_button
        self.view.btn_delete['command'] = self.delete_button
        self.view.btn_center['command'] = self.center_button

        self.view.treeview.bind ('<<TreeviewSelect>>', self._on_tree_select)
        self.get_empresa_matriz()

    def input_validations(self):
        # Codigo Postal
        self.view.var10.trace("w", lambda *args: text_limiter(self.view.var10, 5))
        self.view.cp_entry['validatecommand'] = (self.view.cp_entry.register(number_validation),'%P','%d')

    def new_button(self):
        self.view.msg_label['text'] = ''
        self.tipo_guardado = 1

        self.view.limpiar_formulario()
        self.view._button_save()
        self.view.normal_entry()

        # Validaciones de los inputs
        self.input_validations()
    
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
            self.view.formulario_completo()
            #self.validar_datos_generales()

            if self.tipo_guardado == 1:
                self.add_empresa_matriz() # Llenar Datos Generales y Direccion en la bd
            if self.tipo_guardado == 2:
                self.edit_empresa() # Editar Datos Generales y Direccion en la bd
            self.tipo_guardado = 0
        else:
            self.view.formulario_incompleto()
            self.view.alert()
            
    def edit_button(self):
        self.tipo_guardado = 2

        self.view._button_edit()
        self.view.normal_entry()

    def delete_button(self):
        pass

    def center_button(self):
        route.centro_trabajo(self.selected)

    def _on_tree_select(self, a):
        self.view.bloquear_formulario()
        #self.view.limpiar_formulario()
        
        curItem = self.view.treeview.focus()
        self.selected = self.view.treeview.item(curItem, 'text') # Obtener id de la empresa
        
        self.view._select_company()

        # Imprimir formulario
        self.imprimir_formulario(self.selected)
        
    def entry_validation_general_data(self):
        return (len(self.view.nomEmp_entry.get()) != 0 and len(self.view.nomCorto_entry.get()) != 0 and
            len(self.view.rfc_entry.get()) != 0 and len(self.view.noPatrl_entry.get()) != 0 and
            len(self.view.actPpal_entry.get()) != 0)

    def entry_validation_address(self):
        return (len(self.view.calle_entry.get()) != 0 and len(self.view.num_entry.get()) != 0 and
            len(self.view.col_entry.get()) != 0 and len(self.view.mpio_entry.get()) != 0 and
            len(self.view.cp_entry.get()) != 0 and len(self.view.entFed_entry.get()) != 0 and
            len(self.view.pob_entry.get()) != 0 and len(self.view.tel_entry.get()) != 0)


    # Guardar empresa
    def add_empresa_matriz(self):
        self.model.capture_company_general_data(self.nomEmp, self.nomCorto, self.rfc, self.noPatrl, self.actPpal)
        self.model.capture_company_address(self.calle, self.num, self.col, self.mpio, self.cp, self.entFed, self.pob, self.tel)
        self.model.capture_company_representative(self.noPatrl)

        try:
            # Obtener id de los datos y form_direccion de la empresa
            id_datos_empresa = self.get_id_company_data()
            id_direc_empresa = self.get_id_company_address()
            id_representante = self.get_id_company_representative()
            
            try:
                # Llenar la tabla de empresas
                self.model.capture_company(id_datos_empresa, id_direc_empresa, id_representante)
                try:
                    # Obtener id de la empresa
                    db_row = self.model.get_company(id_datos_empresa, id_direc_empresa)
                    for row in db_row:
                        id = row[0]

                    # Llenar impresa matriz
                    self.model.capture_mother_company(id)

                    self.view.bloquear_formulario()
                    self.get_empresa_matriz()   # Llenar el treeview

                    self.view.msg_label['text'] = 'Empresa capturada correctamente'
                    self.view.msg_label['fg'] = self.color_success
                    
                except:
                    self.view.msg_label['text'] = 'No se logro capturar la Empresa Matriz'
                    self.view.msg_label['fg'] = self.color_danger
            except:
                self.view.msg_label['text'] = 'No se logro capturar la Empresa'
                self.view.msg_label['fg'] = self.color_danger
        except:
            self.view.msg_label['text'] = 'No se logro capturar Los Parametros de Empresas'
            self.view.msg_label['fg'] = self.color_danger

    # Obtener el id de los datos de la empresa
    def get_id_company_data(self):
        db_row = self.model.get_company_general_data(self.rfc, self.noPatrl)
        for row in db_row:
            id = row[0]
            return id

    # Obtener el id de direccion de la empresa
    def get_id_company_address(self):
        db_row = self.model.get_company_address(self.num, self.cp)
        for row in db_row:
            id = row[0]
            return id

    # Obtener el id del representante legal
    def get_id_company_representative(self):
        db_row = self.model.get_company_representative(self.noPatrl)
        for row in db_row:
            id = row[0]
            return id
    

    # Llenar treeview de las empresas matriz
    def get_empresa_matriz(self):
        records = self.view.treeview.get_children()
        for element in records: # Limpiar tabla
            self.view.treeview.delete(element)

        matriz = self.model.get_mother_company()
        for row in matriz:  # Obtener id de empresa en la tabla empresa matriz
            id_emp = row[1]
            db_row = self.model.get_company_by_id(id_emp)
            
            for data in db_row: # Obtener id datos generales de la empreza matriz
                datos = self.model.get_company_general_data_by_id(data[1])

                for tree in datos:
                    name = tree[1] # Obtener nombre de la empreza matriz
                    self.view.treeview.insert('', 0, text=id_emp, values=(name, ))  # Llenar el treeview
    

    # Llenar el formulario
    def imprimir_formulario(self, selected):
        db_row = self.model.get_company_by_id(selected)
        for row in db_row:
            self.form_datosgenerales(row[1])
            self.form_direccion(row[2])

    def form_datosgenerales(self, id_datos):
        db_row = self.model.get_company_general_data_by_id(id_datos)
        for row in db_row:
            self.view.var1.set(row[1])
            self.view.var2.set(row[2])
            self.view.var3.set(row[3])
            self.view.var4.set(row[4])
            self.view.var5.set(row[5])

    def form_direccion(self, id_direccion):
        db_row = self.model.get_company_address_by_id(id_direccion)
        for row in db_row:
            self.view.var6.set(row[1])
            self.view.var7.set(row[2])
            self.view.var8.set(row[3])
            self.view.var9.set(row[4])
            self.view.var10.set(row[5])
            self.view.var11.set(row[6])
            self.view.var12.set(row[7])
            self.view.var13.set(row[8])


    # Editar empresa
    def edit_empresa(self):
        # Validaciones de los inputs
        self.input_validations()

        nomEmp = self.view.nomEmp_entry.get()
        nomCorto = self.view.nomCorto_entry.get()
        rfc = self.view.rfc_entry.get()
        noPatrl = self.view.noPatrl_entry.get()
        actPpal = self.view.actPpal_entry.get()

        calle = self.view.calle_entry.get()
        num = self.view.num_entry.get()
        col = self.view.col_entry.get()
        mpio = self.view.mpio_entry.get()
        cp = self.view.cp_entry.get()
        entFed = self.view.entFed_entry.get()
        pob = self.view.pob_entry.get()
        tel = self.view.tel_entry.get()

        db_row = self.model.get_company_by_id(self.selected)
        for row in db_row:
            try:
                self.model.edit_company_general_data(nomEmp, nomCorto, rfc, noPatrl, actPpal, row[1])
                try:
                    self.model.edit_company_address(calle, num, col, mpio, cp, entFed, pob, tel, row[2])

                    self.view.msg_label['text'] = 'Empresa actualizada correctamente'
                    self.view.msg_label['fg'] = self.color_success
                except:
                    self.view.msg_label['text'] = 'No se logro actualizar la dirección'
                    self.view.msg_label['fg'] = self.color_danger
                '''self.view.msg_label['text'] = 'Empresa actualizada correctamente'
                self.view.msg_label['fg'] = self.color_success'''
            except:
                self.view.msg_label['text'] = 'No se logro actualizar los datos generales'
                self.view.msg_label['fg'] = self.color_danger
        
        self.get_empresa_matriz()   # Actualizar el treeview
        self.view.disabled_entry()
