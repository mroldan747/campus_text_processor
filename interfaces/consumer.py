from abc import ABC, abstractmethod
from typing import Callable, Awaitable

from domaine.entities import TextMessage

CallbackType = Callable[[TextMessage], Awaitable[None]]

class ConsumerInterface(ABC):

    @abstractmethod
    async def start(self, callback: CallbackType):
        raise NotImplementedError
