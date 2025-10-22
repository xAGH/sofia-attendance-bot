from typing import TypedDict


class Absence(TypedDict):
    group_code: str
    name: str
    hours: str
    reason: str
    date: str
