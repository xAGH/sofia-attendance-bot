import logging

from selenium.webdriver.common.by import By

from bot.selenium_bot import SeleniumBot


class SofiaBot(SeleniumBot):
    def login(self, url: str, username: str, password: str):
        logging.info("Iniciando sesión en Sofía Plus...")
        self.driver.get(url)
        self.switch_to_frame(By.ID, "registradoBox1")

        user_input = self.wait_until_located(By.NAME, "ingreso")
        user_input.send_keys(self.username)

        password_input = self.wait_until_located(By.NAME, "josso_password")
        password_input.send_keys(self.password)

        self.driver.find_element(By.NAME, "ingresar").click()
        self.switch_to_default_content()
