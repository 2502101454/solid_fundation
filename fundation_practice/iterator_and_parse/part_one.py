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

参考文章
https://nvie.com/posts/iterators-vs-generators/
https://www.jianshu.com/p/55163ba23796

A object is iterable if have an __iter__() method        iter(obj) 将会调用obj.__iter__()
可迭代对象实现了__iter__方法，该方法返回一个迭代器对象

任何实现了__iter__()和__next__()方法的对象都是迭代器，__iter__返回迭代器自身，__next__返回容器中的下一个值

手动迭代 next(obj) ,相当于 obj.__next__()  obj是迭代器

So an iterator is a value factory.
From the outside, the iterator is like a lazy factory that is idle until you ask it for a value, which is when
it starts to buzz and produce a single value, after which it turns idle again.
迭代器是懒加载的


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

'''
A generator is a special kind of iterator—the elegant kind.
所以，生成器也是一种迭代器，它的实现方式很优雅，不需要写__iter__() and __next__() methods.

所以真要说生成器和迭代器的区别，那就是语法角度，生成器很优雅，不用写__iter__() and __next__() methods.

Any generator also is an iterator (not vice versa!);
任何生成器都是一个迭代器， 反过来就不一定了，生成器是迭代器的子集~
Any generator, therefore, is a factory that lazily produces values.
生成器也是懒加载

两种生成器的类型：
    1.生成器函数 (有yield关键字的函数) A generator function is any function in which the keyword yield appears in its body.
    2.生成器表达式
'''