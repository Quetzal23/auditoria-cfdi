import sqlite3

class Connection:
    def __init__(self):
        db_name = 'auditoria.db'
        with sqlite3.connect(db_name) as self.conn:
            self.cursor = self.conn.cursor() 

    def run_query(self, query, parameters=()):
        result = self.cursor.execute(query, parameters)
        self.conn.commit()
        return result
