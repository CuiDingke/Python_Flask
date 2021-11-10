import hashlib

from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import or_, and_, not_

from apps.user.models import User
from exts import db

user_bp = Blueprint('user', __name__)


# 注册
@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')

        if password == repassword:
            users = User.query.filter(User.phone == phone)
            for user in users:
                if user.phone == phone:
                    return render_template('user/register.html', msg='号码已存在')
            user = User()
            user.username = username
            user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            user.phone = phone
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.user_center'))
        else:
            return '密码不同'

    return render_template('user/register.html')


# 用户中心
@user_bp.route('/')
def user_center():
    # 查询数据库中的数据
    users = User.query.filter(User.isdelele == False).all()  # select * from user
    print(users)
    return render_template('user/center.html', users=users)


# 用户登录
@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # 关键部分 select * from user where username='xxx'
        new_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        user_list = User.query.filter_by(username=username)
        print(user_list)
        for u in user_list:
            if u.password == new_password:
                return '用户登录成功'
        return render_template('user/login.html', msg='用户名或密码错误')
    return render_template('user/login.html')


# 用户搜索
@user_bp.route('/search', methods=['GET', 'POST'])
def search():
    # if request.method == 'get':
    keyword = request.args.get('search')
    users = User.query.filter(or_(User.username.contains(keyword), User.phone.contains(keyword)))
    return render_template('user/center.html', users=users)


# 用户删除
@user_bp.route('/delete')
def delete():
    # 获取用户ID
    id = request.args.get('id')
    # 逻辑删除 -----------》其实就是更新
    # # 获取该id用户
    # user = User.query.get(id)
    # # 逻辑删除
    # user.isdelele = True
    # # 提交
    # db.session.commit()

    # 物理删除
    user = User.query.get(id)
    # 加到缓存中
    db.session.delete(user)
    # 提交
    db.session.commit()
    return redirect(url_for('user.user_center'))


# 用户信息更新
@user_bp.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        username = request.form.get('username')
        phone = request.form.get('phone')
        id = request.form.get('id')
        user = User.query.get(id)
        user.username = username
        user.phone = phone
        db.session.commit()
        return redirect(url_for('user.user_center'))
    else:
        id = request.args.get('id')
        user = User.query.get(id)
        return render_template('user/update.html', user=user)


@user_bp.route('/test')
def test():
    username = request.args.get('username')
    user = User.query.filter_by(username=username).first()
    print(user.username, user.rdatetime)
    # 无last() 属性
    # user = User.query.filter_by(username=username).all()
    print(user.username, user.rdatetime)
    return 'test'


@user_bp.route('/select')
def user_select():
    # 根据主键查询用户部分
    user = User.query.get(1)
    # 注意和fileter_by 的区别
    # user = User.query.filter(User.username=='bing').all()  #all()   first()   user[:]
    # user = User.query.filter(User.username.startswith('b')).all()
    # user = User.query.filter(User.username.contains('b')).all()
    # user = User.query.filter(or_(User.username.like('b%'), User.username.contains('i'))).all()
    # user = User.query.filter(and_(User.rdatetime.__lt__('2021-09-06 22:05:58'), User.username.contains('b'))).all()
    # user = User.query.filter(and_(User.rdatetime < '2021-09-06 22:05:58', User.username.contains('b'))).all()
    # user = User.query.filter(not_( User.username.contains('b'))).all()
    # user = User.query.filter(User.phone.in_(['154254','15736980819'])).all()
    # user = User.query.order_by('rdatetime').all()
    # user = User.query.filter(User.username.contains('b')).order_by('rdatetime').all()
    # user = User.query.order_by(-User.rdatetime).all()
    # user = User.query.filter(User.username.contains('b')).order_by(-User.rdatetime).all()
    # user = User.query.order_by(-User.rdatetime).limit(2).all()
    user = User.query.order_by(-User.rdatetime).offset(2).limit(2).all()
    return render_template('user/select.html', user=user)
