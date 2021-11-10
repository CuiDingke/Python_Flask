import requests

r = requests.get('https://www.baidu.com', verify=False)
print(r.status_code)
print(r.content)


def replace_hello(value):
    print('----------->', value)
    value = value.replace('hello', '')
    print('=======>', value)
    return value


r = replace_hello('hello world!!!')
# strip() 去除前面空格
print(r.strip())



# 继承
class Person():
    def run(self):
        print('run....')


class Student(person)
    pass
