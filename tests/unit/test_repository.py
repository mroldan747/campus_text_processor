import pytest
from unittest.mock import AsyncMock, MagicMock

from adapters.mongo.repository import TextMessageRepository
from domaine.entities import TextMessage, MessageType

TEXT_MESSAGES_COLLECTION = "text_messages"


@pytest.mark.asyncio
async def test_repository_update():
    mock_collection = AsyncMock()
    mock_db = MagicMock()
    mock_db.__getitem__.return_value = mock_collection

    repo = TextMessageRepository(database=mock_db)

    msg = TextMessage(
        id="123",
        user_id="u99",
        type=MessageType.UPDATE,
        text="updated text",
        score=0.11
    )

    await repo.update(msg)

    mock_collection.update_one.assert_awaited_once_with(
        {"id": "123"},
        {"$set": {
            "id": "123",
            "user_id": "u99",
            "type": MessageType.UPDATE.value,
            "text": "updated text",
            "score": 0.11
        }},
        upsert=True
    )


@pytest.mark.asyncio
async def test_repository_delete():
    mock_collection = AsyncMock()
    mock_db = MagicMock()
    mock_db.__getitem__.return_value = mock_collection

    repo = TextMessageRepository(database=mock_db)

    await repo.delete("999")

    mock_collection.delete_one.assert_awaited_once_with({"id": "999"})
