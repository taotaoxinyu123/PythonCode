"""
本文学习的Python线程的通信：用于解决解决复杂的同步问题。
学习1：如果程序中有多个线程，这些线程避免不了需要相互通信的。那么我们怎样在这些线程之间安全地交换信息或数据呢？
        1）从一个线程向另一个线程发送数据最安全的方式可能就是使用 queue 库中的队列了。
        2）创建一个被多个线程共享的 Queue 对象，这些线程通过使用 put() 和 get() 操作来向队列中添加或者删除元素。
学习2：为啥一直读数据，没有读到空的数据呢？

"""
# -*- coding: UTF-8 -*-
from queue import Queue
from threading import Thread
import time

isRead = True


def write(q):
    # 写数据进程
    for value in ['两点水', '三点水', '四点水']:
        print('写进 Queue 的值为：{0}'.format(value))
        q.put(value)
        time.sleep(1)

def read(q):
    # 读取数据进程
    while isRead:
        value = q.get(True)
        print('从 Queue 读取的值为：{0}'.format(value))


if __name__ == '__main__':
    q = Queue()
    t1 = Thread(target=write, args=(q,))
    t2 = Thread(target=read, args=(q,))
    t1.start()
    t2.start()