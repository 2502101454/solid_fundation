"""
理解快排平均时间复杂度和最坏时间复杂度:
这里两组输入
1、[1, 2, 3, 4]  最坏
2、[2, 1, 4, 3]  平均
根据输出结果发现：1的分区方法的执行次数比2多执行了1次
所以这就是时间复杂度上升的关键所在

结论：快排的时间复杂度主要在分区函数的执行次数上，分区不均匀执行次数 > 分区均匀执行次数

为啥分区均匀，分区函数执行的少，
因为分区均匀，假设每次都能对当前区间划分一半的话，下面quick_sort的区间start和end下标很快就可以碰在一起，结束递归，
这里每次划分一半就相当于是一个2份查找的复杂度，logn

如果分布不均匀，那么需要经历的n次才能让递归结束

数组有序的时候，快排的时间复杂度下降为o(n2)

"""

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
    print("pivot_index {}".format(pivot_index))
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
    k = start
    while k <= end:
        print(data_list[k])
        k += 1

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
    # print("partition len {}".format(end-start))
    return i


if __name__ == '__main__':
    data_list = [1,2,3,4]
    quick_sort(data_list=data_list, start=0, end=3)
    print("=============")
    data_list = [2, 1, 4, 3]
    quick_sort(data_list=data_list, start=0, end=3)
