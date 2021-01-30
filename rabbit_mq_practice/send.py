import pika
# 第1节  producer==>queue==>consumer 模型

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# create a queue 多次运行也只会创建一个
channel.queue_declare(queue='hello')

# In RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange
# exchange参数空串即使用了一个默认的exchange，此时，routing_key即指定了队列的名称
# 理解: 直接忘记exchange的存在，就和消息模型一样
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()