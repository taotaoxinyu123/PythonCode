from loguru import logger
import time

"""
本文学习的Python日志怎么使用，使用的loguru的库，它非常的方便和快捷，在github很受推崇
学习1：输出文件位置：1）logger.add("D://PycharmCode//taoxinyu//runtime_{time}.log")
                        可以使用绝对路径，如上所示；
                        可以使用相对路径，例如：runtime_{time}.log或者 ./runtime_{time}.log
                        文件名字可以自己定义，这里自己加了一个{time}，log的文件就可以带时间显示
                    2）logger.add("D://PycharmCode//taoxinyu//runtime_{time}.log", rotation="1 MB")
                        当日志文件达到1MB时候则就创建新的log文件，这时候就明白了加了一个{time}的好处
                        rotation="1 MB"：表示如上所描述
                        rotation="00:00"：表示可以实现每天 0 点新创建一个 log 文件输出了
                        rotation="1 week"：表示每隔一周创建一个 log 文件
学习2：输出日志级别：logger.add("D://PycharmCode//taoxinyu//runtime_{time}.log", level="DEBUG", rotation="1 MB")
                        level="DEBUG"表示输出大于DEBUG的日志级别，其他级别是INFO，DEBUG，WARNING,ERROR
学习3：输出日志文件带参数：logger.info("输出的是：%s" %(a[i]))
                        其实跟print输出带参数是一样的
学习4：try-except中使用日志：其实try-except应该是使用日志最多的地方

学习5：@logger.catch()的使用：在函数的上方加上，可以具体查看出具体的错误显示-----这个感觉第一次惊艳到了我

"""


@logger.catch()
def testerror():
    a = ["1", "2", "3"]
    for i in range(4):
        logger.info("输出的是：%s" % (a[i]))


if __name__ == '__main__':
    logger.add("D://PycharmCode//taoxinyu//runtime_{time}.log", level="DEBUG", rotation="1 MB")
    while True:
        logger.info("That's it, beautiful and simple logging!")
        logger.debug("That's debug information!")
        try:
            testerror()
        except  Exception as ex:
            logger.error('start exception:[%s]' % str(ex))
        time.sleep(1)
