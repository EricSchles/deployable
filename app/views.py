from app import app
from app.models import Code
import json
from app import db
from flask import request #this is better

#this should not accept both get and post
@app.route("/pull", methods=["GET","POST"])
def pull():
    all_code_versions = Code.query.all()
    all_code_versions = sorted(all_code_versions, key=lambda x: x.id)
    result = all_code_versions[-1]
    return json.dumps({"code":result.code, "id":result.id})


@app.route("/push", methods=["GET","POST"]) #this should not accept both get and post
def push():
    code = json.loads(request.get_data())
    code_obj = Code(code["code"])
    db.session.add(code_obj)
    db.session.commit()
    return "success!"
