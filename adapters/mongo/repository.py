from dataclasses import asdict

from config.settings import TEXT_MESSAGES_COLLECTION
from domaine.entities import TextMessage

from motor.motor_asyncio import AsyncIOMotorDatabase

from interfaces.repository import TextRepositoryInterface


class TextMessageRepository(TextRepositoryInterface):

    def __init__(self, database: AsyncIOMotorDatabase):
        self._collection = database[TEXT_MESSAGES_COLLECTION]

    async def create_index(self):
        await self._collection.create_index("id")

    async def update(self, message: TextMessage):
        await self._collection.update_one(
            {"id": message.id},
            {"$set": asdict(message)},
            upsert = True
        )

    async def delete(self, msg_id: str):
        await self._collection.delete_one({"id": msg_id})
