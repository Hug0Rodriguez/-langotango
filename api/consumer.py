import pika
import json
from requests import get
import time
from pika.exceptions import AMQPConnectionError
import os
from bardapi import Bard



# define function to consume messages from rabbit_mq
def converse(ch, method, properties, body):
    content = json.loads(body)
    token = os.environ('__Secure-1PSID')
    bard = Bard(token=token)
    bard.get_answer(content.text)
    # take data from bard response
    text = response.text

    # convert text to speech (MORE RESEARCH REQUIRED)

    # send audio back to user
    pass


while True:
    try:
        parameters = pika.ConnectionParameters(host="rabbitmq")
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.exchange_declare(
            exchange="account_info", exchange_type="fanout"
        )
        result = channel.queue_declare(queue="")
        queue_name = result.method.queue
        channel.queue_bind(exchange="account_info", queue=queue_name)
        channel.basic_consume(
            queue=queue_name,
            on_message_callback=,
            auto_ack=True,
        )
        channel.start_consuming()
    except AMQPConnectionError:
        print("account_info_consumer could not connect to RabbitMQ")
        time.sleep(3.0)
