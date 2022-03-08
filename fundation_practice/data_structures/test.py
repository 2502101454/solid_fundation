# #more on list##

# using lists as Stacks
stack = [1, 2, 3]
stack.append(4)
print('using lists as Stacks--> stack is {stack}'.format(stack=stack))
# 默认remove掉数组最后一个元素 pop(i)移除指定下标的元素
stack.pop()
print('using lists as Stacks--> stack is {stack}'.format(stack=stack))
stack.pop(1)
print('using lists as Stacks--> stack is {stack}'.format(stack=stack))


# using lists as Queues
# 在数组尾部操作元素是快捷的，然而在头部进行增删元素则是低效的，因为要做整体元素的移动
# 使用collections.deque，它可以对数组头部以及尾部都能快速地操作
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)
queue.appendleft(5)
print('using lists as Queues--> queue is {queue}'.format(queue=queue))
# 注意deque构造出来的queue的popleft pop方法不接受代表下标的参数
queue.popleft()
queue.pop()
print('using lists as Queues--> queue is {queue}'.format(queue=queue))
