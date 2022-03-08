import sys
sys.path.append("../")
# sys.path.append("./")

from AA import aa
b = 2
print(aa.a)

"""站在AA目录下，执行python BB/bb.py，使用aa中的变量a，两种写法：
    sys.path.append("../")
    from AA import aa
    
    sys.path.append("./")
    import aa
    
    
"""