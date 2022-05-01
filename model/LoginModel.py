from model.Database import Database

class LoginModel():
    def __init__(self):
        self.db = Database()

    def search_user(self, nuser):
        query = 'SELECT * FROM au_users WHERE username_user=?'
        parameters = (nuser,)
        db_rows = self.db.run_query(query, parameters)
        row = db_rows.fetchall()
        return row

    def search_pass(self, nuser):
        query = 'SELECT * FROM au_users WHERE password_user=?'
        parameters = (nuser,)
        db_rows = self.db.run_query(query, parameters)
        row = db_rows.fetchall()
        return row

    def exists_user(self, id_user, id_rol):
        query = 'SELECT * FROM au_users WHERE id_user=? AND roles_users_id_roles=?'
        parameters = (id_user, id_rol)
        db_rows = self.db.run_query(query, parameters)
        row = db_rows.fetchall()
        return row

    def close(self):
        self.db.cursor.close()

'''
m = Login_DB()

query = 'SELECT * FROM au_roles_users WHERE name_rol=?'
parameters = ('Administrador',)

db_query = m.run_query(query, parameters)
row = db_query.fetchall()
print(row)
'''