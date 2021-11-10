db.session.add(user)
db.session.commit()

模型类.query.all()  ---->列表
模型类.query.get()  ---->对象
user = User.query.filter_by(username='bing').first()  ---->对象
********** 模型类.query.filter() ***********
1. 模型类.query.filter().all()  --------->列表  里面  是  字典对象
2. 模型类.query.filter().first()  ------->对象
3.
    user = User.query.filter(User.username=='bing').all()
    user = User.query.filter(User.username.startswith('b')).all()
    user = User.query.filter(User.username.contains('b')).all()
    user = User.query.filter(User.username.like('b%')).all()
4.
    user = User.query.filter(or_(User.username.like('b%'), User.username.contains('i'))).all()
    #### select * from user where username like 'b%' or username like '%i%'
    user = User.query.filter(and_(User.rdatetime.__lt__('2021-09-06 22:05:58'), User.username.contains('b'))).all()
    user = User.query.filter(and_(User.rdatetime < '2021-09-06 22:05:58', User.username.contains('b'))).all()
    user = User.query.filter(not_( User.username.contains('b'))).all()
    user = User.query.filter(User.phone.in_(['154254','15736980819'])).all()
    并且: and_     或者: or_   not_--->不等于
    补充: __gt__,__lt__,__ge__,__le__,__eq__,__nq__   ----------->应用(整型，日期)
    也可以：  >      <      >=     <=    =      !=
    user = User.age.between(15,30)


    select * from user where age in [12,15,48,26];
    # 升序
    user = User.query.order_by('rdatetime').all()
    user = User.query.filter(User.username.contains('b')).order_by('rdatetime').all()
    # 倒序
    user = User.query.order_by(-User.rdatetime).all()
    user = User.query.filter(User.username.contains('b')).order_by(-User.rdatetime).all()


    限制:limit
    user = User.query.order_by(-User.rdatetime).limit(2).all()
    user = User.query.order_by(-User.rdatetime).offset(2).limit(2).all()