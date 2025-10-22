import time

from bot import SofiaAttendanceBot
from config import Env
from csv_reader import load_absences


def main():
    absences = load_absences(Env.ABSENCES_CSV_URL)
    bot = SofiaAttendanceBot(Env.SENA_SOFIA_USERNAME, Env.SENA_SOFIA_PASSWORD)
    bot.login(Env.SENA_SOFIA_LOGIN_URL)
    bot.select_instructor_rol()
    bot.select_register_absences()
    time.sleep(4)

    for record in absences:
        bot.register_absence(record)

    bot.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
