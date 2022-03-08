"""
使用list实现，python 不用考虑数组初始化大小的问题(自动扩容都让python给做了);
使用单链表实现，反向构造链表，好处，不用进行担心扩容问题
"""
import sys
sys.path.append("../")
from linked_list.wznode import Node


class ListStack(object):

    def __init__(self):
        """

        :param count: 原数个数
        """
        self.items = list()
        self.count = 0

    def push(self, data):
        print("ListStack push data {}".format(data))
        self.items.append(data)
        self.count += 1

    def pop(self):
        if self.count == 0:
            return None

        self.count -= 1
        return self.items[self.count]


class LinkedStack(object):

    def __init__(self):
        '''
        top 指针指向栈的顶部
        '''
        self.top = None

    def push(self, data):
        print("LinkedStack push data {}".format(data))
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        val = self.top.data
        self.top = self.top.next
        return val

    def print_all(self):
        p = self.top
        while p is not None:
            print("LinkedStack data {}".format(p.data))
            p = p.next


if __name__ == '__main__':
    a = ListStack()
    print(a.pop())

    for i in range(1, 4):
        a.push(i)
    for i in range(1, 4):
        print(a.pop())
    print(a.pop())

    print("----------test case for LinkedNode--------------")
    b = LinkedStack()
    print(b.pop())
    for i in range(1, 4):
        b.push(i)
    b.print_all()
    for i in range(1, 4):
        print(b.pop())
    print(b.pop())