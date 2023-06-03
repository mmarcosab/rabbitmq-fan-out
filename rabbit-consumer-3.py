import pika, sys, os

def main():
    credentials = pika.PlainCredentials('user', 'password')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',
                                                                   5672,
                                                                   '${RABBITMQ_DEFAULT_VHOST}',
                                                                   credentials
                                                                   ))
    channel = connection.channel()

    queueName = 'queue-3'
    channel.queue_declare(queue=queueName, durable=True)

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue=queueName, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)