from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    client_id = db.Column(db.String(150), unique=True, nullable=False)
    api_key = db.Column(db.String(200), nullable=False)