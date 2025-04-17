from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_main_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text='GET',
        callback_data='GET'
    )
    return keyboard.as_markup()
