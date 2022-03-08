"""
二分查找: 在一组有序的数组中查找

二分查找的时间复杂度是 O(logn)
"""


def bsearch(list_data, val):
    low = 0
    high = len(list_data) - 1
    while low <= high:
        middle = low + (high - low) // 2
        # mid=(low+high)/2 这种写法是有问题的。因为如果 low 和 high 比较大的话，两者之和就有可能会溢出。
        # 改进的方法是将 mid 的计算方式写成 low+(high-low)/2。这样除法就先计算后面(high-low)/2
        if list_data[middle] == val:
            return middle
        elif list_data[middle] > val:
            high = middle - 1
        else:
            low = middle + 1

    return -1


"""
递归实现二分查找
递推公式:
bs(list, s, e, data) = list[m] or bs(list, s, m-1, data) or bs(list, m+1, e, data)
终止条件:
    list[m] == data  or s > e
"""


def bsearch_recur(list_data, val):
    return bsearch_internally(list_data, low=0, high=len(list_data)-1, val=val)


def bsearch_internally(list_data, low, high, val):
    if low > high:
        return -1

    middle = low + (high - low) // 2
    if list_data[middle] == val:
        return middle
    elif list_data[middle] > val:
        return bsearch_internally(list_data, low, middle-1, val)
    else:
        return bsearch_internally(list_data, middle+1, high, val)


def bsearch_first_equal(list_data, val):
    """
    1.查找第一个值等于给定值的元素

    误区：陷入进行O(n)时间复杂度的数组挨个检索，那么给一组10000个5的数组，查找第一个5，岂不是要累死，要用到2分查找的特性
    :param list_data:
    :param val:
    :return:
    """
    low = 0
    high = len(list_data) - 1
    while low <= high:
        middle = low + (high - low) // 2
        # mid=(low+high)/2 这种写法是有问题的。因为如果 low 和 high 比较大的话，两者之和就有可能会溢出。
        # 改进的方法是将 mid 的计算方式写成 low+(high-low)/2。这样除法就先计算后面(high-low)/2
        if list_data[middle] == val:
            """
            当middle是已经是第数组首位了 或者 middle前面的元素不是val，那么middle肯定是第一个值等于给定值的元素;
            
            否则，middle-1也等于val，那我们就更新 high=mid-1，因为要找的元素肯定出现在[low, mid-1]之间(是闭区间)。
            """
            if middle == 0 or list_data[middle-1] != val:
                return middle
            else:
                high = middle - 1
        elif list_data[middle] > val:
            high = middle - 1
        else:
            low = middle + 1

    return -1


def bsearch_last_equal(list_data, val):
    """
    2.查找最后一个值等于给定值的元素


    :param list_data:
    :param val:
    :return:
    """
    low = 0
    high = len(list_data) - 1
    while low <= high:
        middle = low + (high - low) // 2
        # mid=(low+high)/2 这种写法是有问题的。因为如果 low 和 high 比较大的话，两者之和就有可能会溢出。
        # 改进的方法是将 mid 的计算方式写成 low+(high-low)/2。这样除法就先计算后面(high-low)/2
        if list_data[middle] == val:
            """
            当middle是已经是第数组末尾看 或者 middle后面的元素不是val，那么middle肯定是最后一个值等于给定值的元素;

            否则，middle+1也等于val，那我们就更新 low=mid+1，因为要找的元素肯定出现在[mid+1, high]之间(是闭区间)。
            """
            if middle == len(list_data) - 1 or list_data[middle + 1] != val:
                return middle
            else:
                low = middle + 1
        elif list_data[middle] > val:
            high = middle - 1
        else:
            low = middle + 1

    return -1


