"""
本文学习的Python类里面的继承
学习1：类的继承与定义
        1)概念：新类继承旧类，这样子新类也就有这个功能了（功能是属性和方法）
            单继承：class ClassName(BaseClassName):
            支持多继承：class ClassName(Base1,Base2,Base3):
        2)那么继承的子类可以干什么呢？
            会继承父类的属性和方法;
            可以自己定义，覆盖父类的属性和方法;
学习2：类的继承的使用
        1)子类调用父类的方法：直接调用即可
        2)子类重写父类的方法----------------------需要特别记忆
        3)类型判断：isinstance() 函数
            isinstance(user3, User2):相同类型返回True,不同则返回False
学习3：类的多态
        1）有了继承，才有了多态，也会有不同类的对象对同一消息会作出不同的相应
"""
class UserInfo(object):
    lv = 5

    def __init__(self, name, age, account):
        self.name = name
        self._age = age
        self.__account = account

    def get_account(self):
        return self.__account

    @classmethod
    def get_name(cls):
        return cls.lv

    @property
    def get_age(self):
        return self._age

class UserInfo2(UserInfo):
    # 子类重写父类的方法
    def __init__(self, name, age, account, sex):
        super(UserInfo2, self).__init__(name, age, account)
        self.sex = sex;
    # 子类调用父类的方法
    def function2(self):
        self.get_account()
if __name__ == '__main__':
    userInfo2 = UserInfo2('两点水', 23, 347073565, '男');
    # 打印所有属性
    print(dir(userInfo2))
    # 打印构造函数中的属性
    print(userInfo2.__dict__)
    print(UserInfo2.get_name())