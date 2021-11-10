from datetime import datetime

from exts import db


class Article_category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_name = db.Column(db.String(20), nullable=False)
    articles = db.relationship('Article', backref='article_category')


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    pdatetime = db.Column(db.DateTime, default=datetime.now)
    click_num = db.Column(db.Integer, default=0)
    save_num = db.Column(db.Integer, default=0)
    love_num = db.Column(db.Integer, default=0)
    # 外键  一对多 同步到数据库的关系
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('Comment', backref='article')
    category_id = db.Column(db.Integer, db.ForeignKey('article_category.id'), nullable=False)

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)
    cdatetime = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return self.comment
