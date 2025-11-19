from application.processor import TextProcessor
from domaine.entities import TextMessage, MessageType
from interfaces.publisher import PublisherInterface
from interfaces.repository import TextRepositoryInterface


class ProcessMessage:
    def __init__(self, repository: TextRepositoryInterface, processor: TextProcessor, publisher:PublisherInterface):
        self.repository = repository
        self.processor = processor
        self.publisher = publisher


    async def execute(self, message: TextMessage):
        if message.type == MessageType.DELETE.value:
            await self.repository.delete(message.id)
            return

        score = await self.processor.process(message.text or "")

        message.score = score

        await self.repository.update(message)

        await self.publisher.publish(message)