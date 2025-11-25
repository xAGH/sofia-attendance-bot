import logging
from typing import List

from selenium.webdriver.common.by import By

import bot.elements.login as Elements
from bot.core.selenium_bot import SeleniumBot
from bot.process.attendance import AttendanceBot
from config import Env
from models.absence import Absence


class SofiaBot(SeleniumBot):

    def __init__(self, timeout=10):
        super().__init__(timeout)
        self.username = Env.SENA_SOFIA_USERNAME
        self.password = Env.SENA_SOFIA_PASSWORD
        self.login_url = Env.SENA_SOFIA_LOGIN_URL

    def login(self):
        logging.info("Iniciando sesión en Sofía Plus...")
        self.driver.get(self.login_url)
        self.switch_to_frame(Elements.MAIN_FRAME)

        user_input = self.wait_until_located(Elements.USER_INPUT)
        user_input.send_keys(self.username)

        password_input = self.wait_until_located(Elements.PASSWORD_INPUT)
        password_input.send_keys(self.password)

        login_btn = self.wait_until_clickable(Elements.LOGIN_BTN)
        login_btn.click()

        self.switch_to_default_content()

    def register_absences(self, records: List[Absence]):
        AttendanceBot().execute(records)
