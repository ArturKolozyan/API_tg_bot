import asyncio
import logging
from aiogram import Bot, Dispatcher

from .config import config
from db.database import db
from bot.handlers import router


async def main():
    bot = Bot(token=config.get_bot_token())
    dp = Dispatcher()
    dp.include_router(router)
    logging.basicConfig(level='INFO')
    await db.delete_database()
    await db.create_database()
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info('Exit')
