#--encoding=utf-8--
import functools
import datetime
#定义我的装饰器，装饰器：传入旧函数，返回新函数
def log(func):
    @functools.wraps(func)
    def wrapper():
            print('%s begin' % func.__name__)
            func()
            print('%s end' % func.__name__)
    return wrapper

@log
def test():
    print('wangzeng')


#上面加入了@log就相当于 test = log(test)
test()

#函数带了参数

@log
def test2(**dict_param):
    print(dict_param)

# test2 = log(test2)
# 此时执行报错，因为加了@log注解，那就传入了test2这个旧函数，返回的是wrapper()，test2重新引用，这个wrapper是没有参数的，所以下面就出错
# test2(name = 'wangzeng', sex = 'male')
# 解决方法，让wrapper函数有参数就好了
def log2(func):
    @functools.wraps(func)
    def wrapper(*param, **param2):
        print('%s begin' % func.__name__)
        func(*param, **param2)
        print('%s end' % func.__name__)
    return wrapper

@log2
def test3(**dict_param):
    print(dict_param)
# test3现在就是wrapper了，在调用wrapper的时候没有传入*param，那么执行到func(*param,**param2)的时候*param也就不存在了，
# 所以就是func(**param2)了，所以就调用了test3(**param2)
# 总结：分析装饰器模式的时候第一步先写出test3 = log2(test3)这种表达式
# 其实python函数的参数使用可变参数再加上关键字参数就可以全部包含完毕，所以以后定义装饰器的时候最好给wrapper都加上*param, **param2
# 这样可以概括完毕所有被修饰函数的参数情况
test3(name = 'wangzeng', sex = 'male')


#让装饰器具有参数

def log3(*text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*param, **param2):
            print('%s begin' % func.__name__, text)
            return func(*param, **param2)
        return wrapper
    return decorator

@log3('bless', 'wishes')
def test4(a):
    return a*2

#分析：test4 = log3('bless', 'wishes')(test4)
#首先log3('bless', 'wishes')只是为了将装饰器的参数带入进去，然后返回decorator函数，现在就是decorator(test4),这个返回wrapper(...)
#所以最后结果就是test4 = wrapper，接下来调用test4(...)就是调用wrapper(...)
#注：在函数内部，可变参数是一个tuple
print(test4(9))

#注意到由于现在各个test系列函数已经被wrapper替换了，所以__name__都是wrapper了，解决：在wrapper紧上面加上@functools.wraps(func)
print(test.__name__, test2.__name__, test3.__name__, test4.__name__)


def excute_time(func):
    @functools.wraps(func)
    def wrapper(*param, **param2):
        print('%s start in %s'% (func.__name__, datetime.datetime.now()))
        func(*param, **param2)
    return wrapper

@excute_time
def test5(a, **kw):
    print(a*2, kw)
    print('holy shit!')

test5(3, name='wangzeng')
