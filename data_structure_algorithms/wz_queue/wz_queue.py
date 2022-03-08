import sys
sys.path.append("../")
from linked_list.wznode import Node


class LinkedQueue(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        """
        初始时，tail是None head也是None；
        """
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node

        self.tail = new_node

    def dequeue(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next
            if self.head is None:
                "出队至空时，head是None，tail置为None，下次入队重新初始化队列"
                self.tail = None

            return data


if __name__ == '__main__':
    lq = LinkedQueue()
    print(lq.dequeue())
    lq.enqueue(1)
    lq.enqueue(4)
    lq.enqueue(3)
    print(lq.dequeue())
    print(lq.dequeue())
    lq.enqueue(5)
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
    lq.enqueue(6)
    lq.enqueue(7)
    print(lq.dequeue())
    print(lq.dequeue())
    print(lq.dequeue())
