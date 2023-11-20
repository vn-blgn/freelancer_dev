import asyncio
from src.handlers import data_handler
from src.helpers import send_mess


async def main():
    while True:
        tasks = data_handler()
        for elem in tasks:
            await send_mess(elem)
            await asyncio.sleep(6)
        await asyncio.sleep(3600)


if __name__ == '__main__':
    asyncio.run(main())
