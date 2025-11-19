from aio_pika import connect_robust
from aio_pika.abc import AbstractRobustConnection, AbstractRobustChannel

from connections.broker.base import BrokerManagerInterface


class BrokerManager(BrokerManagerInterface):
    connection: AbstractRobustConnection
    channel: AbstractRobustChannel

    async def connect(self, connection_string: str) -> None:
        self.connection = await connect_robust(connection_string)
        self.channel = await self.connection.channel()

    async def close_connection(self) -> None:
        await self.channel.close()
        await self.connection.close()

    async def get_channel(self) -> AbstractRobustChannel:
        return self.channel
