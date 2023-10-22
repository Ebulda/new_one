from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def start_keyboard():
    markup = InlineKeyboardMarkup()
    registration_button = InlineKeyboardButton(
        'Registration',
        callback_data='fsm_start'
    )
    markup.add(registration_button)
    return markup