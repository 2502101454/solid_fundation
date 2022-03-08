#!/usr/bin/env python

# 第五节, topic exchange
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

# The binding key must also be in the same form. The logic behind the topic exchange is similar to a direct one
# - a message sent with a particular routing key will be delivered to all the queues that are bound with a
# matching binding key

# binding key的两种特殊字符:
# * : 可以代表一个word
# # : 可以代表0个或者多个(包含一个)word

# topic exchange很灵活，当binding key只写个#的时候，该queue就接收所有的消息( regardless of the routing key - like in fanout exchange.)；
# 当binding key不使用 # 和 *的时候(就是纯word的格式), 这时候就表现的和direct类型的exchange一样
for binding_key in binding_keys:
    channel.queue_bind(
        exchange='topic_logs', queue=queue_name, routing_key=binding_key)
    # 当消息的routing key 匹配多个binding key的时候，消息也只会发给这个queue一次

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
