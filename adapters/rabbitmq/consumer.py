import json
import logging
from aio_pika import IncomingMessage

from config.settings import CONSUMER_QUEUE
from domaine.entities import TextMessage
from interfaces.consumer import ConsumerInterface


class RabbitConsumer(ConsumerInterface):
    def __init__(self, channel, queue_name: str = CONSUMER_QUEUE):
        self.channel = channel
        self.queue_name = queue_name
        self._queue = None
        self._consumer_tag = None

    async def _on_message(self, message: IncomingMessage, callback):
        async with message.process():
            try:
                data = json.loads(message.body)
            except Exception:
                logging.exception("Invalid Text")
                return

            try:
                msg = TextMessage(**data)
            except TypeError:
                logging.exception("Message missing required fields")
                return

            await callback(msg)

    async def start(self, callback):
        self._queue = await self.channel.get_queue(self.queue_name)
        await self.channel.set_qos(prefetch_count=10)

        async def _handler(msg: IncomingMessage):
            await self._on_message(msg, callback)

        await self._queue.consume(_handler)