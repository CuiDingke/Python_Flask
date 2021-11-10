from flask import Flask
import settings

app = Flask(__name__)
app.config.from_object(settings)  # 加载配置

data = {'a': '北京', 'b': '南京', 'c': '上海'}


@app.route('/getcity/<key>')  # 也可以是<string:key>
def getcity(key):
    return data.get(key)


@app.route('/add/<int:num>')  # 也可以是<num>
def add(num):
    result = num + 10
    return str(result)


@app.route('/add1/<float:money>')
def add1(money):
    return str(money)


# 拿路径
@app.route('/index/<path:subpath>')
def get_path(subpath):
    print(type(subpath))
    return subpath


# 路由自上而下搜索  相同路由名只能访问第一个；  函数名不能相同，如果相同报错
@app.route('/')  # 路由定义   URL:http://127.0.0.1:5000/
def hello_world():  # 视图函数   mtv： v视图
    return 'Hello World!'


# URL路由为http:127.0.0.1:5000/index
@app.route('/index')
def hello_index():
    return 'index1111'


# 下面是路由的另一种写法
def hello_test():
    return 'test'


app.add_url_rule('/test', view_func=hello_test)  # 绑定到hello_test函数 也就是.route底层执行的函数

if __name__ == '__main__':
    app.run()
