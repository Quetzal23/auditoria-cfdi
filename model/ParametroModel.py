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
        