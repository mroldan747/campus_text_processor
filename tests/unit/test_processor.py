import pytest
from unittest.mock import AsyncMock

from application.process_message import ProcessMessage
from application.processor import TextProcessor
from domaine.entities import TextMessage, MessageType


@pytest.mark.asyncio
async def test_processor_updates_message():
    mock_repo = AsyncMock()
    processor = ProcessMessage(mock_repo, TextProcessor(), AsyncMock())

    message = TextMessage(
        id="1",
        user_id="u1",
        type=MessageType.UPDATE,
        text="hi"
    )

    await processor.execute(message)

    mock_repo.update.assert_awaited_once_with(message)


@pytest.mark.asyncio
async def test_processor_deletes_message():
    mock_repo = AsyncMock()
    processor = ProcessMessage(mock_repo, TextProcessor(), AsyncMock())

    message = TextMessage(
        id="1",
        user_id="u1",
        type=MessageType.DELETE,
        text="ignored"
    )

    await processor.execute(message)

    mock_repo.delete.assert_awaited_once_with("1")
