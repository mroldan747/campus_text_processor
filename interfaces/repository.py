from abc import ABC, abstractmethod

from domaine.entities import TextMessage


class TextRepositoryInterface(ABC):

    @abstractmethod
    async def create_index(self):
        raise NotImplementedError

    @abstractmethod
    async def update(self, message: TextMessage):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, msg_id: str):
        raise NotImplementedError