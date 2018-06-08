import os
import json


class Config:
    def __init__(self, service):
        content = None
        with open(os.path.join(os.path.dirname(__file__), "../access.cfg"), 'r') as f:
            content = json.loads(f.read())
        self.cfg = content[service]


d = Config("database").cfg
