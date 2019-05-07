'''
                                    作用域(变量名解析LEGB原则)
    L(local function)
    E(enclosing function locals)
    G(global module)
    B(built-in)

    每次函数的调用都创建一个新的本地作用域 即L
    而函数内部的任何类型的赋值都会把一个名称划定为本地的，包括=语句，函数参数，import中模块的名称，def中的函数名称。

    E：E是上层函数的作用域，也叫做嵌套作用域，它可以包括任意层的嵌套函数的本地作用域。

    理解时需要记住：
        1.def是可执行的语句；
        2.函数创建时候是执行了def语句，并且封装了内部代码
        3.函数执行的时候才会执行内部代码
        4.嵌套函数被调用的时候才会去寻找嵌套作用域中的变量
    默认参数是在函数创建的时候就会被评估，且只评估这一次。
'''

# def f1():
#     x = 88
#     def f2():
#         print(x)
#     f2()

# f1() # 88 ,先创建函数f1,然后执行f1的时候，执行内部的代码同时创建f2，并在执行f2的时候寻找变量x，x实在嵌套作用域中找到的，所以就是88

# 即使在嵌套的函数返回后，还是可以在调用的时候找到嵌套作用域
# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2
# action = f1()
# action()        # 88

#工厂函数
def maker(N):
    def action(X):
        return X ** N
    return action

a1 = maker(2)
print(a1(3))    # 9
print(a1(4))    # 16

# 函数再次调用，创建新的本地作用域，里面的action函数则为新创建的，和上面的无关
a2 = maker(3)
print(a2(3))    # 27
print(a2(4))    # 64

def maker_lam():
    acts = []
    for i in range(3):
        acts.append(lambda y=i: y ** i )
    return acts
# 调用外层函数，创建lambda函数，注意默认参数在创建lambda函数的时候就评估完成了
acts = maker_lam()
# 调用lambda函数，y使用默认值，i在嵌套域中进行搜寻，注意此时的嵌套域中i的值是2(外层函数结束后嵌套域的i值就是2)，
print(acts[0]())    # 0 ** 2
print(acts[1]())    # 1 ** 2
print(acts[2]())    # 2 ** 2
print('* '*30)
# nonlocal 用于修改嵌套作用域中的变量值, nonlocal是在外层函数创建的时候就会进行解析
def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested

F = tester(0)
F(1)
F(1)
F(1)
print('G '*30)
# 工厂函数，F G无关
G = tester(2)
G(1)
G(1)
G(1)

