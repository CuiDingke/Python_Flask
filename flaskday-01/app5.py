# app.py 与 模板的结合使用
from flask import Flask, request, render_template
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/register1')
def register1():
    s = '''
    <form action="" method="get">
        <p><input type="text" placeholder="请输入用户名"></p>
        <p><input type="text" placeholder="请输入密码"></p>
        <p><input type="submit" value="提交"></p>
    </form>
    '''
    return s  # 自动封装成response 对象


# # 发起请求  根据路由链表规则 找到匹配的函数 执行函数 通过Jinja2 模板引擎找到templates文件夹中的register.html中的内容  并将其转为字符串 然后通过return 返回给浏览器
@app.route('/register')
def register():
    r = render_template('register.html')
    return r


@app.route('/register2', methods=['get', 'post'])
def register2(): # 获取页面提交的内容
    print(request.full_path) # /register2?username=dsf&password=fs
    print(request.path) # /register2
    # get方法用args得到数据
    print(request.args) # 底层是字典类型的 [('username', 'dsf'), ('password', 'fs')]
    print(request.args.get('username'))
    print(request.args.get('password'))

    # post方法用form得到数据
    print(request.form)  # 底层是字典类型的 [('username', 'dsf'), ('password', 'fs')]
    print(request.form.get('username'))
    print(request.form.get('password'))
    return '进来了'


if __name__ == '__main__':
    print(app.url_map)  # 打印路由表
    app.run()
