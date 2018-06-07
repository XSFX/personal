import bcrypt
from database import database as db 
class User:
	def __init__(self):
		pass

	def list(self):
		return [x for x in db.select('SELECT * FROM users')]


	def create(self, username, password, first_name = None, last_name = None, email = None):
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

		return db.do(q, (username,first_name, last_name , email, self.encryptPass(password)))
		
	def encryptPass(self,password):
		return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())	
	
	def checkPass(self,password, hashed):
		return bcrypt.checkpw(password.encode('utf8'), hashed.encode('utf8'))

user = User()
