1.自定义过滤器:
# 过滤器的本质就是函数
1.通过flask模块中的add_template_filter方法
    a.定义函数，带有参数和返回值
    b.添加过滤器 app.add_template_filter(function, name='')
    c.在模板中使用: {{变量 | 自定义过滤器}}
2.使用装饰器完成
    a.定义函数，带有参数和返回值
    b.通过装饰器完成，@app.template_filter('过滤器名称')装饰步骤a的函数
    c.在模板中使用: {{变量 | 自定义过滤器}}
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


复用:
模板继承:
需要模板继承的情况:
1.多个模板具有完全相同的顶部和底部
2.多个模板具有相同的模版内容，但是内容中部分不一样
3.多个模板具有完全相同的模板内容

标签:
{%  block 名字  %}
{%  endblock   %}


include：包含
在A,B,C页面共同的部分，但是其他页面没有这部分
在这个时候使用include
步骤:
1.先定义一个公共的模板部分. xxx.html
2.谁使用则include过来 {% include '文件夹/xxx.html' %}

宏: macro
1.把它看作jinjia2的一个函数，这个函数可以返回一个HTML字符串
2.目的:代码复用，避免代码冗余。

定义两种方式:
1.在模板中直接定义使用:
    类似: macro1.html 中定义使用
2.将宏提取到一个模板中:macro.html
谁想用谁导入:
{% import 'macro,html' as xxx%}
{{xxx.宏名字(参数)}}



{#全局变量#}
{% set username = 'zhangsan' %}
{{ username }}
{#局部变量#}
{% with num=1000 %}
    {{ num }}
{% endwith %}

{% if 条件 %}.....{% endif %}
{% for 条件 %}.....{% endfor %}
{% block 条件 %}.....{% endblock %}
{% macro 条件 %}.....{% endmacro %}

{% include '' %}   包含
{% import '' %}   导入宏
{% extends '' %}

{{url_for('static',filename='')}}


view:
@app.route('/', endpoint='',methods=['GET','POST])
def index()：
    return response|''| render_template('xxx.html')

