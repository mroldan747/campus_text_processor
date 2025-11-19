from abc import ABC, abstractmethod
from typing import Any

from aio_pika.abc import AbstractRobustConnection, AbstractRobustChannel


class BrokerManagerInterface(ABC):

    @abstractmethod
    async def connect(self, connection_string: str) -> None:
        raise NotImplementedError

    @abstractmethod
    async def close_connection(self) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_channel(self) -> AbstractRobustChannel:
        raise NotImplementedError
