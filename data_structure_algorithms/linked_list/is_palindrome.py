"""
    是否是回文
    链表解法:
        快慢指针找'中点'(即要开始反转的节点)，从该点开始反转链表后
        从两头进行判断

    数组解法:
        正反遍历即可

"""
from wznode import Node


def find_middle_node(head):
    '''
    找链表的中间节点，快慢指针,pq

    快慢指针的起点也可以都在头结点
    :param head:
    :return: 如果是基数个Node，返回p, 0(0代表正中间); 偶数个Node，返回p, -1(-1代表偶数情况下偏左)

    '''
    p = head
    q = head.next

    while q is not None:
        if q.next is None:
            return p, -1
        p = p.next
        q = q.next.next
    return p, 0


def jude_main(head):
    """
    找中点，反转后半部分链表，从两头开始遍历链表
    :param head:
    :return:
    """
    if head is None:
        return True

    middle_node, flag = find_middle_node(head)
    if flag == 0:
        begin_reverse_node = middle_node
    else:
        begin_reverse_node = middle_node.next

    tail_head = Node.linked_reverse(begin_reverse_node)
    while tail_head is not head:
        tail_data = tail_head.data
        head_data = head.data
        if tail_data != head_data:
            return False

        if head.next is tail_head:
            break
        head = head.next
        tail_head = tail_head.next

    return True


def chars_filter(line):
    result = []
    for ch in line:
        # print(type(ch)) <class 'str'>
        if ch.isdigit():
            result.append(ch)
        if ch.isalpha():
            result.append(ch.lower())
    return result


def jude_str(s):
    '''
    从前、从后开始遍历字符串，遇到要过滤的字符就保持每次只动一个方向的index，这样可以用到最外层的while循环；
    如果数据判断正确则可以两个方向的index都同时动

    错误思维：总想同时寻找左右两边的有效数据，这样会加上额外的'左右'两个内存循环，同时index还需要关联判断，越写越复杂.
    :param s:
    :return:
    '''
    l_index, r_index = 0, len(s) - 1
    while l_index < r_index:
        l_data = s[l_index]
        r_data = s[r_index]
        if not (l_data.isdigit() or l_data.isalpha()):
            l_index += 1
            continue
        if not (r_data.isdigit() or r_data.isalpha()):
            r_index -= 1
            continue

        if l_data.isalpha():
            l_data = l_data.lower()
        if r_data.isalpha():
            r_data = r_data.lower()

        if l_data != r_data:
            return False

        l_index += 1
        r_index -= 1

    return True


if __name__ == '__main__':
    # head = Node.init_linked_list([1, 2])
    # head = Node.init_linked_list([1, 2, 3, 2, 1])
    # head = Node.init_linked_list([1, 2])
    # head = Node.init_linked_list([1])
    # middle_node, flag = find_middle_node(head)
    # print(middle_node.data, flag)
    # print(jude_main(head))

    # res = chars_filter("A man, a plan, a canal: Panama")
    # res = chars_filter("")
    # print(res)
    # head = Node.init_linked_list(res)
    # print(jude_main(head))

    print(jude_str("A man, a plan, a canal: Panama"))
    print(jude_str(",,,12 1  21..."))
    print(jude_str("1,,"))