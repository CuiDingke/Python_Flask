

1.uuid格式
import uuid
uid = uuid.uuid4()

2.变量规则
str int float path uuid

3.视图函数
返回值:
字符串  会自动转化为response对象
dict json字符串
tuple
response对象  response对象
make_response对象  response对象
redirect() 重定向 302状态码
render_template()  模板渲染+模板
    response对象 响应对象
    response(‘字符串’, headers={key:value})
    response = make_response('....')
    response.headers   content_type  status

    request对象
    from flask import request
    request.path  headers  full_path

    重点:
    request.args  --->get请求
    request.form  --->post请求


模板：（网页）
模板的语法：
  定义:
    name = '冰川'
    friends = ['bing', 'chuan', 'wen', 'xiu']
    dict = {'gift': '金项链', 'gift1': '鲜花', 'gift2': '香蕉'}
    # 创建对象
    Girl_1 = Girl('Bing', 'Bingjing')
    return render_template('show.html', name=name, friends=friends, dict=dict, Girl_1=Girl_1)
  访问:
    变量:{{ name }}
    <br>
    列表:{{ friends[0:2] }}
    <br>
    字典:{{ dict.gift }}
    <br>
    对象:{{ Girl_1 }}-----{{ Girl_1.addr }}-----{{ Girl_1.gender }}

控制块:
{% if %}
{% for %}

loop变量
loop.index    序号从一开始
loop.index0   序号从零开始
loop.revindex 序号从大到小  最小为一
loop.revindex0 序号从大到小  最小为零


过滤器:
过滤器的本质就是函数
模板语法中过滤器:
{{ 变量名 | 过滤器(*args)}}
{{ 变量名 | 过滤器}}
常见的过滤器:
1.safe:禁用转译  msg = '<h1>520快乐！！！</h1>'  {{ msg | safe }}
2.capitalize:首字符大写 name = 'hello' {{ name | capitalize }}
3.全部大小写:upper lower
4.title:一句话中每个单词的首字母大写
5.reverse:一句话翻转
6.{{ '%s is %d years old' | format('BING',24) }}
7.截断:truncate {{ 'hello world' | truncate(5) | upper}}


{#列表过滤器#}
    {{ friends | first }}
    {{ friends | last }}
    {{ friends | length }}
{#{{ friends | sum }}  整形计算#}
    {{ [1,3,5,7] | sum }}
    {{ [1,8,2,7] | sort }}

字典过滤器 keys() values() items()
    {{ users.0}}
    {% for value in users.0.values() %}
        <p>{{ value }}</p>
    {% endfor %}

    {% for key,value in users.0.items() %}
        <p>{{ key }}-----------{{ value }}</p>
    {% endfor %}


1.自定义过滤器:
