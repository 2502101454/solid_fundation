'''
迭代工具：
    能够从左向右扫描对象的工具，常见有for 、列表解析如[for x in L]、in成员关系测试、map内置函数、sorted、zip等。

可迭代对象：iterable
    从宏观上看，本身就是序列或者可以通过迭代工具一次产生一个结果，那么就是可迭代对象

迭代器对象：（通过iter(可迭代对象)获得）iterator
    迭代器对象遵守迭代协议

迭代器协议：
    有__next__方法，该方法可以前进到下一个结果，而在这一系列结果的末尾时，则会引发StopIteration异常

所以迭代对象可以使用for循环或其他迭代工具遍历，因为所有的迭代工具内部工作起来是通过 iter(可迭代对象) 得到一个该对象的迭代器，
然后每次在调用迭代器的__next__方法，并且捕捉到StopIteration异常后退出，所以也可以说迭代工具使用了迭代协议

手动迭代next(obj),相当于obj.__next__() obj是迭代器
文件本身就是迭代器
f = open('xx.x')
f is iter(f)        # True
在一个迭代对象上可以得到多个迭代器，并且这些迭代器互不相干。但是若本身是迭代器，还使用iter(本身)，尝试创建新的迭代器，这是没用的。
'''
a = range(1,5)
b = range(5,10)

    
# print(list(zip(a, b)))
# a, *b = range(1,5)
# print(a,b)

def test():
    print(1)

test.bn = 'wz'
print(test.bn)
ww=1