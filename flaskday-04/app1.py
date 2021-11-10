from flask import Flask, render_template
import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/')
def hello_world():
    msg = 'hello world!!!'
    li = [2, 5, 6, 8, 7, 9]
    return render_template('define_filter.html', msg=msg, li=li)


# 自定义过滤器
# 第一种方式------替换
def replace_hello(value):
    print('----------->', value)
    value = value.replace('hello', '')
    print('===========>', value)
    return value.strip()


app.add_template_filter(replace_hello, 'replace')


# 字符串长度
def length_len(value):
    print('----------->', value)
    length = len(value)
    print('===========>', length)
    return length


app.add_template_filter(length_len, 'Length')


# 第二种方式 装饰器---------反序
@app.template_filter('List_reverse')
def reverse_list(li):
    temp_li = list(li)
    temp_li.reverse()
    return temp_li


if __name__ == '__main__':
    app.run()
