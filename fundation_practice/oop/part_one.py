# 下面大部分知识点摘自刘江的博客   https://www.liujiangblog.com/course/python/43

# 类是抽象的模板

# class 语句是可执行语句，当Python 执行class语句时，会从头到尾执行其主体内的所有语句，
# 在class内赋值的变量则会创建类变量, 而内嵌的def则会创建 *类的* 方法.


# 类变量：定义在类中，方法之外的变量，称作类变量。类变量是所有实例公有的变量，但并不属于实例哦~
# 实例变量：实例变量指的是实例本身拥有的变量。每个实例的变量在内存中都不一样.

# 在类的内部，使用def关键字来定义一个方法。
# 类的方法又分为三种: 实例方法、静态方法和类方法，这些方法无论是在代码编排中还是内存中都** 归属于类 ***，区别在于传入的参数和调用方式不同
#   =======一定注意：类中定义的所有的方法都属于类，不属于实例对象 !!=============
#   1.实例方法由实例调用，至少包含一个self参数，且为第一个参数.
#   2.静态方法由类调用，无默认参数。将实例方法参数中的self去掉，然后在方法定义上方加上@staticmethod，就成为静态方法。
#   它属于类，和实例无关。建议只使用类名.静态方法的调用方式。（虽然也可以使用实例名.静态方法的方式调用），常用来做工具util方法
#   3.类方法由类调用，采用@classmethod装饰，至少传入一个cls（代指类本身，类似self）参数。执行类方法时，自动将调用该方法的类赋值给cls。
#   建议只使用类名.类方法的调用方式。(虽然也可以使用实例名.类方法的方式调用)

# 类、类的方法、类变量、类的实例和实例变量在内存中是如何保存的？
# 类、类的所有方法以及类变量在内存中只有一份，所有的实例共享它们；而每一个实例都在内存中独立的保存自己和自己的实例变量。
# 创建实例时，实例中除了封装实例变量之外，还会保存一个指向所属类的指针。
# 因此，实例可以寻找到自己的类，并进行相关调用，而类无法寻找到自己的某个实例。

# 如下摘自知乎文章=======>https://zhuanlan.zhihu.com/p/36810672
# 实例化：创建一个类的实例，类的具体对象。在实例对象开辟一个空间，并为实例对象添加对类的引用。***并没有复制类中的属性和方法到实例对象中***



# ==========关于继承：摘自刘江博客https://www.liujiangblog.com/course/python/44
# 继承最大的好处是子类获得了父类的***全部变量和方法***的同时(__init__构造方法也是可以继承的，实验亲证)，又可以根据需要进行修改、拓展

# obj.attr or obj.func() 的搜索顺序: =====>我亲测于test_inheritances.py 百说不如一练~
# 对象在***调用某个方法或变量***的时候，首先在实例自身查找，接着是对应的类，再接着才根据继承机制在父类里查找。
# 根据父类定义中的顺序，以深度优先的方式逐一查找父类！(我特意试了下，好像python2 ,3 都是深度的方式)

# ********上面是从对象开始的，注意了下面是类在调用时候的寻址方式*************
# 在类的继承中的，子类.attr or func()     优先在子类自身查找，自身没有才会去父类找。   其实还是从对象开始的搜索过程的一环而已


# 可以查看oop_charts中的相关图表理解哈~

# ===============下面是实例变量和类变量的使用=============

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


# 方法调用方式还可以是class.method(instance, agrs..)进行调用，这是常见的拓展子类方法的方式


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


# super()函数：
# 我们都知道，在子类中如果有与父类同名的成员，那就会覆盖掉父类里的成员。那如果你想强制调用父类的成员呢？
# 使用super()函数！这是一个非常重要的函数，最常见的就是通过super调用父类的实例化方法__init__！

# 语法：super(子类名, self).方法名()，需要传入的是子类名和self，调用的是父类里的方法，按父类的方法需要传入参数。

class A:
    def __init__(self, name):
        self.name = name
        print("父类的__init__方法被执行了！")
    def show(self):
        print("父类的show方法被执行了！")

class B(A):
    def __init__(self, name, age):
        super(B, self).__init__(name=name)
        self.age = age
        A.__init__(self, name=name)
    def show(self):
        super(B, self).show()

obj = B("jack", 18)
obj.show()