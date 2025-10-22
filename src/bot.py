from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from custom_types.absence import Absence


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
        time_management = self.wait_until_clickable(
            By.XPATH, '//*[@id="side-menu"]/li[4]/a'
        )
        time_management.click()
        instructor_time_management = self.wait_until_clickable(
            By.XPATH, '//*[@id="side-menu"]/li[4]/ul/li/a'
        )
        instructor_time_management.click()
        register_absences = self.wait_until_clickable(
            By.XPATH, '//*[@id="24093Opcion"]'
        )
        register_absences.click()

    def find_element_in_table(self, criteria: str, table: WebDriver):
        rows = table.find_elements(By.XPATH, ".//tr")

        for row in rows:
            try:
                second_column = row.find_element(By.XPATH, ".//td[2]")
                if criteria.strip() not in second_column.text.strip():
                    continue
                selector = row.find_element(By.XPATH, ".//td[1]//a")
                selector.click()
                break
            except Exception as e:
                print(f"Error consultando filas de las fichas {e}")
                continue

    def select_group(self, group_code: str):
        group_selector = self.wait_until_clickable(
            By.ID, "formNovedadAprendiz:fichaOLK"
        )
        group_selector.click()
        iframe = self.wait_until_located(By.ID, "viewDialog2_content")
        self.driver.switch_to.frame(iframe)
        groups_table = self.wait_until_located(By.ID, "form2:dtListas")
        self.find_element_in_table(group_code, groups_table)

    def select_student(self, name: str):
        student_selector = self.wait_until_clickable(
            By.ID, "formNovedadAprendiz:aprendizOLK"
        )
        student_selector.click()
        iframe = self.wait_until_located(By.ID, "viewDialog1_content")
        self.driver.switch_to.frame(iframe)
        students_table = self.wait_until_located(By.ID, "form2:dtListas")
        self.find_element_in_table(name, students_table)

    def set_hours(self, hours: int):
        hours_input = self.wait_until_located(By.ID, "formNovedadAprendiz:horasITX")
        hours_input.send_keys(hours)

    def set_justification(self, hours: int, justification: str):
        without_excuse = " NO PRESENTA EXCUSA VÁLIDA"

        if not justification:
            justification = "LLEGA TARDE." if hours < 3 else "NO ASISTE."
            justification += without_excuse

        justification_input = self.wait_until_located(
            By.ID, "formNovedadAprendiz:justificacionITA"
        )
        justification_input.send_keys(justification)

    def set_date(self, date: str):
        start_date_input = self.wait_until_located(
            By.ID, "formNovedadAprendiz:fechaEjecucion"
        )
        start_date_input.send_keys(date)
        end_date_input = self.wait_until_located(By.ID, "formNovedadAprendiz:fechaFin")
        end_date_input.send_keys(date)

    def register_absence(self, record: Absence):
        print(f"Registrando inasistencia: {record['full_name']} - {record['date']}")
        iframe = self.wait_until_located(By.ID, "contenido")
        self.driver.switch_to.frame(iframe)

        # Select group
        self.select_group(record.get("group_code"))
        self.driver.switch_to.frame(iframe)

        # Select student
        self.select_student(record.get("name"))
        self.driver.switch_to.frame(iframe)

        # Set hours
        self.set_hours(int(record.get("hours")))

        # Set justification
        self.set_justification(record.get("justification"))

        # Set date
        self.set_date(record.get("date"))

    def close(self):
        self.driver.quit()
