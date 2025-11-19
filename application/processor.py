import asyncio
import random
import time
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=4)

class TextProcessor:

    def __init__(self, executor_pool: ThreadPoolExecutor = executor):
        self.executor = executor_pool


    def _compute_score(self, text: str) -> float:
        time.sleep(random.uniform(2, 15))
        return random.random()

    async def process(self, text: str) -> float:
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(self.executor, self._compute_score, text)
        return result

