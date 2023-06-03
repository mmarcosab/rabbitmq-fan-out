import pika

credentials = pika.PlainCredentials('user', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',
                                                               5672,
                                                               '${RABBITMQ_DEFAULT_VHOST}',
                                                               credentials
                                                               ))


channel = connection.channel()

message = 'test message sended';
channel.basic_publish(exchange='fanout_exchange',
                      routing_key='',
                      body=message)
print(" [x] ", message)

connection.close()