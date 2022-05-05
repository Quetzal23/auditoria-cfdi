from model.Database import Database

class ParametroModel():
    def __init__(self):
        self.db = Database()

    def capture_company_general_data(self, nomEmp, nomCorto, rfc, noPatrl, actPpal):
        query = 'INSERT INTO au_empresa_datos_generales VALUES(NULL, ?, ?, ?, ?, ?, NULL, NULL, NULL, NULL, NULL, NULL)'
        parameters = (nomEmp, nomCorto, rfc, noPatrl, actPpal)
        self.db.run_query(query, parameters)
        
    def capture_company_address(self, calle, num, col, mpio, cp, entFed, pob, tel):
        query = 'INSERT INTO au_empresa_direccion VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?)'
        parameters = (calle, num, col, mpio, cp, entFed, pob, tel)
        self.db.run_query(query, parameters)
    

    def get_company_general_data(self, rfc):
        query = 'SELECT * FROM au_empresa_datos_generales WHERE rfc_empresa=?'
        parameters = (rfc, )
        db_rows = self.db.run_query(query, parameters)
        row = db_rows.fetchall()
        return row

    def get_company_address(self, cp):
        query = 'SELECT * FROM au_empresa_direccion WHERE cp_empresa=?'
        parameters = (cp, )
        db_rows = self.db.run_query(query, parameters)
        row = db_rows.fetchall()
        return row


    def capture_company(self, id_dato, id_dir):
        query = 'INSERT INTO au_empresa VALUES(NULL, ?, ?, NULL)'
        parameters = (id_dato, id_dir)
        self.db.run_query(query, parameters)

    def get_company(self, id_datos, id_dir):
        query = 'SELECT * FROM au_empresa WHERE au_empresa_datos_generales_id_datos=? AND au_empresa_direccion_id_direccion=?'
        parameters = (id_datos, id_dir)
        db_rows = self.db.run_query(query, parameters)
        row = db_rows.fetchall()
        return row

    def capture_mother_company(self, id_empresa):
        query = 'INSERT INTO au_empresa_matriz VALUES(NULL, ?)'
        parameters = (id_empresa, )
        self.db.run_query(query, parameters)


    def get_mother_companies(self):
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

    def get_data_company_by_id(self, id):
        query = 'SELECT * FROM au_empresa_datos_generales WHERE id_datos_generales=?'
        parameters = (id, )
        db_rows = self.db.run_query(query, parameters)
        row = db_rows.fetchall()
        return row