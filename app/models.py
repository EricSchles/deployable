from app import db

class Code(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String)
    
    def __init__(self, code):
        self.code = code

    def __repr__(self):
        return '<id {}>'.format(self.id)

