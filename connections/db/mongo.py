from connections.db.base import DatabaseManagerInterface

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


class MongoDB(DatabaseManagerInterface):
    client: AsyncIOMotorClient
    database: AsyncIOMotorDatabase

    async def connect_to_database(self, connection_string: str, database: str) -> None:
        self.client = AsyncIOMotorClient(connection_string)
        self.database = self.client[database]

    async def close_database_connection(self) -> None:
        if self.client:
            self.client.close()

    def get_database(self) -> AsyncIOMotorDatabase:
        return self.database