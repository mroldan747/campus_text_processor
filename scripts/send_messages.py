import asyncio
import os
import random
import uuid
import argparse

from adapters.rabbitmq.publisher import RabbitPublisher
from app_setup import ApplicationSetup
from config.settings import CONSUMER_QUEUE
from domaine.entities import TextMessage, MessageType

RABBIT_HOST = os.getenv("RABBITMQ_HOST")
RABBIT_USER = os.getenv("RABBITMQ_USER")
RABBIT_PASS = os.getenv("RABBITMQ_PASS")


async def send_messages(
        count: int,
):
    app = ApplicationSetup()
    channel = await app.get_channel()
    publisher = RabbitPublisher(channel, CONSUMER_QUEUE)

    for i in range(count):
        msg_id = str(uuid.uuid4())
        user_id = f"u_{random.randint(1000, 9999)}"
        text = random.choice([
            "I love this!",
            "This is terrible...",
            "Worst experience ever",
            "Amazing, would do again",
            "This product sucks",
            "Beautiful piece of art",
            "I hate everything about this",
        ])
        msg_type = random.choice([MessageType.UPDATE, MessageType.UPDATE, MessageType.UPDATE, MessageType.DELETE])

        payload = {
            "id": msg_id,
            "user_id": user_id,
            "type": msg_type.value,
            "text": text,
        }

        message = TextMessage(**payload)

        await publisher.publish(message)

        print(f"[{i + 1}/{count}] Sent message {msg_id} ({msg_type})")

    print("\nDone! All messages sent.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=100, help="Number of messages to send")
    args = parser.parse_args()

    asyncio.run(send_messages(
        count=args.count
    ))
