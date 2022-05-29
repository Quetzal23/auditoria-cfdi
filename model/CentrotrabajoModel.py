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

    def edit_company_general_data(self, regPtrl, fIniAct, contPub, fIniAud, fFinAud, fElabDi, actPrin, id):
        query = 'UPDATE au_empresa_datos_generales SET no_reg_patrl_empresa=?, fecha_ini_act=?, contador_publico=?, fecha_ini_aud=?, fecha_fin_aud=?, fecha_elab_dictamen=?, act_ppal_empresa=? WHERE id_datos_generales=?'
        parameters = (regPtrl, fIniAct, contPub, fIniAud, fFinAud, fElabDi, actPrin, id)
        self.db.run_query(query, parameters)

    def edit_company_address(self, calle, num, col, mpio, cp, entFed, pob, tel, id):
        query = 'UPDATE au_empresa_direccion SET calle_empresa=?, no_empresa=?, col_empresa=?, mpio_empresa=?, cp_empresa=?, ent_fed_empresa=?, pob_empresa=?, tels_empresa=? WHERE id_empresa_direccion=?'
        parameters = (calle, num, col, mpio, cp, entFed, pob, tel, id)
        self.db.run_query(query, parameters)
    
    def edit_company_legal_representative(self, nom, puesto, esc, fcert, notaria, noregp, id):
        query = 'UPDATE au_empresa_representante SET nom_representante=?, puesto_representante=?, no_esc_poder_notarial=?, fecha_cert_p_notarial=?, no_notaria=?, no_reg_patrl_empresa=? WHERE id_representante=?'
        parameters = (nom, puesto, esc, fcert, notaria, noregp, id)
        self.db.run_query(query, parameters)