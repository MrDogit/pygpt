from tg.keyboards import get_main_kb
from aiogram import F, Router, html
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(
        f"Hello, {html.bold(message.from_user.full_name)}!",
        reply_markup=await get_main_kb(),
    )


@router.message(Command("test"))
async def handle_button(message: Message) -> None:
    await message.answer("Вы отправили /test", reply_markup=await get_main_kb())
