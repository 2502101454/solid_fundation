import os
print("main a: {}".format(__file__))
from subp import b
import c


"""
__file__  表示当前脚本的路径.
1.在主脚本的话，则执行时脚本路径写的啥就是啥
2.在被引用的脚本的话，则是当前脚本的绝对位置，和主脚本无关~

下面是__file__的取值:

python a.py
输出:
main a: a.py
b: /Users/zeng.wang/PycharmProjects/solid_fundation/fundation_practice/special_var_path_join/subp/b.py
c: /Users/zeng.wang/PycharmProjects/solid_fundation/fundation_practice/special_var_path_join/c.py


python special_var/a.py
输出:
main a: special_var/a.py
b: /Users/zeng.wang/PycharmProjects/solid_fundation/fundation_practice/special_var_path_join/subp/b.py
c: /Users/zeng.wang/PycharmProjects/solid_fundation/fundation_practice/special_var_path_join/c.py

python /Users/zeng.wang/PycharmProjects/solid_fundation/fundation_practice/special_var_path_join/a.py
输出:
main a: /Users/zeng.wang/PycharmProjects/solid_fundation/fundation_practice/special_var_path_join/a.py
b: /Users/zeng.wang/PycharmProjects/solid_fundation/fundation_practice/special_var_path_join/subp/b.py
c: /Users/zeng.wang/PycharmProjects/solid_fundation/fundation_practice/special_var_path_join/c.py
"""


"""
os 模块的常用操作:
1.获取路径的上层目录
os.path.dirname("/Users/zeng.wang/PycharmProjects/solid_fundation/fundation_practice/special_var_path_join/c.py")
输出: /Users/zeng.wang/PycharmProjects/solid_fundation/fundation_practice/special_var_path_join

2.获取路径的文件名
os.path.basename("/Users/zeng.wang/PycharmProjects/solid_fundation/fundation_practice/special_var_path_join/c.py")
输出: c.py

3.获取 相对路径的绝对路径
os.path.abspath()
该方法**始终**以python命令执行时所处的路径为基准(所以主脚本、被引用的脚本执行该方法基准路径一样)，再和参数里的相对路径做join
"""
print("----"*10)
print("main a abspath: {}".format(os.path.abspath('./222/ww.py')))
"""
 python fundation_practice/special_var_path_join/a.py 
 输出:
 main a abspath: /Users/zeng.wang/PycharmProjects/solid_fundation/222/ww.py
 c 模块的输出:
 c abspath:: /Users/zeng.wang/PycharmProjects/solid_fundation/222/ww.py
"""
# print("main a abspath __file__: {}".format(os.path.abspath(__file__)))