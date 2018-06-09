import bcrypt
import jwt
from database import database as db


class User:
    def __init__(self):
        pass

    def list(self):
        return [x for x in db.select('SELECT * FROM users')]

    def create(self, username, password, first_name=None, last_name=None, email=None):
        q = '''
            INSERT INTO users
            (
                username,
                first_name,
                last_name,
                email,
                password
            )
            VALUES
            (
                %s, %s, %s, %s, %s
            )
            '''

        return db.do(q, (username, first_name, last_name, email, self.encryptPass(password)))

    def auth(self, **params):
        q = '''
                SELECT 
                    password
                FROM
                    users
                WHERE 
                    username = %s
            '''
        return self.checkPass(password = params['password'], hashed =  db.selectObject(q, (params['username'], ))['password'])

    def encryptPass(self, password):
        return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

    def checkPass(self, **params):
        return bcrypt.checkpw(params['password'].encode('utf8'), params['hashed'].encode('utf8'))

    def sessionCreate(self, **params):
            return jwt.encode({"some":"test"}, params['secret'], algorithm='HS256')
        pass

user = User()
