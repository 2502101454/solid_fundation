"""
冒泡排序:
    每一轮从左到右，相邻数据进行比较，不满足大小关系则相邻数据互换。
    一轮冒泡会让至少一个元素移动到它应该在的位置，重复 n 次，就完成了 n 个数据的排序工作。
    优化：当某次冒泡操作已经没有数据交换时，说明已经达到完全有序，不用再继续执行后续的冒泡操作

    冒泡排序包含两个操作原子，比较和交换。

    我的理解：
    好像其实重复n-1次就够了，假设有n个数据，那么就有n个位置，所以n-1就可以让n-1个数据确定了它们应该在的位置，
    那么剩下的那个第n-1个数据自然也在应该在的位置
    代码执行上，最后一轮内存for循环初始化直接结束，执行不了的
"""


def bubble_sort(input_list):
    len_list = len(input_list)
    # range(0, 4) 即 [0, 1, 2, 3]
    # 外层循环代表多少轮，内层表示每一轮直接的比较、移动
    # 比较n轮，最后一轮真是多余的?
    for i in range(1, len_list + 1):
        flag = False
        for j in range(0, len_list - i):
            print(j)
            if input_list[j] > input_list[j + 1]:
                tmp = input_list[j]
                input_list[j] = input_list[j + 1]
                input_list[j + 1] = tmp
                flag = True
        print("current list {}".format(input_list))
        if not flag:
            print("this round no data exchange~")
            break


"""
插入排序:
    我们将数组中的数据分为两个区间，已排序区间和未排序区间。初始已排序区间只有一个元素，就是数组的第一个元素。
    插入算法的核心思想是取未排序区间中的元素，在已排序区间中找到合适的插入位置将其插入(从尾遍历已排序区间)，并保证已排序区间数据一直有序。
    重复这个过程，直到未排序区间中元素为空，算法结束。

插入排序也包含两种操作，一种是元素的比较，一种是元素的移动
"""


def insert_sort(input_list):
    input_list = [3, 1, 4, 2, 6, 5]
    # input_list = [1,2,3, -1]
    len_list = len(input_list)

    # range(start, stop, step) 逆序: range(3, -1, -1), [3, 2, 1, 0]

    # n个元素，第一个元素设为已排序，n-1个元素未排序， 则要取n-1个元素进行每轮的比较
    # 外层循环是未排序的区间
    for i in range(1, len_list):
        value = input_list[i]
        j = i - 1
        # 内层循环是对已经排序区间从尾部遍历
        # java的for循环终止时候i是肯定不符合大小判断条件的，但是python中，这里用range模拟的都是正确的下标情况，所以建议使用while
        while j >= 0:
            if input_list[j] > value:
                input_list[j+1] = input_list[j]
            else:
                break
            j -= 1

        # for j in range(i-1, -1, -1):
        #     if input_list[j] > value:
        #         input_list[j+1] = input_list[j]
        #     else:
        #         break
        input_list[j+1] = value
    print(input_list)

"""
选择排序算法的实现思路有点类似插入排序，也分已排序区间和未排序区间。
但是选择排序每次会从未排序区间中找到最小的元素，将其放到已排序区间的末尾(交换)
"""


def select_sort(input_list):
    len_list = len(input_list)
    # 外层表示多少轮
    for i in range(0, len_list):
        min_index = i
        j = i
        # 内层表示这一轮开始寻找最小数据
        while j < len_list:
            if input_list[j] < input_list[min_index]:
                min_index = j
            j += 1

        tmp = input_list[i]
        input_list[i] = input_list[min_index]
        input_list[min_index] = tmp


"""
归并排序：
    分治思想，拆分子问题，递归技巧求解
    原问题：data_list, 下标p ~ r 的数组排序
    规律：转化子问题，原数组分为两半，两半各自都排好序，然后对两半进行merge，即合并两个有序的数组
    两半的下标分布： p ~ m  m即(p+r)/2 即p + (r-p)/2, m+1 ~ r
    
    递推公式：merge_sort(data_list, p, r) = merge(merge_sort(data_list, p, m), merge_sort(data_list, m+1, r))
    递推终止条件: p >= r 即当前只对应一个元素的时候，不用再分下去了
    
    PS：假设子问题都已解，即对应这里，假设两半各自都已经排好序
    如何理解递归代码呢？如果一个问题A可以分解为若干个子问题B、C、D，你可以假设子问题B、C、D已经解决。而且，
    你只需要思考问题A与子问题B、C、D两层之间的关系即可
        
"""


