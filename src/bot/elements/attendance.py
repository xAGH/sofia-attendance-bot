from selenium.webdriver.common.by import By

ROL_VALUE = "13"
MAIN_FRAME = (By.ID, "contenido")
ROL_SELECTOR = (By.ID, "seleccionRol:roles")
TIME_MANAGEMENT = (By.XPATH, '//*[@id="side-menu"]/li[4]/a')
INSTRUCTOR_TIME_MANAGEMENT = (By.XPATH, '//*[@id="side-menu"]/li[4]/ul/li/a')
REGISTER_ABSENCES = (By.XPATH, '//*[@id="24093Opcion"]')
CURRENT_TABLE_ROWS = (By.XPATH, ".//tr")
SECOND_TABLE_COLUMN = (By.XPATH, ".//td[2]")
FIRST_TABLE_COLUMN_A = (By.XPATH, ".//td[1]//a")


class Group:
    ELEMENT = (By.ID, "formNovedadAprendiz:fichaOLK")
    FRAME = (By.ID, "viewDialog2_content")
    NEXT_BTN = (By.ID, "form2:dsListasnext")
    TABLE = (By.ID, "form2:dtListas")


class Student:
    ELEMENT = (By.ID, "formNovedadAprendiz:aprendizOLK")
    FRAME = (By.ID, "viewDialog1_content")
    NEXT_BTN = (By.ID, "form2:dsListasnext")
    TABLE = (By.ID, "form2:dtListas")


HOURS_INPUT = (By.ID, "formNovedadAprendiz:horasITX")
JUSTIFICATION_INPUT = (By.ID, "formNovedadAprendiz:justificacionITA")
START_DATE_INPUT = (By.ID, "formNovedadAprendiz:fechaEjecucion")
END_DATE_INPUT = (By.ID, "formNovedadAprendiz:fechaFin")
