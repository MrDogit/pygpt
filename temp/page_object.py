from selenium import webdriver


class BasePage(object):
    def __init__(self, driver):
        self.driver: webdriver.Chrome = driver


class MainPage(BasePage):
    def send_message():
        pass


class LoginPage(BasePage):
    pass


class ChooseConversationPage(BasePage):
    pass
