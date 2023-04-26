from flask_login import UserMixin
from app.extensions.database import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    picture_url = db.Column(db.String(260))
    slug = db.Column(db.String(80), unique=True)
    notes = db.relationship('Note')