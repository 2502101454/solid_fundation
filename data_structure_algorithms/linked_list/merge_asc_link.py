from wznode import Node


def merge(l1, l2):
    '''

    题目描述: 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

    题解: 创建一个头结点(技巧，哨兵节点)，再依次比较

    :param l1:  listNode
    :param l2:  listNode
    :return:    listNode
    '''
    head = Node(None)
    head_p = head

    while l1 is not None and l2 is not None:
        if l1.data <= l2.data:
            head_p.next = l1
            l1 = l1.next
        else:
            head_p.next = l2
            l2 = l2.next

        head_p = head_p.next

    if l1 is None:
        head_p.next = l2
    if l2 is None:
        head_p.next = l1

    return head.next