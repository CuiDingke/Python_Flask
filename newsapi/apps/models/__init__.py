from datetime import datetime

from exts import db


class BaseModel(db.Model):
    __abstract__ = True  # 当前作为抽象类  不能单独作为一个模型出现   只能作为一个父类出现
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_time = db.Column(db.DateTime, default=datetime.now)