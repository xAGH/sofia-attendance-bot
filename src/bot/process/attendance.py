from time import sleep
from typing import List, Union

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

import bot.elements.attendance as Elements
from bot.core.selenium_bot import SeleniumBot
from core.exceptions import NotFound
from models.absence import Absence


class AttendanceBot(SeleniumBot):

    def select_instructor_rol(self):
        print("Seleccionando rol de instructor...")
        dropdown_element = self.wait_until_located(Elements.ROL_SELECTOR)
        role_select = Select(dropdown_element)
        role_select.select_by_value(Elements.ROL_VALUE)

    def select_register_absences(self):
        self.wait_until_spiner_disappear()
        print("Accediendo a 'Gestión de tiempos'...")
        time_management = self.wait_until_clickable(Elements.TIME_MANAGEMENT)
        time_management.click()

        print("Accediendo a 'Gestión de tiempos del instructor'...")
        instructor_time_management = self.wait_until_clickable(
            Elements.INSTRUCTOR_TIME_MANAGEMENT
        )
        instructor_time_management.click()

        print("Accediendo a 'Registrar inasistencias del aprendiz'...")
        register_absences = self.wait_until_clickable(Elements.REGISTER_ABSENCES)
        register_absences.click()

    def find_element_in_table(
        self, criteria: Union[int, str], table: WebDriver
    ) -> bool:
        rows = table.find_elements(Elements.CURRENT_TABLE_ROWS)

        for row in rows:
            try:
                second_column = row.find_element(Elements.SECOND_TABLE_COLUMN)
                if str(criteria).strip() in second_column.text.strip():
                    selector = row.find_element(Elements.FIRST_TABLE_COLUMN_A)
                    selector.click()
                    return True
            except:
                continue
        return False

    def select_group(self, group_code: str):
        sleep(1.5)
        print("Seleccionando ficha...")
        group_selector = self.wait_until_clickable(Elements.Group.ELEMENT)
        group_selector.click()
        iframe = self.wait_until_located(Elements.Group.FRAME)
        self.driver.switch_to.frame(iframe)
        max_pages = 5
        current_page = 1
        found = False

        while current_page <= max_pages:
            if current_page != 1:
                next_btn = self.wait_until_clickable(Elements.Group.NEXT_BTN)
                next_btn.click()
            groups_table = self.wait_until_located(Elements.Group.TABLE)
            found = self.find_element_in_table(group_code, groups_table)
            if found:
                break
            current_page += 1
        else:
            raise NotFound("ficha", group_code)
        print("Ficha seleccionada ✅")

    def select_student(self, name: str):
        print("Seleccionando aprendiz...")
        student_selector = self.wait_until_clickable(Elements.Student.ELEMENT)
        student_selector.click()
        iframe = self.wait_until_located(Elements.Student.FRAME)
        self.driver.switch_to.frame(iframe)
        max_pages = 5
        current_page = 1
        found = False

        while current_page <= max_pages:
            if current_page != 1:
                next_btn = self.wait_until_clickable(Elements.Student.NEXT_BTN)
                next_btn.click()
            students_table = self.wait_until_located(Elements.Student.TABLE)
            found = self.find_element_in_table(name, students_table)
            if found:
                break
            current_page += 1
        else:
            raise NotFound("nombre", name)
        print("Aprendiz seleccionado ✅")

    def set_hours(self, hours: int):
        hours_input = self.wait_until_located(Elements.HOURS_INPUT)
        hours_input.send_keys(hours)

    def set_justification(self, hours: int, justification: str):
        without_excuse = " NO PRESENTA EXCUSA VÁLIDA"

        if not justification:
            justification = "LLEGA TARDE." if hours < 3 else "NO ASISTE."
            justification += without_excuse

        justification_input = self.wait_until_located(Elements.JUSTIFICATION_INPUT)
        justification_input.send_keys(justification)

    def set_date(self, date: str):
        start_date_input = self.wait_until_located(Elements.START_DATE_INPUT)
        start_date_input.send_keys(date)
        end_date_input = self.wait_until_located(Elements.END_DATE_INPUT)
        end_date_input.send_keys(date)

    def register_absence(self, record: Absence):
        print(f"Registrando inasistencia: {record}")

        def switch_content_iframe():
            self.driver.switch_to.default_content()
            iframe = self.wait_until_located(Elements.MAIN_FRAME)
            self.driver.switch_to.frame(iframe)

        switch_content_iframe()

        group_code = record.get("group_code")
        name = record.get("name")
        hours = record.get("hours")
        justification = record.get("justification")
        date = record.get("date")

        # Select group
        self.select_group(group_code)
        switch_content_iframe()

        # Select student
        self.select_student(name)
        switch_content_iframe()

        self.set_hours(int(hours))
        self.set_justification(hours, justification)

        # Set date
        self.set_date(date)
        sleep(10)

    def execute(self, absences: List[Absence]):
        self.select_instructor_rol()
        self.select_register_absences()

        for absence in absences:
            try:
                self.register_absence(absence)
            except NotFound as err:
                print(err)
                exit()
