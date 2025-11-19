import asyncio
import logging
import signal

from adapters.rabbitmq.consumer import RabbitConsumer
from app_setup import ApplicationSetup

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

SHUTDOWN = False


def _handle_signal(sig):
    global SHUTDOWN
    SHUTDOWN = True


async def main():
    loop = asyncio.get_running_loop()
    for s in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(s, lambda sig=s: _handle_signal(sig))

    container = ApplicationSetup()
    await container.init_resources()

    use_case = container.get_use_case()

    channel = await container.get_channel()
    consumer = RabbitConsumer(channel)

    await consumer.start(use_case.execute)

    # Keep running until signal
    while not SHUTDOWN:
        await asyncio.sleep(0.5)

    await container.shutdown()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
