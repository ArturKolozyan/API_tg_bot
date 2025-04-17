import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import Config
from bot.handlers import router

config = Config()


async def main():
    bot = Bot(token=config.get_bot_token())
    dp = Dispatcher()
    dp.include_router(router)
    logging.basicConfig(level='INFO')
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