def bs_first_gte(list_data, val):
    """
    查找第一个大于等于给定值的元素
    误区：陷入分命中和不命中两种情况，大于等于泛化成一种情况处理即可
    :param list_data:
    :param val:
    :return:
    """
    low = 0
    high = len(list_data) - 1
    while low <= high:
        middle = low + (high - low) // 2
        # mid=(low+high)/2 这种写法是有问题的。因为如果 low 和 high 比较大的话，两者之和就有可能会溢出。
        # 改进的方法是将 mid 的计算方式写成 low+(high-low)/2。这样除法就先计算后面(high-low)/2
        if list_data[middle] >= val:
            """
            当middle是已经是第数组首位 或者 middle前面的元素小于val，那么middle肯定是第一个值大于等于给定值的元素;

            否则，middle-1也大于等于val，那我们就更新 high=mid-1，因为要找的元素肯定出现在[low, mid-1]之间(是闭区间)。
            """
            if middle == 0 or list_data[middle - 1] < val:
                return middle
            else:
                high = middle - 1
        else:
            low = middle + 1

    return -1


def bs_last_lte(list_data, val):
    """
    查找最后一个小于等于给定值的元素
    :param list_data:
    :param val:
    :return:
    """
    low = 0
    high = len(list_data) - 1
    while low <= high:
        middle = low + (high - low) // 2
        # mid=(low+high)/2 这种写法是有问题的。因为如果 low 和 high 比较大的话，两者之和就有可能会溢出。
        # 改进的方法是将 mid 的计算方式写成 low+(high-low)/2。这样除法就先计算后面(high-low)/2
        if list_data[middle] <= val:
            """
            当middle是已经是第数组首位 或者 middle前面的元素小于val，那么middle肯定是第一个值大于等于给定值的元素;

            否则，middle+1也小于等于val，那我们就更新 low=mid+1，因为要找的元素肯定出现在[mid+1, high]之间(是闭区间)。
            """
            if middle == len(list_data) - 1 or list_data[middle + 1] > val:
                return middle
            else:
                low = middle + 1
        else:
            high = middle - 1

    return -1


def search(nums, target):
    """
    1.将数组从中间分开成左右两部分的时候，一定有一部分的数组是有序的
    2.对有序部分进行二分查找，如果需要在无序部分进行查找，可以继续分为1的情况
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    low = 0
    high = len(nums) - 1

    while (low <= high):
        middle = low + ((high - low) >> 1)
        print(low, high)
        print(middle)
        if nums[middle] == target:
            return middle
        # low 和 high是可控的，所以额外判断可能减少运行时间
        if nums[low] == target:
            return low
        if nums[high] == target:
            return high

        # 查找有序部分

        # 如果[low, middle -1] 有序
        if nums[low] <= nums[middle - 1]:
            # target 符合 有序范围
            if target >= nums[low] and target <= nums[middle - 1]:
                high = middle - 1
            else:
                # 在对应无序那部分继续找
                low = middle + 1
                print(low)

        else:
            # 如果[middle +1, high] 有序
            # target 符合 有序范围
            if target >= nums[middle + 1] and target <= nums[high]:
                low = middle + 1
            else:
                # 在对应无序那部分继续找
                high = middle - 1

    return -1


if __name__ == '__main__':
    # list_data = [3, 5, 7, 8, 9]
    # print(bsearch(list_data=list_data, val=8))
    # print(bsearch_recur(list_data=list_data, val=8))
    # print(bsearch(list_data=list_data, val=9))
    # print(bsearch_recur(list_data=list_data, val=9))
    # print(bsearch(list_data=list_data, val=10))
    # print(bsearch_recur(list_data=list_data, val=10))
    # print(bsearch(list_data=list_data, val=0))

    # list_data = [1, 3, 5, 5, 5, 6, 8]
    # print(bsearch_first_equal(list_data=list_data, val=5))
    # print(bsearch_last_equal(list_data=list_data, val=5))
    # print(bs_first_gte(list_data=list_data, val=5))
    # print(bs_last_lte(list_data=list_data, val=5))

    nums = [4,5,6,7,0,1,2]
    print(search(nums, 0))