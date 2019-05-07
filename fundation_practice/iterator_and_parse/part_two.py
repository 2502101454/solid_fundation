'''
    为了延迟结果的产生，所以引入了生成器的概念，有两种语法实现：
        1.生成器函数
        2.生成器表达式    返回一个生成器对象

    当调用生成器函数的时候，得到的是一个生成代器对象，生成器对象支持迭代协议，所以迭代器那套它都有，而且for循环以及其他迭代环境将会以往常
    的方式与生成器一起工作


'''

def generator1(N):
    for x in range(N):
        yield x ** 2
a = generator1(3)
print(type(a))  # <class 'generator'>
print(type(iter(a)))    # <class 'generator'>
print(iter(a) is a)     # True

print(next(a))  # 0
print(a.__next__())  # 1
c = iter(a)
print(next(c))  # 4
#next(a)     # StopIteration raise

b = range(4)
print(type(b))  # <class 'range'>
print(type(iter(b)))    # <class 'range_iterator'>
print('-'*30)
# 生成器函数执行了yield表达式后立马被挂起，随后yield表达式的值可以通过send进行指定
def gen2():
    for i in range(3):
        x = (yield i) + 3     # yield i + 3  这样写自然是i+3的值作为返回被yield
        print(x)

g2 = gen2()
# 首先调用next()打开生成器
print(next(g2))    # 运行yield i后挂起，同时将当前的i值进行返回      0
#print(next(g2))    # 再次next时，函数继续恢复执行，yield i 本身的返回值没有被指定，所以就是None，在此处None +3报错
# 这个时候就需要send出马了，send指定的是上一次被挂起的yield语句的返回值， 然后继续向下执行。
print(g2.send(3))   # 设置上次的yield i 的返回值是3 然后 3 + 3， 接下来打印 6， 再次循环，直到再次yield i执行后，挂起，返回当前i值
print(g2.send(4))   # 继续设置yield表达式的返回值，然后继续执行   7   2
#print(g2.send(5))   # 继续设置yield表达式的返回值，打印8后，继续执行，由于函数已经执行完毕，所以raise StopIteration

# 所以send 其实和 next都是让函数往下走同时遇到yield 表达式进行挂起，但是send可以设置上次挂起的yield语句的返回值，如果刚开始没有进行挂起
# 的操作，那么直接send(val)是会报错的, 这就是我们先行next的原因，当然也可以send(None) 不过后者不常用而已。

print('='*30)
# 当生成器表达式实在其他函数调用的括号内，且当前调用只有生成器表达式这一个参数的时候，可以忽略生成器表达式的()
print(sorted(x ** 2 for x in range(4)))
print(sorted((x ** 2 for x in range(4)), reverse=True))

def gen3(N):
    for x in N:
        yield x*4
g3 = gen3('spam')
print(list(g3))