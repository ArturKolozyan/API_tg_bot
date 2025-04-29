from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from .include import texts, keyboards
from src.db.database import DatabaseService

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(text=texts.cmd_start_text, reply_markup=keyboards.get_main_keyboard())


@router.callback_query(F.data == 'GET')
async def cmd_callback(
        callback: CallbackQuery,
        db: DatabaseService
):
    await db.create_database()
    # await db.delete_database()
    await callback.answer()
    await callback.message.answer("Вы нажали кнопку!")
