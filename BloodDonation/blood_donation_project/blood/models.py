from app import db

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(100), nullable=False)
