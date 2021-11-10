from flask import Flask, Response, make_response
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/index7')
def index7():
    return Response(('北京', '南京', '上海'))  # application json


@app.route('/index')
def index():
    return {'a': '北京', 'b': '南京', 'c': '上海'}  # application json


@app.route('/index1')
def index1():
    response = Response('<h1>你想吃什么</h1>')
    print(response.headers)
    print(response.content_type)
    print(response.status_code)  # 200
    print(response.status)
    return response  # 返回Response对象


@app.route('/index3')
def index3():
    return '<h1>你想吃什么</h1>'  # 会自动调用Response  做response对象的封装  返回Response对象  默认把字符串转换为html


# make_response 可以定制响应头 需要传递一个可变参数
@app.route('/index4')
def index4():
    content = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>首页</title>
    <style>
        div{
            width: 100%;
            height: 100px;
            border: red;
        }
    </style>
</head>
<body>
<h1>欢迎来到京东购物网站</h1>
<div>
    <ul>
        <li>hello</li>
        <li>abc</li>
        <li>world</li>
    </ul>
</div>
</body>
</html>
    '''
    response = make_response(content) # 返回值就是一个response对象
    # 定制响应头
    response.headers['mytest'] = '123'  # 自己定制的请求头
    return response


if __name__ == '__main__':
    app.run()
