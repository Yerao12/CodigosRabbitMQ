import pika, sys

#credentials = pika.PlainCredentials('vitao', '12345')
#parameters = pika.ConnectionParameters('192.168.0.110',5672,'/',credentials)
#connection = pika.BlockingConnection(parameters)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

assuntos = sys.argv[1:]
if not assuntos:
    sys.stderr.write("Modo de usar: %s [esportes] [clima] [famosos] [geral]\n" % sys.argv[0])
    sys.exit(1)

for assunto in assuntos:
    channel.queue_bind(
        exchange='direct_logs', queue=queue_name, routing_key=assunto)

print(' [*] Esperando por conteúdo. Pressione CTRL+C para sair')


def callback(ch, method, properties, body):
    f = open("noticias.log","a")
    f.write(" [x] %r:%r \n" % (method.routing_key, body))
    print(" [x] %r:%r" % (method.routing_key, body))
    f.close()


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()