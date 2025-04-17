from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from .keyboards import *
from .texts import *

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(text=cmd_start_text, reply_markup=get_main_keyboard())


@router.callback_query(F.data == 'GET')
async def cmd_callback(callback: CallbackQuery):

    await callback.message.answer('GET')
