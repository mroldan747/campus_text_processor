import json
from dataclasses import asdict

from aio_pika import Message

from config.settings import PUBLISHER_QUEUE
from domaine.entities import TextMessage
from interfaces.publisher import PublisherInterface



class RabbitPublisher(PublisherInterface):
    def __init__(self, channel, queue_name: str = PUBLISHER_QUEUE):
        self.channel = channel
        self.queue_name = queue_name

    async def publish(self, message: TextMessage):
        body = json.dumps(asdict(message)).encode("utf-8")
        msg = Message(body=body)
        await self.channel.default_exchange.publish(msg, routing_key=self.queue_name)