from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumBot:

    def __init__(self, timeout=10):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, timeout)

    def wait_until_located(self, by: str, value: str):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def wait_until_clickable(self, by: str, value: str):
        return self.wait.until(EC.element_to_be_clickable((by, value)))

    def wait_until_appear_and_disappear(self, by: str, value: str):
        expected_condition = EC.visibility_of_any_elements_located((by, value))

        self.wait.until(expected_condition)
        self.wait.until_not(expected_condition)

    def wait_until_appear_and_disappear(self, by: str, value: str):
        expected_condition = EC.visibility_of_any_elements_located((by, value))

        self.wait.until(expected_condition)
        self.wait.until_not(expected_condition)

    def switch_to_frame(self, by: str, value: str):
        frame = self.wait.until(EC.frame_to_be_available_and_switch_to_it((by, value)))
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def close(self):
        self.driver.quit()
