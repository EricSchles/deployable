import requests
import json
requests.post("http://localhost:5000/push", data=json.dumps({"code":"print('hello')"}))