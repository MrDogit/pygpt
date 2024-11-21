from platform import system
from selenium.webdriver import ChromeOptions

from typing import Iterable
from fake_useragent import UserAgent

TELEGRAM_TOKEN: str = ""
DEBUG: bool = True
ADMINS: Iterable[str] = [-1]

WEBDRIVER_OPTIONS: ChromeOptions = ChromeOptions()
WEBDRIVER_OPTIONS.add_argument("enable-automation")
WEBDRIVER_OPTIONS.add_argument("--no-sandbox")
WEBDRIVER_OPTIONS.add_argument("--disable-extensions")
WEBDRIVER_OPTIONS.add_argument("--disable-gpu")

WEBDRIVER_OPTIONS.add_argument(f"user-agent={UserAgent.random}")
# WEBDRIVER_OPTIONS.add_argument("user-data-dir=./")
# WEBDRIVER_OPTIONS.add_experimental_option("detach", True)
# WEBDRIVER_OPTIONS.add_experimental_option("excludeSwitches", ["enable-logging"])
# WEBDRIVER_OPTIONS.add_argument(
#     "--ignore-certificate-errors"
# )  # try to fix handshake failed
WEBDRIVER_OPTIONS.add_argument("--ignore-ssl-errors")  # try to fix handshake failed
if system() == "Linux":
    WEBDRIVER_OPTIONS.add_argument("--dns- prefetch-disable")  # cause crash on windows
if not DEBUG:
    WEBDRIVER_OPTIONS.add_argument("--headless=new")  # TODO: Check with screenshots
