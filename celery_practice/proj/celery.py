from celery import Celery

app = Celery('proj2',
             broker='amqp://',
             backend='rpc://',
             include=['proj.tasks'])
# 文档demo的backend是amqp但是运行找不到包，官网说过时了，所以就换了backend
# The include argument is a list of modules to import, so that the worker is able to find our tasks.

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

# if __name__ == '__main__':
#     app.start()