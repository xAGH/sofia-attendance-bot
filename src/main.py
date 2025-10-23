import time
from typing import List

from bot.selenium_bot import SofiaAttendanceBot
from config import Env
from core.exceptions import NotFound
from csv_reader import load_absences
from models.absence import Absence


def main():
    absences: List[Absence] = load_absences(Env.ABSENCES_CSV_URL)
    bot = SofiaAttendanceBot(Env.SENA_SOFIA_USERNAME, Env.SENA_SOFIA_PASSWORD)
    bot.login(Env.SENA_SOFIA_LOGIN_URL)
    bot.select_instructor_rol()
    bot.select_register_absences()

    for record in absences:
        try:
            bot.register_absence(record)
        except NotFound:
            print("Fallo seguro")
            exit()

    bot.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
