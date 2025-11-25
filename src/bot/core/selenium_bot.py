from typing import Tuple

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumBot:

    def __init__(self, timeout=10):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, timeout)

    def wait_until_located(self, element_selector: Tuple[str, str]):
        return self.wait.until(EC.presence_of_element_located(element_selector))

    def wait_until_clickable(self, element_selector: Tuple[str, str]):
        return self.wait.until(EC.element_to_be_clickable(element_selector))

    def wait_until_appear_and_disappear(self, element_selector: Tuple[str, str]):
        expected_condition = EC.visibility_of_any_elements_located(element_selector)

        self.wait.until(expected_condition)
        self.wait.until_not(expected_condition)

    def wait_until_appear_and_disappear(self, element_selector: Tuple[str, str]):
        expected_condition = EC.visibility_of_any_elements_located(element_selector)

        self.wait.until(expected_condition)
        self.wait.until_not(expected_condition)

    def switch_to_frame(self, element_selector: Tuple[str, str]):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(element_selector))

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def close(self):
        self.driver.quit()
