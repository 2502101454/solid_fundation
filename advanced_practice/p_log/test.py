import logging
# 第一步就要调用basicConfig(),而且basicConfig()仅仅第一次调用有效，后续的调用都没效果
# 在不指定文件模式的时候默认是追加      w就是每次都覆盖重新写
# logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG,
#                     format='%(asctime)s %(levelname)s %(message)s') # 更多format的参数详见文档
#logging.warning('1') #在不指定basicConfig()的时候，默认WARNING:root:1

logging.basicConfig(level=logging.DEBUG)
# logger的使用     logging生成的logger具备logging的basicConfig，所以下面的logger对象也就使用默认的format了
# 默认的format格式是：severity(Log Level):logger name:message, 当然也可以指定logging.basicConfig从而影响logger的format
'''
Loggers expose the interface that application code directly uses.
Handlers send the log records (created by loggers) to the appropriate destination.
Filters provide a finer grained facility for determining which log records to output.
Formatters specify the layout of log records in the final output.
'''
logger = logging.getLogger(__name__)
# Multiple calls to getLogger() with the same name will return a reference to the same logger object.
import one
import sub_p_log.two    # 注意two脚本执行的时候其内部的__name__变成了sub_p_log.two
logger.info('main module') #其实这个logger本身也是没有Handler,最后还是交给了root logger的默认Handler
# 我们经常直接是使用logging.info(xxx)这种其实是直接使用root logger.
# 直接使用logging 或者设置logging.basicConfig都是相当于创建了root logger
