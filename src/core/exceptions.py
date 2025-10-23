class NotFound(Exception):
    def __init__(self, criteria: str, value: str):
        message = f"No se ha encontrado el aprendiz con {criteria} %{value}%"
        super().__init__(message)
