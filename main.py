import asyncio
from aiogram import Bot

from config import Config

config = Config()


async def main():
    bot = Bot(token=config.get_bot_token())


if __name__ == "__main__":
    asyncio.run(main())
