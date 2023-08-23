import pika
import json
from requests import get
from pika.exceptions import AMQPConnectionError
import os
from bardapi import Bard
import time


# BARD EXAMPLE
# from bardapi import Bard
# (token from 08/23 @4pm)
# bard = Bard(token='aAjFqKGwYEp32myZHuDxafvHU6wOMKc5prWPlvqu8ydT9V4ITLpNMBkoQaVJ3r2dfyalKw.')
# bard.get_answer("hola me llamo beau")['content']
def Hugo_cool():
    print("Hugo is the best")


# define function to consume messages from rabbit_mq
# do we all this converse function inside a route?
def converse(ch, method, properties, body):
    content = json.loads(body)
    # print("🪩🪩🪩Content looks like: ", content)
    # token = os.environ("BARD_API_KEY")
    bard = Bard(token=os.environ("BARD_API_KEY"))
    bard.get_answer(content.text)["content"]
    print("hello")


# convert text to speech (MORE RESEARCH REQUIRED)
def bard_text_to_speech():
    # send text to bard to convert to speech
    pass


# Or will we use websockets to send audio files back to client?
def speech_to_user():
    # send speech to user/play speech for user
    pass


def start_connection():
    print("0")
    try:
        # connect to host image
        print("1")
        parameters = pika.ConnectionParameters(host="rabbitmq")
        # set variable equal to connection parameters of rabbitmq
        print("2")
        connection = pika.BlockingConnection(parameters)
        # set a channel with the channel() function
        print("3")
        channel = connection.channel()

        # channel.exchange_declare(
        #     exchange="text_to_bard",
        #     exchange_type="fanout",
        # )
        print("4")
        channel.queue_declare(queue="messages")
        # Creating a queue
        # messages = result.method.queue
        # channel.queue_bind(exchange="", queue="messages")
        print("5")
        channel.basic_consume(
            queue="messages",
            on_message_callback=converse,
            auto_ack=True,
        )
        print("Consumer.py is now consuming")
        channel.start_consuming()

    except Exception:
        print("account_info_consumer could not connect to RabbitMQ")
        time.sleep(3.0)
