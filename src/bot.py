import time
from typing import Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


class SofiaAttendanceBot:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def wait_until_located(self, by: str, value: str):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def wait_until_clickable(self, by: str, value: str):
        return self.wait.until(EC.element_to_be_clickable((by, value)))

    def login(self, url: str):
        print("Iniciando sesión en Sofía Plus...")
        self.driver.get(url)

        iframe = self.wait_until_located(By.ID, "registradoBox1")
        self.driver.switch_to.frame(iframe)

        user_input = self.wait_until_located(By.NAME, "ingreso")
        user_input.send_keys(self.username)

        password_input = self.wait_until_located(By.NAME, "josso_password")
        password_input.send_keys(self.password)

        self.driver.find_element(By.NAME, "ingresar").click()
        self.driver.switch_to.default_content()

    def select_instructor_rol(self):
        print("Seleccionando rol de instructor...")
        dropdown_element = self.wait_until_located(By.ID, "seleccionRol:roles")
        role_select = Select(dropdown_element)
        role_select.select_by_value("13")

    def select_register_absences(self):
        print("Entrando a la pantalla de registrar inasistencias...")
        time_management = self.wait_until_clickable(
            By.XPATH, '//*[@id="side-menu"]/li[4]/a'
        )
        print(time_management)
        time_management.click()
        instructor_time_management = self.wait_until_clickable(
            By.XPATH, '//*[@id="side-menu"]/li[4]/ul/li/a'
        )
        instructor_time_management.click()
        register_absences = self.wait_until_clickable(
            By.XPATH, '//*[@id="24093Opcion"]'
        )
        register_absences.click()

    def register_absence(self, record):
        print(f"Registrando inasistencia: {record['full_name']} - {record['date']}")

    def close(self):
        self.driver.quit()
