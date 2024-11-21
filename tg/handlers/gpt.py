from tg.keyboards import get_main_kb, get_gpt_kb_by_state
from aiogram import F, Router
from aiogram.types import (
    BufferedInputFile,
    Message,
)
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from datetime import datetime
from temp import selenium_driver

router = Router()


class ChromeWebdriver(StatesGroup):
    webdriver_launched = State()


@router.message(StateFilter(None), F.text == "Создать driver")
async def create_webdriver_handle(message: Message, state: FSMContext) -> None:
    webdriver = selenium_driver.create_webdriver()
    await message.answer("Driver создан", reply_markup=await get_gpt_kb_by_state())
    await state.set_state(ChromeWebdriver.webdriver_launched)
    await state.update_data(webdriver=webdriver)


@router.message(StateFilter("*"), Command("Screenshot"))
@router.message(StateFilter("*"), F.text == "Скриншот")
async def send_screenshot_handler(message: Message, state: FSMContext) -> None:
    print(state)
    state_data = await state.get_data()
    webdriver = state_data.get("webdriver")
    page_screenshot = selenium_driver.get_page_screenshot(webdriver)
    time_now = datetime.now()
    screenshot_file = BufferedInputFile(
        page_screenshot, f"Screenshot_{time_now.strftime('%H.%M.%S')}.png"
    )

    await message.answer_photo(
        screenshot_file, f"Screenshot time: {time_now.strftime('%H:%M:%S')}"
    )


@router.message(StateFilter("*"), Command("stop"))
@router.message(StateFilter("*"), F.text == "stop")
async def stop_handler(message: Message, state: FSMContext) -> None:
    state_data = await state.get_data()
    webdriver = state_data.get("webdriver")
    selenium_driver.tear_down(webdriver)
    state.update_data(webdriver=None)
    await message.answer("Driver закрыт", reply_markup=await get_main_kb())
