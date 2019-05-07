import logging
logger = logging.getLogger('simple_example.one')
# logger.propagate = False
# 当不在向父级传播的时候，会前往logger自身的Handler,然而自身没有设置Handler，所以当我们执行test.py的时候，这里的日志将不会打印。
logger.info('one....')
