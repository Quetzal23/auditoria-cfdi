class CentroTrabajoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.id_mother_company = self.view.id_empresa

        self.view.treeview.bind ('<<TreeviewSelect>>', self._on_tree_select)
        self.get_empresas()

    def _on_tree_select(self, a):
        self.view.bloquear_formulario()
        
        curItem = self.view.treeview.focus()
        self.selected = self.view.treeview.item(curItem, 'text') # Obtener id de la empresa
        
        '''self.view._select_company()'''

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
        db_row = self.model.get_company_by_id(selected)
        for row in db_row:
            self.form_datosgenerales(row[1])
            self.form_direccion(row[2])
            self.form_representante_legal(row[3])
    
    def form_datosgenerales(self, id_datos):
        db_row = self.model.get_company_general_data_by_id(id_datos)
        for row in db_row:
            self.view.var1.set(row[4])
            #self.view.var2.set(row[6])
            self.view.var3.set(row[8])
            #self.view.var4.set(row[9])
            #self.view.var5.set(row[11])
            #self.view.var6.set(row[12])
            #self.view.var7.set(row[7])
            self.view.var8.set(row[5])

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