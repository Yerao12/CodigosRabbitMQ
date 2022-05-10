#!/usr/bin/env python
import pika, sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

assunto = sys.argv[1] if len(sys.argv) > 1 else 'geral'
message = ' '.join(sys.argv[2:]) or 'Essa é uma mensagem padrão do método publish/subscribe'
channel.basic_publish(
    exchange='direct_logs', routing_key=assunto, body=message)
print(" [x] Sent %r:%r" % (assunto, message))
connection.close()