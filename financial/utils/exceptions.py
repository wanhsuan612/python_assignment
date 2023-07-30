from datetime import date

class CustomizeException(Exception):
    def __init__(self, *args: object):
        self.message = ""

    def __str__(self) -> str:
        return self.message


class InvalidDateZone(CustomizeException):
    def __init__(self, start: date, end:date):
        self.message = f"Invalid date zone. start_date {start} is bigger than end_date {end}."


class SymbolNotFound(CustomizeException):
    def __init__(self, symbol: str):
        self.message = f"Symbol {symbol} not found."

class DateNotFound(CustomizeException):
    def __init__(self, start: date, end: date):
        self.message = f"No data. Please search between {start} and {end}"
