from datetime import datetime

from exts import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(15), nullable=False)
    phone = db.Column(db.String(11))
    icon = db.Column(db.String(50))
    isdelete = db.Column(db.Boolean())
    email = db.Column(db.String(100))
    udatetime = db.Column(db.DateTime, default=datetime.now)
    # friends = db.relationship('Friend', backref='user')


class Friend(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    fid = db.Column(db.Integer, db.ForeignKey('user.id'))
