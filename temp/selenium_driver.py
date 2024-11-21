from selenium import webdriver
from config import WEBDRIVER_OPTIONS
import undetected_chromedriver as uc

GPT_URL = "https://chatgpt.com/"


def create_webdriver() -> webdriver.Chrome:
    driver = uc.Chrome(options=WEBDRIVER_OPTIONS)
    driver.get(GPT_URL)
    return driver


async def send_message(driver: webdriver.Chrome, message: str) -> None:
    pass


def get_page_screenshot(driver: webdriver.Chrome) -> bytes:
    return driver.get_screenshot_as_png()


def tear_down(driver: webdriver.Chrome) -> None:
    driver.close()
