from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    state = db.Column(db.String(150))
    country = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    age = db.Column(db.Integer())
    verify = db.relationship('Verify')

class Verify(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(150))
    cardFront = db.Column(db.Integer())
    cardBack = db.Column(db.Integer())
#    Payment information ( card number_ visa)
    CardHolderName = db.Column(db.Integer())
    ExpiryDate = db.Column(db.String(150))
    CvvCode = db.Column(db.Integer())
    Skills = db.Column(db.String(15000))
    Preferences = db.Column(db.String(15000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
