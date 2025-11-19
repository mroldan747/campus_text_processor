from abc import ABC, abstractmethod
from typing import Any


class DatabaseManagerInterface(ABC):

    @abstractmethod
    async def connect_to_database(self, connection_string: str, database: str) -> None:
        raise NotImplementedError

    @abstractmethod
    async def close_database_connection(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_database(self) -> Any:
        raise NotImplementedError
