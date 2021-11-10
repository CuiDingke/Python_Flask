import json

from flask import Flask, render_template, request, redirect, url_for
import settings

app = Flask(__name__)
app.config.from_object(settings)

users = []


@app.route('/', endpoint='index')
def index():
    return render_template('index.html')


@app.route('/add/<int:n>/<int:m>')
def add(n, m):
    if n > 0 and m > 0:
        r = n + m
        return str(r)
    return '<h1>输入数据不符合标准</h1>'


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        # 密码一致性验证
        if password == repassword:
            # 保存用户
            user = {'username': username, 'password': password}
            users.append(user)
            # return '注册成功!!! <a href="/">返回首页</a>'
            # 重定向让其跳转
            return redirect('/')  # 有两次响应：1：302状态码+location 2.返回location请求地址内容
        else:
            return '两次密码不一致'
    return render_template('register.html')


@app.route('/show')
def show():
    # users[] ----> str  json字符串
    j_str = json.dumps(users)
    return j_str


@app.route('/test')
def test():
    url = url_for('index')  # 反向解析  用一个名 找到 匹配的路径  默认的情况下是函数名  但是函数名也会长  所以可以自定义endpoint起别名
    print(url)
    return redirect(url_for('index'))


# 重定向会改变URL   render_template不会改变URL

if __name__ == '__main__':
    app.run()
