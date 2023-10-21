from aiogram import types, Dispatcher
from config import bot


async def chat_action(message: types.Message):
    ban_words = ['fuck', 'bitch', 'damn']
    print(message.chat.id)
    if message.chat.id == -4062920738:
        for word in ban_words:
            if word in message.text.lower().replace(' ',''):
                await bot.delete_message(
                    chat_id=message.chat.id,
                    message_id=message.message_id
                )
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f'{message.from_user.username}, ты подозрителен и можешь быть забанен!!11!!1!1'
                )

def register_chat_action_handlers(dp: Dispatcher):
    dp.register_message_handler(chat_action)