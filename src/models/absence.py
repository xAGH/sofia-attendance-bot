from typing import TypedDict


class Absence(TypedDict):
    group_code: str
    name: str
    hours: str
    justification: str
    date: str
