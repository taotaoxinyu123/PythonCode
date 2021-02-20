"""
本文学习的Python类与对象的，在实际代码中经常用到
学习1：类的定义和调用
        1)类的定义：class A()：属性+方法(通常不用加访问权限修饰词)
        2)变量、方法的访问：类.属性   类.方法
学习2：类方法
        1)类方法如何调用类属性----------------重要
            在方法上面，用 @classmethod 声明该方法是类方法。只有声明了是类方法，才能使用类属性
            类方法想要使用类属性，在第一个参数中，需要写上 cls , cls 是 class 的缩写，其实意思就是把这个类作为参数，传给自己，这样就可以使用类属性了
            类属性的使用方式就是 cls.变量名
        2)类方法传递参数:与普通函数传递参数一样
学习3：类与对象
        1)类的实例化--生成对象
            实例名 = 类() 的方式实例化对象，为类创建一个实例
            使用 实例名.函数() 的方式调用对应的方法 ，使用 实例名.变量名 的方法调用类的属性
            你把类实例化之后，里面的属性和方法，就不叫类属性和类方法了，改为叫实例属性和实例方法，也可以叫对象属性和对象方法(方法里面的参数 cls 改为 self)------------重要
        2)重写
            类方法重写：类.原始函数 = 新函数 ；要注意的是，这里的赋值是在替换方法，并不是调用函数。所以是不能加上括号的，也就是 类.原始函数() = 新函数() 这个写法是不对的
            不能重写实例方法
        3)实例属性与类属性关系：
            类属性改变后，实例属性随之改变；
            实例属性改变后，类属性不改变；
        4）实例方法与类方法关系：
            类方法改变了，实例方法也是会跟着改变
            实例方法不可以重写
学习4：初始化函数--构造函数(初始化函数的意思是，当你创建一个实例的时候，这个函数就会被调用)
            __init__(self) 函数就是初始化函数,第一个参数一定要写上 self，不然会报错
      析构函数(这个当一个对象销毁的时候，就会调用析构函数)
            __del__(self);写法：del 实例名
"""
class ClassA():
    #学习1
    var1 = 100
    var2 = 0.01
    var3 = '两点水'

    def fun1():
        print('我是 fun1')

    def fun2():
        print('我是 fu2')

    def fun3():
        print('我是 fun3')
    #学习2
    @classmethod
    def fun4(cls,age): #类方法
        print("我是类函数，我的年纪是：{}".format(age))
    #学习3
    def fun5(self,age): #对象方法
        print("我是对象函数：我的年纪是：{}".format(age))
    #学习4
    def __init__(self,var1,var2,var3):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
if __name__ == '__main__':
    #学习1
    print(ClassA.var1)
    ClassA.fun1()
    #学习2
    ClassA.fun4(18)
    #学习3
    a = ClassA(1,2,3) #类的实例化
    a.fun4(19)
    def changeFun4(cls,age):
        print("我是改变类方法函数,我的年纪是：{}".format(age))
    ClassA.fun4 = changeFun4 #重写类方法+改变类方法
    a.fun4(18)
    #学习4
    del a