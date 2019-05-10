import logging
# logging.basicConfig(level=logging.WARNING)
# logging.warning('11111')
# 注意上面任何一行注掉的语句都会创建root logger对象，即如果只仅仅import logging则不会有root logger产生，那么下面的
# 测试产生的logger对象也不会有对应的父类logger了！！！

# logger的主要工作流程，logger自身设置log_level,然后只产生高于该等级的log_record，并把log_record进行向后传递，
# 如果logger自身还绑定了filter对象，那么log_record交给filter，如果通过的话，log_record将前往logger自身绑定的Handler
# (所以子级logger有handler的话，也会进行日志的输出)，同时有父级logger对象的话，log_record会继续向父级传播，更加详细的请参加文档

# 关于logger的父子级定义
# given a logger with a name of foo, loggers with names of foo.bar, foo.bar.baz, and foo.bam are all descendants(后代) of foo.

# logger对象level的设置
# 如果一个的logger的level没有设置，那就会默认使用父级logger对象的level，如果还没有设置，那就会继续往上找，
# 毕竟最终的root logger对象的level默认是WARNING(Logging default level)

# logger对象log record的传播
# 当有父级logger的时候，所有logger也会把通过的record传递给父级的Logger对象（**注意：此时父级logger无条件接受这个record，
# 和父级logger的level的高低无关！），接下来传递给父级logger的Handler。
# 所以我们只需为顶级logger配置Handler即可

# Handler也可以进行设置setLevel()      logger对象的setLevel()只是决定产生高于其level的record,然后如果record有幸到达Handler，
# Handler的setLevel()设置的等级表示高于该level的record可以被输送到对应的目的地
# Handler的setFormatter() selects a Formatter object for this handler to use
# 还有addFilter() and removeFilter() respectively configure and deconfigure filter objects on handlers.

# logger对象没有设置formatter的操作，都是给Handler设置

# 创建logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)
# 创建输出控制台的Handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)   # 设置Handler的将处理的日志级别

# 创建输入文件的Handler
fh = logging.FileHandler(filename='%s.log' % __file__, mode='w') # 默认是追加模式 a
fh.setLevel(logging.WARNING)

# 创建formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 给Handler装配formatter
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# 给logger装配Handler
logger.addHandler(ch)
logger.addHandler(fh)

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

import one
import sub_p_log.two