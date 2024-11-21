from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters import StateFilter


async def get_main_kb() -> ReplyKeyboardMarkup:

    kb_builder = ReplyKeyboardBuilder()

    kb_builder.add(
        KeyboardButton(text="Создать driver"),
        KeyboardButton(text="/test"),
    )
    return kb_builder.as_markup(resize_keyboard=True)


async def get_gpt_kb_by_state() -> ReplyKeyboardMarkup:
    kb_builder = ReplyKeyboardBuilder()

    if StateFilter("*"):
        kb_builder.add(
            KeyboardButton(text="Отправить сообщение"),
            KeyboardButton(text="Скриншот"),
            KeyboardButton(text="Залогиниться"),
            KeyboardButton(text="stop"),
            KeyboardButton(text="test1"),
        )

    return kb_builder.as_markup(resize_keyboard=True)
