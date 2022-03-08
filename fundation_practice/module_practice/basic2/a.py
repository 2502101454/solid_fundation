import sys
sys.path.append('../../')
print(sys.path) # 这样加入的相对路径在list中还是 ../没变化，经过试验发现，其实../是基于你执行python这条命令时所在的目录的一个确定的目录(绝对路径)
# 我在进入module_practice目录后 执行 python basic2/a.py ，执行到这里的时候../就代表基于module_practice目录下的上层路径，即
# /Users/zeng.wang/PycharmProjects/solid_fundation/fundation_practice/   所以接下来b中import iterator_and_parse.part_one
# 就可以寻找到了。
# 如何证明这里绝不是基于的顶层脚本主目录？
# sys.path.append('../../') 然后继续在module_practice目录下 执行 python basic2/a.py ，假设是主目录，那么这样执行肯定是可以的。
# 但是结果报错，此时进入basic2下面执行python a.py 没有报错     (在ideal中直接右键run应该也是在当前这个文件所在的目录下执行python命令)

#       ****** 创建包后，包里的模块名称千万要避免和包名一致，！！！！******


# 包导入：包导入路径中最左边的部分任仍然是相对于模块搜索路径sys.path列表中的每个目录作为基准去搜索的
import packet.b     #在主脚本目录/xxx/basic2/ + packet/b.py
from packet.b import test   # 和上面一样的搜索方式
# 单纯的包导入如下
# import packet #这并不会去执行packet下面所有的脚本，只是会执行packet的__init__文件
# import packet.subpacket 只会沿途执行__init__
# 假设packet下有模块a a有属性attr
# import packet     接下来packet.a.attr 报错 module 'packet' has no attribute 'a'  所以这样导包再使用模块是不可以的

#   **所以总结一句话，导入只有包那就单纯的导入执行沿途包的__init__；导入只有模块文件，那就单纯执行模块文件
#   导入有包又有模块文件，那就沿途执行包的__init__最后再执行模块
# from还可以这么用 from pack import module       因为对于包pack来说 module也是它的变量，同上，先执行__init__再执行module代码
# 不过这种让人伤神的用法还是尽量少用。。。。


# 包导入方式分为两种：1.绝对导入，上面这些直接搜索sys.path的都是。   2.相对导入
# 相对导入的形式如下：当且仅当使用 from . import A 才为相对导入。
# 相对导入只会检查当前包含了from . import A这个语句的文件所在的目录(包),在这个目录下去找A模块，并不会用常规的sys.path查找
# 如果前面再加一个点. 则代表从当前目录的父目录的相对导入

# from .A import a      这种写法同样代表包含该行语句的文件所在的目录中寻找A模块，然后赋值其a变量到当前命名空间
# 绝对导入是首选

# 关于__init__文件。
# 它是属于包(模块包)的，在第一次导入包的时候就会执行该文件中的内容，从而初始化目录模块的命名空间，比如当前basic2下的__init__文件中如果
# 有t = 1这个赋值语句，那么如果有如下语句 import basic2 或者import module_practice.basic2（意指多层级联）
#  这些都会去执行沿途包的__init__文件的内容，同时接下来我们就可以使用basic2.t  即为1

