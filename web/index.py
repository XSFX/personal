from flask import Flask, request, json, jsonify

import router

app = Flask(__name__)
def default(self, o):
    try:
        if isinstance(o, (bytes, )):
            return o.decode('utf8')
    except TypeError:
        pass
    return json.JSONEncoder.default(self, o)
json.JSONEncoder.default = default
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/', methods=['POST'])
def index():
    if request.method == "POST":
        print(json.dumps(request.json, indent=4, default=str))
        action = request.json['action']
    func = getattr(router, action, None)
    if func:
        return jsonify(func(**request.json))
