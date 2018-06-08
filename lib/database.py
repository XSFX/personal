import config
import mysql.connector


class Database:
    def __init__(self):
        self.con = mysql.connector.connect(**config.d)
        self.cur = self.con.cursor()

    def select(self, q, params=None):
        if not self.con.is_connected():
            self.con.reconnect()
        self.cur.execute(q, params)
        return self.cur.fetchall()

    def do(self, q, params=None):
        if not self.con.is_connected():
            self.con.reconnect()
        self.cur.execute(q, params)
        self.con.commit()
        return self.cur.rowcount


database = Database()
