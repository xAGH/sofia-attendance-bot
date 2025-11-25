from typing import List

from bot.core.sofia_bot import SofiaBot
from config import Env
from core.exceptions import NotFound
from csv_reader import load_absences
from models.absence import Absence


def main():
    absences: List[Absence] = load_absences(Env.ABSENCES_CSV_URL)
    bot = SofiaBot()
    bot.login()
    bot.register_absences(absences)
    bot.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
