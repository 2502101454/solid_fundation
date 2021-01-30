class A(object):
    m = 3
    def run(self):
        print("A run..")
    pass


class B(A):
    # m = 1
    def run(self):
        print("B run..")


b = B()
# b.m = 2

# def run():
#     print("outside func run...")
#
# b.run = run

# b.run()

print(b.m)



#测试子类覆盖父类的私有方法
# 结果：父类私有的方法不可以被覆盖，在父类中，子类实例self.__xx() 执行的还是父类内部__xx
#

class P(object):
    def run(self):
        self.__me()

    def __me(self):
        print("p me")

class S(P):
    def __me(self):
        print("s me")

s = S()
s.run() # p me


# class P(object):
#     def run(self):
#         self.me()
#
#     def me(self):
#         print("p me")
#
#
# class S(P):
#     def me(self):
#         print("s me")
#
#
# s = S()
# s.run()


# 子类可以使用父类class method、static method
# 子类.父类的class_method() 调用时    父类的class_method(cls)中的cls传的是子类

class AA(object):
    name = "aa"
    @classmethod
    def aa_c(cls):
        print("aa_c")
        print(cls.name)

    @staticmethod
    def aa_s():
        print("aa_s")


class BB(AA):
    # name = "bb"
    pass
    # 子类当然可以覆盖父类的class、static method，这样调用的就是子类自身的了
    # 所以这里就是        子类.attr or func() 在继承中的寻址方式吧，优先子类自身，自身没有才会去父类找
    # @classmethod
    # def aa_c(cls):
    #     print("bb_c")
    #     print(cls.name)
    #
    # @staticmethod
    # def aa_s():
    #     print("bb_s")

BB.aa_c()
BB.aa_s()
print(BB.name)


class CC(object):
    def __init__(self, name):
        self.name = name
        print("self class is {}".format(self.__class__))

class DD(CC):
    pass

dd = DD(name="wangzeng")    #self class is <class '__main__.DD'>
print("DD inherit parent __init__ func and name {}".format(dd.name))
#DD inherit parent __init__ func and name wangzeng

