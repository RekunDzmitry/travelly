from flask_login import UserMixin
from . import db
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id          = db.Column(db.Integer, primary_key=True)
    email       = db.Column(db.String(150), unique=True)
    password    = db.Column(db.String(150))
    first_name  = db.Column(db.String(150))
    travels     = db.relationship('Travel')

class Travel(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(150))
    description = db.Column(db.String(150))
    date        = db.Column(db.DateTime(timezone=True), default=func.now())
    data        = db.Column(db.String(3000))
    user_id     = db.Column(db.Integer, db.ForeignKey('user.id'))





