from flask import Flask, request, json, jsonify
import json

import router

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
	if request.method == "POST":
		action = request.json['action']
	func = getattr(router, action, None)
	if func:
		return jsonify(func(**request.json))



