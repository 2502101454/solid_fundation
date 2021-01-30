#!/usr/bin/env python
# 第六节 RPC, 这里是简单实现方式之一：
# 1.client 发送消息到(指定本次请求的唯一id-correlation id 和callback queue名字)rpc queue
# 2.rpc server 消耗rpc queue的消息，拿到这个消息指定的callback queue 和 correlation id，当把这次任务执行完了，
# 接着把结果发到callback queue(也带上xxid，表示是哪个request的结果)
# 3.client 还要继续消耗callback queue的消息，根据他上次发消息的xxx id和队列里的消息的xxx id 做匹配，就可以确定到上次request的结果了

import pika
import uuid

class FibonacciRpcClient(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)
        # 这里没start_consuming

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(n))
        # properties里的参数：
        # reply_to: Commonly used to name a callback queue.
        # correlation_id: Useful to correlate RPC responses with requests.

        while self.response is None:
            # 一个等待消息的阻塞过程，连接的任何消息都可以使它脱离阻塞状态
            # 和sqs那块的一个方法一样，没消息那么程序就block在这一行了，有消息就接着执行
            self.connection.process_data_events()
        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(30)
print(" [.] Got %r" % response)