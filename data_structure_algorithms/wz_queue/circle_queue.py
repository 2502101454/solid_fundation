"""
环形队列，定义head、tail两个下标:
    队列为空时 head == tail
    队列满时 (tail + 1) % size == head  (浪费一个数组存储空间，从而不会和判断队列为空的条件冲突，也不用引入额外的变量判断队满)
    普通入队出队的时，head tail的更新都是要进行取模运算，这样才能维持在0~size-1的下标
"""


class CircleQueue(object):

    def __init__(self, size):
        self.size = size
        self.queue = []
        self.head = 0
        self.tail = 0

    def enqueue(self, data):
        if (self.tail + 1) % self.size == self.head:
            return False
        self.queue[self.tail] = data
        self.tail = (self.tail + 1) % self.size
        return True

    def dequeue(self):
        if self.tail == self.head:
            return None
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.size
        return data