import sqlite3

class Database:
    def __init__(self, db):
        #self.db_name = db
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def run_query(self, query, parameters=()):
        result = self.cursor.execute(query, parameters)
        self.conn.commit()

        return result

    def search_user(self, nuser):
        query = 'SELECT * FROM user_login WHERE ulogin_user=?'
        parameters = (nuser,)
        db_rows = self.run_query(query, parameters)
        row = db_rows.fetchall()
        
        return row

    def search_pass(self, passw):
        query = 'SELECT * FROM user_login WHERE ulogin_pass=?'
        parameters = (passw,)
        db_rows = self.run_query(query, parameters)
        row = db_rows.fetchall()

        return row

    
    ## Registro de login
    def add_logins(self, time, fail, action, username, ip, so):
        query = 'INSERT INTO logins VALUES(NULL, ?, ?, ?, ?, ?, ?)'
        parameters = (time, fail, action, username, ip, so)
        self.run_query(query, parameters)

    def add_login_failed(self, uid, uname, date, ip):
        query = 'INSERT INTO login_failed VALUES(NULL, ?, ?, ?, ?)'
        parameters = (uid, uname, date, ip)
        self.run_query(query, parameters)

    def add_login_activity(self, uid, uname, login, logout, ip, so):
        query = 'INSERT INTO login_activity VALUES(NULL, ?, ?, ?, ?, ?, ?)'
        parameters = ( uid, uname, login, logout, ip, so)
        self.run_query(query, parameters)
    
    def __del__(self):
        #print('Close')
        self.conn.close()

    '''
    # Registro de empresas
    def add_empresa(self, n_empresa, n_corto, rfc):
        query = 'INSERT INTO parametros_empresa VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        parameters = ()
        self.run_query(query, parameters)
    '''