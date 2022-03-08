#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# queue durability
channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

# 消息的状态:
# 1.Ready: A message is Ready when it is waiting to be processed.
# 2.Unacked: 就是没有进行发送ACK的消息，所以包括很多情况(channel关闭、执行中的消息、执行完但没发送ack的消息等情况)
# Unacked means that the consumer has promised to process them but has not acknowledged that they are processed


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.')+10)
    print(" [x] Done")
    # 由consumer的channel来发送ack给rabbitMQ
    # 一旦忘记发送ACK，那么处理完的消息都会变成unack状态，这些消息属于当前的worker，
    # 就消息重新分配而言：当前worker不会重复执行自己unack的消息，只要当前worker没挂，这些unack的消息是不会分配其他worker的
    # Messages will be redelivered when your client quits (which may look like random redelivery)
    # 所以一般情况下，所有worker都没挂，worker们忘记发送ack，那么每个worker都会积攒大量的unack消息，一直存在内存中
    # RabbitMQ will eat more and more memory as it won't be able to release any unacked messages.
    ch.basic_ack(delivery_tag=method.delivery_tag)


# 告诉rabbitMq 一次最多发送一条消息给worker，并且直到该worker 处理完任务且ACK后，才可以继续给该worker分配任务
channel.basic_qos(prefetch_count=1)
# 默认auto_ack=False，auto_ack参数就是no_ack，所以默认是有ack的
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()

connection.process_data_events()