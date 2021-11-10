# ORM对象关系映射    类------》 表
# 类对象  ----》 表中的一条记录
from datetime import datetime

from exts import db


# create table user(id int primarykey auto_increment, username varchar(20) not null,....)
class User(db.Model):
    # db.Column(类型， 约束) 映射表中的列
    '''
    db.Integer      int
    db.String(15)   varchar(15)
    db.Datetime      datetime
    '''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 逐渐自增
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(12), nullable=False)
    phone = db.Column(db.String(11), unique=True)
    email = db.Column(db.String(20))
    rdatetime = db.Column(db.DateTime, default=datetime.now)


    def __str__(self):
        return self.username


class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    realname = db.Column(db.String(20))
    gender = db.Column(db.Boolean, default=False)

    def __str__(self):
        return self.realname