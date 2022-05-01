from model.Database import Database

class IndexModel():
    def __init__(self):
        self.db = Database()
    
    def exists_user(self, id_user, id_rol):
        query = 'SELECT * FROM au_users WHERE id_user=? AND roles_users_id_roles=?'
        parameters = (id_user, id_rol)
        db_rows = self.db.run_query(query, parameters)
        row = db_rows.fetchall()
        return row