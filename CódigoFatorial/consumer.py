import pika, sys, os

def main():
    #credentials = pika.PlainCredentials('vitao', '12345')
    #parameters = pika.ConnectionParameters('192.168.0.110',5672,'/',credentials)
    #connection = pika.BlockingConnection(parameters)

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        conteudo = str(body)
        print(conteudo)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

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