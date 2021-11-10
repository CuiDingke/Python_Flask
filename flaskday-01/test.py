class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print('%s正在学习！！！' % (self.name))

stu = Student('Bing')
stu.study()