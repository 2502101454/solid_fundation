# obj.attr,每次obj.attr都会开启新的独立搜索。
# 属性的搜索顺序: 该对象自身，该类，从下而上搜索父类并按照从左至右的顺序。
'''
       A
     +
    B      C
      +   +
        D
'''
    # python 2.6中搜索方式即为经典搜索，如果到了左边父类的节点处，还会继续向左边父类的上层去深度搜索，然后最后才返回左边父类处，接着向右搜索
    # 也就是说是继承搜索顺序是绝对深度优先的  D B A C

    # 但是在python 3.0中搜索方式就变成了 绝对宽度优先  D B C A
    # 这中流程的变化基于这样的假设：如果在树中较低处混入C，和A相比，可能会比较想获取C的属性.
# __init__构造方法也是可以继承的
# instance.method(args....) 是常见的方法调用方式，还可以使用class.method(instance, agrs..)进行调用，后者是常见的拓展子类方法的方式

# 继承最大的好处是子类获得了父类的全部变量和方法的同时，又可以根据需要进行修改、拓展

# 如下拓展子类的构造方法，当然还可以拓展一般的方法
class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    # 运算符重载case，这样打印一个对象时，该对象就会调用这个方法
    def __str__(self):
        return self.name + '-'*4 + self.job

class Manager(Person):
    def __init__(self, name):
        Person.__init__(self, name=name, job='Manager')

ma = Manager(name='wz')
# 使用父类的str方法
print(ma)

# 一些获取类名称的特殊属性
print(ma.__class__.__name__) # Manager
print(Manager.__name__) # Manager
print(Manager.__bases__) # (<class '__main__.Person'>,)

# 获取实例的属性
print(ma.__dict__)  # {'name': 'wz', 'job': 'Manager'}


# class 的细节
# class 语句也是真正的可执行语句，当Python 执行class语句时，会从头到尾执行其主体内的所有语句，在class内赋值的变量名，会创建类属性,
# 而内嵌的def则会创建类的方法.

# 类的方法又分为三种: 实例方法、静态方法和类方法

# 实例方法由实例调用，至少包含一个self参数，且为第一个参数.

# 静态方法由类调用，无默认参数。将实例方法参数中的self去掉，然后在方法定义上方加上@staticmethod，就成为静态方法。
#   它属于类，和实例无关。建议只使用类名.静态方法的调用方式。（虽然也可以使用实例名.静态方法的方式调用），常用来做工具util方法

# 类方法由类调用，采用@classmethod装饰，至少传入一个cls（代指类本身，类似self）参数。执行类方法时，自动将调用该方法的类赋值给cls。
#   建议只使用类名.类方法的调用方式。(虽然也可以使用实例名.类方法的方式调用)

print('class detail inside' + '.'*30)
class ShareData(object):
    # 类属性附加在这个类中，不过被所有实例共享
    spam = 99

x = ShareData()
y = ShareData()
# 可以通过实例或者类来引用它
print(x.spam, y.spam, ShareData.spam) # 99 99 99  启动继承搜索

# **那么通过实例来给spam赋值会产生啥效果？
x.spam = 88 # 对实例的属性进行赋值运算会在该实例内创建或修改变量， 而不会影响共享的类。
print(x.spam, y.spam, ShareData.spam) # 88 99 99
# 通常：继承搜索（属性的搜索顺序）只会在属性引用时发生，而不是在赋值运算时，对对象属性赋值总会修改该对象自身，除此之外无其他影响。

ShareData.spam = 100
print(x.spam, y.spam, ShareData.spam) # 88 100 100
# 实例属性是由对方法内self属性进行赋值运算产生的
# 类属性时通过class语句内的语句(赋值语句)而生成的

class C:
    X = 33
    def m(self):
        X = 44      # 注意这里的X是这个m方法的本地域的变量，绝不是引用自类属性X，还记得LEGB法则不？
        self.X = 55 # 实例属性

print(C.X)  # 33
c = C()
c.m()
print(C.X)  # 33