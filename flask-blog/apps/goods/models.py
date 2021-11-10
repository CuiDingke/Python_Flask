from exts import db


class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gname = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    users = db.relationship('User', backref='goods', secondary='user_goods')

    def __str__(self):
        return self.gname


# 关系表：user与goods表
class User_goods(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    goods_id = db.Column(db.Integer, db.ForeignKey('goods.id'))
    number = db.Column(db.Integer, default=1)
