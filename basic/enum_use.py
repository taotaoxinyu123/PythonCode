"""
本文学习的Python里面的枚举
学习1：枚举的概念
        1）枚举类型可以看作是一种标签或是一系列常量的集合，通常用于表示某些特定的有限集合，例如星期、月份、状态等。
        2）定了了枚举后，成员名和成员就不能改变
学习2：枚举的使用
        1)定义枚举时，成员名不允许重复
        2)成员值允许相同(默认)，若要不能定义相同的成员值，可以通过 unique 装饰
        3)枚举取值(互相取值)
            通过成员名来获取成员
            通过成员值来获取成员
"""
from enum import Enum, unique
class Color(Enum):
    red   = 1
    green = 1
    blue  = 4

print(Color['red'])  #  通过成员名来获取成员
print(Color(4))  #  通过成员值来获取成员

@unique
class Color(Enum):
    red = 1
    green = 2
    blue = 3
