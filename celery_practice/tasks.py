from celery import Celery

# app = Celery('tasks', broker='pyamqp://guest@localhost//')
app = Celery('wz_tasks', backend='rpc://', broker='pyamqp://')
# 第一个参数，app_name(随便起)，文档说 The first argument to Celery is the name of the current module.
# app = Celery()
# app.config_from_object('celeryconfig')

'''
celery的架构?
Celery, like a consumer appliance, doesn’t need much configuration to operate. 
It has an input and an output. The input must be connected to a broker, 
and the output can be optionally connected to a result backend
'''

@app.task
def add(x, y):
    return x + y