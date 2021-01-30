#!/usr/bin/env python

# 第2节: 默认的消息分发机制、ACK、队列&消息持久化、公平分发(prefetch_count，让真正空闲了的worker才接受新的任务去执行)
# By default, RabbitMQ will send each message to the next consumer, in sequence. On average every consumer will get the
# same number of messages. This way of distributing messages is called round-robin
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# queue durability
channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))
print(" [x] Sent %r" % message)
connection.close()