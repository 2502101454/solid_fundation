#!/usr/bin/env python

# 参考第三节的消息模型就可以理解了，publisher 做publisher和 exchange之前的事情
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 创建exchange 指定name和类型
channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
# 当exchange=''(即使用默认时)，消息会被发送到routing_key指定的队列中去，所以结合前面1、2节中的demo和消息模型也就理解了
#  We need to supply a routing_key when sending, but its value is ignored for fanout exchanges.
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close()