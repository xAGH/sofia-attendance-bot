from dotenv import load_dotenv

load_dotenv()
from os import environ

SENA_SOFIA_USERNAME = environ.get("SENA_SOFIA_USERNAME")
SENA_SOFIA_PASSWORD = environ.get("SENA_SOFIA_PASSWORD")
SENA_SOFIA_LOGIN_URL = "http://senasofiaplus.edu.co/sofia-public/"
ABSENCES_CSV_URL = environ.get("ABSENCES_CSV_URL")
