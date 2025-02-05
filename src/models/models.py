from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from werkzeug.security import  check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'Users'  # Use existing table
    id = db.Column(db.Integer, primary_key=True)
    identification = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=text('CURRENT_TIMESTAMP'), nullable=False)
    def check_password(self, password):
        return check_password_hash(self.password, password)