def merge_sort_main(data_list):
    """
    归并排序入口函数
    :param data_list:
    :return:
    """
    merge_sort(data_list, 0, len(data_list)-1)


def merge_sort(data_list, start, end):
    """
    表示对 data_list，在区间start至end上进行排序
    :param data_list:
    :param start:
    :param end:
    :return:
    """
    if start >= end:
        return
    # 注意 python 3的取整除法
    middle = (start + end) // 2
    merge_sort(data_list, start, middle)
    merge_sort(data_list, middle + 1, end)

    merge(data_list, start, middle, middle+1, end)


def merge(data_list, cur1, cur2, cur3, cur4):
    """
    对两个有序区间进行合并，最终修改原数组data_list
    已知data_list的cur1 到 cur2的区间是有序的
    cur3 到 cur4的区间是有序的
    :param data_list:
    :param cur1:
    :param cur2:
    :param cur3:
    :param cur4:
    :return:
    """
    tmp = []
    i, j = cur1, cur3
    while i <= cur2 and j <= cur4:
        if data_list[i] <= data_list[j]:
            tmp.append(data_list[i])
            i += 1
        else:
            tmp.append(data_list[j])
            j += 1

    while i <= cur2:
        tmp.append(data_list[i])
        i += 1

    while j <= cur4:
        tmp.append(data_list[j])
        j += 1

    for i in range(0, len(tmp)):
        data_list[cur1+i] = tmp[i]
    print("cur 1 {} cur 4 {} data_list {}".format(cur1, cur4, data_list))


"""
快速排序:
    如果要排序数组中下标从 p 到 r 之间的一组数据，我们选择 p 到 r 之间的任意一个数据作为 pivot（分区点）(分区点一般选取最后一个数组元素)
    我们遍历 p 到 r 之间的数据，将小于 pivot 的放到左边，将大于 pivot 的放到右边，将 pivot 放到中间(下标q)。经过这一步骤之后，
    数组 p 到 r 之间的数据就被分成了三个部分，前面 p 到 q-1 之间都是小于 pivot 的，中间是 pivot，后面的 q+1 到 r 之间是大于 pivot 的。
    
    根据分治、递归的处理思想，我们可以用递归排序下标从 p 到 q-1 之间的数据和下标从 q+1 到 r 之间的数据，直到区间缩小为 1，就说明所有的数据都有序了
    
    递推公式：
    quick_sort(p…r) = quick_sort(p…q-1) + quick_sort(q+1… r)
    终止条件：
    p >= r
"""


def quick_sort_main(data_list):
    quick_sort(data_list, 0, len(data_list) - 1)


def quick_sort(data_list, start, end):
    """

    :param data_list:
    :param start: 开始下标
    :param end: 结束下标
    :return:
    """
    if start >= end:
        return
    pivot_index = partition(data_list, start, end)
    quick_sort(data_list, start, pivot_index - 1)
    quick_sort(data_list, pivot_index + 1, end)


def partition(data_list, start, end):
    """
    选取数组最后元素作为pivot值，对data_list进行整理，思想：
    在数组头指定两个游标i, j，利用选择排序的思想，j遍历一次data_list, i专门存放小于pivot的元素(a[i]和a[j]交换, i++)，那么最后a[i]和
    pivot值(即a[end])交换一下，则就构成了 pivot在中间，左边小，右边大的场面.
    :param data_list:
    :param start:
    :param end:
    :return: 返回pivot值 最后存放的位置
    """

    pivot = data_list[end]
    i, j = start, start
    while j <= end:
        if data_list[j] < pivot:
            tmp = data_list[i]
            data_list[i] = data_list[j]
            data_list[j] = tmp
            i += 1
        j += 1

    tmp = data_list[i]
    data_list[i] = pivot
    data_list[end] = tmp

    return i

def quick_sort2(data_list, start, end):
    l, r = start, end
    pivod = data_list[l]
    while l < r:


