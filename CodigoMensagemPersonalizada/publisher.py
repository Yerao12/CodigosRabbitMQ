import pika
nome = input("Digite uma mensagem: ");
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body= nome)
print("Enviou " + nome)
connection.close()
