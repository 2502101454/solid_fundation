"""
优先考虑正常情况，边界问题往往是正常情况的特殊case，不然一上来就考虑边界问题会让思维混乱；
边界情况可能是在正常情况的基础上进行的补充；
p：上一个节点
q: 下一个节点
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    @staticmethod
    def init_linked_list(values):
        len_v = len(values)
        i = len_v - 1
        q = None
        while i >= 0:
            p = Node(values[i])
            p.next = q
            q = p
            i = i - 1

        return q

    @staticmethod
    def iter_linked_list(head):
        print("iter linked begin..")
        while head is not None:
            print(head.data)
            head = head.next
        print("iter linked over..")

    @staticmethod
    def linked_reverse(head):
        p = head
        q = p.next
        while q is not None:
            tmp = q.next
            q.next = p
            p = q
            q = tmp
        head.next = None
        return p


if __name__ == '__main__':
    # print(Node.init_linked_list([]))
    # head = Node.init_linked_list(["a", "b", "c"])
    head = Node.init_linked_list(["a", "b", "c", "d"])
    head = Node.init_linked_list(["a"])
    head = Node.linked_reverse(head)
    Node.iter_linked_list(head=head)
    print("outside head data {}".format(head.data))