#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 解决需要定期上机器删日志的痛苦，这里完全自动删除老旧的日志文件
import logging
import time
from logging.handlers import TimedRotatingFileHandler
import os
LOG_DIR = "./log"

def init():

    if not os.path.exists(LOG_DIR):
        os.mkdir(LOG_DIR)

    '''
    "handlers": {
            "controller_handler": {
                "level": "DEBUG",
                "formatter": "detail",
                "filename": log_path,
                # "class": "logging.FileHandler",
                "delay": 0,
                "utc": True,
                "interval": 1,
                "when": "midnight",
                "backupCount": 7,
                "class": "logging.handlers.TimedRotatingFileHandler",
            }
        }'''

    # 为root logger设置Handler 后面所有的logger也就不再单独设置handler了，这样日志向上传播至root logger，最后使用root的Handler打印
    root_logger = logging.getLogger('')
    root_logger.setLevel(logging.INFO)

    file_name = "%s/%s.log" % (LOG_DIR, __file__)
    # timed_handler = TimedRotatingFileHandler(file_name, when='midnight',
    #                         interval=1, backupCount=4, encoding=None, delay=False, utc=True)
    timed_handler = TimedRotatingFileHandler(file_name, when='s',
                                             interval=10, backupCount=3, encoding=None, delay=False, utc=False)
    timed_handler.setLevel(logging.INFO)
    # 如果是天级别的话，这里设置下日志后缀为日期就行了
    # timed_handler.suffix = "%Y-%m-%d"
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] [%(filename)s] [%(funcName)s] [%(lineno)d] %(message)s')
    timed_handler.setFormatter(formatter)

    root_logger.addHandler(timed_handler)

if __name__ == '__main__':
    init()
    root_logger = logging.getLogger('')
    sun_logger = logging.getLogger('sun')
    for x in range(0, 100):
        print(x)
        root_logger.info('root logger is print %s' % x)
        sun_logger.info('sun logger is print %s' % x)
        time.sleep(2)



