import json
class Config:
	def __init__(self, service):
		content = None
		with open('./access.cfg', 'r') as f:
			content = json.loads(f.read())
		self.cfg = content[service]



d = Config("database").cfg