"""
首先桶排序有两种情况，一种是数据范围较大时，先进行整体扫描，然后分范围各自先排序，然后再拼接；
一种是范围不大，就分范围个桶，把相同的数据放到同一个桶中（即下标就是数据值，下标位置存放的是等于该下标值的数值的个数），然后再按桶一次排序。
而计数排序则是在下标位置上，存入的是比该下标值小于或等于的数值的个数

桶排序（桶内使用归并排序，保证稳定性）：
首先，要排序的数据需要很容易就能划分成 m 个桶，并且，桶与桶之间有着天然的大小顺序。这样每个桶内的数据都排序完之后，桶与桶之间的数据不需要再进行排序。
其次，数据在各个桶之间的分布是比较均匀的。如果数据经过桶的划分之后，有些桶里的数据非常多，有些非常少，很不平均，那桶内数据排序的时间复杂度就不是常量级了。
在极端情况下，如果数据都被划分到一个桶里，那就退化为 O(nlogn) 的排序算法了

计数排序：
计数排序其实是桶排序的一种特殊情况。当要排序的 n 个数据，所处的范围并不大的时候，比如最大值是 k，我们就可以把数据划分成 k 个桶。
每个桶内的数据值都是相同的，省掉了桶内排序的时间。
计数排序只能用在数据范围不大的场景中，如果数据范围 k 比要排序的数据 n 大很多，就不适合用计数排序了。而且，计数排序只能给非负整数排序，
如果要排序的数据是其他类型的，要将其在不改变相对大小的情况下，转化为非负整数。

基数排序：
基数排序对要排序的数据是有要求的，需要可以分割出独立的“位”来比较，而且位之间有递进的关系，如果 a 数据的高位比 b 数据大，那剩下的低位就不用比较了。
除此之外，每一位的数据范围不能太大，要可以用线性排序算法来排序，否则，基数排序的时间复杂度就无法做到 O(n) 了。
因为基数排序算法需要借助桶排序或者计数排序来完成每一个位的排序工作。
"""

"""
排序算法优化：

快速排序最坏时间复杂度 O(n2)
我举一个比较极端的例子。如果数组中的数据原来已经是有序的了，比如 1，3，5，6，8。如果我们每次选择最后一个元素作为 pivot，那每次分区得到的两
个区间都是不均等的。我们需要进行大约 n 次分区操作，才能完成快排的整个过程。每次分区我们平均要扫描大约 n/2 个元素，这种情况下，快排的时间
复杂度就从 O(nlogn) 退化成了 O(n2)。实际上，这种 O(n2) 时间复杂度出现的主要原因还是因为我们分区点选得不够合理。

a.优化，在pivot分区方面:
最理想的分区点是：被分区点分开的两个分区中，数据的数量差不多。
1. 三数取中法,我们从区间的首、尾、中间，分别取出一个数，然后对比大小，取这 3 个数的中间值作为分区点。
2. 随机法, 随机法就是每次从要排序的区间中，随机选择一个元素作为分区点。

b.优化，递归深度限制：
快速排序是用递归来实现的。递归要警惕堆栈溢出。为了避免快速排序里，递归过深而堆栈过小，导致堆栈溢出，
我们有两种解决办法：第一种是限制递归深度。一旦递归过深，超过了我们事先设定的阈值，就停止递归。
第二种是通过在堆上模拟实现一个函数调用栈，手动模拟递归压栈、出栈的过程，这样就没有了系统栈大小的限制。

在小规模数据面前，O(n2) 时间复杂度的算法并不一定比 O(nlogn) 的算法执行时间长。
时间复杂度代表的是一个增长趋势，如果画成增长曲线图，你会发现 O(n2) 比 O(nlogn) 要陡峭，也就是说增长趋势要更猛一些。
但是，我们前面讲过，在大 O 复杂度表示法中，我们会省略低阶、系数和常数，也就是说，O(nlogn) 在没有省略低阶、系数、常数之前可能是 O(knlogn + c)，
而且 k 和 c 有可能还是一个比较大的数。
"""


if __name__ == '__main__':
    # input_list = [5, 4, 2, 3, 4, 6, 1]
    # input_list = [5, 4, 3, 2, 1]
    # input_list = [3, 2 , 1]
    # input_list = [1, 3, 4, 2, 5]
    input_list = [1, 2, 3, 4, 5]
    # input_list = [1]
    # bubble_sort(input_list)

    # insert_sort(input_list)
    # select_sort(input_list)
    # merge_sort_main(input_list)
    quick_sort_main(input_list)
    print(input_list)
