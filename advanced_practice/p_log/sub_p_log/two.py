import logging
logger = logging.getLogger(__name__)
print(__name__)
# 当前这个logger本身没有设置Handler 所以按照日志的传播性，最后其实是root logger在进行打印
logger.info('two....')