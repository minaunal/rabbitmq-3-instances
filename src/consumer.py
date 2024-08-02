import pika

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

def main(queue_name):
    credentials = pika.PlainCredentials('user', '12345')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost', 5672, '/', credentials)
    )
    channel = connection.channel(channel_number=1)

    channel.queue_declare(queue=queue_name, durable=True)

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(f" [*] Waiting for messages in queue '{queue_name}'. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == "__main__":
    queue_name = input("Queue name: ")
    main(queue_name)