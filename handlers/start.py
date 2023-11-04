import sqlite3

from aiogram import types, Dispatcher
from aiogram.utils.deep_linking import _create_link

from config import bot
from database.sql_commands import Database
from keyboards.inline_buttoons import start_keyboard


async def start_button(message: types.Message):
    print(message)
    print(message.get_full_command())
    command = message.get_full_command()
    if command[1] != "":
        link = await _create_link(link_type="start", payload=command[1])
        owner = Database().sql_select_user_by_link_query(
            link=link
        )
        if owner[0]["telegram_id"] == message.from_user.id:
            await bot.send_message(
                chat_id=message.from_user.id,
                text="You can not use own referral link"
            )
            return
        print(f"owner: {owner}")
        try:
            Database().sql_insert_referral_query(
                owner=owner[0]['telegram_id'],
                referral=message.from_user.id
            )
        except sqlite3.IntegrityError:
            pass

    try:
        Database().sql_insert_user_query(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
        )
    except sqlite3.IntegrityError:
        pass

    await bot.send_message(
        chat_id=message.chat.id,
        text="Hello, my dear!",
        reply_markup=await start_keyboard()
    )


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=['start'])