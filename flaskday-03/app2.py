import json

from flask import Flask, render_template, request, redirect, url_for
import settings

app = Flask(__name__)
app.config.from_object(settings)


class Girl:
    def __init__(self, name, addr):
        self.name = name
        self.gender = '女'
        self.addr = addr

    def __str__(self):
        return self.name


@app.route('/show')
def show():
    name = 'hello'
    friends = ['bing', 'chuan', 'wen', 'xiu']
    dict = {'gift': '金项链', 'gift1': '鲜花', 'gift2': '香蕉'}
    # 创建对象
    Girl_1 = Girl('Bing', 'Bingjing')
    users = [
        {'username':'Bing',  'password':'123456', 'phone':'15736980819'},
        {'username':'Chuan', 'password':'123456', 'phone':'18172185862'},
        {'username':'Xue',   'password':'123456', 'phone':'18137369626'}
    ]
    msg = '<h1>520快乐！！！</h1>'
    return render_template('show_GLQ.html', name=name, friends=friends, dict=dict, Girl_1=Girl_1, users=users, msg=msg)


# 重定向会改变URL   render_template不会改变URL

if __name__ == '__main__':
    app.run()
