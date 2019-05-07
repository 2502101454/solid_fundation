# import cc.c 放在这里，然后去执行a顶层脚本，这在执行cc的时候，由于b之前已被导入了(在a中)，所以直接取内存中的b，但是b并没有执行完毕，
# 所以没有test变量，所以就会在c中报错。
test = 1
# __file__ 当被其他模块引入时 执行的结果就是该模块的绝对路径 /Users/zeng.wang/PycharmProjects/solid_fundation/fundation_practice/module_practice/basic/b.py
# 但是如果直接python执行该模块，结果就是python后b脚本的整个路径了，如 python b.py  结果是b.py       python basic/b.py (python 脚本位于上层) 结果basic/b.py
# python ../b.py python位于下层，结果是../b.py
# __name__ 无论当前位置在哪，当直接python该脚本的时候__name__是__main__ 但是当别的模块中Import 该脚本，此时执行__name__就是b 即该模块名称
# 如果import 包.脚本名称   那么 脚本内的__name__就是包.脚本名称
print('b module __file__', __file__)
print('b module __name__', __name__)
import cc.c
