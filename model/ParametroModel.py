from model.Database import Database

class ParametroModel():
    def __init__(self):
        self.db = Database()

    def get_mother_company(self):
        query = 'SELECT * FROM au_empresa_matriz ORDER BY au_empresa_id_empresa DESC'
        db_rows = self.db.run_query(query)
        row = db_rows.fetchall()
        return row
    
    def get_company_by_id(self, id):
        query = 'SELECT * FROM au_empresa WHERE id_empresa=?'
        parameters = (id, )
        db_rows = self.db.run_query(query, parameters)
        row = db_rows.fetchall()
        return row

    def get_company_general_data_by_id(self, id):
        query = 'SELECT * FROM au_empresa_datos_generales WHERE id_datos_generales=?'
        parameters = (id, )
        db_rows = self.db.run_query(query, parameters)
        row = db_rows.fetchall()
        return row

    def get_company_address_by_id(self, id):
        query = 'SELECT * FROM au_empresa_direccion WHERE id_empresa_direccion=?'
        parameters = (id, )
        db_rows = self.db.run_query(query, parameters)
        row = db_rows.fetchall()
        return row

    def capture_company_general_data(self, nomEmp, nomCorto, rfc, noPatrl, actPpal):
        query = 'INSERT INTO au_empresa_datos_generales VALUES(NULL, ?, ?, ?, ?, ?, NULL, NULL, NULL, NULL, NULL, NULL)'
        parameters = (nomEmp, nomCorto, rfc, noPatrl, actPpal)
        self.db.run_query(query, parameters)

    def capture_company_address(self, calle, num, col, mpio, cp, entFed, pob, tel):
        query = 'INSERT INTO au_empresa_direccion VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)'
        parameters = (calle, num, col, mpio, cp, entFed, pob, tel)
        self.db.run_query(query, parameters)

    def capture_company_representative(self, noPatrl):
        query = 'INSERT INTO au_empresa_representante VALUES(NULL, NULL, NULL, NULL, NULL, NULL , ?)'
        parameters = (noPatrl, )
        self.db.run_query(query, parameters)

    def get_company_general_data(self, rfc, noPatrl):
        query = 'SELECT * FROM au_empresa_datos_generales WHERE rfc_empresa=? AND no_reg_patrl_empresa=?'
        parameters = (rfc, noPatrl)
        db_rows = self.db.run_query(query, parameters)
        row = db_rows.fetchall()
        return row

    def get_company_address(self, num, cp):
        query = 'SELECT * FROM au_empresa_direccion WHERE no_empresa=? AND cp_empresa=?'
        parameters = (num, cp)
        db_rows = self.db.run_query(query, parameters)
        row = db_rows.fetchall()
        return row
        
    def get_company_representative(self, noPatrl):
        query = 'SELECT * FROM au_empresa_representante WHERE no_reg_patrl_empresa=?'
        parameters = (noPatrl, )
        db_rows = self.db.run_query(query, parameters)
        row = db_rows.fetchall()
        return row

    def get_company(self, id_datos, id_direccion):
        query = 'SELECT * FROM au_empresa WHERE au_empresa_datos_generales_id_datos=? AND au_empresa_direccion_id_direccion=?'
        parameters = (id_datos, id_direccion)
        db_rows = self.db.run_query(query, parameters)
        row = db_rows.fetchall()
        return row

    def capture_company(self, id_dato, id_dir, id_rep):
        query = 'INSERT INTO au_empresa VALUES(NULL, ?, ?, ?)'
        parameters = (id_dato, id_dir, id_rep)
        self.db.run_query(query, parameters)

    def capture_mother_company(self, id_empresa):
        query = 'INSERT INTO au_empresa_matriz VALUES(NULL, ?)'
        parameters = (id_empresa, )
        self.db.run_query(query, parameters)

    def edit_company_general_data(self, nomEmp, nomCorto, rfc, noPatrl, actPpal, id):
        query = 'UPDATE au_empresa_datos_generales SET nom_empresa=?, nom_corto_empresa=?, rfc_empresa=?, no_reg_patrl_empresa=?, act_ppal_empresa=? WHERE id_datos_generales=?'
        parameters = (nomEmp, nomCorto, rfc, noPatrl, actPpal, id)
        self.db.run_query(query, parameters)
        
    def edit_company_address(self, calle, num, col, mpio, cp, entFed, pob, tel, id):
        query = 'UPDATE au_empresa_direccion SET calle_empresa=?, no_empresa=?, col_empresa=?, mpio_empresa=?, cp_empresa=?, ent_fed_empresa=?, pob_empresa=?, tels_empresa=? WHERE id_empresa_direccion=?'
        parameters = (calle, num, col, mpio, cp, entFed, pob, tel, id)
        self.db.run_query(query, parameters)
