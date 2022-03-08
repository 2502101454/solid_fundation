#!/usr/bin/env python

# 第五节
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'

# topic类型的exchange，routing_key - it must be a list of words, delimited by dots.
# 也请命名的有意义一点，和消息自身有关系
# 对于consumer一方的 binding_key的格式也是一样的
# (自己实验单独一个word也可以呀，比如"vm"，对于routing key和 binding key，和direct 一样)

channel.basic_publish(
    exchange='topic_logs', routing_key=routing_key, body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()
