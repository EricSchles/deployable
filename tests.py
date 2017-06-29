import requests
from app import app
import json

def testing_push_pull():
    app.testing = True
    with app.test_client() as c:
        data = {"code":"testing"}
        c.post("push",data=json.dumps(data))
        rv = c.get('pull')
        assert json.loads(rv.get_data())["code"] == "testing"
    
