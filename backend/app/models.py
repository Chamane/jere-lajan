from werkzeug.security import generate_password_hash, check_password_hash
from .extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    
    def generate_hashed_password(self, password):
        return generate_password_hash(self.password, password)
    
    def check_password_hash(self, password):
        return check_password_hash(self.password, password)
    
    
class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), default="", nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), default="", nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    user = db.relationship('User', backref=db.backref('expenses', lazy=True))