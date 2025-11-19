from abc import ABC, abstractmethod

from domaine.entities import TextMessage


class PublisherInterface(ABC):

    @abstractmethod
    async def publish(self, message: TextMessage):
        raise NotImplementedError