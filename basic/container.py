"""
本文学习的Python容器的，对鞋代码帮助很大，经常用到
学习1：list列表--本质就是数据结构里面的有序链表
        1)创建list列表：列表就是用中括号 [] 括起来的数据，里面的每一个数据就叫做元素，元素不一定是相同的数据类型。
        2)访问list列表和修改list列表：下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符
        3)删除list列表：del 语句来删除列表或者列表中的元素
        4)迭代
        5)list列表的方法

学习2：tuple元组--有序列表 List,tuple 和 List 非常类似，但是 tuple 一旦初始化就不能修改
        1)创建tuple元组：元组就是用中括号 () 括起来的数据
        2)访问tuple元组和修改tuple元组：下标索引来访问元组中的值和-----记住，元组中的元素值是不允许修改的，但是有特例，这里不详细说，不修改便是
        3)删除tuple元组：del 语句来删除元组 ---------记住不可以删除元组里面的元素
        4)迭代
        5)tuple元组的方法:
        只有 len():
            max()和min():
            tuple(seq):将list列表转换为tuple元组

学习3：dict字典
        1)创建dict字典：字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号{}中
        2)访问dict字典和修改dict字典：dict["key"]访问和修改
        3)删除dict字典：del 语句来删除字典中或者字典中的元素
                       也可以调用 clear() 方法可以清除字典中的所有元素
        4)迭代
        5)dict字典的方法:
            掌握基本的即可 len()
            dict.value():返回所有值，没有键

学习4：容器的优势比较list与dict(链表跟hash一样的比较)
        1）dict 有以下几个特点：
            查找和插入的速度极快，不会随着key的增加而变慢
            需要占用大量的内存，内存浪费多

        2）list的特点则相反
            查找和插入的时间随着元素的增加而增加
            占用空间小，浪费内存很少
学习5：set的是哟个，先熟练掌握上面三种容器类型吧
"""
if __name__ == '__main__':
    """
    list列表的使用
    """
    # 创建了一个空的列表，当然也可以直接赋值创建
    list = []
    name = ['一点水', '两点水', '三点水', '四点水', '五点水']
    del name[0]
    #删除列表的元素
    print("删除后的值:{}".format(name))
    #迭代
    for x in name:
        print("输出遍历的值:{}".format(x))
    #list常用的方法
    length = len(name)#列表长度
    maxValue = max(name) #最大值
    minValue = min(name)
    list = list(('1点水', '2点水', '3点水', '4点水', '5点水')) #将元组转换为列表
    #list列表调用的方法
    name.append("六点水") #末尾增加
    name.insert(2,"中间增加的水") #中间增加
    name.extend(list) #末尾增加另外一个list

    name.pop()#末尾删除
    name.remove(2) #中间移除

    name.index("六点水") #查找元素值，并返回元素下标
    name.count("六点水") #查找元素出现的次数

    name.reverse() #反序
    name.sort()#排序


