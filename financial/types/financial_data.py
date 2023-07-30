from datetime import date

from pydantic import BaseModel


class FinancialData(BaseModel):
    symbol: str
    date: date
    open_price: str
    close_price: str
    volume: str
