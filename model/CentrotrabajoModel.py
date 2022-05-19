from model.Database import Database

class CentroTrabajoModel():
    def __init__(self):
        self.db = Database()

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

    def get_legal_representative_by_id(self, id):
        query = 'SELECT * FROM au_empresa_representante WHERE id_representante=?'
        parameters = (id, )
        db_rows = self.db.run_query(query, parameters)
        row = db_rows.fetchall()
        return row