from datetime import date


class CustomizeException(Exception):
    """Base class for customized exceptions in the financial application."""

    def __init__(self, *args: object):
        self.message = ""

    def __str__(self) -> str:
        return self.message


class InvalidDateZone(CustomizeException):
    """Exception raised when the start date is greater than the end date.

    Args:
        start (date): The start date.
        end (date): The end date.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, start: date, end: date):
        self.message = f"Invalid date zone. start_date {start} is bigger than end_date {end}."


class SymbolNotFound(CustomizeException):
    """Exception raised when the requested stock symbol is not found in the data.

    Args:
        symbol (str): The symbol that was not found.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, symbol: str):
        self.message = f"Symbol {symbol} not found."


class DateNotFound(CustomizeException):
    """Exception raised when no data is found within the requested date range.

    Args:
        start (date): The start date of the range.
        end (date): The end date of the range.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, start: date, end: date):
        self.message = f"No data. Please search between {start} and {end}"
