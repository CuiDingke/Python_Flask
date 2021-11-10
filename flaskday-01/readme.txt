1.pip list

当初创建项目的时候，已经指定了flask 所以pycharm会自动执行：pip install flasks

pip install falsk==1.1.0(安装指定的版本)

2.项目结构介绍：

--项目名:
    |---static (静态)  js css
    |--templates (模板)
    |--app.py (运行|启动)

web项目:
    mvc
    model 模型
    view  视图
    controler 控制器

python:
    mtv
    model 模型
    template 模板 ===>html
    view 视图    起控制作用

request  请求
response 响应

虚拟环境:
pip install virtualenv
pip install virtualenvwrapper-win  ======》window使用加win

虚拟环境常用命令:
mkvirtualenv 虚拟环境名字    ==》创建虚拟环境
lsvirtualenv 查看所有虚拟环境名称
cdvirtualenv 切换到目前的虚拟环境下
rmvirtualenv 虚拟环境名字    ==》删除虚拟环境
workon 虚拟环境名字          ==》虚拟环境之间切换


WSGI协议=====》flask与服务器进行融合部署。

run(host='ip地址',port=‘端口号’,debug=True)
debug=True   ===>可以调试,代码发生改变会自动加载
如果host改成：0.0.0.0  外网可以访问
默认情况下只能是本机访问

# app.config['ENV'] = 'development'  #开发环境
# app.config['DEBUG'] = True         #允许调试


设置配置文件:
# 配置文件
ENV = 'development'  #开发环境
DEBUG = True         #允许调试

路由的请求与响应：
浏览器地址栏输入的内容：http://127.0.0.1:5000/index  --->服务器  --->app  --->有没有这个路由
--->就会执行路由匹配的内容  --->return ‘’hello world‘  ---->response  ---->客户端的浏览器

请求request
http协议:
resquest
请求行:   地址:http://0.0.0.0:8000/index
         请求方法: get  post
请求头:
请求体:

respnse
响应行:    状态码  200 ok  404  not found
响应头:
响应体:返回的内容


所有的路由规则都是自上而下进行搜索，在写路由时，路由是唯一的

return 返回
    字符串
    字典     {'a': '北京', 'b': '南京', 'c': '上海'}

2、视图
返回值：
response响应对象

request请求对象

3.模板