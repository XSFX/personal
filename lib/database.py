import config
import mysql.connector


class Database:
    def __init__(self):
        self.con = mysql.connector.connect(**config.d)
        self.cur = self.con.cursor(buffered = True)

    def select(self, q, params=None):
        if not self.con.is_connected():
            self.con.reconnect()
        self.cur.execute(q, params)
        return self.cur.fetchall()

    def selectObject(self, q, params=None):
        if not self.con.is_connected():
            self.con.reconnect()
        self.cur.execute(q, params)
        if self.cur.rowcount < 1:
            return {}
        return dict(zip([c[0] for c in self.cur.description], self.cur.fetchone()))


    def selectObjects(self, q, params=None):
        if not self.con.is_connected():
            self.con.reconnect()
        self.cur.execute(q, params)
        return [dict(zip([c[0] for c in self.cur.description], x)) for x in self.cur.fetchall()]

    def do(self, q, params=None):
        if not self.con.is_connected():
            self.con.reconnect()
        self.cur.execute(q, params)
        self.con.commit()
        return self.cur.rowcount


database = Database()
