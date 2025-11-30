from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db import DatabaseService
from api import JSONPlaceholderClient
from schemas import UserSchema

router = Router()

def get_main_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text='GET',
        callback_data='GET'
    )
    return keyboard.as_markup()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(
        text=(f'Привет!\n\n'
        f'Это бот, который интегрируется с открытым API '
        f'(JSON Placeholder), получает данные,'
        f' обрабатывает их, и сохраняет в базе данных и Google Sheets.'),
        reply_markup=get_main_keyboard())


@router.callback_query(F.data == 'GET')
async def cmd_callback(
        callback: CallbackQuery,
        db: DatabaseService,
        api: JSONPlaceholderClient,
):
    try:
        raw_data = await api.get_data()
        users_data = []
        for raw_user_data in raw_data:
            try:
                user = UserSchema(**raw_user_data)
                users_data.append(user.id)
                await db.create_user(**user.model_dump())
            except Exception as e:
                print(f"Ошибка валидации или сохранения пользователя: {e}.  Пропущен пользователь с данными: {raw_user_data}")

        await callback.answer()
        await callback.message.answer(f'Данные успешно получены и сохранены, id сохраненных пользователей:\n{users_data}')
    except Exception as e:
        print(f"Произошла общая ошибка: {e}")
        await callback.answer("Произошла ошибка при обработке данных", show_alert=True)
