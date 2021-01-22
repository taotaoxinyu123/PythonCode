"""
本文学习的Python值传递的问题，写代码都不知道写的变量怎么变化了
学习1：在 Python 中，字符串，整形，浮点型，tuple 是不可更改的对象，而 list ， dict 等是可以更改的对象。
        不可更改的类型：变量赋值 b = 1，其实就是生成一个整形对象 1 ，然后变量 b 指向 1，当 b = 1000 其实就是再生成一个整形对象 1000(重新生成很重要，前面提及不可改变，相互呼应)，
        然后改变 b 的指向，不再指向整形对象 1 ，而是指向 1000，最后 1 会被丢弃
        可更改的类型：变量赋值 a = [1,2,3,4,5,6] ，就是生成一个对象 list ，list 里面有 6 个元素，
        而变量 a 指向 list ，a[2] = 5则是将 list a 的第三个元素值更改,这里跟上面是不同的，并不是将 a 重新指向，而是直接修改 list 中的元素值。
额外学习2：调整代码风格：Alt+Ctrl+L
额外学习3：
        print('函数中一开始 b 的值：{}'.format(b)) 这样输出很好用，可以针对任何类型
"""


def chagne_number(b):
    print('函数中一开始 b 的值：{}'.format(b))
    b = 1000
    print('函数中 b 赋值后的值：{}'.format(b))


def chagne_list(a):
    print('函数中一开始 a 的值：{}'.format(a))
    a.append(1000)
    print('函数中 a 赋值后的值：{}'.format(a))


if __name__ == '__main__':
    b = 1
    chagne_number(b)
    print('最后输出 b 的值：{}'.format(b))

    a = [1, 2, 3, 4, 5]
    chagne_list(a)
    print('最后输出 a 的值：{}'.format(a))
