
import inspect
# 注意本质是默认参数的值(可以画引用图来理解)
# 默认参数将会在方法定义的时候进行赋值(所以也就赋值一次,想要多次赋值那就重复定义这个方法)
def f(a, L=None):
    print(L)
    if L == None:
        L = [] #只是将变量L的引用指向了[]，但是默认参数的值还是None没变化。
    L.append(a)
    return L
#
# print(f(1)) # 由于没给L传值，所以使用默认参数值None
# print(f(2)) # 但是由于没给L传值，所以使用默认参数值None
# print(f(3))


#============函数注解，校验参数以及返回值类型====

class Pet:
    def __init__(self, name):
        self.name = name
        pass


# 校验参数以及返回值类型的注解
def verify_func(func):
    def wrapper(*args, **kwargs):
        # __annotations__返回dict，k是param_name    v是annotation
        # e.g {'name': <class 'str'>, 'age': <class 'int'>, 'pet': <class '__main__.Pet'>, 'return': <class 'float'>}
        param_rules = func.__annotations__
        print('func {func_name} its annotations is {func_annotatinos}'.format(func_name=func.__name__,
                                                                              func_annotatinos=param_rules))
        # 兼容多种传参方式
        # 取得所有的values
        args_rules_v = list(param_rules.values())
        args_rules_k = list(param_rules.keys())
        print('args_rules_v is %s' % args_rules_v)
        print('args_rules_k is %s' % args_rules_k)
        for i, arg in enumerate(args):
            if not isinstance(arg, args_rules_v[i]):
                raise RuntimeError('param %s type should %s' % (args_rules_k[i], args_rules_v[i]))

        # python3 没有iteritems()，只有这个items()，然后返回是dict_items([(1, 2)])对象，使用k,v可取值。注：该方法2也有，用法一致
        for k, v in kwargs.items():
            if not isinstance(v, param_rules[k]):
                raise RuntimeError('param %s type should %s' % (k, param_rules[k]))

        res = func(*args, **kwargs)

        if not isinstance(res, param_rules['return']):
            raise RuntimeError('return value type should %s' % param_rules['return'])
        return res
    return wrapper


@verify_func
def f2(name: str, age: int, pet: Pet) -> float:
    print(name, end=',  ')
    print(age, end=',  ')
    print(pet)
    return 1.0


# @verify_func
def f3(ham: str, eggs: str = 'eggs') -> int:
    '''
    文档给出的annotatinos的key value顺序是 {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
    但是实际上的顺序是  {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}  return在最后面
    这里是为了测试如果按照文档上给出的顺的话，return类型匹配到eggs的字符串类型应该会报错的case
    :param ham:
    :param eggs:
    :return:
    '''
    print('Annotations:', f3.__annotations__)
    print('Arguments:', ham, eggs)
    return 1


# f3('wz_f3', 'www')


# print(inspect.signature(f2).parameters)
# print(f2(name='wz', age=21.1, pet=Pet(name='wz_pet')))
# print(f2('wz', 21.1, Pet(name='wz_pet')))
# print(f2('wz', 21, Pet(name='wz_pet')))
# print(f2(22, age=21, pet=Pet(name='wz_pet')))
# print(f2('wz', age=21.2, pet=Pet(name='wz_pet')))

'''
同样可以通过inspect进行实现
# inspect.getargspec(f2) #已过时
# inspect.signature() which is in all the versions of Python 3 we support, but not 2.7.
通过signature对象可以得到方法的参数名称类型以及返回值类型
# sig = inspect.signature(f2)
# print(sig)
# print(sig.parameters['name'].annotation)  #取得属性name的注解<class 'str'>
# print(sig.return_annotation)    # 取得返回值对应的注解 <class 'float'>
        
'''

# def wether_ordered(l:int, o:int, v:int, e:int):
#     pass
#
#
# print(wether_ordered.__annotations__)
# # {'l': <class 'int'>, 'o': <class 'int'>, 'v': <class 'int'>, 'e': <class 'int'>}
# print(inspect.signature(wether_ordered))
# # (l:int, o:int, v:int, e:int)
# # 事实证明都是按照原参数顺序进行构建对应的对象(和v无关)
# # python 2.7定义a = {'l':0,'o':0, 'v':0, 'e':0} 打印时{'e': 0, 'l': 0, 'o': 0, 'v': 0}
# # python 3.7定义a = {'l':0,'o':0, 'v':0, 'e':0} 打印时{'l':0,'o':0, 'v':0, 'e':0} 从3.6开始已经默认字典遵循插入顺序排序了


# 函数参数形式组合廖雪峰
# 关键字参数函数，调用时候可以传入多个或0个关键字参数，
def func(**kwargs):
    kwargs['ww'] = 'zz'
    print(kwargs)


a = {'1': 1}
# 该种调用方式参数拿到的是dict  a的一份拷贝(内容拷贝)，对参数进行改变并不会影响到原来的dict的内容
func(**a)
print(a)


# 为啥需要命名关键字参数？因为关键字参数无法限制参数的名称！
# *后面的是命名关键字参数，每个必填
def name_kw(name, *, city, address):
    print(name, city, address)


# 而且传值的时候必须带上参数名称，否则调用报错
name_kw('wz', city=22, address=33)


# 命名关键字参数也可以有缺省值
def name_kw2(name, *, city='西安', address):
    print(name, city, address)


name_kw2('wangzeng', address='周至county')


# 当有可变参数的时候，可变参数args后面的city job则为命名关键字参数
def person(name, age, *args, city, job):
    pass


# 五种参数可以共同使用，但是顺序是必选参数、默认参数、可变参数、命名关键字参数、关键字参数
def param_sequence(a, b, c=0, *args, d, **kwargs):
    pass


