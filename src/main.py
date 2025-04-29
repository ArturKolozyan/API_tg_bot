import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import config
from app.handlers import router
from db.database import DatabaseService


def create_dispatcher():
    dp = Dispatcher()
    dp.include_router(router)
    dp.workflow_data.update(
        db=DatabaseService()
    )
    return dp


async def main():
    bot = Bot(token=config.get_bot_token)
    dp = create_dispatcher()
    logging.basicConfig(level='INFO')
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
