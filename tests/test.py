import requests

url = 'http://127.0.0.1:5000'

params = {"action": "test"}


r = requests.post(url, json = params)

print(r.text)
