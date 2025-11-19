import json
import pytest
from unittest.mock import AsyncMock, MagicMock


from adapters.rabbitmq.consumer import RabbitConsumer
from domaine.entities import TextMessage


@pytest.mark.asyncio
async def test_consumer_parses_message_and_calls_callback():
    mock_channel = AsyncMock()
    consumer = RabbitConsumer(mock_channel, queue_name="test_queue")

    # Fake payload
    payload = {
        "id": "abc",
        "user_id": "u123",
        "type": "UPDATE",
        "text": "hello"
    }

    body = json.dumps(payload).encode()

    incoming = MagicMock()
    incoming.body = body
    incoming.process.return_value.__aenter__.return_value = incoming
    incoming.process.return_value.__aexit__.return_value = False

    callback = AsyncMock()

    await consumer._on_message(incoming, callback)

    callback.assert_awaited_once()

    message_passed = callback.call_args[0][0]

    assert isinstance(message_passed, TextMessage)
    assert message_passed.id == "abc"
    assert message_passed.text == "hello"