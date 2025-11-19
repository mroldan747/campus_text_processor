import os

from adapters.mongo.repository import TextMessageRepository
from adapters.rabbitmq.publisher import RabbitPublisher
from config.settings import DATABASE
from connections.db.mongo import MongoDB
from connections.broker.rabbitmq import BrokerManager
from application.process_message import ProcessMessage
from application.processor import TextProcessor


class ApplicationSetup:

    def __init__(self):
        self._mongo = None
        self._broker = None
        self._channel = None

    async def init_resources(self):
        await self.init_mongo()
        await self.init_broker()


    async def init_mongo(self):
        user = os.getenv('MONGO_INITDB_ROOT_USERNAME')
        p = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
        uri = (
            f"mongodb://{user}:"
            f"{p}@mongodb:27017/"
        )
        self._mongo = MongoDB()
        await self._mongo.connect_to_database(uri, DATABASE)
        await self.get_repository().create_index()

    async def init_broker(self):
        self._broker = BrokerManager()
        user = os.getenv('RABBITMQ_USER')
        p = os.getenv('RABBITMQ_PASS')
        host = os.getenv('RABBITMQ_HOST')
        await self._broker.connect(
            f"amqp://{user}:"
            f"{p}@{host}/"
        )
        self._channel = await self._broker.get_channel()

    async def get_channel(self):
        if not self._channel:
            await self.init_broker()
        return self._channel



    def get_repository(self):
        return TextMessageRepository(self._mongo.get_database())

    def get_publisher(self):
        return RabbitPublisher(self._channel)

    def get_processor(self):
        return TextProcessor()

    def get_use_case(self):
        return ProcessMessage(
            repository=self.get_repository(),
            processor=self.get_processor(),
            publisher=self.get_publisher(),
        )

    async def shutdown(self):
        if self._broker:
            await self._broker.close_connection()
        if self._mongo:
            await self._mongo.close_database_connection()
