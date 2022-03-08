"""
理解协程：
    提个额外概念，子程序： 就是函数；
    子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。

    比如子程序A、B：
    def A():
        print('1')
        print('2')
        print('3')

    def B():
        print('x')
        print('y')
        print('z')

    假设由协程执行，在执行A的过程中，可以随时中断，去执行B，B也可能在执行过程中中断再去执行A，结果可能是：
    1
    2
    x
    y
    3
    z

    看起来A、B的执行有点像多线程，但协程的特点在于是一个线程执行

协程，又称微线程，英文名Coroutine，是运行在单线程中的“并发”，协程相比多线程的一大优势就是省去了多线程之间的切换开销，获得了更高的运行效率

进程/线程：操作系统提供的一种并发处理任务的能力。
协程：程序员通过高超的代码能力，在代码执行流程中人为的实现多任务并发，是单个线程内的任务调度技巧


参考廖老师的例子好理解~
Python对协程的支持是通过generator实现的。
因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能

"""

# import time
#
#
# def task1():
#     while True:
#         yield "<甲>也累了，让<乙>工作一会儿"
#         time.sleep(1)
#         print("<甲>工作了一段时间.....")
#
#
# def task2(t):
#     """
#     只有包含了yield关键字的才是一个生成器函数，所以，task2就是一个普通的函数
#     :param t:
#     :return:
#     """
#
#     """
#     这个开头next(t):
#     1.激活task1 生成器对象
#     2.注意这里并没有打印next(t)的值哈
#     """
#     next(t)
#     while True:
#         print("-----------------------------------")
#         print("<乙>工作了一段时间.....")
#         time.sleep(2)
#         print("<乙>累了，让<甲>工作一会儿....")
#         ret = t.send(None)
#         print(ret)
#     t.close()

"""
传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。

如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高：

整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务
"""


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    # 等效于next(c) 激活生成器对象
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


if __name__ == '__main__':
    # t = task1()
    # task2(t)
    c = consumer()
    produce(c)