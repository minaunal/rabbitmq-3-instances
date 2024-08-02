import pika

def main(exchange, routing_key, message):
    credentials = pika.PlainCredentials('user', '12345')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost', 5672, '/', credentials)
    )
    channel = connection.channel(channel_number=1)

    #channel.exchange_declare(exchange=exchange, exchange_type='direct', durable=True)

    channel.basic_publish(exchange=exchange, routing_key=routing_key, body=message)
    print(f" [x] Sent '{message}' to exchange '{exchange}' with routing key '{routing_key}'")
    connection.close()

if __name__ == "__main__":
    exchange = input("Exchange name: ")
    routing_key = input("Routing key: ")
    message = input("Message: ")
    main(exchange, routing_key, message)
