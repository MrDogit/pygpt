from tg.keyboards import get_main_kb
from aiogram import F, Router, html
from aiogram.types import Message

router = Router()


@router.message()
async def last_chance_handler(message: Message) -> None:
    await message.answer(
        (
            "Я тебя не понял и в благородство играть не буду.\n"
            f"Пришли мне своё сообщение ещё раз, но {html.bold('корректно')} и тогда поговорим."
        ),
        reply_markup=await get_main_kb(),
    )
