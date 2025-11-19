import json
import pytest
from unittest.mock import AsyncMock

from adapters.rabbitmq.publisher import RabbitPublisher
from domaine.entities import TextMessage, MessageType


@pytest.mark.asyncio
async def test_publisher_sends_correct_message():
    # Fake channel + default exchange mock
    mock_exchange = AsyncMock()
    mock_channel = AsyncMock()
    mock_channel.default_exchange = mock_exchange

    publisher = RabbitPublisher(mock_channel, queue_name="test_queue")

    msg = TextMessage(
        id="123",
        user_id="u1",
        type=MessageType.UPDATE,
        text="hello world"
    )

    await publisher.publish(msg)

    # The message published must be JSON encoded
    args, kwargs = mock_exchange.publish.call_args
    sent_message = args[0]  # aio_pika.Message
    routing_key = kwargs["routing_key"]

    assert routing_key == "test_queue"
    body = json.loads(sent_message.body.decode())

    assert body == {
        "id": "123",
        "user_id": "u1",
        "type": MessageType.UPDATE.value,
        "text": "hello world",
        "score": None
    }