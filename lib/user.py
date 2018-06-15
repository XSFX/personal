import bcrypt
import jwt
from datetime import datetime
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
        q = '''SELECT * FROM users WHERE username = %s OR email = %s'''
        user = db.selectObject(q, (params['username'], params['username']))
        if 'password' in user and self.checkPass(password = params['password'], hashed = user['password']):
            token = self.sessionCreate(username = user['username'], secret = user['username'])
            q = '''
                    REPLACE INTO sessions (username, token, expires) VALUES(%s, %s, now() + INTERVAL 1 DAY)
                '''
            db.do(q, (user['username'], token, ))
            return {"username":user['username'], "token":token}
        return False

    def checkToken(self, **params):
        if 'username' not in params:
            return {'error': 'Parameter "username" is required'}
        if 'token' not in params:
            return {'error': 'Parameter "token" is required'}
        q = ''' SELECT * FROM sessions where username = %s'''
        session = db.selectObject(q, (params['username'], ))
        if params['token'] == session['token'] and jwt.decode(params['token'], params['username'], algorithms=['HS256'])['username'] == params['username']:
            return True
        return False


    def encryptPass(self, password):
        return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

    def checkPass(self, **params):
        return bcrypt.checkpw(params['password'].encode('utf8'), params['hashed'].encode('utf8'))

    def sessionCreate(self, **params):
        return jwt.encode({"createdAt":str(datetime.now()), 'username': str(params['username'])}, str(params['secret']), algorithm='HS256')

user = User()
