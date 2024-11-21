import logging
from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
from tg.handlers import gpt, test, last_chance

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import TELEGRAM_TOKEN


async def main() -> None:
    bot = Bot(
        token=TELEGRAM_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(test.router)
    dp.include_router(gpt.router)
    dp.include_router(last_chance.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
