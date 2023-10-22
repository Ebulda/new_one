from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup



class FormStates(StatesGroup):
    nickname = State()
    bio = State()
    age = State()
    occupation = State()
    photo = State()


async def fsm_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text='Send me ur nickname'
    )
    await FormStates.nickname.set()

async def load_nickname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Now send me ur bio'
    )
    await FormStates.next()

async def load_bio(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['bio'] = message.text

    await bot.send_message(
        chat_id=message.from_user.id,
        text='How old r u? \n'
             '(only numbers)'
    )
    await FormStates.next()

async def load_age(message: types.Message, state: FSMContext):
    try:
        if type(int(message.text)) != int:
            pass
        async with state.proxy() as data:
            data['age'] = message.text

        await bot.send_message(
            chat_id=message.from_user.id,
            text='What is your occupation?'
        )
        await FormStates.next()

    except ValueError as e:
        await message.reply(
            text='Use numbers not letters \n'
                 'please register again'
        )
        await state.finish()
        return

async def load_occupation(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['occupation'] = message.text

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Send me ur photo, not file'
    )
    await FormStates.next()

async def load_photo(message: types.Message, state: FSMContext):
    path = await message.photo[-1].download(
        destination_dir='D:\pythonProject\media'
    )
    async with state.proxy() as data:
        with open(path.name, 'rb') as photo:
            await bot.send_photo(
                chat_id=message.chat.id,
                photo=photo,
                caption=f"Nickname: {data['nickname']}\n"
                        f"Bio: {data['bio']}\n"
                        f"Age: {data['age']}\n"
                        f"Occupation: {data['occupation']}\n"
            )
        await bot.send_message(
            chat_id=message.from_user.id,
            text='Registered successfully!'
        )
        await state.finish()


def register_fsm_form_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(fsm_start, lambda call: call.data == 'fsm_start')
    dp.register_message_handler(load_nickname, state=FormStates.nickname, content_types=['text'])
    dp.register_message_handler(load_bio, state=FormStates.bio, content_types=['text'])
    dp.register_message_handler(load_age, state=FormStates.age, content_types=['text'])
    dp.register_message_handler(load_occupation, state=FormStates.occupation, content_types=['text'])
    dp.register_message_handler(load_photo, state=FormStates.photo, content_types=types.ContentType.PHOTO)
