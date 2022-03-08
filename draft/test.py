from multiprocessing import Process,JoinableQueue,Queue
import  time,random


def producter(name, q):
    for i in range(3):
        time.sleep(random.randint(1,2))
        print("\033[46m%s生产了 热狗%s\033[0m" % (name,i))
        q.put("%s的 热狗%s" % (name,i))


def customer(name, q):
    while True:
        time.sleep(random.randint(1, 2))
        hot_dog = q.get()
        # get默认就是阻塞的，如果设置不阻塞就会刨除Empty exception
        """
         def get(self, block=True, timeout=None):
            Remove and return an item from the queue.

            If optional args 'block' is true and 'timeout' is None (the default),
            block if necessary until an item is available. If 'timeout' is
            a non-negative number, it blocks at most 'timeout' seconds and raises
            the Empty exception if no item was available within that time.
            Otherwise ('block' is false), return an item if one is immediately
            available, else raise the Empty exception ('timeout' is ignored
            in that case).
        """
        print("\033[47m%s 吃掉了 %s \033[0m" % (name, hot_dog))


if __name__ == '__main__':
    q = Queue()

    p1 = Process(target=producter,args=("北京?店",q))
    p2 = Process(target=producter,args=("上海?店",q))
    p3 = Process(target=producter, args=("深圳?店", q))
    p1.start()
    p2.start()
    p3.start()

    c1 = Process(target=customer,args=("王思聪",q))
    c1.start()