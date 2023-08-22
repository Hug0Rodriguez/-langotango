import pika
import json
from requests import get


# define function to consume messages from rabbit_mq
def converse(ch, method, properties, body):
    content = json.loads(body)
    headers = {"Authorization": "Bearer " + content["bard_token"]}
    # send data to bard
    response = get("https://bard.ai/api/v1/generate", headers=headers)

    # take data from bard response
    text = response.text

    # convert text to speech (MORE RESEARCH REQUIRED)

    # send audio back to user
    pass


def update_accountvo(ch, method, properties, body):
    content = json.loads(body)
    first_name = content["first_name"]
    last_name = content["last_name"]
    email = content["email"]
    is_active = content["is_active"]
    updated_string = content["updated"]
    updated = datetime.fromisoformat(updated_string)
    if is_active:
        AccountVO.objects.update_or_create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_active=is_active,
            updated=updated,
        )
    else:
        AccountVO.objects.delete(email=email)


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
            on_message_callback=update_accountvo,
            auto_ack=True,
        )
        channel.start_consuming()
    except AMQPConnectionError:
        print("account_info_consumer could not connect to RabbitMQ")
        time.sleep(3.0)
