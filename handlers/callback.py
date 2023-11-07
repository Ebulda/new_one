from aiogram import types, Dispatcher
from config import bot
from scraping.news_scraper import NewsScraper


async def latest_news_call(call: types.CallbackQuery):
    scraper = NewsScraper()
    links = scraper.parse_data()
    for link in links:
        await bot.send_message(
            chat_id=call.message.chat.id,
            text=link,
        )



def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(latest_news_call,
                                    lambda call: call.data == "latest_news")