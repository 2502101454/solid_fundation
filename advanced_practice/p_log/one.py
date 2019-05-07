import logging
logger = logging.getLogger(__name__)
print(__name__)
ch = logging.FileHandler(filename='%s.log' % __name__, mode='w')
logger.addHandler(ch)
logger.info('one....')