import asyncio


class BackgroundRunner:
    def __init__(self):
        self.value = 0
        self.is_running = False

    async def run_main(self):
        while True:
            if(not self.is_running):
                await asyncio.sleep(1)
                continue
            await asyncio.sleep(0.1)
            self.value += 1
