import pika
import json
from requests import get
import time
from pika.exceptions import AMQPConnectionError
import os
from bardapi import Bard


# define function to consume messages from rabbit_mq
# do we all this converse function inside a route?
def converse(ch, method, properties, body):
    content = json.loads(body)
    print("🪩🪩🪩Content looks like: ", content)
    token = os.environ("__Secure-1PSID")
    bard = Bard(token=token)
    # turbo cntrl+opt+L
    print(
        "🚀 ~ file: consumer.py:17 ~  bard = Bard(token=token):",
        bard=Bard(token=token),
    )
    bard.get_answer(content.text)
    # take data from bard response
    text = response.text

    # convert text to speech (MORE RESEARCH REQUIRED)


def bard_text_to_speech():
    # send text to bard to convert to speech
    pass


# Or will we use websockets to send audio files back to client?
def speech_to_user():
    # send speech to user/play speech for user
    pass


# while True:
#     try:
#         parameters = pika.ConnectionParameters(host="rabbitmq")
#         connection = pika.BlockingConnection(parameters)
#         channel = connection.channel()
#         channel.exchange_declare(
#             # change account_info?
#             exchange="account_info",
#             exchange_type="fanout",
#         )
#         result = channel.queue_declare(queue="")
#         queue_name = result.method.queue
#         channel.queue_bind(exchange="account_info", queue=queue_name)
#         channel.basic_consume(
#             queue=queue_name,
#             on_message_callback=converse,
#             auto_ack=True,
#         )
#         channel.start_consuming()
#     except AMQPConnectionError:
#         print("account_info_consumer could not connect to RabbitMQ")
#         time.sleep(3.0)
